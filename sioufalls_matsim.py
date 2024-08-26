from uxsim import *
from tqdm import tqdm
import csv
# Define the main simulation
# Units are standardized to seconds (s) and meters (m)
# Simulation main

# The earliest time in end_time1 is: 06:24:48
W = World(
    name="sioufalls_matsim3",
    deltan=1,
    tmax=10500,
    print_mode=1, save_mode=1, show_mode=1,
    random_seed=0
)

W.generate_Nodes_from_csv("matsim/nodes.csv")
W.generate_Links_from_csv("matsim/links.csv")

# bus demand
data = pd.read_csv('matsim/bus.csv')
# 按线路ID分组
lines = data.groupby('id')
# 循环每一条公交线路
for line_id, stops in lines:
    print(f"线路: {line_id}")
    # 对每条线路的发车时间进行模拟，从0秒开始，每隔500秒发车，直到10500秒结束
    for start_time in range(60, 10561, 500):
        current_time = start_time
        # 按顺序模拟每一站之间的行驶
        for i in range(len(stops) - 1):
            current_stop = stops.iloc[i]
            next_stop = stops.iloc[i + 1]
            W.adddemand_point2point(
                    float(current_stop['x']), float(current_stop['y']),
                    float(next_stop['x']), float(next_stop['y']),
                    float(current_time), 
                    float(current_time)+W.DELTAT,
                    flow=1
                )
            current_time += current_stop['inter_stop_time']

csv_file = 'matsim/population_time_converted.csv'

# 打开CSV文件
with open(csv_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # 获取总行数以便初始化进度条
    total_lines = sum(1 for row in csv.reader(open(csv_file))) - 1  # 减去标题行

    # 初始化进度条
    with tqdm(total=total_lines, desc="私家车demand") as pbar:
        last_origin=''
        # 遍历每一行
        for row in reader:
            if row['mode1']=='car' and row['type2']=='work' and row['facility1']!=last_origin:
                W.adddemand_point2point(
                    float(row['x1']), float(row['y1']),
                    float(row['x2']), float(row['y2']),
                    float(row['end_time1_seconds']), 
                    float(row['end_time1_seconds'])+W.DELTAT,
                    flow=1
                )
                # W.adddemand_point2point(
                #     float(row['x2']), float(row['y2']),
                #     float(row['x3']), float(row['y3']),
                #     float(row['end_time2_seconds']),
                #     float(row['end_time2_seconds']) + W.DELTAT,
                #     flow=1
                # )
            last_origin = row['facility1']
            # 更新进度条
            pbar.update(1)

W.exec_simulation()

W.analyzer.print_simple_stats()
W.analyzer.network_anim(animation_speed_inverse=15, detailed=0, network_font_size=0)
W.analyzer.network_fancy(animation_speed_inverse=15, sample_ratio=0.1, interval=10, trace_length=5, speed_coef=4)