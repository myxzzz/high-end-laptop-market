import pandas as pd
import jieba
from collections import Counter
import re

def execute(dataframe1=None, dataframe2=None, dataframe3=None):
    if dataframe1 is None or dataframe1.empty:
        return pd.DataFrame([{"分词": "无数据", "词频": 0}])

    df = dataframe1.copy()

    # 1. 过滤好评 (4-5星)
    star_col = next((c for c in df.columns if "星" in str(c)), "")
    if star_col:
        df = df[df[star_col].astype(str).str.contains('4|5', na=False)] # 只有加了str()才能用contains(),contains()是模糊匹配，na=False避免空值报错

    # 2. 停用词库 (过滤掉无意义的虚词和废话)
    stop_words = {
        "的", "了", "我", "在", "是", "这个", "也", "都", "不", "就", "人", "和", "有", 
        "一个", "很", "上", "到", "说", "要", "去", "你", "会", "着", "没", "及", "与", 
        "买", "用", "觉得", "还是", "已经", "比较", "真的", "感觉", "非常", "以后", "其实",
        "不错", "可以", "喜欢", "挺好", "满意", "确实", "一直", "东西", "一款", "京东", "发货"
    }

    # 3. 分词统计
    text_col = next((c for c in df.columns if "内容" in str(c) or "评论" in str(c)), "")
    all_text = "".join(df[text_col].astype(str).tolist())
    all_text = re.sub(r'[^\u4e00-\u9fa5]', '', all_text) # 只留中文

    words = jieba.lcut(all_text)
    # 长度大于1且不在停用词里
    cleaned_words = [w for w in words if len(w) > 1 and w not in stop_words]
    
    word_counts = Counter(cleaned_words).most_common(100)
    return pd.DataFrame(word_counts, columns=['分词', '词频'])