import pandas as pd

# 读取 xlsx 文件
df = pd.read_excel('execution_record/execution_record.xlsx')

# 提取列的名称（第一列假设为Time，不处理）
columns = df.columns[1:]  # 跳过第一列 'Time'

# 创建一个空的字典用于存储相同前缀的列数据
new_columns = {}



# 遍历列名
for col in columns:
    prefix = col.split('_')[0]  # 提取下划线前的部分
    if prefix not in new_columns:
        new_columns[prefix] = df[col]  # 如果该前缀还未出现，创建一个新列
    else:
        new_columns[prefix] += df[col]  # 如果该前缀已经出现，累加该列数据

# 创建新的 DataFrame，保留第一列 'Time'
new_df = pd.DataFrame(df['Time'])

# 对前缀进行排序并按顺序添加列到 new_df 中
for prefix in sorted(new_columns.keys(), key=lambda x: int(x)):  # 按数值排序
    new_df[prefix] = new_columns[prefix]

# 保存到新的 Excel 文件
new_df.to_excel('execution_record/processed_file.xlsx', index=False)

print("Data processed and saved as 'execution_record/processed_file.xlsx'")
