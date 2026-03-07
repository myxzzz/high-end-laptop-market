import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 璁剧疆涓枃瀛椾綋涓庡叏灞€鏍峰紡
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 24

DATA_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛鍒嗘瀽缁撴灉"
INPUT_FILE = os.path.join(DATA_PATH, "鍚勫搧鐗屽奖瀛愪环鏍兼煡.csv")
OUTPUT_DIR = os.path.join(DATA_PATH, "鍙鍖栧浘鐗?)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "鍚勫搧鐗岀‖浠跺奖瀛愪环鏍煎姣斿浘.png")

def generate_shadow_price_chart():
    # 1. 鍔犺浇鏁版嵁
    try:
        df = pd.read_csv(INPUT_FILE, encoding='gbk')
    except:
        df = pd.read_csv(INPUT_FILE, encoding='utf-8')

    # 灏嗘暟鎹垎涓哄唴瀛樺拰纭洏涓ょ粍
    df_mem = df[df['纭欢绫诲瀷'] == '鍐呭瓨'].sort_values('骞冲潎褰卞瓙浠锋牸', ascending=False)
    df_disk = df[df['纭欢绫诲瀷'] == '纭洏'].sort_values('骞冲潎褰卞瓙浠锋牸', ascending=False)

    # 2. 缁樺浘 - 浣跨敤鍙岃仈瀛愬浘锛岃В鍐抽噺绾у樊寮傞棶棰?
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(28, 14), dpi=150, facecolor='#FDFDFD')

    # --- 宸﹀瓙鍥撅細鍐呭瓨褰卞瓙浠锋牸 (閲忕骇杈冨ぇ) ---
    sns.barplot(data=df_mem, x='鍝佺墝', y='骞冲潎褰卞瓙浠锋牸', color='#3498DB', ax=ax1, hue='鍝佺墝', legend=False)
    ax1.set_title('馃 鍐呭瓨锛氬钩鍧囧奖瀛愪环鏍?, fontsize=40, pad=30, fontweight='bold', color='#1F618D')
    ax1.set_ylabel('褰卞瓙浠锋牸 (鍏?GB)', fontsize=32, fontweight='bold')
    ax1.set_xlabel('鍝佺墝', fontsize=30)
    ax1.tick_params(labelsize=26)
    
    # 鍐呭瓨鏍囨敞
    for p in ax1.patches:
        ax1.annotate(f'锟p.get_height():.1f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', fontsize=28, fontweight='bold',
                    xytext=(0, 12), textcoords='offset points')

    # --- 鍙冲瓙鍥撅細纭洏褰卞瓙浠锋牸 (閲忕骇杈冨皬锛岀嫭绔嬬缉鏀? ---
    sns.barplot(data=df_disk, x='鍝佺墝', y='骞冲潎褰卞瓙浠锋牸', color='#E67E22', ax=ax2, hue='鍝佺墝', legend=False)
    ax2.set_title('馃捑 纭洏锛氬钩鍧囧奖瀛愪环鏍?(鐙珛閲忕▼)', fontsize=40, pad=30, fontweight='bold', color='#A04000')
    ax2.set_ylabel('褰卞瓙浠锋牸 (鍏?GB)', fontsize=32, fontweight='bold')
    ax2.set_xlabel('鍝佺墝', fontsize=30)
    ax2.tick_params(labelsize=26)
    
    # 纭洏鏍囨敞 (淇濈暀涓や綅灏忔暟锛屽洜涓烘暟鍊煎皬)
    for p in ax2.patches:
        ax2.annotate(f'锟p.get_height():.2f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', fontsize=28, fontweight='bold',
                    xytext=(0, 12), textcoords='offset points')

    # 3. 瑁呴グ
    plt.suptitle('鏍稿績纭欢褰卞瓙浠锋牸锛氬弻閲忕▼娣卞害瀵规瘮鍒嗘瀽鍥?, fontsize=52, y=1.05, fontweight='bold', color='#1A2521')
    sns.despine()
    plt.tight_layout()

    # 纭繚淇濆瓨鐩綍瀛樺湪
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
    print(f"褰卞瓙浠锋牸瀵规瘮鍥惧凡鐢熸垚: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_shadow_price_chart()
    print("Done")

