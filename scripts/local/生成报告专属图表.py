import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# 璁剧疆涓枃瀛椾綋
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 22  # 璋冨ぇ涓鸿嚦灏婂ぇ瀛楃増

DATA_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛鍒嗘瀽缁撴灉"
OUTPUT_DIR = os.path.join(DATA_PATH, "鍙鍖栧浘鐗?)
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def generate_market_share_pie():
    """鐢熸垚绮剧編鐨勫搧鐗屼环鍊间唤棰濈幆褰㈠浘"""
    df = pd.read_csv(os.path.join(DATA_PATH, "hhi璁＄畻缁撴灉.csv"))
    
    core_brands = ['鑱旀兂', '鍗庣', '鑻规灉', '鎯犳櫘', '鎴村皵', '寰槦', '鍗庝负']
    df_core = df[df['鍝佺墝'].isin(core_brands)].copy()
    df_others = df[~df['鍝佺墝'].isin(core_brands)]
    
    if not df_others.empty:
        others_share = df_others['浠峰€间唤棰漘鍗犳瘮'].sum()
        new_row = pd.DataFrame({'鍝佺墝': ['鍏朵粬鍝佺墝'], '浠峰€间唤棰漘鍗犳瘮': [others_share]})
        plot_df = pd.concat([df_core[['鍝佺墝', '浠峰€间唤棰漘鍗犳瘮']], new_row], ignore_index=True)
    else:
        plot_df = df_core[['鍝佺墝', '浠峰€间唤棰漘鍗犳瘮']]

    plot_df = plot_df.sort_values('浠峰€间唤棰漘鍗犳瘮', ascending=False)

    plt.figure(figsize=(14, 12), dpi=100)
    # 浣跨敤鏇寸幇浠ｇ殑閰嶈壊
    colors = sns.color_palette('pastel', n_colors=len(plot_df))
    
    # 缁樺埗鐜舰鍥?
    explode = [0.03] * len(plot_df) # 鎵€鏈夊潡閮界◢寰暀涓€鐐圭紳闅?
    
    wedges, texts, autotexts = plt.pie(
        plot_df['浠峰€间唤棰漘鍗犳瘮'], 
        labels=plot_df['鍝佺墝'],
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        explode=explode,
        shadow=False,
        pctdistance=0.75,
        wedgeprops={'width': 0.4, 'edgecolor': 'white', 'linewidth': 2}
    )
    
    # 瀛椾綋鍔犲己
    plt.setp(autotexts, size=24, weight="bold")
    plt.setp(texts, size=28, weight="bold")
    
    # 涓績鏂囧瓧
    plt.text(0, 0, '2025\n甯傚満鍒嗗竷', ha='center', va='center', fontsize=32, fontweight='bold', color='#333333')
    
    plt.title('2025骞寸瑪璁版湰甯傚満鍝佺墝浠峰€间唤棰濆崰姣?, fontsize=42, pad=60, fontweight='bold')
    
    plt.axis('equal')
    save_path = os.path.join(OUTPUT_DIR, "鍝佺墝浠峰€间唤棰濆崰姣旂幆褰㈠浘_鑷冲皧澶у瓧鐗?png")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"鐜舰鍥惧凡鐢熸垚: {save_path}")

def generate_hhi_status_bar():
    """鐢熸垚澶у瓧鐗?HHI 鐜扮姸璇勪及鏉?""
    hhi_value = 2307.12
    
    plt.figure(figsize=(18, 9), dpi=100)
    ax = plt.gca()
    
    # 鑳屾櫙鑹插潡
    plt.axvspan(0, 1500, color='#2ecc71', alpha=0.15)
    plt.axvspan(1500, 2500, color='#f1c40f', alpha=0.15)
    plt.axvspan(2500, 5000, color='#e74c3c', alpha=0.15)
    
    # 鎸囩ず绾?
    plt.axvline(hhi_value, color='#2C3E50', linestyle='-', linewidth=6)
    
    # 鎸囩ず鏍囨敞
    plt.annotate(f'褰撳墠 HHI: {hhi_value}\n涓害闆嗕腑甯傚満', 
                 xy=(hhi_value, 0.4), xytext=(hhi_value, 0.88),
                 arrowprops=dict(facecolor='#2C3E50', shrink=0.05, width=6),
                 ha='center', fontsize=32, fontweight='bold', 
                 bbox=dict(boxstyle="round4,pad=0.8", fc="white", ec="#2C3E50", alpha=1, lw=2))

    plt.xlim(0, 4000)
    plt.ylim(0, 1)
    plt.yticks([]) 
    plt.xticks([0, 1500, 2500, 4000], ['0', '1500\n(绔炰簤鐘舵€?', '2500\n(闆嗕腑绾㈢嚎)', '4000+'], fontsize=26, fontweight='bold')
    plt.xlabel('璧笇鏇?璧姮杈惧皵鎸囨暟 (HHI) 椋庨櫓鍒诲害', fontsize=28, labelpad=20, fontweight='bold')
    plt.title('甯傚満绔炰簤鏍煎眬璇勪及 (HHI)', fontsize=42, pad=60, fontweight='bold')
    
    plt.text(750, 0.15, '浣庡害闆嗕腑', ha='center', color='#1e8449', fontsize=26, fontweight='bold')
    plt.text(2000, 0.15, '涓害闆嗕腑', ha='center', color='#9a7d0a', fontsize=26, fontweight='bold')
    plt.text(3250, 0.15, '鏋侀珮闆嗕腑', ha='center', color='#943126', fontsize=26, fontweight='bold')

    plt.tight_layout()
    save_path = os.path.join(OUTPUT_DIR, "甯傚満闆嗕腑搴HI鐜扮姸璇勪及鏉鑷冲皧澶у瓧鐗?png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"HHI璇勪及鍥惧凡鐢熸垚: {save_path}")

if __name__ == "__main__":
    generate_market_share_pie()
    generate_hhi_status_bar()

