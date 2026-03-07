import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =================================================================
# 1. 鍩虹閰嶇疆锛氳繖閲屽拰 SQL 鐨勮鍥?View)鎴栬〃杩炴帴鍓嶇殑鍑嗗绫讳技
# =================================================================
# 璁剧疆涓枃瀛椾綋锛堣В鍐冲彲瑙嗗寲鏈€澶寸柤鐨勪腑鏂囦贡鐮侀棶棰橈級
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 璺緞绠＄悊 (浣跨敤 raw string 澶勭悊 Windows 鐨勫弽鏂滄潬)
COMMENT_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛== 璇勮 =="
RESULT_PATH = r"c:\Users\Administrator\Desktop\25涓夊垱璧涜祫鏂橽绗旇鏈數鑴戞暟鎹甛鍒嗘瀽缁撴灉"
FILE_MAP = {"0": "0-鏈€鏂版帓搴?xlsx", "1": "1-鏈€鏂版帓搴?xlsx", "2": "2-鏈€鏂版帓搴?xlsx"}
TIER_NAMES = {"0": "鍏ラ棬鍙婁富娴佹。浣?, "1": "楂樼鍙婃€ц兘妗ｄ綅", "2": "椤剁骇鍙婃棗鑸版。浣?}

# 瀹氫箟鎴戜滑鍏冲績鐨勨€滃績鏅虹淮搴︹€?
KEYWORDS = ["灞忓箷", "鎬ц兘", "娴佺晠", "杞昏杽", "鏁ｇ儹", "AI", "璐ㄦ劅", "棰滃€?, "鎬т环姣?]

