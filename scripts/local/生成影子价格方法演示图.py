import matplotlib.pyplot as plt
import numpy as np
import os

# 璁剧疆涓枃瀛椾綋
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

DATA_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛鍒嗘瀽缁撴灉"
OUTPUT_DIR = os.path.join(DATA_PATH, "鍙鍖栧浘鐗?)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "褰卞瓙浠锋牸璁＄畻閫昏緫婕旂ず鍥?png")

def generate_logic_demo_chart():
    # 妯℃嫙鏁版嵁锛氫互 2026娆?MacBook Pro 14 涓轰緥
    # 16G+1T 鐗堟湰 vs 24G+1T 鐗堟湰
    base_price = 16999  # 鍩虹浠锋牸鍗囩骇
    prices = [16999, 16999 + 1500] # 妯℃嫙 1500 鍏冨樊浠?

    sku_names = ['2026娆?MacBook Pro 14\n(16GB / 1TB)', '2026娆?MacBook Pro 14\n(24GB / 1TB)']

    # 1. 缁樺浘
    plt.figure(figsize=(26, 16), dpi=150, facecolor='#FDFDFD')
    ax = plt.gca()

    # 缁樺埗鏇村鐨勬煴瀛愪互鍑忓皯鎷ユ尋鎰?
    bar_width = 0.5
    indices = [0, 1.2] # 澧炲姞涓や釜鏌卞瓙涔嬮棿鐨勮窛绂?
    
    # 缁樺埗鍩虹浠锋牸閮ㄥ垎
    plt.bar(indices, [base_price, base_price], width=bar_width, label='鍏辨湁閰嶇疆 (M5鑺墖/楂樼骇妯″叿/瑙嗙綉鑶滃睆)', 
            color='#D5DBDB', edgecolor='#7F8C8D', linewidth=2)
    # 缁樺埗婧环宸€奸儴鍒?
    plt.bar(indices[1], 1500, bottom=base_price, width=bar_width, label='鍐呭瓨鍗囩骇宸环 (8GB)', 
            color='#E74C3C', edgecolor='#C0392B', linewidth=2)

    # 2. 浠锋牸瀵规瘮鏍囨敞 (鐩存帴绉诲埌鏌变綋涓婃柟锛岄伩鍏嶉噸鍙?
    plt.text(indices[0], base_price + 300, f'锟base_price:,.0f}', ha='center', fontsize=34, fontweight='bold', color='#2C3E50')
    plt.text(indices[1], base_price + 1500 + 300, f'锟base_price+1500:,.0f}', ha='center', fontsize=34, fontweight='bold', color='#C0392B')
    
    # 鏌变綋鍐呴儴鏍囨敞鍏辨湁閮ㄥ垎
    plt.text(indices[0], base_price/2, "鍩虹鐗╂枡浠峰€?, ha='center', va='center', fontsize=32, fontweight='bold', color='#566573')
    plt.text(indices[1], base_price/2, "鍩虹鐗╂枡浠峰€?, ha='center', va='center', fontsize=32, fontweight='bold', color='#566573')

    # 3. 閫昏緫杩炴帴涓庡垎鏋愭 (绉诲姩鍒板彸渚у紑闃斿尯鍩?
    # 缁樺埗姘村钩鎻愮ず铏氱嚎
    plt.hlines(y=[base_price, base_price+1500], xmin=indices[0]+bar_width/2, xmax=indices[1]-bar_width/2, 
               colors='#7F8C8D', linestyles='--', alpha=0.5)
    
    # 鍏紡姘旀场 (璋冨ぇ濉厖锛屽姞澶ц竟璺?
    formula_text = (
        "绗竴姝ワ細銆愬奖瀛愪环鏍煎墺绂汇€慭n"
        " 螖 甯傚満鍞环 (锟?,500)\n"
        " 鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€ = 锟?87.5/GB\n"
        " 螖 鍐呭瓨瀹归噺 (8 GB)\n\n"
        "绗簩姝ワ細銆愭孩浠风巼璁＄畻銆慭n"
        " 鍝佺墝褰卞瓙浠?(锟?87.5)\n"
        " 鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€ = 1.79 鍊峔n"
        " 闆跺敭甯傚満浠?(锟?05.0)\n\n"
        " 缁撹锛歕n 璇ユ満鍨嬪唴瀛樺崌绾ф孩浠风巼楂樿揪 79%\n 杩滆秴琛屼笟骞冲潎姘村钩"
    )
    plt.text(1.7, (base_price + 750), formula_text, fontsize=32, fontweight='bold', 
             bbox=dict(facecolor='#FEF9E7', edgecolor='#F1C40F', boxstyle='round,pad=1.5'),
             va='center')

    # 4. 淇グ - 鏋佽嚧澶у瓧娓呮櫚鐗?
    plt.title('2026娆?MacBook Pro (M5)锛氬奖瀛愪环鏍尖€滃樊鍊煎墺绂烩€濋€昏緫婕旂ず', fontsize=56, pad=80, fontweight='bold', color='#1A2521')
    plt.ylabel('鏈哄瀷甯傚満鍞环 (浜烘皯甯?', fontsize=38, labelpad=25)
    
    plt.xticks(indices, sku_names, fontsize=32, fontweight='bold')
    plt.yticks(fontsize=30)
    
    plt.legend(fontsize=28, loc='upper left', frameon=True, shadow=True)
    
    # 璁剧疆鍚堢悊鐨勫潗鏍囪酱鑼冨洿锛岄槻姝㈡枃瀛楀嚭鐣?
    plt.xlim(-0.6, 3.2)
    plt.ylim(0, base_price + 4500)

    sns.despine()
    plt.tight_layout()

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
    print(f"婕旂ず鍥惧凡鐢熸垚: {OUTPUT_FILE}")

if __name__ == "__main__":
    import seaborn as sns
    generate_logic_demo_chart()
    print("Done")

