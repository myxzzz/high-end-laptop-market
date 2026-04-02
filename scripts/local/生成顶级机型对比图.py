import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 璁剧疆涓枃瀛椾綋涓庡叏灞€鏍峰紡
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 28  # 鍏ㄥ眬瀛楀彿鍐嶆鍔犲ぇ

EXCEL_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛== 鐢佃剳 ==\鍓湰椤剁骇鏈哄瀷.xlsx"
DATA_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛鍒嗘瀽缁撴灉"
OUTPUT_DIR = os.path.join(DATA_PATH, "鍙鍖栧浘鐗?)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "椤剁骇鏃楄埌鏈哄瀷閰嶇疆瀵规瘮鍥?png")

def generate_elite_model_chart():
    # 1. 鍔犺浇鏁版嵁
    try:
        df = pd.read_excel(EXCEL_PATH)
    except Exception as e:
        print(f"璇诲彇澶辫触: {e}")
        return

    # 璁＄畻纭欢浠峰€煎拰婧环
    # 鍋囪杩欎簺椤剁骇鏈哄瀷鐨勭‖浠跺崰姣斿湪 Excel 涓凡鏈夛紙鏍规嵁涔嬪墠鐨勫懡浠よ杈撳嚭纭宸叉湁璇ュ垪锛?
    df['纭欢浠峰€?] = df['鍞环'] * df['纭欢浠锋牸鍗犳瘮']
    df['鍝佺墝婧环涓庨泦鎴愬埄娑?] = df['鍞环'] - df['纭欢浠峰€?]
    df['鍗犳瘮鏂囨湰'] = (df['纭欢浠锋牸鍗犳瘮'] * 100).apply(lambda x: f"{x:.0f}%")

    # 2. 缁樺浘 - 涓よ仈鎺掞細鍞环瀵规瘮 + 浠峰€兼瀯鎴?
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(28, 14), dpi=150, facecolor='#FDFDFD')
    
    # 绠€鍖栧瀷鍙峰悕绉版樉绀?
    df['鏄剧ず鍨嬪彿'] = ["鑱旀兂 鎷晳鑰匼nY9000P", "寰槦 娉板潶\n18 Ultra"]

    # --- 宸﹀浘锛氬敭浠峰姣?---
    colors_p = ['#3498DB', '#E74C3C'] # 钃濊壊 vs 绾㈣壊
    sns.barplot(data=df, x='鏄剧ず鍨嬪彿', y='鍞环', palette=colors_p, ax=ax1, hue='鏄剧ず鍨嬪彿', legend=False)
    ax1.set_title('馃捀 鍞环瀵规瘮锛氭瀬鑷存孩浠锋柇灞?, fontsize=38, pad=30, fontweight='bold')
    ax1.set_ylabel('鍞环 (鍏?', fontsize=30)
    ax1.set_xlabel('')
    ax1.tick_params(axis='both', which='major', labelsize=26)
    for p in ax1.patches:
        ax1.annotate(f'锟p.get_height():,.0f}', (p.get_x() + p.get_width()/2, p.get_height()),
                    xytext=(0, 10), textcoords='offset points', ha='center', fontsize=36, fontweight='bold', color='#2C3E50')

    # --- 鍙冲浘锛氱‖浠朵环鍊煎崰姣?(鍫嗗彔鏌辩姸鍥? ---
    bar_width = 0.6
    ax2.bar(df['鏄剧ず鍨嬪彿'], df['纭欢浠峰€?], width=bar_width, label='鏍稿績纭欢浠峰€?(绾?6%)', color='#BDC3C7', edgecolor='black', linewidth=2)
    ax2.bar(df['鏄剧ず鍨嬪彿'], df['鍝佺墝婧环涓庨泦鎴愬埄娑?], width=bar_width, bottom=df['纭欢浠峰€?], label='鍝佺墝婧环鍙婂埄娑︾┖闂?, 
            color='#E74C3C', alpha=0.8, edgecolor='black', linewidth=2)
    
    ax2.set_title('鈿栵笍 浠峰€肩粨鏋勶細鈥滈珮鍩烘暟銆佺ǔ鍗犳瘮鈥濈瓥鐣?, fontsize=38, pad=30, fontweight='bold')
    ax2.set_ylabel('閲戦 (鍏?', fontsize=30)
    ax2.set_xlabel('')
    ax2.tick_params(axis='both', which='major', labelsize=26)
    ax2.legend(fontsize=24, loc='upper left')

    # 鍦ㄥ爢鍙犲浘涓婃爣娉ㄥ崰姣?
    for i in range(len(df)):
        # 鏍囨敞纭欢鍗犳瘮
        ax2.text(i, df.loc[i, '纭欢浠峰€?]/2, f"鏍稿績纭欢浠峰€糪n({df.loc[i, '鍗犳瘮鏂囨湰']})", 
                 ha='center', va='center', fontsize=28, color='black', fontweight='bold')
        # 鏍囨敞鍒╂鼎棰?
        ax2.text(i, df.loc[i, '纭欢浠峰€?] + df.loc[i, '鍝佺墝婧环涓庨泦鎴愬埄娑?]/2, 
                 f"鍝佺墝婧环涓庡埄娑n锟df.loc[i, '鍝佺墝婧环涓庨泦鎴愬埄娑?]:,.0f}", 
                 ha='center', va='center', fontsize=28, color='white', fontweight='bold')

    # 3. 瑁呴グ
    plt.suptitle('2025骞撮《绾ф棗鑸版満鍨嬶細纭欢鍗犳瘮涓庢孩浠烽€昏緫鍏ㄦ櫙鍥?, fontsize=52, y=1.08, fontweight='bold', color='#1A2521')
    sns.despine(ax=ax1)
    sns.despine(ax=ax2)
    plt.tight_layout()

    # 纭繚淇濆瓨鐩綍瀛樺湪
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
    print(f"椤剁骇鏈哄瀷鍗犳瘮瀵规瘮鍥惧凡鐢熸垚: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_elite_model_chart()
    print("Done")

