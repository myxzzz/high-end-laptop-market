import pandas as pd
try:
    df = pd.read_excel(r'c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛== 鐢佃剳 ==\鍓湰椤剁骇鏈哄瀷.xlsx')
    print("Columns:", df.columns.tolist())
    print(df.head())
except Exception as e:
    print("Error:", e)

