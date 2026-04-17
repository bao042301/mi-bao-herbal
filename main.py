import streamlit as st
import time
import os

# 1. 視覺比例校準 (質感平衡、一屏優化、選中加粗、Line連動)
st.set_page_config(page_title="米寶漢方｜您的植感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域鎖定：米寶品牌色與字體 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 容器間距校準：不滑動的關鍵在於 Padding 而非字小 */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 3rem !important;
    }

    /* 標題與引導語：維持質感大小，壓縮上下邊距 */
    h3 { 
        font-size: 1.1rem !important; font-weight: 700 !important;
        margin: 5px 0 !important; text-align: center !important; color: #7A8450 !important;
    }
    .question-text {
        font-size: 1.05rem !important; font-weight: bold !important;
        text-align: center !important; margin-bottom: 10px !important;
    }
    .quote { 
        font-style: italic; color: #8B8B7A !important; text-align: center; 
        margin-bottom: 10px !important; font-size: 0.8rem !important; 
    }

    /* Logo 比例調整 */
    [data-testid="stImage"] img { max-height: 50px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: -10px !important; }

    /* 選項卡片設計 (靠左對齊) */
    [data-testid="stRadio"] div[role="radiogroup"] { gap: 8px !important; } 
    [data-testid="stRadio"] label {
        border-radius: 10px !important; padding: 10px 15px !important;
        width: 100% !important; border: 1px solid rgba(0,0,0,0.05) !important;
        display: flex !important; justify-content: flex-start !important; 
        text-align: left !important; font-size: 0.95rem !important; 
    }

    /* 預設三色網底 */
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(1) label { background-color: #F1F4E8 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(2) label { background-color: #FDF2E9 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(3) label { background-color: #EBF5FB !important; } 

    /* 【功能鎖定】選中後的字體加粗放大、底色變綠 */
    div[data-testid="stRadio"] div[role="radiogroup"] div[aria-checked="true"] label {
        font-size: 1.05rem !important; 
        font-weight: 900 !important;   
        color: #2D301D !important;     
        border: 2px solid #7A8450 !important;
        background-color: #E9EDC9 !important;
    }

    /* 結果頁質感框 */
    .result-card {
        background-color: #FFFFFF; padding: 15px; border-radius: 15px; 
        border: 1px solid #E9EDC9; margin-bottom: 10px;
    }
    .benefit-item { font-size: 0.95rem !important; line-height: 1.6 !important; font-weight: bold !important; color: #7A8450 !important; }
    .price-text { 
        font-size: 1.4rem !important; font-weight: bold !important; 
        color: #7A8450 !important; margin-top: 10px; 
        display: block; text-align: center !important; 
    }

    /* 複製區塊圖案恆久強顯 */
    [data-testid="stCodeBlock"] button {
        opacity: 1 !important; visibility: visible !important; display: block !important;
        background-color: rgba(233, 237, 201, 1) !important;
        border: 1px solid #7A8450 !important; right: 10px !important; top: 10px !important;
    }

    /* 按鈕樣式 (橄欖綠) */
    .stButton > button {
        width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important;
        border-radius: 25px !important; height: 2.8em !important; font-weight: bold !important;
    }
    .stButton > button p { color: #FFFFFF !important; }

    /* LINE 按鈕自定義樣式 */
    .line-btn-custom {
        background-color: #06C755; color: white !important; text-align: center; 
        padding: 12px; border-radius: 12px; font-weight: bold; 
        text-decoration: none; display: block; margin-top: 5px;
    }

    /* 固定頁尾 */
    .custom-footer {
        position: fixed; left: 0; bottom: 8px; width: 100%; text-align: center;
        background-color: transparent; z-index: 99;
    }
    .footer-text { font-size: 0.65rem !important; color: #8B8B7A !important; line-height: 1.3 !important; }

    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

def show_leaves():
    leaves_html = "".join([f'<div class="leaf" style="left:{i*15}vw; animation-delay:{i*1.2}s; position:fixed; top:-10vh; font-size:20px; pointer-events:none; z-index:999; animation: falling 10s linear infinite;">🍃</div>' for i in range(7)])
    st.markdown(leaves_html + """<style>@keyframes falling {0% {transform:translateY(0) rotate(0deg); opacity:0;} 10% {opacity:1;} 100% {transform:translateY(110vh) rotate(360deg); opacity:0;}}</style>""", unsafe_allow_html=True)

# ----------------- 邏輯初始化 -----------------
for key in ['step', 'answers', 'custom_name', 'is_first_time', 'plan']:
    if key not in st.session_state:
        st.session_state[key] = 1 if key=='step' else [] if key=='answers' else ""

# 頂部 Logo
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
st.markdown('<p class="quote">「在忙碌中，給自己留一刻鐘的溫暖。」</p>', unsafe_allow_html=True)

# ----------------- 測驗流程 -----------------
if st.session_state.step == 1:
    st.markdown("### 第一步：聽聽身體的聲音")
    st.markdown('<p class="question-text">當您靜下心，您的身體正低聲說著...？</p>', unsafe_allow_html=True)
    q1 = st.radio("", ["我有些疲累，想沐浴在溫潤透亮的晨光", "我有些沉重，想沉浸在輕盈自在的微風", "我有些燥熱，想念山間清澈甘甜的泉水"], index=None, key="q1", label_visibility="collapsed")
    if st.button("緩緩走向下一步 ➔"):
        if q1: st.session_state.answers.append(q1); st.session_state.step = 2; st.rerun()

elif st.session_state.step == 2:
    st.markdown("### 第二步：梳理日常的步調")
    st.markdown('<p class="question-text">關於這段日子的作息，您的狀態是...？</p>', unsafe_allow_html=True)
    q2 = st.radio("", ["長時間待在冷氣房，手腳冰冷循環差", "生活忙碌常熬夜，作息不規律隨意吃", "壓力大節奏快，心神緊繃難入眠"], index=None, key="q2", label_visibility="collapsed")
    if st.button("傾聽日常的節奏 ➔"):
        if q2: st.session_state.answers.append(q2); st.session_state.step = 3; st.rerun()

elif st.session_state.step == 3:
    st.markdown("### 第三步：說說您嚮往的瞬間")
    st.markdown('<p class="question-text">在最需要喘息的午後，您嚮往的是...？</p>', unsafe_allow_html=True)
    q3 = st.radio("", ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，從容自在"], index=None, key="q3", label_visibility="collapsed")
    if st.button("開啟您的專屬禮遇 ➔"):
        if q3: st.session_state.answers.append(q3); st.session_state.step = 4; st.rerun()

elif st.session_state.step == 4:
    st.markdown("### 💎 您是米寶的新朋友嗎？")
    opts = ["是的，我是新朋友 👋", "我是老朋友 🤗"]
    choice = st.radio("", opts, index=None, key="choice", label_visibility="collapsed")
    if st.button("遇見您的專屬植感陪伴 ➔"):
        if choice == opts[0]: st.session_state.is_first_time = "是的"; st.session_state.step = 4.5; st.rerun()
        elif choice == opts[1]: st.session_state.is_first_time = "不是"; st.session_state.step = 4.5; st.rerun()

elif st.session_state.step == 4.5:
    st.markdown("### 🌿 選擇您的陪伴方案")
    p_opts = ["月度植感陪伴 (40入) $1,680", "一週輕體驗組 (10入) $680"]
    c = st.radio("", p_opts, index=None, key="p", label_visibility="collapsed")
    if st.button("查看我的專屬配比 ➔"):
        if c:
            st.session_state.plan = "月度" if "$1,680" in c else "體驗"
            if st.session_state.is_first_time == "是的" and st.session_state.plan == "月度": st.session_state.step = 5
            else: st.session_state.custom_name = "驚喜茶包" if st.session_state.plan=="月度" else "植感初體驗"; st.session_state.step = 6
            st.rerun()

elif st.session_state.step == 5:
    st.markdown("### 💎 鐫刻您的專屬風格")
    st.markdown("""<div style='background-color: #FFFFFF; padding: 15px; border-radius: 12px; border: 1px solid #E9EDC9; font-size:0.9rem; text-align:center; line-height:1.7;'>
        為您準備一只質感的玻璃隨行杯。<br>
        讓我們在木蓋上，鐫刻只專屬於您的風格，<br>
        陪伴您植感生活的每一天。
    </div>""", unsafe_allow_html=True)
    u = st.text_input("雷刻文字 (最多12字)", max_chars=12, placeholder="例如：Mila")
    if st.button("查看您的專屬植感配方 ➔"):
        if u: st.session_state.custom_name = u; st.session_state.step = 6; st.rerun()

elif st.session_state.step == 6:
    ans, name, first, plan = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time, st.session_state.plan
    if plan == "月度":
        pr, am = "$1,680", "40 入深度植感漢方茶組"
        if "晨光" in ans[0]: m_t, a_t = "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
        elif "微風" in ans[0]: m_t, a_t = "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
        else: m_t, a_t = "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"
        gt = f"• 精品首購禮：專屬刻名玻璃隨行杯 ({name})" if first=="是的" else "• 老朋友回饋禮：加贈驚喜茶包 3 包"
    else:
        pr, am = "$680", "10 入一週輕體驗茶組"
        if "晨光" in ans[0]: m_t, a_t = "黃耆元氣茶 (4入) + 金菊牛蒡茶 (1入)", "當歸紅棗茶 (3入) + 黑豆漢方茶 (2入)"
        elif "微風" in ans[0]: m_t, a_t = "洛神山楂茶 (3入) + 金菊牛蒡茶 (2入)", "玫瑰決明茶 (3入) + 黑豆漢方茶 (2入)"
        else: m_t, a_t = "金菊牛蒡茶 (4入) + 黃耆元氣茶 (1入)", "玫瑰決明茶 (4入) + 當歸紅棗茶 (1入)"
        gt = "• 體驗方案：感受草本植感的相遇"
    show_leaves()
    dg = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    st.markdown(f"""<div class="result-card">
        <h3 style='margin:0;'>✨ 您是：{dg}氣質</h3>
        <hr style='border:0.5px solid #E9EDC9; margin:10px 0;'>
        <p style='font-size:1rem; margin:5px 0; font-weight:bold;'>☀️ 晨曦：{m_t}</p>
        <p style='font-size:1rem; margin:5px 0; font-weight:bold;'>🌙 午後：{a_t}</p>
        <hr style='border:0.5px solid #E9EDC9; margin:10px 0;'>
        <p class="benefit-item" style='margin:0;'>• {am}<br>• 米寶生活語錄收藏卡 (暖心支持)<br>{gt}</p>
        <span class="price-text">方案陪伴價 {pr}</span></div>""", unsafe_allow_html=True)
    if st.button("預約這份植感時光 ➔"): st.session_state.step = 7; st.rerun()

elif st.session_state.step == 7:
    ans, name, first, plan = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time, st.session_state.plan
    dg = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    if plan == "月度":
        if "晨光" in ans[0]: m_t, a_t = "黃耆元氣茶(14入)+金菊(6入)", "當歸紅棗(12入)+黑豆(8入)"
        elif "微風" in ans[0]: m_t, a_t = "洛神山楂(12入)+金菊(8入)", "玫瑰決明(10入)+黑豆(10入)"
        else: m_t, a_t = "金菊(15入)+黃耆(5入)", "玫瑰決明(14入)+當歸(6入)"
        eng = f"🌿 杯蓋刻上：{name} ✨" if first == "是的" else "🌿 老朋友月度組，領取加贈茶包 🐢🎁"
    else:
        if "晨光" in ans[0]: m_t, a_t = "黃耆(4入)+金菊(1入)", "當歸(3入)+黑豆(2入)"
        elif "微風" in ans[0]: m_t, a_t = "洛神(3入)+金菊(2入)", "玫瑰(3入)+黑豆(2入)"
        else: m_t, a_t = "金菊(4入)+黃耆(1入)", "玫瑰(4入)+當歸(1入)"
        eng = "🌿 方案：一週輕體驗組 🍵"
    show_leaves()
    msg = f"Hi 米寶！🐢✨\n\n我想預約【{plan}方案】。我是【{dg}氣質】。\n\n專屬植感配比：\n☀️ 晨曦：{m_t}\n🌙 午後：{a_t}\n\n{eng}\n期待與這份草本暖茶相遇。🌿🍵"
    st.markdown('<p style="font-size:0.9rem; text-align:center; margin-bottom:5px;">請點擊☆右上方圖示☆複製文字：</p>', unsafe_allow_html=True)
    st.code(msg, language=None)
    # 【關鍵修復】LINE@ 連結連動
    st.markdown(f'<a href="https://line.me/R/ti/p/@716osfvq" target="_blank" class="line-btn-custom">🌿 前往 LINE@ 貼上配方給米寶 ➔</a>', unsafe_allow_html=True)
    if st.button("重新探索"): st.session_state.clear(); st.rerun()

st.markdown("""<div class="custom-footer"><p class="footer-text">米寶漢方｜慶和蔘藥行研製</p><p class="footer-text">本產品屬一般食品。 © 2026 Mibao Herbal</p></div>""", unsafe_allow_html=True)
