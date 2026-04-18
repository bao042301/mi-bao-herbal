import streamlit as st
import os

# 1. 究極視覺鎖定 (去黑底、縮小黑點、自動換行、價格分級)
st.set_page_config(page_title="米寶漢方｜您的植感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域鎖定 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    .block-container { padding-top: 0rem !important; padding-bottom: 50px !important; max-width: 95% !important; }

    /* 標題與題目：壓縮間距確保不滑動 */
    h3 { font-size: 0.85rem !important; font-weight: 700 !important; margin-top: -15px !important; margin-bottom: 2px !important; text-align: center !important; color: #7A8450 !important; }
    .question-text { font-size: 0.85rem !important; font-weight: bold !important; text-align: center !important; margin-bottom: 4px !important; line-height: 1.1 !important; }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 5px !important; font-size: 0.65rem !important; line-height: 1.1 !important; }

    /* Logo 尺寸鎖定 */
    [data-testid="stImage"] img { max-height: 40px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: -15px !important; margin-top: -5px !important; }

    /* 選項卡片設計 (靠左對齊) */
    [data-testid="stRadio"] div[role="radiogroup"] { gap: 4px !important; } 
    [data-testid="stRadio"] label {
        border-radius: 8px !important; padding: 6px 12px !important;
        width: 100% !important; border: 1px solid rgba(0,0,0,0.05) !important;
        display: flex !important; justify-content: flex-start !important; 
        text-align: left !important; font-size: 0.8rem !important; line-height: 1.2 !important;
    }
    /* 【修正】縮小選項前的黑點 */
    [data-testid="stRadio"] div[role="radiogroup"] [data-testid="stRadioButton"] > div:first-child { transform: scale(0.6) !important; margin-top: 2px !important; }

    /* 選項預設三色 */
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(1) label { background-color: #F1F4E8 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(2) label { background-color: #FDF2E9 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(3) label { background-color: #EBF5FB !important; } 

    /* 【核心修正】選中後強烈對比：加粗、放大、橄欖綠底 */
    div[data-testid="stRadio"] div[role="radiogroup"] div[aria-checked="true"] label {
        font-size: 0.95rem !important; font-weight: 900 !important;   
        color: #2D301D !important; border: 2px solid #7A8450 !important;
        background-color: #E9EDC9 !important;
    }

    /* 結果呈現與價格置中 */
    .benefit-item { font-size: 0.85rem !important; line-height: 1.3 !important; font-weight: bold !important; color: #7A8450 !important; }
    .price-text { font-size: 1.25rem !important; font-weight: bold !important; color: #7A8450 !important; margin-top: 5px; display: block; text-align: center !important; }

    /* 【核心修正】徹底解決黑底、禁止左右滑動、自動換行 */
    [data-testid="stCodeBlock"], [data-testid="stCodeBlock"] pre, [data-testid="stCodeBlock"] code {
        background-color: #F8F9F1 !important; 
        color: #4A4E31 !important;
        white-space: pre-wrap !important; 
        word-break: break-all !important;
        font-size: 0.75rem !important;
        line-height: 1.2 !important;
        padding: 8px !important;
        border: 1px solid #E9EDC9 !important;
        border-radius: 8px !important;
    }
    [data-testid="stCodeBlock"] button { opacity: 1 !important; visibility: visible !important; background-color: rgba(233, 237, 201, 1) !important; scale: 0.7; }
    [data-testid="stCodeBlock"] { margin-bottom: 2px !important; }
    code span { background-color: transparent !important; color: #4A4E31 !important; }

    /* 按鈕體積極致化 */
    .stButton > button { width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important; border-radius: 18px !important; height: 2.2em !important; font-weight: bold !important; border: none !important; }
    .stButton > button p { color: #FFFFFF !important; font-size: 0.85rem !important; }

    /* LINE 按鈕修復 */
    .line-btn-wrap { display: block !important; text-decoration: none !important; margin-top: 4px !important; position: relative; z-index: 999; }
    .line-btn-body { background-color: #06C755 !important; color: white !important; text-align: center !important; padding: 10px; border-radius: 12px; font-weight: bold; font-size: 0.85rem; }

    /* 固定頁尾與管理屏蔽 */
    .custom-footer { position: fixed; left: 0; bottom: 5px; width: 100%; text-align: center; background-color: transparent; z-index: 99; }
    .footer-text { font-size: 0.55rem !important; color: #8B8B7A !important; line-height: 1 !important; margin: 0 !important; }
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

def show_leaves():
    leaves_html = "".join([f'<div class="leaf" style="left:{i*15}vw; animation-delay:{i*1.2}s; position:fixed; top:-5vh; font-size:12px; pointer-events:none; z-index:999; animation: falling 12s linear infinite;">🍃</div>' for i in range(7)])
    st.markdown(leaves_html + """<style>@keyframes falling {0% {transform:translateY(0) rotate(0deg); opacity:0;} 10% {opacity:1;} 100% {transform:translateY(100vh) rotate(360deg); opacity:0;}}</style>""", unsafe_allow_html=True)

# ----------------- 邏輯初始化 -----------------
for k in ['step','answers','custom_name','bundle']:
    if k not in st.session_state: st.session_state[k] = 1 if k=='step' else [] if k=='answers' else ""

# 頂部 Logo
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center; margin:0;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
st.markdown('<p class="quote">「在忙碌中，給您留一刻鐘的溫暖。」</p>', unsafe_allow_html=True)

# ----------------- 測驗流程 -----------------
if st.session_state.step == 1:
    st.markdown("### 第一步：聽聽身體的聲音")
    st.markdown('<p class="question-text">當您靜下心，您的身體正低聲說著...？</p>', unsafe_allow_html=True)
    q1 = st.radio("", ["我有些疲累，渴望溫潤透亮的晨光", "我有些沉重，想找回輕盈自在的微風", "我有些燥熱，想念山間清澈甘甜的泉水"], index=None, key="q1_final", label_visibility="collapsed")
    if st.button("緩緩走向下個瞬間 ➔"):
        if q1: st.session_state.answers.append(q1); st.session_state.step = 2; st.rerun()

elif st.session_state.step == 2:
    st.markdown("### 第二步：梳理日常的步調")
    st.markdown('<p class="question-text">關於這段日子的作息，您的狀態是...？</p>', unsafe_allow_html=True)
    q2 = st.radio("", ["長時間待在冷氣房，手腳冰冷循環差", "生活忙碌常熬夜，作息不規律隨意吃", "壓力大節奏快，心神緊繃難入眠"], index=None, key="q2_final", label_visibility="collapsed")
    if st.button("傾聽日常的節奏 ➔"):
        if q2: st.session_state.answers.append(q2); st.session_state.step = 3; st.rerun()

elif st.session_state.step == 3:
    st.markdown("### 第三步：說說您嚮往的瞬間")
    st.markdown('<p class="question-text">在最需要喘息的午後，您想感受到的是...？</p>', unsafe_allow_html=True)
    q3 = st.radio("", ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，從容自在"], index=None, key="q3_final", label_visibility="collapsed")
    if st.button("開啟您的專屬禮遇 ➔"):
        if q3: st.session_state.answers.append(q3); st.session_state.step = 4; st.rerun()

# ----------------- 方案整合頁面 (Step 4) -----------------
elif st.session_state.step == 4:
    st.markdown("### ✨ 選擇您的植感預約組合")
    bundles = [
        "首購限定組 $1,980 [贈：精品刻名隨行杯 👋]",
        "老友回購組 $1,880 [贈：驚喜茶包 3 入 🤗]",
        "一週輕體驗組 $680 [初次邂逅草本 🍵]"
    ]
    selected = st.radio("", bundles, index=None, key="bundle_select_final", label_visibility="collapsed")
    
    engraving = ""
    if selected == bundles[0]:
        st.markdown("<p style='font-size:0.7rem; margin:2px 0; text-align:center;'>雷刻文字 (12字內)：</p>", unsafe_allow_html=True)
        engraving = st.text_input("", placeholder="例如：Mila", label_visibility="collapsed")
    
    if st.button("遇見您的專屬植感陪伴 ➔"):
        if selected:
            st.session_state.bundle = selected
            st.session_state.custom_name = engraving if selected == bundles[0] else "老友禮遇"
            st.session_state.step = 5; st.rerun()

# ----------------- 結果頁面 (Step 5) -----------------
elif st.session_state.step == 5:
    ans, bundle, name = st.session_state.answers, st.session_state.bundle, st.session_state.custom_name
    if "$1,980" in bundle: pr, pr_val, am = "$1,980", 1980, "40 入深度植感漢方茶組"
    elif "$1,880" in bundle: pr, pr_val, am = "$1,880", 1880, "40 入深度植感漢方茶組"
    else: pr, pr_val, am = "$680", 680, "10 入一週輕體驗茶組"
    
    if pr_val >= 1880:
        if "晨光" in ans[0]: m_t, a_t = "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
        elif "微風" in ans[0]: m_t, a_t = "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
        else: m_t, a_t = "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"
        gift = f"• 首購禮：專屬刻名隨行杯 ({name})" if "$1,980" in bundle else "• 老友禮：加贈驚喜茶包 3 包"
    else:
        if "晨光" in ans[0]: m_t, a_t = "黃耆元氣茶 (4入) + 金菊牛蒡茶 (1入)", "當歸紅棗茶 (3入) + 黑豆漢方茶 (2入)"
        elif "微風" in ans[0]: m_t, a_t = "洛神山楂茶 (3入) + 金菊牛蒡茶 (2入)", "玫瑰決明茶 (3入) + 黑豆漢方茶 (2入)"
        else: m_t, a_t = "金菊牛蒡茶 (4入) + 黃耆元氣茶 (1入)", "玫瑰決明茶 (4入) + 當歸紅棗茶 (1入)"
        gift = "• 體驗方案：感受植感初相遇"

    show_leaves()
    dg = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    st.markdown(f"""<div style="background-color: #FFFFFF; padding: 8px; border-radius: 10px; border: 1px solid #E9EDC9;">
        <h3 style='margin:0; font-size:1rem !important;'>✨ 您是：{dg}氣質</h3>
        <hr style='border: 0.5px solid #E9EDC9; margin: 4px 0;'>
        <p style='font-size:0.85rem; margin:0; font-weight:bold;'>☀️ 晨：{m_t}</p>
        <p style='font-size:0.85rem; margin:0; font-weight:bold;'>🌙 午：{a_t}</p>
        <hr style='border: 0.5px solid #E9EDC9; margin: 4px 0;'>
        <p class="benefit-item" style='margin:0;'>• {am}<br>{gift}</p>
        <span class="price-text">方案預約價 {pr}</span></div>""", unsafe_allow_html=True)
    if st.button("查看完整預約配方 ➔"): st.session_state.step = 6; st.rerun()

# ----------------- 預約轉化 (Step 6) -----------------
elif st.session_state.step == 6:
    ans, bundle, name = st.session_state.answers, st.session_state.bundle, st.session_state.custom_name
    dg = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    
    if pr_val := ("1980" if "$1,980" in bundle else "1880" if "$1,880" in bundle else "680"):
        if pr_val != "680":
            m_v, a_v = ("黃耆元氣茶(14)+金菊牛蒡茶(6)", "當歸紅棗茶(12)+黑豆漢方茶(8)") if "晨光" in ans[0] else ("洛神山楂茶(12)+金菊牛蒡茶(8)", "玫瑰決明茶(10)+黑豆漢方茶(10)") if "微風" in ans[0] else ("金菊牛蒡茶(15)+黃耆元氣茶(5)", "玫瑰決明茶(14)+當歸紅棗茶(6)")
            eng = f"🌿 杯蓋刻字：{name}" if "$1,980" in bundle else "🌿 老朋友續購補充組"
        else:
            m_v, a_v = ("黃耆元氣茶(4)+金菊牛蒡茶(1)", "當歸紅棗茶(3)+黑豆漢方茶(2)") if "晨光" in ans[0] else ("洛神山楂茶(3)+金菊牛蒡茶(2)", "玫瑰決明茶(3)+黑豆漢方茶(2)") if "微風" in ans[0] else ("金菊牛蒡茶(4)+黃耆元氣茶(1)", "玫瑰決明茶(4)+當歸紅棗茶(1)")
            eng = "🌿 一週輕體驗組"
    
    show_leaves()
    msg = f"Hi 米寶！🐢✨\n預約組合：{bundle}\n我是：【{dg}氣質】\n☀️ 晨：{m_v}\n🌙 午：{a_v}\n{eng}\n期待草本溫暖。🌿🍵"
    st.markdown('<p style="font-size:0.75rem; text-align:center; margin-bottom:2px;">點擊☆右上角☆複製文字後貼給米寶：</p>', unsafe_allow_html=True)
    st.code(msg, language=None)
    st.markdown(f'''<a href="https://line.me/R/ti/p/@716osfvq" target="_blank" class="line-btn-wrap"><div class="line-btn-body">🌿 前往 LINE@ 貼上配方預約米寶 ➔</div></a>''', unsafe_allow_html=True)
    if st.button("重新探索"): st.session_state.clear(); st.rerun()

st.markdown("""<div class="custom-footer"><p class="footer-text">米寶漢方｜慶和蔘藥行研製</p><p class="footer-text">本產品屬一般食品。 © 2026 Mibao Herbal</p></div>""", unsafe_allow_html=True)
