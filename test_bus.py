import pandas as pd

# 读取csv文件
data = pd.read_csv('matsim/bus.csv')

# 按线路ID分组
lines = data.groupby('id')

# 定义模拟函数
def simulate_bus_lines(lines):
    # 循环每一条公交线路
    for line_id, stops in lines:
        print(f"线路: {line_id}")
        # 对每条线路的发车时间进行模拟，从0秒开始，每隔500秒发车，直到10500秒结束
        for start_time in range(60, 10561, 500):
            print(f"\n{line_id} 线路的公交车在 {start_time} 秒发车")
            current_time = start_time
            # 按顺序模拟每一站之间的行驶
            for i in range(len(stops) - 1):
                current_stop = stops.iloc[i]
                next_stop = stops.iloc[i + 1]
                print(f"时间 {current_time} 秒，公交车从站点 {current_stop['stop_id']} (x={current_stop['x']}, y={current_stop['y']}) 出发")
                current_time += current_stop['inter_stop_time']
                print(f"时间 {current_time} 秒，公交车到达站点 {next_stop['stop_id']} (x={next_stop['x']}, y={next_stop['y']})")
        print("\n" + "="*40 + "\n")

# 调用模拟函数
simulate_bus_lines(lines)
