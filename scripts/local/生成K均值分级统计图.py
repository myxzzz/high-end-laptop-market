import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 璁剧疆涓枃瀛椾綋涓庡叏灞€鏍峰紡
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 22

DATA_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛鍒嗘瀽缁撴灉"
FILE_NAME = "鐢佃剳k鍧囧€?csv"
OUTPUT_DIR = os.path.join(DATA_PATH, "鍙鍖栧浘鐗?)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "K鍧囧€艰仛绫诲垎绾у叏鏅浘.png")

def generate_kmeans_summary_chart():
    # 1. 鍔犺浇鏁版嵁
    try:
        df = pd.read_csv(os.path.join(DATA_PATH, FILE_NAME), encoding='utf-8')
    except:
        df = pd.read_csv(os.path.join(DATA_PATH, FILE_NAME), encoding='gbk')
    
    # 鏄犲皠缁勫埆 ID 鍒颁笓涓氭。浣嶅悕绉?
    # 鏍规嵁鍞环鐗瑰緛杩涜鍖归厤
    tier_map = {
        1: "绉诲姩宸ヤ綔绔欑骇",
        2: "鍙戠儳鍒涗綔绾?,
        3: "鎬ц兘杩涢樁绾?,
        0: "楂樼鍏ラ棬绾?
    }
    df['妗ｄ綅鍚嶇О'] = df['Group_prediction'].map(tier_map)
    
    # 鎸夊敭浠蜂粠楂樺埌浣庢帓鍒?
    df = df.sort_values("Avg_鍞环", ascending=False)

    # 2. 缁樺埗鍙屽瓙鍥撅細宸﹁竟鍞环锛屽彸杈规満鍨嬫暟閲?
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 12), sharey=True)
    fig.patch.set_facecolor('#FDFDFD')

    # --- 鍥?: 骞冲潎鍞环 ---
    sns.barplot(data=df, x='Avg_鍞环', y='妗ｄ綅鍚嶇О', palette='rocket', ax=ax1, hue='妗ｄ綅鍚嶇О', legend=False)
    ax1.set_title('馃捀 骞冲潎鍞环 (鍏?', fontsize=32, pad=30, fontweight='bold')
    ax1.set_xlabel('')
    ax1.set_ylabel('鑱氱被鍒嗙骇瑙嗚', fontsize=26, fontweight='bold')
    for p in ax1.patches:
        val = p.get_width()
        ax1.annotate(f'锟val:,.0f}', (val, p.get_y() + p.get_height()/2),
                    xytext=(10, 0), textcoords='offset points', va='center', fontsize=22, fontweight='bold')

    # --- 鍥?: 鏈哄瀷鏁伴噺鍒嗗竷 ---
    sns.barplot(data=df, x='Count_鍨嬪彿', y='妗ｄ綅鍚嶇О', palette='mako', ax=ax2, hue='妗ｄ綅鍚嶇О', legend=False)
    ax2.set_title('馃捇 鏈哄瀷SKU鏁伴噺', fontsize=32, pad=30, fontweight='bold')
    ax2.set_xlabel('')
    ax2.set_ylabel('')
    for p in ax2.patches:
        val = p.get_width()
        ax2.annotate(f'{val:.0f} 娆?, (val, p.get_y() + p.get_height()/2),
                    xytext=(10, 0), textcoords='offset points', va='center', fontsize=22, fontweight='bold')

    # 3. 鎬绘爣棰樹笌淇グ
    plt.suptitle('绗旇鏈競鍦鸿仛绫诲垎鏋愶細鍚勫垎绾ф。浣嶈妯′笌浠峰€煎姣斿浘', fontsize=40, y=1.05, fontweight='bold', color='#2C3E50')
    plt.tight_layout()

    # 纭繚淇濆瓨鐩綍瀛樺湪
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
    print(f"K鍧囧€艰仛绫绘€荤粨鍥惧凡鐢熸垚: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_kmeans_summary_chart()
    print("Done")

