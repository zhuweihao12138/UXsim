import csv
import pandas as pd

def read_csv(file_path):
    # 读取CSV文件为DataFrame
    df = pd.read_csv(file_path)
    return df

def extract_road_id(road_id):
    # 提取下划线前的部分
    return road_id.split('_')[0] if '_' in road_id else road_id

def process_routes(df):
    # 存储每一条完整的道路
    routes = []
    
    # 过滤出以数字开头的start
    start_rows = df[df['start'].str.match(r'^\d+$')]
    
    for index, row in start_rows.iterrows():
        total_length = row['length']  # 当前路段的总长度
        current_end = row['end']  # 当前路段的end
        
        # 提取road_id
        road_id = extract_road_id(row['id'])

        # 创建一个包含当前路段的列表
        route = [row]
        
        # 循环查找与当前end匹配的下一个start，直到end不带下划线
        while '_' in str(current_end):
            next_row = df[df['start'] == current_end]
            if not next_row.empty:
                next_row = next_row.iloc[0]  # 选择第一行匹配的记录
                total_length += next_row['length']
                route.append(next_row)
                current_end = next_row['end']  # 更新current_end
            else:
                break
        
        # 如果最后的end不包含下划线，记录这一条完整的道路
        if '_' not in str(current_end):
            routes.append({
                'road_id': road_id,
                'start': row['start'],
                'end': current_end,
                'total_length': total_length
            })
    
    return routes

def write_csv(routes, output_file):
    # 将结果写入新的CSV文件
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['road_id', 'start', 'end', 'total_length'])
        writer.writeheader()
        for route in routes:
            writer.writerow(route)

if __name__ == "__main__":
    # 读取csv文件路径
    input_file = "matsim/links.csv"  # 替换为你的csv文件路径
    output_file = "matsim/links_combined.csv"  # 输出文件路径

    # 读取csv数据
    df = read_csv(input_file)

    # 处理路段
    routes = process_routes(df)

    # 将结果写入输出csv文件
    write_csv(routes, output_file)

    print(f"导出的路段数据已经保存到 {output_file}")
