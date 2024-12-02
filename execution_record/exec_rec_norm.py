import pandas as pd

def process_files(csv_file, xlsx_file, output_file):
    # Step 1: 读取CSV文件的第四列
    csv_data = pd.read_csv(csv_file)
    lengths = csv_data.iloc[:, 3].values  # 获取第四列，注意列索引从0开始，所以3是第四列
    # Step 2: 读取Excel文件
    excel_data = pd.read_excel(xlsx_file)

    # Step 3: 遍历Excel文件的每行，从第2列到最后一列，每行元素除以对应的长度向量值
    for i in range(10500):  # 行索引从0到10499
            for j in range(0,76):  # 列索引从1开始，遍历第2到最后一列
                excel_data.iloc[i, j+1] = excel_data.iloc[i, j+1] / lengths[j]

    # Step 4: 将结果保存回Excel文件
    excel_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    # 输入的CSV文件路径和Excel文件路径
    csv_file = 'matsim/links_combined.csv'      # 替换为你的CSV文件路径
    xlsx_file = 'execution_record/execution_record_road_combined.xlsx'    # 替换为你的Excel文件路径
    output_file = 'execution_record/exec_rec_touse.csv' # 输出结果的Excel文件路径

    # 处理文件
    process_files(csv_file, xlsx_file, output_file)

    print(f"处理后的数据已保存到 {output_file}")
