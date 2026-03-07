import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 璁剧疆涓枃瀛椾綋
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 22 # 璋冨ぇ鍩虹瀛椾綋

DATA_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛鍒嗘瀽缁撴灉"
FILE_NAME = "涓嶅悓绫荤‖浠跺崰姣?csv"
OUTPUT_PATH = os.path.join(DATA_PATH, "鍙鍖栧浘鐗?, "鍚勬。浣嶆牳蹇冨弬鏁板姣斿浘.png")

def generate_tier_comparison_chart():
    # 1. 鍔犺浇骞舵暣鐞嗘暟鎹?
    try:
        df = pd.read_csv(os.path.join(DATA_PATH, FILE_NAME), encoding='utf-8')
    except:
        df = pd.read_csv(os.path.join(DATA_PATH, FILE_NAME), encoding='gbk')
    
    # 鎸夊敭浠蜂粠浣庡埌楂樻帓鍒楋紝鏂逛究瑙傚療瓒嬪娍
    df = df.sort_values("璇ュ钩鍧囨。鍞环", ascending=True)

    # 2. 鍒涘缓涓€涓洓鑱旀帓姘村钩鏌辩姸鍥?
    # 澧炲姞鈥滅‖浠跺崰姣斺€濆睍绀猴紝鏇寸洿瑙傚湴鎻ず鍚勬。浣嶇殑鎴愭湰缁撴瀯
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(32, 12), sharey=True)
    fig.patch.set_facecolor('#FDFDFD')

    # --- 鍥?: 骞冲潎鍞环 ---
    sns.barplot(data=df, x='璇ュ钩鍧囨。鍞环', y='鏈哄瀷妗ｄ綅', palette='Blues_d', ax=ax1, hue='鏈哄瀷妗ｄ綅', legend=False)
    ax1.set_title('馃捀 骞冲潎鍞环 (鍏?', fontsize=30, pad=30, fontweight='bold')
    ax1.set_xlabel('')
    ax1.set_ylabel('鏈哄瀷妗ｄ綅', fontsize=26, fontweight='bold')
    for p in ax1.patches:
        ax1.annotate(f'锟p.get_width():,.0f}', (p.get_width(), p.get_y() + p.get_height()/2),
                    xytext=(10, 0), textcoords='offset points', va='center', fontsize=22, fontweight='bold')

    # --- 鍥?: 骞冲潎鍐呭瓨 ---
    sns.barplot(data=df, x='骞冲潎鍐呭瓨_G', y='鏈哄瀷妗ｄ綅', palette='Greens_d', ax=ax2, hue='鏈哄瀷妗ｄ綅', legend=False)
    ax2.set_title('馃 骞冲潎鍐呭瓨 (GB)', fontsize=30, pad=30, fontweight='bold')
    ax2.set_xlabel('')
    ax2.set_ylabel('')
    for p in ax2.patches:
        ax2.annotate(f'{p.get_width():.1f} G', (p.get_width(), p.get_y() + p.get_height()/2),
                    xytext=(10, 0), textcoords='offset points', va='center', fontsize=22, fontweight='bold')

    # --- 鍥?: 骞冲潎纭洏 ---
    sns.barplot(data=df, x='骞冲潎纭洏_G', y='鏈哄瀷妗ｄ綅', palette='Oranges_d', ax=ax3, hue='鏈哄瀷妗ｄ綅', legend=False)
    ax3.set_title('馃捑 骞冲潎纭洏 (GB)', fontsize=30, pad=30, fontweight='bold')
    ax3.set_xlabel('')
    ax3.set_ylabel('')
    for p in ax3.patches:
        ax3.annotate(f'{p.get_width():,.0f} G', (p.get_width(), p.get_y() + p.get_height()/2),
                    xytext=(10, 0), textcoords='offset points', va='center', fontsize=22, fontweight='bold')

    # --- 鍥?: 纭欢浠峰€煎崰姣?(鏍稿績鍒嗘瀽椤? ---
    # 浣跨敤绾㈢传鑹茬郴绐佸嚭鈥滃搧鐗屾孩浠封€濅弗閲嶇殑鍖哄煙
    sns.barplot(data=df, x='纭欢鍗犳瘮', y='鏈哄瀷妗ｄ綅', palette='RdPu_r', ax=ax4, hue='鏈哄瀷妗ｄ綅', legend=False)
    ax4.set_title('鈿栵笍 纭欢浠峰€煎崰姣?(%)', fontsize=30, pad=30, fontweight='bold', color='#C0392B')
    ax4.set_xlabel('')
    ax4.set_ylabel('')
    ax4.set_xlim(0, 0.6) # 鍗犳瘮閫氬父鍦?-1涔嬮棿锛屼负浜嗙湅娓呭樊寮傝缃埌0.6
    for p in ax4.patches:
        val = p.get_width()
        color = 'red' if val < 0.35 else 'black' # 鍗犳瘮杩囦綆鐨勭敤绾㈣壊鏍囨敞
        ax4.annotate(f'{val:.1%}', (val, p.get_y() + p.get_height()/2),
                    xytext=(10, 0), textcoords='offset points', va='center', 
                    fontsize=24, fontweight='bold', color=color)

    # 3. 鎬绘爣棰樹笌甯冨眬
    plt.suptitle('鍚勬。浣嶇瑪璁版湰鏍稿績鍙傛暟瀵规瘮 (鑷冲皧楂樻竻澶у瓧鐗?', fontsize=42, y=1.08, fontweight='bold', color='#2C3E50')
    plt.tight_layout()

    
    # 纭繚淇濆瓨鐩綍瀛樺湪
    if not os.path.exists(os.path.dirname(OUTPUT_PATH)):
        os.makedirs(os.path.dirname(OUTPUT_PATH))
        
    plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight')
    print(f"瀵规瘮鏌辩姸鍥惧凡鐢熸垚: {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_tier_comparison_chart()
    print("Done") # 鏄惧紡鎵撳嵃鎴愬姛鏍囧織

