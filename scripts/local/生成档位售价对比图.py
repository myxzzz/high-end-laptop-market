import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 璁剧疆涓枃瀛椾綋涓庡叏灞€鏍峰紡
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 24  # 鍏ㄩ潰閲囩敤瓒呭ぇ瀛椾綋

DATA_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛鍒嗘瀽缁撴灉"
FILE_NAME = "涓嶅悓绫荤‖浠跺崰姣?csv"
OUTPUT_DIR = os.path.join(DATA_PATH, "鍙鍖栧浘鐗?)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "鍚勬。浣嶅钩鍧囧敭浠峰浘_涓撲笟澶у瓧鐗?png")

def generate_simple_price_chart():
    # 1. 鍔犺浇鏁版嵁
    try:
        df = pd.read_csv(os.path.join(DATA_PATH, FILE_NAME), encoding='utf-8')
    except:
        df = pd.read_csv(os.path.join(DATA_PATH, FILE_NAME), encoding='gbk')
    
    # 鎸夊敭浠风敱楂樺埌浣庢帓鍒?
    df = df.sort_values("璇ュ钩鍧囨。鍞环", ascending=False)

    # 2. 缁樺浘
    plt.figure(figsize=(16, 10), dpi=300, facecolor='#F8F9FA')
    ax = plt.gca()
    ax.set_facecolor('#F8F9FA')

    # 浣跨敤 Seaborn 缁樺埗鏉″舰鍥?
    colors = sns.color_palette("flare", n_colors=len(df)) # 閲囩敤娓愬彉鑹茬郴
    ax = sns.barplot(
        data=df, 
        x='璇ュ钩鍧囨。鍞环', 
        y='鏈哄瀷妗ｄ綅', 
        palette=colors,
        hue='鏈哄瀷妗ｄ綅',
        legend=False
    )

    # 娣诲姞鏁板€兼爣娉?
    for p in ax.patches:
        width = p.get_width()
        ax.annotate(f'锟width:,.0f}', 
                    (width, p.get_y() + p.get_height() / 2),
                    xytext=(15, 0), 
                    textcoords='offset points',
                    va='center', 
                    fontsize=26, 
                    fontweight='bold',
                    color='#2C3E50')

    # 淇グ鍧愭爣杞?
    plt.title('2025骞寸瑪璁版湰甯傚満锛氬悇妗ｄ綅鏈哄瀷骞冲潎鍞环瀵规瘮', fontsize=36, pad=40, fontweight='bold', color='#1A2521')
    plt.xlabel('骞冲潎闆跺敭璇勪及浠?(鍏?', fontsize=24, labelpad=20)
    plt.ylabel('甯傚満缁嗗垎妗ｄ綅', fontsize=24, labelpad=20)
    
    # 闅愯棌涓婃柟鍜屽彸鏂圭殑杈规
    sns.despine(top=True, right=True)
    
    # 璋冩暣甯冨眬
    plt.tight_layout()

    # 纭繚淇濆瓨鐩綍瀛樺湪
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    # 淇濆瓨缁撴灉
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
    print(f"涓撲笟鍞环鍥惧凡鐢熸垚: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_simple_price_chart()
    print("Done")

