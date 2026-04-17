import streamlit as st
import time
import os

# 1. 極致空間壓縮 CSS (目標：100% 不滑動)
st.set_page_config(page_title="米寶漢方｜妳的月度質感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域字體與背景 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 1. Logo 極致縮小 */
    [data-testid="stImage"] img { max-height: 65px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: -20px !important; margin-top: -15px !important; }

    /* 2. 標題與引言極致壓縮 */
    h3 { 
        font-size: 1.05rem !important; font-weight: 700 !important;
        margin-top: 0px !important; margin-bottom: 10px !important;
        text-align: center !important; color: #7A8450 !important;
    }
    .quote { color: #8B8B7A !important; text-align: center; margin-bottom: 15px; font-size: 0.75rem; font-style: italic; }

    /* 3. 選項卡片設計：移除黑點 + 三色網底 + 緊湊間距 (解決滑動問題) */
    [data-testid="stRadio"] div[role="radiogroup"] input { display: none !important; }
    [data-testid="stRadio"] div[role="radiogroup"] { gap: 8px !important; } /* 極小間距確保一屏 */
    
    [data-testid="stRadio"] label {
        border-radius: 12px !important; padding: 10px 15px !important;
        width: 100% !important; border: 1px solid rgba(0,0,0,0.03) !important;
        display: flex !important; justify-content: center !important; 
        text-align: center !important; font-size: 0.95rem !important;
        transition: all 0.2s ease !important; cursor: pointer !important;
    }

    /* 三色網底精準歸位 */
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(1) label { background-color: #F1F4E8 !important; }
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(2) label { background-color: #FDF2E9 !important; }
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(3) label { background-color: #EBF5FB !important; }

    /* 選中狀態 */
    [data-testid="stRadio"] div[aria-checked="true"] label {
        border: 2px solid #7A8450 !important; transform: scale(1.01) !important;
    }

    /* 4. 按鈕扁平化：節省垂直空間 */
    .stButton > button {
        width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important;
        border-radius: 25px !important; height: 2.8em !important; font-weight: bold !important; 
        border: none !important; margin-top: 10px !important;
    }
    .stButton > button p { color: #FFFFFF !important; font-size: 0.95rem !important; }

    /* 5. 複製區與輸入框：去黑底 */
    .stTextInput input { height: 35px !important; background-color: #FFFFFF !important; border: 1px solid #E9EDC9 !important; border-radius: 8px !important; }
    [data-testid="stCodeBlock"], pre, code { background-color: #F8F9F1 !important; border-radius: 10px !important; }

    /* 落葉特效 */
    @keyframes falling { 0% { transform: translateY(-5vh) rotate(0deg); opacity: 0; } 10% { opacity: 1; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
    .leaf { position: fixed; top: -5vh; font-size: 20px; pointer-events: none; z-index: 9999; animation: falling 8s linear infinite; }

    /* 隱藏原生元件 */
    #MainMenu, footer, header { visibility: hidden; }
    div[data-testid="stStatusWidget"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

def show_leaves():
    leaves_html = "".join([f'<div class="leaf" style="left:{i*10}vw; animation-delay:{i*0.8}s;">🍃</div>' for i in range(10)])
    st.markdown(leaves_html, unsafe_allow_html=True)

# 初始化
if 'step' not in st.session_state: st.session_state.step = 1
if 'answers' not in st.session_state: st.session_state.answers = []
if 'custom_name' not in st.session_state: st.session_state.custom_name = ""
if 'is_first_time' not in st.session_state: st.session_state.is_first_time = ""

# 頂部 Logo
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
st.markdown('<p class="quote">「給自己留一刻鐘的溫柔」</p>', unsafe_allow_html=True)

# ----------------- 測驗流程 -----------------
if st.session_state.step == 1:
    st.markdown("### 第一步：聽聽身體的低語")
    q1 = st.radio("", ["我有些疲累，渴望溫潤晨光", "我有些沉重，想找回輕盈微風", "我有些燥熱，想念山間泉水"], index=None, key="v27_q1")
    if st.button("延續這份溫柔 ➔"):
        if q1: st.session_state.answers.append(q1); st.session_state.step = 2; st.rerun()

elif st.session_state.step == 2:
    st.markdown("### 第二步：梳理日常的步調")
    q2 = st.radio("", ["待在冷氣房，手腳冰冷", "忙碌熬夜，晚餐不規律", "壓力大，晚上心神不寧"], index=None, key="v27_q2")
    if st.button("傾聽日常的節奏 ➔"):
        if q2: st.session_state.answers.append(q2); st.session_state.step = 3; st.rerun()

elif st.session_state.step == 3:
    st.markdown("### 第三步：妳嚮往的喘息瞬間")
    q3 = st.radio("", ["臉龐恢復紅潤元氣", "找回輕盈律動，不束縛", "內心恢復安靜穩定"], index=None, key="v27_q3")
    if st.button("開啟妳的專屬禮遇 ➔"):
        if q3: st.session_state.answers.append(q3); st.session_state.step = 4; st.rerun()

elif st.session_state.step == 4:
    st.markdown("### 💎 妳是米寶的新朋友嗎？")
    choice = st.radio("", ["是的，我是新朋友", "不是，我是老朋友了"], index=None, key="v27_choice")
    if st.button("前往專屬的陪伴 ➔"):
        if choice == "是的，我是新朋友": st.session_state.is_first_time = "是的"; st.session_state.step = 5; st.rerun()
        elif choice == "不是，我是老朋友了": st.session_state.is_first_time = "不是"; st.session_state.custom_name = "老朋友回購"; st.session_state.step = 6; st.rerun()

elif st.session_state.step == 5:
    st.markdown("### 💎 鐫刻妳的專屬溫柔")
    user_name = st.text_input("雷刻名字 (最多12字)", max_chars=12, placeholder="例如：Mila")
    if st.button("查看我的質感配比 ➔"):
        if user_name: st.session_state.custom_name = user_name; st.session_state.step = 6; st.rerun()

elif st.session_state.step == 6:
    ans, name, first = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time
    if "晨光" in ans[0]: diag, m, a = "暖陽系", "黃耆元氣茶+金菊牛蒡茶", "當歸紅棗茶+黑豆漢方茶"
    elif "微風" in ans[0]: diag, m, a = "微風系", "洛神山楂茶+金菊牛蒡茶", "玫瑰決明茶+黑豆漢方茶"
    else: diag, m, a = "清泉系", "金菊牛蒡茶+黃耆元氣茶", "玫瑰決明茶+當歸紅棗茶"
    
    show_leaves()
    st.markdown(f"""<div class="result-card"><h3 style='margin:0;'>✨ 妳是：{diag}女子</h3><hr style='margin:8px 0;'><p style='font-size:0.9rem; margin:0;'>☀️ 晨曦：{m}<br>🌙 午後：{a}</p><hr style='margin:8px 0;'><p style='font-size:0.8rem; margin:0;'>內容：40入茶包+語錄卡+{"刻名杯" if first=="是的" else "加贈茶包"}<br><b>月度陪伴價 $1,980</b></p></div>""", unsafe_allow_html=True)
    if st.button("領取專屬陪伴 ➔"): st.session_state.step = 7; st.rerun()

elif st.session_state.step == 7:
    st.write("### 📢 預約暖心的相遇")
    st.code(f"我是【{st.session_state.answers[0]}女子】。想預約月度陪伴。")
    st.markdown(f'<a href="https://line.me/R/ti/p/@716osfvq" style="text-decoration:none;"><div style="background-color: #06C755; color: white; text-align: center; padding: 12px; border-radius: 12px; font-weight: bold;">✨ LINE 貼上發送 ➔</div></a>', unsafe_allow_html=True)
    if st.button("重新探索"): st.session_state.clear(); st.rerun()

st.markdown("<p style='text-align:center; font-size:0.7rem; color:#8B8B7A; margin-top:10px;'>米寶漢方 | 慶和蔘藥行研製 © 2026 Mibao Herbal</p>", unsafe_allow_html=True)
