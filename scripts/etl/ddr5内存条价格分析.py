import pandas as pd
import numpy as np
import re

def execute(dataframe1=None, dataframe2=None, dataframe3=None):
    if dataframe1 is None or dataframe1.empty:
        return pd.DataFrame([{"分析": "无数据", "值": 0}])

    df = dataframe1.copy()
    # 清理列名空格
    df.columns = df.columns.str.strip()

    # 1. 匹配列
    daiji_col = next((c for c in df.columns if "代际" in str(c)), "")
    cap_col = next((c for c in df.columns if "容量" in str(c) or "标识" in str(c)), "")
    price_col = next((c for c in df.columns if "价" in str(c)), "")
    pinlv_col = next((c for c in df.columns if "频率" in str(c)), "")

    # 2. 严格过滤 DDR5
    df = df[df[daiji_col].astype(str).str.contains('DDR5', case=False)]

    # 3. 严谨提取容量（处理 2*16G 等套装情况）
    def process_capacity(val):
        try:
            val_str = str(val).upper()
            if '*' in val_str:
                nums = re.findall(r'\d+', val_str)
                if len(nums) >= 2:
                    return int(nums[0]) * int(nums[1])
            nums = re.findall(r'\d+', val_str)
            return int(nums[0]) if nums else 0
        except:
            return 0

    df['容量_数字'] = df[cap_col].apply(process_capacity)
    df[price_col] = pd.to_numeric(df[price_col], errors='coerce')
    
    # 【核心一步】算出 1GB 多少钱
    df = df[df['容量_数字'] > 0] # 防止除以0报错
    df['每GB单价'] = df[price_col] / df['容量_数字']

    # 4. 按频率统计：看看不同性能档位的 1GB 成本
    # 这样你就知道 5600MHz 的 1GB 值多少钱，6400MHz 的又值多少钱了
    result = df.groupby(pinlv_col).agg({
        '每GB单价': 'mean',
        price_col: 'mean',
        '容量_数字': 'count' # 看看这个频率下有多少款条子
    }).reset_index().rename(columns={'容量_数字': '样本数'})

    return result.round(2)