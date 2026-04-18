import streamlit as st
import os

# 1. 視覺鎖定：V74 質感、去黑底卡片、茶包垂直換行、LINE 原生協議、動態溫暖提示
st.set_page_config(page_title="米寶漢方｜您的植感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域鎖定 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    .block-container { padding-top: 0.5rem !important; padding-bottom: 60px !important; }

    /* 隱藏原生組件 */
    #MainMenu, footer, header { visibility: hidden !important; }

    /* 標題與引導：V74 比例 */
    h3 { font-size: 1.1rem !important; font-weight: 700 !important; margin: 10px 0 !important; text-align: center !important; color: #7A8450 !important; }
    .question-text { font-size: 1.05rem !important; font-weight: bold !important; text-align: center !important; margin-bottom: 15px !important; }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 10px; font-size: 0.8rem; }

    /* Logo 鎖定 */
    [data-testid="stImage"] img { max-height: 50px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: -10px !important; }

    /* 選項點點與選中加粗 (V74 靈魂) */
    [data-testid="stRadio"] div[role="radiogroup"] [data-testid="stRadioButton"] > div:first-child { transform: scale(0.6) !important; }
    [data-testid="stRadio"] label {
        border-radius: 12px !important; padding: 10px 18px !important;
        width: 100% !important; border: 1px solid rgba(0,0,0,0.05) !important;
        display: flex !important; justify-content: flex-start !important; 
        text-align: left !important; font-size: 0.95rem !important; 
    }
    div[data-testid="stRadio"] div[role="radiogroup"] div[aria-checked="true"] label {
        font-size: 1.1rem !important; font-weight: 900 !important;   
        color: #2D301D !important; border: 2px solid #7A8450 !important;
        background-color: #E9EDC9 !important;
    }

    /* 精品配方卡片 */
    .recipe-card {
        background-color: #F8F9F1 !important; border: 1.5px solid #E9EDC9 !important; border-radius: 15px !important;
        padding: 20px !important; font-size: 1rem !important; line-height: 1.6 !important;
        white-space: pre-wrap !important; word-break: break-all !important; margin: 15px 0 !important;
    }

    /* LINE 原生跳轉按鈕 */
    .line-native-btn {
        display: block !important; background-color: #06C755 !important; color: white !important;
        text-align: center !important; padding: 16px !important; border-radius: 15px !important;
        text-decoration: none !important; font-weight: 900 !important; font-size: 1.05rem !important;
        margin: 12px 0 !important; box-shadow: 0 4px 12px rgba(6, 199, 85, 0.4);
    }

    /* 按鈕樣式 (橄欖綠) */
    .stButton > button { width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important; border-radius: 25px !important; height: 3em !important; font-weight: bold !important; border: none !important; }
    .stButton > button p { color: #FFFFFF !important; font-size: 1rem !important; }

    /* 溫暖提示語樣式 (微縮精緻) */
    .warm-warning { font-size: 0.85rem !important; color: #B08968 !important; text-align: center !important; margin-top: 5px !important; font-weight: bold !important; }

    /* 頁尾 */
    .custom-footer { position: fixed; left: 0; bottom: 8px; width: 100%; text-align: center; font-size: 0.65rem; color: #8B8B7A; }
    </style>
    """, unsafe_allow_html=True)

# ----------------- 邏輯初始化 -----------------
for k in ['step','answers','custom_name','bundle']:
    if k not in st.session_state: st.session_state[k] = 1 if k=='step' else [] if k=='answers' else ""

# 頂部 Logo
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
st.markdown('<p class="quote">「在忙碌中，給您留一刻鐘的溫暖。」</p>', unsafe_allow_html=True)

# ----------------- 測驗流程 (Step 1-3) -----------------
if st.session_state.step <= 3:
    qs = ["當您靜下心，您的身體正低聲說著...？", "關於這段日子的作息，您的狀態是...？", "在最需要喘息的午後，您想感受到的是...？"]
    opts = [
        ["我有些疲累，渴望溫潤透亮的晨光", "我有些沉重，想找回輕盈自在的微風", "我有些燥熱，想念山間清澈甘甜的泉水"],
        ["長時間待在冷氣房，手腳冰冷循環差", "生活忙碌常熬夜，作息不規律隨意吃", "壓力大節奏快，心神緊繃難入眠"],
        ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，從容自在"]
    ]
    warm_msgs = [
        "🌿 請先聽聽身體的聲音，再告訴米寶喔。",
        "☕️ 沒關係，深呼吸，選一個最接近您最近狀態的選項吧。",
        "✨ 您的嚮往對米寶很重要，請讓我們知道您的心情。"
    ]
    
    st.markdown(f"### 第 {st.session_state.step} 步")
    st.markdown(f'<p class="question-text">{qs[st.session_state.step-1]}</p>', unsafe_allow_html=True)
    ans = st.radio("", opts[st.session_state.step-1], index=None, key=f"q{st.session_state.step}", label_visibility="collapsed")
    
    if st.button("繼續 ➔"):
        if ans:
            st.session_state.answers.append(ans)
            st.session_state.step += 1
            st.rerun()
        else:
            st.markdown(f'<p class="warm-warning">{warm_msgs[st.session_state.step-1]}</p>', unsafe_allow_html=True)

# ----------------- 方案選擇 (Step 4) -----------------
elif st.session_state.step == 4:
    st.markdown("### ✨ 選擇您的專屬陪伴方案")
    bundles = [
        "首購限定組合 $1,980 [贈：精品刻名隨行杯 👋]",
        "老友回購組合 $1,880 [贈：驚喜茶包 3 入 🤗]",
        "一週輕體驗組合 $680 [初次邂逅草本 🍵]"
    ]
    selected = st.radio("", bundles, index=None, key="bundle_v92", label_visibility="collapsed")
    
    eng = ""
    if selected == bundles[0]:
        st.markdown("<p style='font-size:0.85rem; margin:10px 0 5px; text-align:center;'>雷刻文字 (最多12字)：</p>", unsafe_allow_html=True)
        eng = st.text_input("", placeholder="例如：Mila", label_visibility="collapsed")
    
    if st.button("查看您的專屬配比 ➔"):
        if selected:
            st.session_state.bundle = selected
            st.session_state.custom_name = eng if selected == bundles[0] else "熟客禮遇"
            st.session_state.step = 5
            st.rerun()
        else:
            st.markdown('<p class="warm-warning">🥣 請選擇一個組合，讓這份溫暖能精準送達您的手中。</p>', unsafe_allow_html=True)

# ----------------- 結果頁面 (Step 5) -----------------
elif st.session_state.step == 5:
    ans, bundle, name = st.session_state.answers, st.session_state.bundle, st.session_state.custom_name
    diag = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    
    if "$680" in bundle:
        m_v, a_v = ("黃耆元氣茶 (4入)\n+ 金菊牛蒡茶 (1入)", "當歸紅棗茶 (3入)\n+ 黑豆漢方茶 (2入)") if diag=="暖陽系" else ("洛神山楂茶 (3入)\n+ 金菊牛蒡茶 (2入)", "玫瑰決明茶 (3入)\n+ 黑豆漢方茶 (2入)") if diag=="微風系" else ("金菊牛蒡茶 (4入)\n+ 黃耆元氣茶 (1入)", "玫瑰決明茶 (4入)\n+ 當歸紅棗茶 (1入)")
        note = "🌿 方案：一週輕體驗"
    else:
        m_v, a_v = ("黃耆元氣茶 (14入)\n+ 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入)\n+ 黑豆漢方茶 (8入)") if diag=="暖陽系" else ("洛神山楂茶 (12入)\n+ 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入)\n+ 黑豆漢方茶 (10入)") if diag=="微風系" else ("金菊牛蒡茶 (15入)\n+ 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入)\n+ 當歸紅棗茶 (6入)")
        note = f"🌿 杯蓋雷刻：{name}" if "$1,980" in bundle else "🌿 老友回購加贈禮"

    st.markdown(f"### ✨ 您是：{diag}氣質")
    final_msg = f"Hi 米寶！🐢✨\n預約：{bundle}\n我是：【{diag}】\n\n☀️ 晨曦：\n{m_v}\n\n🌙 午後：\n{a_v}\n\n{note}\n期待這份草本溫暖。🌿🍵"
    
    st.markdown(f'<div class="recipe-card">{final_msg}</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size:0.8rem; margin-top:-10px;">長按上方文字區塊即可全選複製</p>', unsafe_allow_html=True)
    st.markdown(f'<a href="line://ti/p/@716osfvq" target="_top" class="line-native-btn" style="text-decoration:none;">🌿 前往 LINE@ 貼上專屬植感配方 ➔</a>', unsafe_allow_html=True)
    
    if st.button("重新探索"):
        st.session_state.clear()
        st.rerun()

st.markdown('<div class="custom-footer">慶和蔘藥行研製｜本產品屬一般食品。 © 2026 Mibao Herbal</div>', unsafe_allow_html=True)