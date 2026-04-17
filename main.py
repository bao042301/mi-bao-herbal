import streamlit as st
import time
import os

# 1. 究極視覺鎖定 (極致一屏、間距壓縮、價格置中、Line連結連動)
st.set_page_config(page_title="米寶漢方｜您的植感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域文字與背景鎖定 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 【關鍵修正】容器間距極致壓縮，確保絕對不滑動 */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 60px !important;
    }

    /* 標題與引導語縮小：節省垂直空間 */
    h3 { 
        font-size: 0.85rem !important; font-weight: 700 !important;
        margin-top: -15px !important; margin-bottom: 2px !important;
        text-align: center !important; color: #7A8450 !important;
    }
    .question-text {
        font-size: 0.9rem !important; font-weight: bold !important;
        text-align: center !important; margin-bottom: 2px !important;
        line-height: 1.1 !important;
    }
    .quote { 
        font-style: italic; color: #8B8B7A !important; text-align: center; 
        margin-bottom: 5px !important; font-size: 0.65rem !important; 
        line-height: 1.1 !important;
    }

    /* Logo 尺寸微調 */
    [data-testid="stImage"] img { max-height: 40px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: -15px !important; margin-top: -5px !important; }

    /* 選項卡片極致化 (靠左) */
    [data-testid="stRadio"] div[role="radiogroup"] { gap: 3px !important; } 
    [data-testid="stRadio"] label {
        border-radius: 8px !important; padding: 6px 12px !important;
        width: 100% !important; border: 1px solid rgba(0,0,0,0.05) !important;
        display: flex !important; justify-content: flex-start !important; 
        text-align: left !important; font-size: 0.85rem !important; 
        line-height: 1.2 !important;
    }

    /* 預設三色網底 */
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(1) label { background-color: #F1F4E8 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(2) label { background-color: #FDF2E9 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(3) label { background-color: #EBF5FB !important; } 

    /* 【固定功能】選中後的字體加粗且放大 */
    div[data-testid="stRadio"] div[role="radiogroup"] div[aria-checked="true"] label {
        font-size: 0.95rem !important; 
        font-weight: 900 !important;   
        color: #2D301D !important;     
        border: 1.5px solid #7A8450 !important;
        background-color: #E9EDC9 !important;
    }

    /* 結果頁：方案內容緊湊化 */
    .benefit-item { font-size: 0.85rem !important; line-height: 1.3 !important; font-weight: bold !important; color: #7A8450 !important; }
    .price-text { 
        font-size: 1.2rem !important; font-weight: bold !important; 
        color: #7A8450 !important; margin-top: 5px; 
        display: block; text-align: center !important; 
    }

    /* 複製區塊高度壓縮與圖案強顯 */
    [data-testid="stCodeBlock"] button {
        opacity: 1 !important; visibility: visible !important; display: block !important;
        background-color: rgba(233, 237, 201, 1) !important;
        border: 1px solid #7A8450 !important; right: 5px !important; top: 5px !important;
        scale: 0.7;
    }
    [data-testid="stCodeBlock"] { margin-bottom: 2px !important; }
    [data-testid="stCodeBlock"] pre { padding: 8px !important; }
    code { font-size: 0.75rem !important; line-height: 1.2 !important; }

    /* 按鈕體積優化 */
    .stButton > button {
        width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important;
        border-radius: 20px !important; height: 2.2em !important; font-weight: bold !important;
        margin-top: 0px !important;
    }
    .stButton > button p { color: #FFFFFF !important; font-size: 0.85rem !important; }

    /* LINE 按鈕視覺鎖定 */
    .line-btn {
        background-color: #06C755; color: white !important; text-align: center; 
        padding: 8px; border-radius: 12px; font-weight: bold; 
        margin-bottom: 2px; font-size: 0.85rem; text-decoration: none; display: block;
    }

    /* 固定頁尾 */
    .custom-footer {
        position: fixed; left: 0; bottom: 5px; width: 100%; text-align: center;
        background-color: transparent; z-index: 99;
    }
    .footer-text { font-size: 0.55rem !important; color: #8B8B7A !important; line-height: 1 !important; margin: 0 !important; }

    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

def show_leaves():
    leaves_html = "".join([f'<div class="leaf" style="left:{i*15}vw; animation-delay:{i*1.2}s; position:fixed; top:-5vh; font-size:12px; pointer-events:none; z-index:999; animation: falling 10s linear infinite;">🍃</div>' for i in range(7)])
    st.markdown(leaves_html + """<style>@keyframes falling {0% {transform:translateY(0) rotate(0deg); opacity:0;} 10% {opacity:1;} 100% {transform:translateY(100vh) rotate(360deg); opacity:0;}}</style>""", unsafe_allow_html=True)

# ----------------- 邏輯初始化 -----------------
for key in ['step', 'answers', 'custom_name', 'is_first_time', 'plan']:
    if key not in st.session_state:
        st.session_state[key] = 1 if key=='step' else [] if key=='answers' else ""

# 頂部 Logo
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center; margin:0;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
st.markdown('<p class="quote">「在忙碌中，給您留一刻鐘的溫暖。」</p>', unsafe_allow_html=True)

# ----------------- 測驗流程 -----------------
if st.session_state.step == 1:
    st.markdown("### 第一步：聽聽身體的聲音")
    st.markdown('<p class="question-text">當您靜下心，您的身體正低聲說著...？</p>', unsafe_allow_html=True)
    q1 = st.radio("", ["我有些疲累，想沐浴在晨光中", "我有些沉重，想沉浸在微風裡", "我有些燥熱，想念山間的泉水"], index=None, key="q1", label_visibility="collapsed")
    if st.button("緩緩走向下一步 ➔"):
        if q1: st.session_state.answers.append(q1); st.session_state.step = 2; st.rerun()

elif st.session_state.step == 2:
    st.markdown("### 第二步：梳理日常的步調")
    st.markdown('<p class="question-text">關於這段日子的作息，您的狀態是...？</p>', unsafe_allow_html=True)
    q2 = st.radio("", ["手腳冰冷循環差", "作息不規律隨意吃", "心神緊繃難入眠"], index=None, key="q2", label_visibility="collapsed")
    if st.button("傾聽日常的節奏 ➔"):
        if q2: st.session_state.answers.append(q2); st.session_state.step = 3; st.rerun()

elif st.session_state.step == 3:
    st.markdown("### 第三步：說說您嚮往的瞬間")
    st.markdown('<p class="question-text">在最需要喘息的午後，您嚮往的是...？</p>', unsafe_allow_html=True)
    q3 = st.radio("", ["恢復紅潤元氣", "找回輕盈律動", "恢復安靜穩定"], index=None, key="q3", label_visibility="collapsed")
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
    st.markdown("<p class='quote' style='font-size:0.75rem !important;'>我們在木蓋上，鐫刻只專屬於您的風格。</p>", unsafe_allow_html=True)
    u = st.text_input("雷刻文字 (最多12字)", max_chars=12, placeholder="例如：Mila")
    if st.button("查看您的專屬植感配方 ➔"):
        if u: st.session_state.custom_name = u; st.session_state.step = 6; st.rerun()

elif st.session_state.step == 6:
    ans, name, first, plan = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time, st.session_state.plan
    if plan == "月度":
        pr, am = "$1,680", "40 入深度植感漢方茶組"
        if "晨光" in ans[0]: m_t, a_t = "黃耆元氣茶(14入)+金菊牛蒡茶(6入)", "當歸紅棗茶(12入)+黑豆漢方茶(8入)"
        elif "微風" in ans[0]: m_t, a_t = "洛神山楂茶(12入)+金菊牛蒡茶(8入)", "玫瑰決明茶(10入)+黑豆漢方茶(10入)"
        else: m_t, a_t = "金菊牛蒡茶(15入)+黃耆元氣茶(5入)", "玫瑰決明茶(14入)+當歸紅棗茶(6入)"
        gt = f"• 精品首購禮：專屬隨行杯 ({name})" if first=="是的" else "• 老朋友禮：加贈茶包 3 包"
    else:
        pr, am = "$680", "10 入一週輕體驗組"
        if "晨光" in ans[0]: m_t, a_t = "黃耆元氣茶(4入)+金菊牛蒡茶(1入)", "當歸紅棗茶(3入)+黑豆漢方茶(2入)"
        elif "微風" in ans[0]: m_t, a_t = "洛神山楂茶(3入)+金菊牛蒡茶(2入)", "玫瑰決明茶(3入)+黑豆漢方茶(2入)"
        else: m_t, a_t = "金菊牛蒡茶(4入)+黃耆元氣茶(1入)", "玫瑰決明茶(4入)+當歸紅棗茶(1入)"
        gt = "• 體驗方案：草本植感初相遇"
    show_leaves()
    dg = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    st.markdown(f"""<div style="background-color:#FFF; padding:8px; border-radius:10px; border:1px solid #E9EDC9;">
        <h3 style='margin:0; font-size:1rem !important;'>✨ 您是：{dg}氣質</h3>
        <p style='font-size:0.85rem; margin:2px 0; font-weight:bold;'>☀️ 晨：{m_t}</p>
        <p style='font-size:0.85rem; margin:2px 0; font-weight:bold;'>🌙 午：{a_t}</p>
        <hr style='margin:4px 0;'><p class="benefit-item" style='margin:0;'>• {am}<br>{gt}</p>
        <span class="price-text">{pr}</span></div>""", unsafe_allow_html=True)
    if st.button("預約這份時光 ➔"): st.session_state.step = 7; st.rerun()

elif st.session_state.step == 7:
    ans, name, first, plan = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time, st.session_state.plan
    dg = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    if plan == "月度":
        if "晨光" in ans[0]: m_t, a_t = "黃耆元氣茶(14)+金菊(6)", "當歸紅棗(12)+黑豆(8)"
        elif "微風" in ans[0]: m_t, a_t = "洛神山楂(12)+金菊(8)", "玫瑰決明(10)+黑豆(10)"
        else: m_t, a_t = "金菊(15)+黃耆(5)", "玫瑰決明(14)+當歸(6)"
        eng = f"🌿 杯蓋刻字：{name}" if first == "是的" else "🌿 老朋友月度回購贈茶"
    else:
        if "晨光" in ans[0]: m_t, a_t = "黃耆(4)+金菊(1)", "當歸(3)+黑豆(2)"
        elif "微風" in ans[0]: m_t, a_t = "洛神(3)+金菊(2)", "玫瑰(3)+黑豆(2)"
        else: m_t, a_t = "金菊(4)+黃耆(1)", "玫瑰(4)+當歸(1)"
        eng = "🌿 方案：一週輕體驗"
    show_leaves()
    msg = f"Hi 米寶！🐢✨\n預約【{plan}方案】|我是【{dg}】\n☀️ 晨：{m_t}\n🌙 午：{a_t}\n{eng}\n期待與草本暖茶相遇。🌿"
    st.markdown('<p style="font-size:0.75rem; text-align:center; margin-bottom:2px;">點擊右上方圖示複製後貼給米寶：</p>', unsafe_allow_html=True)
    st.code(msg, language=None)
    # 【關鍵修復】正確連動 Line@ 連結
    st.markdown(f'<a href="https://line.me/R/ti/p/@716osfvq" target="_blank" class="line-btn">🌿 前往 LINE@ 貼上配方給米寶 ➔</a>', unsafe_allow_html=True)
    if st.button("重新探索"): st.session_state.clear(); st.rerun()

st.markdown("""<div class="custom-footer"><p class="footer-text">米寶漢方｜慶和蔘藥行研製</p><p class="footer-text">本產品屬一般食品。 © 2026 Mibao Herbal</p></div>""", unsafe_allow_html=True)
