import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('matsim/population_time_converted.csv')

# 统计第四列中 'always' 的数量
count = (df.iloc[:, 3] == 'always').sum()

print(f"总共有 {count} 个 'always'")