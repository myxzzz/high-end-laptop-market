import pandas as pd
import re

def execute(dataframe1=None, dataframe2=None, dataframe3=None):
    """
    思睿智训平台专用入口函数
    dataframe1: 平台读入的 内存条.xlsx 数据
    """
    # 如果没传入数据，直接返回
    if dataframe1 is None:
        return pd.DataFrame()

    df = dataframe1.copy()

    # 1. 鲁棒性处理：清理表头空格
    df.columns = df.columns.str.strip()

    # 定义处理容量的内部函数（兼容 Python 3.7.4）
    def process_ram_capacity(row):
        try:
            # 获取列名，注意使用 txt 中提到的全角字符
            # 假设列名为 '单／套条标识' 或 '容量（GB）'
            # 我们先尝试从 '单／套条标识' 提取
            target_col = '单／套条标识'
            capacity_col = '容量（GB）'
            
            # 安全检查：列是否存在
            if target_col not in df.columns or capacity_col not in df.columns:
                return 0

            val = str(row[target_col])
            
            # 逻辑 A：如果包含 '*' 号 (如 2*16G)
            if '*' in val:
                nums = re.findall(r'\d+', val) # re.findall可以提取字符，这里为提取数字
                if len(nums) >= 2:
                    # nums[0] 是数量（2），nums[1] 是单条容量（16）
                    return int(nums[0]) * int(nums[1])
            
            # 逻辑 B：如果不包含 *，取 '容量（GB）' 列的数字
            cap_val = str(row[capacity_col])
            nums = re.findall(r'\d+', cap_val)
            if nums:
                return int(nums[0])
            
            return 0
        except:
            return 0

    # 2. 应用计算逻辑，生成新列 '实际总容量'
    df['实际总容量'] = df.apply(process_ram_capacity, axis=1)

    # 3. 价格清洗（防止含有 '元' 或其他字符导致无法计算）
    def clean_price(val):
        try:
            res = re.sub(r'[^\d.]', '', str(val))
            return float(res) if res else 0.0
        except:
            return 0.0

    if '价格' in df.columns:
        df['价格'] = df['价格'].apply(clean_price)

    # 4. 必须返回 DataFrame 对象
    return df