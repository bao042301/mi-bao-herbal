import streamlit as st
import time
import os

# 1. 究極視覺鎖定 (文字全名還原、黑點縮小、LINE跳轉修復、選中加粗)
st.set_page_config(page_title="米寶漢方｜您的植感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域文字與背景鎖定 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 容器間距極致壓縮 */
    .block-container {
        padding-top: 0.1rem !important;
        padding-bottom: 70px !important;
    }

    /* 標題與題目：縮小以釋放空間 */
    h3 { 
        font-size: 0.9rem !important; font-weight: 700 !important;
        margin-top: -5px !important; margin-bottom: 2px !important;
        text-align: center !important; color: #7A8450 !important;
    }
    .question-text {
        font-size: 0.9rem !important; font-weight: bold !important;
        text-align: center !important; margin-bottom: 4px !important;
        line-height: 1.2 !important;
    }
    .quote { 
        font-style: italic; color: #8B8B7A !important; text-align: center; 
        margin-bottom: 8px !important; font-size: 0.7rem !important; 
    }

    /* Logo 尺寸優化 */
    [data-testid="stImage"] img { max-height: 45px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: -15px !important; }

    /* 選項卡片設計 (左對齊) */
    [data-testid="stRadio"] div[role="radiogroup"] { gap: 4px !important; } 
    [data-testid="stRadio"] label {
        border-radius: 10px !important; padding: 8px 15px !important;
        width: 100% !important; border: 1px solid rgba(0,0,0,0.05) !important;
        display: flex !important; justify-content: flex-start !important; 
        text-align: left !important; transition: all 0.2s ease !important; cursor: pointer !important;
        font-size: 0.9rem !important; line-height: 1.3 !important;
    }

    /* 選項前的黑點/圓點縮小 */
    [data-testid="stRadio"] div[role="radiogroup"] [data-testid="stRadioButton"] > div:first-child {
        transform: scale(0.7) !important;
        margin-top: 1px !important;
    }

    /* 預設三色網底 */
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(1) label { background-color: #F1F4E8 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(2) label { background-color: #FDF2E9 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(3) label { background-color: #EBF5FB !important; } 

    /* 選中後的字體加粗且放大 */
    div[data-testid="stRadio"] div[role="radiogroup"] div[aria-checked="true"] label {
        font-size: 1.0rem !important; 
        font-weight: 900 !important;   
        color: #2D301D !important;     
        border: 2px solid #7A8450 !important;
        background-color: #E9EDC9 !important;
    }

    /* 結果清單與價格 */
    .benefit-item { font-size: 0.9rem !important; line-height: 1.5 !important; font-weight: bold !important; color: #7A8450 !important; }
    .price-text { 
        font-size: 1.3rem !important; font-weight: bold !important; 
        color: #7A8450 !important; margin-top: 8px; 
        display: block; text-align: center !important; 
    }

    /* 複製按鈕圖案強顯，彻底消除黑底 */
    [data-testid="stCodeBlock"] button {
        opacity: 1 !important; visibility: visible !important; display: block !important;
        background-color: rgba(233, 237, 201, 1) !important;
        border: 1px solid #7A8450 !important; right: 8px !important; top: 8px !important;
        scale: 0.8;
    }
    [data-testid="stCodeBlock"], [data-testid="stCodeBlock"] > div, pre, code {
        background-color: #F8F9F1 !important; border: 1px solid #E9EDC9 !important; border-radius: 8px !important;
    }
    code span { background-color: transparent !important; color: #4A4E31 !important; }

    /* 按鈕樣式 (橄欖綠) */
    .stButton > button {
        width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important;
        border-radius: 25px !important; height: 2.6em !important; font-weight: bold !important; border: none !important;
    }
    .stButton > button p { color: #FFFFFF !important; font-size: 0.9rem !important; }

    /* LINE 按鈕跳轉路徑加強 */
    .line-link {
        display: block !important; text-decoration: none !important; margin-top: 5px !important;
        position: relative !important; z-index: 9999 !important;
    }
    .line-btn-styled {
        background-color: #06C755 !important; color: white !important; text-align: center !important;
        padding: 10px 15px !important; border-radius: 12px !important; font-weight: bold !important;
        font-size: 0.85rem !important; box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    }

    /* 固定頁尾 */
    .custom-footer {
        position: fixed; left: 0; bottom: 8px; width: 100%; text-align: center;
        background-color: transparent; z-index: 99;
    }
    .footer-text { font-size: 0.6rem !important; color: #8B8B7A !important; line-height: 1.2 !important; }

    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

def show_leaves():
    leaves_html = "".join([f'<div class="leaf" style="left:{i*15}vw; animation-delay:{i*1.5}s; position:fixed; top:-5vh; font-size:15px; pointer-events:none; z-index:9999; animation: falling 10s linear infinite;">🍃</div>' for i in range(7)])
    st.markdown(leaves_html + "<style>@keyframes falling {0% {transform:translateY(0) rotate(0deg); opacity:0;} 10% {opacity:1;} 100% {transform:translateY(100vh) rotate(360deg); opacity:0;}}</style>", unsafe_allow_html=True)

# ----------------- 邏輯初始化 -----------------
for k in ['step','answers','custom_name','is_first_time','plan']:
    if k not in st.session_state: st.session_state[k] = 1 if k=='step' else [] if k=='answers' else ""

# 頂部 Logo
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
st.markdown('<p class="quote">「在忙碌中，給您留一刻鐘的溫暖。」</p>', unsafe_allow_html=True)

# ----------------- 測驗流程 -----------------
if st.session_state.step == 1:
    st.markdown("### 第一步：聽聽身體的聲音")
    st.markdown('<p class="question-text">當您靜下心，您的身體正低聲說著...？</p>', unsafe_allow_html=True)
    q1 = st.radio("", ["我有些疲累，想沐浴在溫潤透亮的晨光", "我有些沉重，想沉浸在輕盈自在的微風", "我有些燥熱，想念山間清澈甘甜的泉水"], index=None, key="q1_v80", label_visibility="collapsed")
    if st.button("緩緩走向下一步 ➔"):
        if q1: st.session_state.answers.append(q1); st.session_state.step = 2; st.rerun()

elif st.session_state.step == 2:
    st.markdown("### 第二步：梳理日常的步調")
    st.markdown('<p class="question-text">關於這段日子的作息，您的狀態是...？</p>', unsafe_allow_html=True)
    q2 = st.radio("", ["長時間待在冷氣房，手腳冰冷循環差", "生活忙碌常熬夜，作息不規律隨意吃", "壓力大節奏快，心神緊繃難入眠"], index=None, key="q2_v80", label_visibility="collapsed")
    if st.button("傾聽日常的節奏 ➔"):
        if q2: st.session_state.answers.append(q2); st.session_state.step = 3; st.rerun()

elif st.session_state.step == 3:
    st.markdown("### 第三步：說說您嚮往的瞬間")
    st.markdown('<p class="question-text">在最需要喘息的午後，您最想感受到的是...？</p>', unsafe_allow_html=True)
    q3 = st.radio("", ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，從容自在"], index=None, key="q3_v80", label_visibility="collapsed")
    if st.button("開啟您的專屬禮遇 ➔"):
        if q3: st.session_state.answers.append(q3); st.session_state.step = 4; st.rerun()

elif st.session_state.step == 4:
    st.markdown("### 💎 您是米寶的新朋友嗎？")
    opts = ["是的，我是新朋友 👋", "我是老朋友 🤗"]
    choice = st.radio("", opts, index=None, key="choice_v80", label_visibility="collapsed")
    if st.button("遇見您的專屬植感陪伴 ➔"):
        if choice == opts[0]: st.session_state.is_first_time = "是的"; st.session_state.step = 4.5; st.rerun()
        elif choice == opts[1]: st.session_state.is_first_time = "不是"; st.session_state.step = 4.5; st.rerun()

elif st.session_state.step == 4.5:
    st.markdown("### 🌿 選擇您的陪伴方案")
    p_opts = ["月度植感陪伴 (40入) $1,680", "一週輕體驗組 (10入) $680"]
    c = st.radio("", p_opts, index=None, key="p_v80", label_visibility="collapsed")
    if st.button("查看我的專屬配比 ➔"):
        if c:
            st.session_state.plan = "月度" if "$1,680" in c else "體驗"
            if st.session_state.is_first_time == "是的" and st.session_state.plan == "月度": st.session_state.step = 5
            else: st.session_state.custom_name = "老朋友驚喜" if st.session_state.plan == "月度" else "植感初體驗"; st.session_state.step = 6
            st.rerun()

elif st.session_state.step == 5:
    st.markdown("### 💎 鐫刻您的專屬風格")
    st.markdown("""<div style='background-color: #FFFFFF; padding: 10px; border-radius: 12px; border: 1px solid #E9EDC9; font-size:0.85rem; text-align:center; line-height:1.5;'>為您準備一只質感的玻璃隨行杯。<br>讓我們在木蓋上，鐫刻只專屬於您的風格。</div>""", unsafe_allow_html=True)
    user_name = st.text_input("雷刻文字 (最多12字)", max_chars=12, placeholder="例如：Mila")
    if st.button("查看您的專屬植感配方 ➔"):
        if user_name: st.session_state.custom_name = user_name; st.session_state.step = 6; st.rerun()

elif st.session_state.step == 6:
    ans, name, first, plan = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time, st.session_state.plan
    if plan == "月度":
        price, amount = "$1,680", "40 入深度植感漢方茶組"
        if "晨光" in ans[0]: m_tea, a_tea = "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
        elif "微風" in ans[0]: m_tea, a_tea = "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
        else: m_tea, a_tea = "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"
        gift = f"• 精品首購禮：專屬刻名隨行杯 ({name})" if first=="是的" else "• 老朋友回饋禮：加贈驚喜茶包 3 包"
    else:
        price, amount = "$680", "10 入一週輕體驗茶組"
        if "晨光" in ans[0]: m_tea, a_tea = "黃耆元氣茶 (4入) + 金菊牛蒡茶 (1入)", "當歸紅棗茶 (3入) + 黑豆漢方茶 (2入)"
        elif "微風" in ans[0]: m_tea, a_tea = "洛神山楂茶 (3入) + 金菊牛蒡茶 (2入)", "玫瑰決明茶 (3入) + 黑豆漢方茶 (2入)"
        else: m_tea, a_tea = "金菊牛蒡茶 (4入) + 黃耆元氣茶 (1入)", "玫瑰決明茶 (4入) + 當歸紅棗茶 (1入)"
        gift = "• 體驗方案：初探草本植感相遇"
    show_leaves() 
    diag = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    st.markdown(f"""<div style="background-color: #FFFFFF; padding: 10px; border-radius: 12px; border: 1px solid #E9EDC9;">
        <h3 style='margin:0; font-size:1.1rem !important;'>✨ 您是：{diag}氣質</h3>
        <hr style='border: 0.5px solid #E9EDC9; margin: 4px 0;'>
        <p style='font-size:0.95rem; margin:0; font-weight:bold;'>☀️ 晨曦：{m_tea}</p>
        <p style='font-size:0.95rem; margin:0; font-weight:bold;'>🌙 午後：{a_tea}</p>
        <hr style='border: 0.5px solid #E9EDC9; margin: 4px 0;'>
        <p class="benefit-item" style='margin:0;'>• {amount}<br>{gift}</p>
        <span class="price-text">方案陪伴價 {price}</span></div>""", unsafe_allow_html=True)
    if st.button("預約這份植感時光 ➔"): st.session_state.step = 7; st.rerun()

elif st.session_state.step == 7:
    ans, name, first, plan = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time, st.session_state.plan
    diag = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    if plan == "月度":
        if "晨光" in ans[0]: m_t, a_t = "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
        elif "微風" in ans[0]: m_t, a_t = "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
        else: m_t, a_t = "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"
        eng = f"🌿 杯蓋刻上：{name} ✨" if first == "是的" else "🌿 老朋友月度組，回購領贈茶"
    else:
        if "晨光" in ans[0]: m_t, a_t = "黃耆元氣茶 (4入) + 金菊牛蒡茶 (1入)", "當歸紅棗茶 (3入) + 黑豆漢方茶 (2入)"
        elif "微風" in ans[0]: m_t, a_t = "洛神山楂茶 (3入) + 金菊牛蒡茶 (2入)", "玫瑰決明茶 (3入) + 黑豆漢方茶 (2入)"
        else: m_t, a_t = "金菊牛蒡茶 (4入) + 黃耆元氣茶 (1入)", "玫瑰決明茶 (4入) + 當歸紅棗茶 (1入)"
        eng = "🌿 方案：一週輕體驗組 🍵"
    show_leaves()
    msg = f"Hi 米寶！🐢✨\n預約【{plan}方案】|【{diag}】\n☀️ 晨：{m_t}\n🌙 午：{a_t}\n{eng}\n期待與這份草本暖茶相遇。🌿🍵"
    st.markdown('<p style="font-size:0.8rem; margin-bottom:2px; text-align:center;">點擊☆右上角☆複製文字後傳給米寶：</p>', unsafe_allow_html=True)
    st.code(msg, language=None)
    st.markdown(f'''<a href="https://line.me/R/ti/p/@716osfvq" target="_blank" class="line-link"><div class="line-btn-styled">🌿 前往 LINE@ 貼上配方預約米寶吧！ ➔</div></a>''', unsafe_allow_html=True)
    if st.button("重新探索"): st.session_state.clear(); st.rerun()

st.markdown("""<div class="custom-footer"><p class="footer-text">米寶漢方｜慶和蔘藥行研製</p><p class="footer-text">本產品屬一般食品。 © 2026 Mibao Herbal</p></div>""", unsafe_allow_html=True)