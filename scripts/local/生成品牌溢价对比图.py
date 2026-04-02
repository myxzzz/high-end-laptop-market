import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 璁剧疆涓枃瀛椾綋涓庡叏灞€鏍峰紡
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

DATA_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛鍒嗘瀽缁撴灉"
INPUT_FILE = os.path.join(DATA_PATH, "鍝佺墝纭欢婧环瀵规瘮鍒嗘瀽.csv")
OUTPUT_DIR = os.path.join(DATA_PATH, "鍙鍖栧浘鐗?)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "鍝佺墝纭欢婧环鐭╅樀鍒嗘瀽鍥?png")

def generate_premium_analysis_chart():
    # 1. 鍔犺浇鏁版嵁
    try:
        df = pd.read_csv(INPUT_FILE, encoding='gbk')
    except:
        df = pd.read_csv(INPUT_FILE, encoding='utf-8')

    # 鎺掑簭锛氭寜婧环鍊嶇巼浠庨珮鍒颁綆
    df = df.sort_values('婧环鍊嶇巼', ascending=False)

    # 2. 缁樺浘璁剧疆
    plt.figure(figsize=(26, 16), dpi=150, facecolor='#F8F9F9')
    ax = plt.gca()
    
    # 浣跨敤鏁ｇ偣鍥?姘旀场鍥惧睍绀虹煩闃靛叧绯伙紝鎴栬€呴珮绾ф潯褰㈠浘
    # 杩欓噷鎴戜滑閲囩敤鈥滅粍鍚堝潗鏍囪酱鏉″舰鍥锯€濇潵灞曠ず 鍘傚晢浠锋牸 vs 甯傚満浠锋牸
    
    # 鍒涘缓 鍝佺墝+纭欢 鐨勭粍鍚堟爣绛?
    df['缁勫悎椤圭洰'] = df['鍝佺墝'] + "\n(" + df['纭欢椤圭洰'] + ")"
    
    # 缁樺埗婧环鍊嶇巼鏉″舰鍥?
    # 棰滆壊鏍规嵁鈥滆瘎浠封€濇潵瀹?
    color_map = {'鏆村埄': '#E74C3C', '甯歌': '#F1C40F', '鑹績': '#2ECC71'}
    
    # 鏄惧紡浼犻€掑浐瀹氱殑棰滆壊鍒楄〃缁?palette锛岄伩鍏?hue 鏄犲皠瀵艰嚧鐨勬墍鏈夊彉鑹查棶棰?
    # 鍚屾椂灏嗚瘎浠峰垪鏄犲皠鍒板叿浣撶殑棰滆壊
    df['棰滆壊'] = df['璇勪环'].map(color_map)
    
    bars = sns.barplot(data=df, x='缁勫悎椤圭洰', y='婧环鍊嶇巼', hue='璇勪环', palette=color_map, dodge=False)
    
    # 娣诲姞1.0鍊嶅弬鑰冪嚎锛堝嵆骞充环绾匡級
    plt.axhline(y=1.0, color='#34495E', linestyle='--', linewidth=3, alpha=0.6, label='甯傚満鍩哄噯浠风嚎(1.0x)')

    # 3. 鏁版嵁鏍囨敞 (鍐嶆鍔犲ぇ瀛楀彿)
    for i, bar in enumerate(ax.patches):
        height = bar.get_height()
        if height > 0:
            # 鏍囨敞鍊嶇巼 - 鎻愬崌鑷?32pt
            ax.annotate(f'{height:.2f}x', 
                        (bar.get_x() + bar.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=32, fontweight='bold',
                        xytext=(0, 10), textcoords='offset points', color='#1A2521')
            
            # 鏍囨敞 瀹為檯浠锋牸瀵规瘮 - 鎻愬崌鑷?24pt
            # 鑾峰彇褰撳墠 bar 瀵瑰簲鐨勫師濮嬫暟鎹储寮?
            # 娉ㄦ剰锛歛x.patches 鐨勯『搴忓彲鑳戒笌 df 椤哄簭涓€鑷达紝浣嗕负浜嗙ǔ濡ワ紝鎴戜滑閫氳繃 i 鑾峰彇
            brand_price = df.iloc[i]['鍘傚晢鍗囩骇鍗曚环_姣廏B']
            market_price = df.iloc[i]['闆跺敭甯傚満鍗曚环_姣廏B']
            price_text = f"鍘傚晢:锟brand_price:.1f}\n甯傚満:锟market_price:.1f}"
            
            # 鏂囧瓧鍨傜洿浣嶇疆鑷€傚簲
            txt_y = height / 2 if height > 1.2 else height + 0.4
            txt_color = 'white' if height > 1.2 else '#2C3E50'
            
            ax.text(bar.get_x() + bar.get_width() / 2., txt_y, price_text, 
                    ha='center', va='center', fontsize=24, color=txt_color, fontweight='bold',
                    bbox=dict(facecolor='none', edgecolor='none', alpha=0.5))

    # 4. 瑙嗚淇グ (瀛楀彿鎻愬崌)
    plt.title('2025骞寸瑪璁版湰鍝佺墝纭欢婧环娣卞害閫忚 (楂樻竻鐗瑰ぇ瀛楃増)', fontsize=56, pad=70, fontweight='bold', color='#1A2521')
    plt.xlabel('鍝佺墝鍙婄‖浠堕」鐩?, fontsize=38, labelpad=25, fontweight='bold')
    plt.ylabel('婧环鍊嶇巼 (涓庡競鍦轰环鐩告瘮)', fontsize=38, labelpad=25, fontweight='bold')
    
    # 澧炲姞鍒诲害瀛楀彿
    plt.xticks(fontsize=28, fontweight='bold')
    plt.yticks(fontsize=30)
    
    # 鍥句緥鍔犲ぇ
    plt.legend(title='浠峰€艰瘎浠峰垎绾?, title_fontsize=34, fontsize=30, loc='upper right', frameon=True, shadow=True)

    # 鍏抽敭閫昏緫鎵规敞鍔犲ぇ
    plt.text(0.98, 0.45, "馃毄 璀︽儠锛歕n鍊嶇巼 > 2.0x 灞炰簬瓒呴珮婧环鍖哄煙\n澶氬嚭鐜板湪鐗瑰畾鍝佺墝瀛樺偍鍗囩骇涓?, 
             transform=ax.transAxes, fontsize=32, color='#C0392B', fontweight='bold',
             ha='right', bbox=dict(facecolor='#FDEDEC', edgecolor='#E74C3C', boxstyle='round,pad=1.2'))

    sns.despine()
    plt.tight_layout()

    # 纭繚淇濆瓨鐩綍瀛樺湪
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
    print(f"鍝佺墝婧环鐭╅樀鍒嗘瀽鍥惧凡鐢熸垚: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_premium_analysis_chart()
    print("Done")

