import pandas as pd

# 读取 CSV 文件
file_path = 'execution_record/exec_rec_touse.csv'  # 替换为你的 CSV 文件路径
df = pd.read_csv(file_path)

# 提取第 2 列到最后一列的数据（跳过第一列）
data_columns = df.iloc[:, 1:]  # iloc[:, 1:] 表示从第 2 列开始取数据

# 将所有数据平展为一维数组
all_values = data_columns.values.flatten()

# 查找前 100 个最大的值
top_1000_values = pd.Series(all_values).nlargest(1000)

# 输出结果
print(f'从第2列到最后一列的前100个最大值为: \n{top_1000_values}')
