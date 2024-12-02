import pandas as pd
import json
import numpy as np

# 读取 links_combined.csv
links_df = pd.read_csv('matsim/links_combined.csv')

# 读取 exec_rec_touse.csv
exec_rec_df = pd.read_csv('execution_record/exec_rec_touse.csv')

# 读取 SiouxFallsCoordinates.geojson
with open('matsim/SiouxFallsCoordinates.geojson', 'r') as f:
    geojson_data = json.load(f)

# 将 GeoJSON 数据转换为字典，方便查找坐标
coordinates = {feature['properties']['id']: feature['geometry']['coordinates'] for feature in geojson_data['features']}

# 偏移距离 (单位为经纬度上的小值，实际可根据需要调整)
offset_distance = 0.0006

# 创建空的 FeatureCollection
link_geojson_output = {
    "type": "FeatureCollection",
    "features": []
}

# 函数：计算垂直于 link 方向的偏移量
def compute_offset(start_coords, end_coords, offset_distance):
    # 将经纬度转换为 numpy 数组
    start_point = np.array(start_coords)
    end_point = np.array(end_coords)
    
    # 计算 link 方向的向量
    direction_vector = end_point - start_point
    
    # 计算垂直于方向向量的90度旋转向量 (顺时针)
    offset_vector = np.array([-direction_vector[1], direction_vector[0]])
    
    # 归一化方向向量以获取单位向量
    unit_offset_vector = offset_vector / np.linalg.norm(offset_vector)
    
    # 按偏移距离缩放单位向量
    offset = unit_offset_vector * offset_distance
    
    return offset

# 遍历 links_combined.csv 中的每一行
for _, row in links_df.iterrows():
    link_id = int(row['link_id'])
    start_id = row['start']
    end_id = row['end']
    length = row['total_length']
    
    # 获取 start 和 end 的经纬度
    start_coords = coordinates.get(start_id)
    end_coords = coordinates.get(end_id)
    
    if start_coords and end_coords:
        # 计算偏移
        offset = compute_offset(start_coords, end_coords, offset_distance)
        
        # 在顺时针方向增加偏移量
        start_coords_offset = start_coords + offset
        end_coords_offset = end_coords + offset

        # 从 exec_rec_touse.csv 中提取与该 road_id 对应的列向量
        exec_data = exec_rec_df[str(link_id)].tolist()  # 列向量
        
        # 创建新的 GeoJSON Feature
        feature = {
            "type": "Feature",
            "properties": {
                "link_id": link_id,
                "length": length,
                "exec_data": exec_data,
                "start_id": start_id,
                "end_id": end_id
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [start_coords_offset.tolist(), end_coords_offset.tolist()]
            }
        }
        
        # 将 Feature 添加到 features 列表中
        link_geojson_output["features"].append(feature)

# 将生成的 GeoJSON 数据保存到文件
with open('server/links_with_exec_data1.geojson', 'w') as f:
    json.dump(link_geojson_output, f)
