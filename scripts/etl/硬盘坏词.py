import pandas as pd
import jieba
from collections import Counter
import re

def execute(dataframe1=None, dataframe2=None, dataframe3=None):
    if dataframe1 is None or dataframe1.empty:
        return pd.DataFrame([{"分词": "无数据", "词频": 0}])

    df = dataframe1.copy()

    # 1. 过滤差评 (1-3星)
    star_col = next((c for c in df.columns if "星" in str(c)), "")
    if star_col:
        df = df[df[star_col].astype(str).str.contains('1|2|3', na=False)]

    # 2. 差评停用词
    stop_words = {
        "的", "了", "我", "在", "是", "这个", "也", "都", "不", "就", "人", "和", "有", "及",
        "一个", "已经", "觉得", "还是", "比较", "非常", "其实", "以后", "收到", "买的", "由于"
    }

    # 3. 分词统计
    text_col = next((c for c in df.columns if "内容" in str(c) or "评论" in str(c)), "")
    all_text = "".join(df[text_col].astype(str).tolist())
    all_text = re.sub(r'[^\u4e00-\u9fa5]', '', all_text)

    words = jieba.lcut(all_text)
    cleaned_words = [w for w in words if len(w) > 1 and w not in stop_words]
    
    word_counts = Counter(cleaned_words).most_common(100)
    return pd.DataFrame(word_counts, columns=['分词', '词频'])