import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 璁剧疆涓枃瀛椾綋涓庡叏灞€鏍峰紡
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

DATA_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛鍒嗘瀽缁撴灉"
INPUT_FILE = os.path.join(DATA_PATH, "涓嶅悓绫荤‖浠跺崰姣?csv")
OUTPUT_DIR = os.path.join(DATA_PATH, "鍙鍖栧浘鐗?)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "鏈哄瀷妗ｄ綅鍞环涓庣‖浠跺崰姣斿叧绯诲浘.png")

def generate_tier_logic_chart():
    # 1. 鍔犺浇鏁版嵁
    try:
        df = pd.read_csv(INPUT_FILE, encoding='utf-8')
    except:
        df = pd.read_csv(INPUT_FILE, encoding='gbk')

    # 鎺掑簭锛氭寜鍞环浠庝綆鍒伴珮灞曠ず妗ｄ綅婕旇繘
    df = df.sort_values("璇ュ钩鍧囨。鍞环", ascending=True)

    # 2. 缁樺浘 - 鍙岃酱鍥?(鍞环 vs 鍗犳瘮)
    fig, ax1 = plt.subplots(figsize=(26, 14), dpi=150, facecolor='#FDFDFD')
    
    # --- 鏌辩姸鍥撅細灞曠ず骞冲潎鍞环 ---
    color_price = '#3498DB'
    bars = sns.barplot(data=df, x='鏈哄瀷妗ｄ綅', y='璇ュ钩鍧囨。鍞环', color=color_price, ax=ax1, alpha=0.7, label='骞冲潎妗ｄ綅鍞环')
    ax1.set_ylabel('骞冲潎妗ｄ綅鍞环 (鍏?', fontsize=34, fontweight='bold', color=color_price, labelpad=20)
    ax1.tick_params(axis='y', labelsize=28, colors=color_price)
    ax1.set_xlabel('', fontsize=0) # 鍒犳帀X杞存爣棰?
    ax1.set_title('鍚勬。浣嶆満鍨嬶細甯傚満鍞环涓庢牳蹇冪‖浠跺崰姣斿叧绯荤洿瑙傞€忚', fontsize=52, pad=60, fontweight='bold')

    # 鍞环鏁板€兼爣娉ㄤ笌妗ｄ綅鍚嶇О (灏嗘。浣嶅悕鐩存帴鍐欏湪鏌变綋搴曢儴锛岃В鍐崇湅涓嶆竻鐨勯棶棰?
    meta_tiers = df['鏈哄瀷妗ｄ綅'].tolist()
    for i, p in enumerate(ax1.patches):
        # 1. 鏍囨敞妗ｄ綅鍚嶇О (鏀惧湪鏌卞瓙鏍归儴涓婃柟涓€鐐癸紝鐢ㄩ啋鐩殑榛戝簳鐧藉瓧)
        ax1.text(p.get_x() + p.get_width() / 2., 2000, meta_tiers[i], 
                 ha='center', va='bottom', fontsize=32, fontweight='bold', color='white',
                 bbox=dict(facecolor='#2C3E50', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.5'))
        
        # 2. 鏍囨敞鍞环
        ax1.annotate(f'锟p.get_height():,.0f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=34, fontweight='bold',
                    xytext=(0, 10), textcoords='offset points', color=color_price)

    # --- 鎶樼嚎鍥撅細灞曠ず纭欢鍗犳瘮 ---
    # 淇鍒楀悕涓?CSV 涓疄闄呭瓨鍦ㄧ殑 '纭欢鍗犳瘮'
    ax2 = ax1.twinx() 
    color_ratio = '#E74C3C'
    sns.lineplot(data=df, x='鏈哄瀷妗ｄ綅', y='纭欢鍗犳瘮', color=color_ratio, ax=ax2, marker='o', markersize=20, linewidth=6, label='纭欢浠峰€煎崰姣?)
    ax2.set_ylabel('鏍稿績纭欢浠锋牸鍗犳瘮 (%)', fontsize=34, fontweight='bold', color=color_ratio, labelpad=20)
    ax2.tick_params(axis='y', labelsize=28, colors=color_ratio)
    ax2.set_ylim(0, 0.6) 

    # 鍗犳瘮鏁板€兼爣娉?
    for i in range(len(df)):
        val = df.iloc[i]['纭欢鍗犳瘮']
        ax2.annotate(f'{val:.1%}', 
                    (i, val), 
                    xytext=(0, 25), textcoords='offset points',
                    ha='center', va='bottom', fontsize=32, fontweight='bold',
                    color=color_ratio, bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

    # 3. 瑁呴グ涓庝慨楗?
    # 娣诲姞鑳屾櫙閫昏緫娉ㄩ噴
    insight_text = "馃挕 鍏抽敭鍙戠幇锛歕n涓珮绔満鍨?1.6涓?纭欢鍗犳瘮瑙﹀簳(31%)\n鏃楄埌鏈哄瀷閫氳繃鈥淎I缁戝畾鈥濆洖褰掔ǔ鍗犳瘮"
    plt.text(0.02, 0.85, insight_text, transform=ax1.transAxes, fontsize=30, 
             fontweight='bold', color='#2C3E50', bbox=dict(facecolor='#EBEDEF', boxstyle='round,pad=1'))

    plt.xticks([], []) # 褰诲簳绂佺敤 X 杞村埢搴︽爣绛撅紝閬垮厤閲嶅彔涓旂湅涓嶆竻
    sns.despine(top=True, right=False)
    plt.tight_layout()

    # 纭繚鐩綍瀛樺湪
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
    print(f"妗ｄ綅鍗犳瘮鍥惧凡鐢熸垚: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_tier_logic_chart()
    print("Done")

