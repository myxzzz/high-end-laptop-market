import pandas as pd
import re

def execute(dataframe1=None, dataframe2=None, dataframe3=None):
    if dataframe1 is None or dataframe1.empty:
        return pd.DataFrame()

    df = dataframe1.copy()

    # 1. 清理表头空格
    df.columns = df.columns.str.strip()

    # 清理函数：安全提取第一个数字
    def clean_predication(raw):
        if pd.isna(raw): # 处理空值
            return 0
        
        raw_str = str(raw) # 转换成字符串，方便正则提取
        match = re.search(r'(\d)', raw_str) # 在字符串里找第一个数字
        if match:
            return int(match.group(1))
        return 0
    
    # 2. 查找包含 predication 的列
    target_col = next((c for c in df.columns if 'predication' in str(c).lower()), "")

    if target_col:
        # 对该列应用清理函数
        df['Predication_Index'] = df[target_col].apply(clean_predication)

    # 3. 调整列顺序
    if 'Predication_Index' in df.columns:
        cols = ['Predication_Index'] + [c for c in df.columns if c != 'Predication_Index']
        df = df[cols]

    return df