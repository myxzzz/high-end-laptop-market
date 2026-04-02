import pandas as pd
import re

def execute(dataframe1=None, dataframe2=None, dataframe3=None):
    """
    思睿智训平台专用入口函数
    任务：将 内存条.xlsx 的 '代际' 列转换为索引值
    逻辑：DDR4 -> 0, DDR5 -> 1
    """
    if dataframe1 is None:
        return pd.DataFrame()

    df = dataframe1.copy()

    # 1. 清理表头空格
    df.columns = df.columns.str.strip()

    def clean_generation(raw):
        text = str(raw).lower()
        # 提取 DDR4 或 DDR5 中的数字
        match = re.search(r'ddr\s*(\d)', text)
        if match:
            num = int(match.group(1))
            # 核心翻译逻辑：DDR4 为 0，DDR5 为 1
            if num == 4:
                return 0
            if num == 5:
                return 1
        return 0
    
    # 2. 查找并处理列
    # 我们假设原始列名包含 '代际' 字样
    target_col = ''
    for col in df.columns:
        if '代际' in col:
            target_col = col
            break

    if target_col:
        # 生成模型需要的 Generation_Index 列
        df['Generation_Index'] = df[target_col].apply(clean_generation)

    # 3. 调整列顺序（可选，将新列放在前面）
    if 'Generation_Index' in df.columns:
        cols = ['Generation_Index'] + [c for c in df.columns if c != 'Generation_Index']
        df = df[cols]

    return df