def analyze_tier_comments():
    """
    鏁版嵁鎻愬彇灞傦細鐩稿綋浜?SQL 鐨?SELECT + GROUP BY
    """
    results = []
    # 瀹氫箟鈥滄€т环姣斺€濈浉鍏崇殑杩戜箟璇嶄笡鏋楋紝鐢ㄤ簬缁煎悎缁熻锛圢LP 閲岀殑妯＄硦鍖归厤鎬濇兂锛?
    value_synonyms = ["鎬т环姣?, "瀹炴儬", "鍥借ˉ", "鍒掔畻", "渚垮疁", "琛ヨ创", "鐪熼"]

    for tier, filename in FILE_MAP.items():  # 澶or寰幆鍏堟彁鍙栧瓧鍏?12鏂囦欢
        file_full_path = os.path.join(COMMENT_PATH, filename) # 鍒朵綔閬嶅巻瀹屽畬鏁存暣鐨勬枃浠惰矾寰?
        if os.path.exists(file_full_path):
            df = pd.read_excel(file_full_path)
            # 灏嗘墍鏈夎瘎璁烘嫾鎺ユ垚涓€涓秴绾уぇ鏂囨湰锛屾柟渚跨畻鎬昏瘝棰?
            full_text = " ".join(df['璇勪环鍐呭'].astype(str))
            
            # 鎵嬪姩娉ㄥ叆鈥滄€т环姣斺€濈患鍚堢粺璁?(杩欓噷鐨勫簳灞傞€昏緫灏辨槸缁熻瀛愪覆鍑虹幇娆℃暟)
            value_count = sum(full_text.count(s) for s in value_synonyms)
            
            # 璁＄畻鎬诲叧閿瘝鎻愬強閲?鈥斺€?杩欓噷鐨勯€昏緫闈炲父鍍?SQL 鐨勭獥鍙ｅ嚱鏁?SUM() OVER(PARTITION BY Tier)
            # 鎴戜滑闇€瑕佺煡閬撳湪璇ユ。浣嶄笅锛岃繖鍑犱釜鏍稿績鍏虫敞鐐瑰姞璧锋潵涓€鍏辫鎻愬埌浜嗗灏戞锛屼綔涓哄垎姣?
            other_keywords_count = sum(full_text.count(word) for word in KEYWORDS if word != "鎬т环姣?)
            total_hits = other_keywords_count + value_count
            
            for word in KEYWORDS:
                count = value_count if word == "鎬т环姣? else full_text.count(word)  # word鏄湪閬嶅巻鍒楄〃KEYWORDS閲岄潰鐨勮瘝
                
                # 鎸囨爣 1: 鎻愬強瀵嗗害 (姣?00鏉¤瘎璁烘彁鍑犳) -> 鍙嶆槧缁濆鐑害锛屽垎姣嶄负涓€涓。浣嶇殑浜烘暟
                density = (count / len(df)) * 100
                
                # 鎸囨爣 2: 妗ｄ綅鍐呭崰姣?-> 鍙嶆槧鐩稿鏉冮噸 (鐜綋鍥剧殑鏍稿績)锛屽垎姣嶄负鎵€鏈夎瘽棰樻暟
                # 杩欏氨鏄?SQL 閲岀殑: count / SUM(count) OVER(PARTITION BY 妗ｄ綅)
                ratio = (count / total_hits * 100) if total_hits > 0 else 0
                
                results.append({
                    "妗ｄ綅": TIER_NAMES[tier],
                    "鍏抽敭璇?: word,
                    "鎻愬強棰戠巼(%)": density,
                    "妗ｄ綅鍐呭崰姣?: ratio
                })
                
                # 浠呭睍绀哄墠涓ゆ寰幆鐨勫師濮嬬姸鎬侊紝閬垮厤鍒峰睆
                if len(results) <= 2:
                    print(f"\n[鏁欏鎻愮ず] 褰撳墠 results 鍒楄〃鍐呭 (鍘熷妗ｆ琚嬪舰寮?:\n{results}\n")
                    
    return pd.DataFrame(results)

if __name__ == "__main__":
    # 鍚庨潰鍙互缁х画璋冪敤缁樺浘鍑芥暟
    df_data = analyze_tier_comments()
    # ... existing code ...
def plot_tier_donut_gallery(df_res):
    """
    鍙鍖栧眰 A锛氱幆浣撳浘銆傚睍绀烘暟鎹儗鍚庣殑鈥滅粨鏋勬瘮閲嶁€濄€?
    """
    if df_res.empty: return

    # 1x3 鐢诲竷锛氬苟鎺掑睍绀轰笁涓。浣嶏紝鏂逛究璇勫妯悜瀵规瘮
    fig, axes = plt.subplots(1, 3, figsize=(32, 14), dpi=150, facecolor='#FDFDFD')
    colors = sns.color_palette("muted", n_colors=len(KEYWORDS))

    for i, tier_name in enumerate(TIER_NAMES.values()):
        ax = axes[i]
        tier_data = df_res[df_res['妗ｄ綅'] == tier_name]
        
        # 鐢婚ゼ鍥?
        wedges, texts, autotexts = ax.pie(
            tier_data['妗ｄ綅鍐呭崰姣?], 
            labels=tier_data['鍏抽敭璇?],
            autopct='%1.1f%%',
            startangle=140,
            colors=colors,
            pctdistance=0.75,
            textprops={'fontsize': 24, 'fontweight': 'bold'}
        )
        
        # 鍙樷€滈ゼ鍥锯€濅负鈥滅幆浣撳浘鈥濈殑榄旀硶锛氬湪涓績鐢讳竴涓櫧鑹茬殑鍦?
        centre_circle = plt.Circle((0,0), 0.60, fc='white')
        ax.add_artist(centre_circle)
        
        # 鍦ㄥ渾蹇冧腑鍐欎笂鏂囨锛屽鍔犺璁℃劅
        ax.text(0, 0, tier_name.replace("鍙?, "\n鍙?), 
                ha='center', va='center', fontsize=34, fontweight='black', color='#2C3E50')
        ax.set_title(f"Tier {i}: {tier_name}", fontsize=36, pad=30, fontweight='bold', color='#1A237E')

    plt.suptitle('娑堣垂鍔ㄦ満婕傜Щ锛氬悇妗ｄ綅鐢ㄦ埛鏍稿績蹇冩櫤鍒嗗竷', fontsize=54, y=1.05, fontweight='black', color='#B71C1C')
    plt.tight_layout()
    plt.savefig(os.path.join(RESULT_PATH, "鍙鍖栧浘鐗?, "涓嶅悓妗ｄ綅璇勪环鐜綋瀵规瘮鍥?png"), dpi=300, bbox_inches='tight')

def plot_comment_comparison_v2(df_res):
    """
    鍙鍖栧眰 B锛氬ぇ鍙峰瓧浣撶殑鏌辩姸鍥俱€傚睍绀衡€滃０閲忊€濈殑缁濆瀵规瘮銆?
    """
    plt.figure(figsize=(28, 14), dpi=150, facecolor='#FDFDFD')
    # 浣跨敤 seaborn 鐨?barplot锛屼竴琛屼唬鐮佸疄鐜?Hue 鍒嗙被锛堢浉褰撲簬 SQL 鐨勪笁缁勫姣旓級
    ax = sns.barplot(data=df_res, x='鍏抽敭璇?, y='鎻愬強棰戠巼(%)', hue='妗ｄ綅', palette="magma")
    
    # 鑷姩鏍囨敞鏁板€奸€昏緫
    for p in ax.patches:
        if p.get_height() > 0:
            ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', fontsize=22, fontweight='bold', xytext=(0, 12), textcoords='offset points')

    plt.title('2025-2026 甯傚満闇€姹傦細鍚勬。浣嶆牳蹇冨叧娉ㄧ偣鈥滃０閲忊€濆姣?, fontsize=50, pad=50, fontweight='black', color='#1B5E20')
    plt.xlabel('鍏抽敭璇嶅強鍏跺叧鑱旂皣', fontsize=34, fontweight='bold')
    plt.ylabel('鎻愬強瀵嗗害 (姣?00鏉¤瘎璁烘彁鍙婃鏁?', fontsize=34, fontweight='bold')
    plt.xticks(fontsize=30, fontweight='bold')
    plt.yticks(fontsize=26)
    plt.legend(title='鏈哄瀷妗ｄ綅娣卞害瑙ｆ瀽', fontsize=22, title_fontsize=24, loc='upper right')
    sns.despine() # 鍘绘帀涓戦檵鐨勪笂杈规鍜屽彸杈规
    plt.tight_layout()
    plt.savefig(os.path.join(RESULT_PATH, "鍙鍖栧浘鐗?, "涓嶅悓妗ｄ綅璇勪环鍏抽敭璇嶅姣斿浘_V2.png"), dpi=300, bbox_inches='tight')

if __name__ == "__main__":
    df_data = analyze_tier_comments()
    plot_comment_comparison_v2(df_data)
    plot_tier_donut_gallery(df_data)
    print("Done")
