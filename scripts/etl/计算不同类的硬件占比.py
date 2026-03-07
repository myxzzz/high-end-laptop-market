import pandas as pd
import numpy as np

def execute(dataframe1=None, dataframe2=None, dataframe3=None):
    if dataframe1 is None or dataframe1.empty:
        return pd.DataFrame([{"结果": "尚未输入 K-Means 聚类结果表"}])
        
    # 1. 提取聚类汇总后的数据
    laptop_k = dataframe1.copy()

    # 2. 清洗并确保数值类型
    cols_to_fix = ['Group_prediction', 'Avg_售价', 'Avg_内存（G）', 'Avg_储存（G）']
    for col in cols_to_fix:
        if col in laptop_k.columns:
            laptop_k[col] = pd.to_numeric(laptop_k[col], errors='coerce')
    
    laptop_k = laptop_k.dropna(subset=cols_to_fix)

    # 3. 设定正确的市场基准价 (基于你之前的分析结论)
    ram_base = 104.93  # 每 GB 内存约 104 元
    ssd_base = 1.35    # 每 GB 硬盘约 1.35 元 (PCIe 4.0/5.0 平均)

    analysis_results = []
    
    # 4. 遍历每个聚类类别
    for _, row in laptop_k.iterrows():
        prediction = row['Group_prediction']
        price = row['Avg_售价']
        ram = row['Avg_内存（G）']
        ssd = row['Avg_储存（G）']

        # 计算该档位机型的“公允硬件价值”
        fair_hardware_value = (ram * ram_base) + (ssd * ssd_base) 

        # 计算“价格/硬件价值比” (即溢价率)
        # 注意：这里的溢价包含了品牌、模具、屏幕、CPU/GPU等所有其他成本
        premium_ratio = fair_hardware_value / price if price > 0 else 0
           
        analysis_results.append({
            '机型档位_Cluster': int(prediction),
            '该平均档售价': round(price, 2),
            '平均内存_G': round(ram, 2),
            '平均硬盘_G': round(ssd, 2),
            '公允内存硬盘价值': round(fair_hardware_value, 2),
            '硬件占比': round(premium_ratio, 2)
        })

    # 5. 生成结果
    result_df = pd.DataFrame(analysis_results)
    
    # 按照售价排序
    return result_df.sort_values(by='该平均档售价', ascending=False)

