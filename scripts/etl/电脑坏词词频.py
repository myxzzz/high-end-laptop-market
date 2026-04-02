import pandas as pd
import jieba
from collections import Counter
import re

def execute(dataframe1=None, dataframe2=None, dataframe3=None):
    if dataframe1 is None or dataframe1.empty:
        return pd.DataFrame([{"分析项": "无数据", "频次": 0}])

    df = dataframe1.copy()

    # 1. 过滤差评：仅保留情感得分 < 0.5 的评论 (负面情绪较重的)
    sentiment_col = next((c for c in df.columns if "情感得分" in str(c)), "") #next()函数智能匹配，在这里是匹配“情感得分”，找不到则返回空字符串
    if sentiment_col:
        df[sentiment_col] = pd.to_numeric(df[sentiment_col], errors='coerce')
        df = df[df[sentiment_col] < 0.5]
    
    if df.empty:
        return pd.DataFrame([{"分析项": "暂无明显负面评价数据", "频次": 0}])

    # 2. 定义负面评价聚类映射 (锁定 AI 笔记本核心痛点)
    # 我帮你把一些口语化的词做了聚合，让数据更集中
    negative_topics = {
        "设计缺陷": ["接口位置不合理", "电源口靠右", "鼠标打架", "沾指纹", "下巴宽", "档次感差", "笨重", "做工粗糙"],
        "噪音散热": ["风噪", "风扇声大", "发热", "一惊一乍", "烫手", "啸叫", "降频"],
        "溢价与背刺": ["降价太快", "被背刺", "价格偏高", "智商税", "不值这个钱", "溢价过高", "虚高", "割韭菜"],
        "售后与服务": ["客服敷衍", "售后差", "无人修理", "不退不换", "二手机", "退货难"],
        "稳定性故障": ["闪退", "黑屏", "自动重启", "声卡顿", "适配差", "调亮度", "死机", "蓝屏", "风扇策略智障"]
    }

    # 为了保证分词准确性，将长词加入 jieba 词库
    for kws in negative_topics.values(): # 遍历每个分类的关键词列表
        for kw in kws:          # 遍历具体关键词
            jieba.add_word(kw)

    # 3. 准备评论文本
    text_col = next((c for c in df.columns if "内容" in str(c) or "评论" in str(c)), "")
    all_text = "".join(df[text_col].astype(str).tolist())

    # 4. 统计与分析
    raw_results = []
    
    # 我们遍历所有的具体坏词关键词
    for category, keywords in negative_topics.items(): # items() 方法返回字典的键和值
        for kw in keywords:
            # 采用字符串统计，比分词统计对长难句更准
            count = all_text.count(kw)
            
            if count > 0:
                # 设定权重：溢价和稳定性词汇权重倍数设为3（词云里显示会更大）
                weight_factor = 3 if category in ["溢价与背刺", "稳定性故障"] else 1
                
                raw_results.append({
                    "坏词关键词": kw,
                    "所属痛点分类": category,
                    "出现频次": count,
                    "可视化权重": count * weight_factor
                })

    # 5. 返回结果并按频次排序
    result_df = pd.DataFrame(raw_results).sort_values(by="出现频次", ascending=False)

    return result_df