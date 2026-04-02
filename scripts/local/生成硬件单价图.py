import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 璁剧疆涓枃瀛椾綋
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

DATA_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛鍒嗘瀽缁撴灉"
MEM_FILE = os.path.join(DATA_PATH, "鍐呭瓨鏉℃瘡GB浠锋牸.csv")
DISK_FILE = os.path.join(DATA_PATH, "纭洏浠锋牸GB.csv")
OUTPUT_DIR = os.path.join(DATA_PATH, "鍙鍖栧浘鐗?)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "纭欢鍗曚綅瀹归噺浠锋牸瀵规瘮鍥?png")

def generate_unit_price_chart():
    # 1. 鍔犺浇鍐呭瓨鏁版嵁 (棰戠巼)
    try:
        df_mem = pd.read_csv(MEM_FILE, encoding='utf-8')
    except:
        df_mem = pd.read_csv(MEM_FILE, encoding='gbk')
    
    # 2. 鍔犺浇纭洏鏁版嵁 (鍗忚)
    # 纭洏 CSV 涔嬪墠璇诲彇鎶ラ敊锛屽啀娆″皾璇曞苟澶勭悊缂栫爜
    try:
        df_disk = pd.read_csv(DISK_FILE, encoding='utf-8')
    except:
        # 濡傛灉 utf-8 澶辫触锛屽皾璇曚互 'latin1' 璇诲彇鍐嶈浆鐮佹垨鑰呰烦杩囬敊璇瓧鑺?
        df_disk = pd.read_csv(DISK_FILE, encoding='utf-8-sig')

    # 3. 缁樺浘 - 涓よ仈鎺掞細鍐呭瓨棰戠巼 vs 纭洏鍗忚
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(26, 12), dpi=150, facecolor='#FDFDFD')

    # --- 宸﹀浘锛氬唴瀛橀鐜?vs 姣廏B浠锋牸 ---
    sns.barplot(data=df_mem, x='棰戠巼锛圡Hz锛?, y='姣廏B鍗曚环', palette='coolwarm', ax=ax1, hue='棰戠巼锛圡Hz锛?, legend=False)
    ax1.set_title('馃 鍐呭瓨锛氶鐜囪秺楂?鍗曚綅浠锋牸瓒婇珮', fontsize=36, pad=30, fontweight='bold')
    ax1.set_xlabel('棰戠巼 (MHz)', fontsize=28)
    ax1.set_ylabel('姣廏B鍗曚环 (鍏?GB)', fontsize=28)
    ax1.tick_params(labelsize=24)
    for p in ax1.patches:
        ax1.annotate(f'锟p.get_height():.1f}', (p.get_x() + p.get_width()/2, p.get_height()),
                    xytext=(0, 10), textcoords='offset points', ha='center', fontsize=30, fontweight='bold')

    # --- 鍙冲浘锛氱‖鐩樺崗璁?vs 姣廏B浠锋牸 ---
    # 鏍规嵁瀹為檯鍒楀悕 ['鍗忚_鏍囩', '姣廏B鍗曚环', '浠锋牸', '鏍锋湰鏁?]
    disk_x_col = '鍗忚_鏍囩'
    disk_y_col = '姣廏B鍗曚环'
    
    sns.barplot(data=df_disk, x=disk_x_col, y=disk_y_col, palette='viridis', ax=ax2, hue=disk_x_col, legend=False)
    ax2.set_title('馃捑 纭洏锛氬崗璁鏍间笌鍗曚綅浠锋牸瀵规瘮', fontsize=36, pad=30, fontweight='bold')
    ax2.set_xlabel('瀛樺偍鍗忚/瑙勬牸 (NVMe绛?', fontsize=28)
    ax2.set_ylabel('姣廏B鍗曚环 (鍏?GB)', fontsize=28)
    ax2.tick_params(labelsize=24)
    for p in ax2.patches:
        ax2.annotate(f'锟p.get_height():.2f}', (p.get_x() + p.get_width()/2, p.get_height()),
                    xytext=(0, 10), textcoords='offset points', ha='center', fontsize=30, fontweight='bold')

    # 4. 鎬讳慨楗?
    plt.suptitle('绗旇鏈牳蹇冨瓨鍌ㄧ粍浠讹細鍗曚綅瀹归噺(Per GB)甯傚満瀹氫环鍒嗘瀽', fontsize=48, y=1.08, fontweight='bold', color='#2C3E50')
    sns.despine()
    plt.tight_layout()

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
    print(f"纭欢鍗曚环鍥惧凡鐢熸垚: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_unit_price_chart()

