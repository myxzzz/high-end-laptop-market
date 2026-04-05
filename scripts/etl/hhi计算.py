import pandas as pd
import numpy as np

def execute(dataframe1=None, dataframe2=None, dataframe3=None):
    if dataframe1 is None or dataframe1.empty:
        return pd.DataFrame([{"分析": "无输入数据", "值": 0}])

    df = dataframe1.copy()

    # 1. 智能匹配核心列
    model_col = next((c for c in df.columns if "型号" in str(c)), "")
    brand_col = next((c for c in df.columns if "品牌" in str(c)), "")
    price_col = next((c for c in df.columns if "价" in str(c)), "")
    comment_col = next((c for c in df.columns if "评论" in str(c)), "")

    # 2. 预处理：去重与数值转化
    df[price_col] = pd.to_numeric(df[price_col], errors='coerce')
    df[comment_col] = pd.to_numeric(df[comment_col], errors='coerce').fillna(0)

    # 【去重逻辑】每个型号取一个代表性的配置（价格最高且评论最多的）
    model_df = df.groupby(model_col).agg({
        brand_col: 'first',
        price_col: 'max',
        comment_col: 'max'
    }).reset_index()

    # 3. 【核心创新】计算“估算产值” (Economic Impact)
    # 用 售价 * 评论数 模拟销售额，这样 3万元的Brand_A比 1万元的Brand_B更占权重
    model_df['估算产值'] = model_df[price_col] * model_df[comment_col]

    # 4. 按品牌聚合
    brand_stats = model_df.groupby(brand_col).agg({
        model_col: 'count',        # 顺便统计该品牌有多少款型号
        '估算产值': 'sum',
        comment_col: 'sum'
    }).reset_index()

    total_market_value = brand_stats['估算产值'].sum()
    
    if total_market_value == 0:
        return pd.DataFrame([{"结果": "数据不足或数值为0"}])

    # 5. 计算基于产值的市场份额和 HHI
    brand_stats['价值份额_占比'] = ((brand_stats['估算产值'] / total_market_value) * 100).round(2)
    brand_stats['价值平方'] = (brand_stats['价值份额_占比'] ** 2).round(2)
    hhi_index = (brand_stats['价值平方'].sum()).round(2)

    # 6. 结果整理
    brand_stats = brand_stats.sort_values(by='价值份额_占比', ascending=False)
    
    # 增加 HHI 评价
    brand_stats['全局HHI'] = round(hhi_index, 2)
    brand_stats['市场类型'] = "高集中度" if hhi_index > 2500 else ("中度竞争" if hhi_index > 1000 else "完全竞争")
    
    # 重命名列名，方便展示
    return brand_stats.rename(columns={
        model_col: '产品SKU数',
        comment_col: '总热度值'
    })