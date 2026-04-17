import streamlit as st
import time
import os

# 1. 視覺鎖定 (一屏設計、三色網底、特效回歸、去黑底)
st.set_page_config(page_title="米寶漢方｜妳的植感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域顯色鎖定 - 橄欖綠文字 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 壓縮容器間距，確保一屏不滑動 */
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 0rem !important;
    }

    /* 步驟標題 */
    h3 { 
        font-size: 1rem !important; font-weight: 700 !important;
        margin-top: 0px !important; margin-bottom: 5px !important;
        text-align: center !important; color: #7A8450 !important;
    }
    
    /* 質感問題文案 */
    .question-text {
        font-size: 1.1rem !important;
        font-weight: bold !important;
        text-align: center !important;
        margin-bottom: 15px !important;
        line-height: 1.4 !important;
    }

    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 15px; font-size: 0.8rem; }

    /* Logo 尺寸優化 */
    [data-testid="stImage"] img { max-height: 75px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: -15px !important; }

    /* 選項卡片與三色網底 (徹底移除黑點) */
    [data-testid="stRadio"] div[role="radiogroup"] input { display: none !important; }
    [data-testid="stRadio"] div[role="radiogroup"] { gap: 10px !important; }
    
    [data-testid="stRadio"] label {
        border-radius: 12px !important; padding: 12px 18px !important;
        width: 100% !important; border: 1px solid rgba(0,0,0,0.05) !important;
        display: flex !important; justify-content: center !important; text-align: center !important;
        transition: all 0.2s ease !important; cursor: pointer !important;
    }

    /* 三色網底精準歸位 */
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(1) label { background-color: #F1F4E8 !important; }
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(2) label { background-color: #FDF2E9 !important; }
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(3) label { background-color: #EBF5FB !important; }

    /* 選中狀態 */
    [data-testid="stRadio"] div[aria-checked="true"] label { border: 2px solid #7A8450 !important; transform: scale(1.01); }

    /* 去黑底鎖定 - 輸入框 */
    .stTextInput input { background-color: #FFFFFF !important; border: 2px solid #E9EDC9 !important; border-radius: 10px !important; }
    
    /* 複製區：質感米白，絕不變黑 */
    [data-testid="stCodeBlock"], [data-testid="stCodeBlock"] > div, pre, code {
        background-color: #F8F9F1 !important; border: 1px solid #E9EDC9 !important; border-radius: 12px !important;
    }
    code span { background-color: transparent !important; color: #4A4E31 !important; }

    /* 按鈕樣式 (橄欖綠) */
    .stButton > button {
        width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important;
        border-radius: 30px !important; height: 3.2em !important; font-weight: bold !important; border: none !important;
    }
    .stButton > button p { color: #FFFFFF !important; }

    /* 森林落葉特效 */
    @keyframes falling {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .leaf { position: fixed; top: -10vh; font-size: 24px; pointer-events: none; z-index: 9999; animation: falling 12s linear infinite; }

    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

def show_leaves():
    leaves_html = "".join([f'<div class="leaf" style="left:{i*15}vw; animation-delay:{i*1.2}s;">🍃</div>' for i in range(7)])
    st.markdown(leaves_html, unsafe_allow_html=True)

# ----------------- 邏輯初始化 -----------------
if 'step' not in st.session_state: st.session_state.step = 1
if 'answers' not in st.session_state: st.session_state.answers = []
if 'custom_name' not in st.session_state: st.session_state.custom_name = ""
if 'is_first_time' not in st.session_state: st.session_state.is_first_time = ""

# 頂部 Logo
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h2 style='text-align:center;'>🌿 米寶漢方</h2>", unsafe_allow_html=True)
st.markdown('<p class="quote">「在忙碌中，給自己留一刻鐘的溫柔。」</p>', unsafe_allow_html=True)

# ----------------- 測驗流程 -----------------
if st.session_state.step == 1:
    st.markdown("### 第一步：聽聽身體的低語")
    st.markdown('<p class="question-text">當妳靜下心，妳的身體正低聲說著...？</p>', unsafe_allow_html=True)
    q1 = st.radio("", ["我有些疲累，渴望溫潤透亮的晨光...", "我有些沉重，想找回輕盈自在的微風...", "我有些燥熱，想念山間清徹甘甜的泉水..."], index=None, key="v37_q1", label_visibility="collapsed")
    if st.button("緩緩走向下個瞬間 ➔"):
        if q1: st.session_state.answers.append(q1); st.session_state.step = 2; st.rerun()

elif st.session_state.step == 2:
    st.markdown("### 第二步：梳理日常的步調")
    st.markdown('<p class="question-text">關於這段日子的作息，妳目前的感受是？</p>', unsafe_allow_html=True)
    q2 = st.radio("", ["長時間待在冷氣房，循環緩慢且手腳冰冷", "工作忙碌常熬夜，晚餐不規律導致不適", "壓力大節奏快，晚上難以入眠且心神不寧"], index=None, key="v37_q2", label_visibility="collapsed")
    if st.button("傾聽日常的節奏 ➔"):
        if q2: st.session_state.answers.append(q2); st.session_state.step = 3; st.rerun()

elif st.session_state.step == 3:
    st.markdown("### 第三步：妳嚮往的喘息瞬間")
    st.markdown('<p class="question-text">在最需要喘息的午後，妳最嚮往的瞬間？</p>', unsafe_allow_html=True)
    q3 = st.radio("", ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，優雅從容"], index=None, key="v37_q3", label_visibility="collapsed")
    if st.button("開啟妳的專屬禮遇 ➔"):
        if q3: st.session_state.answers.append(q3); st.session_state.step = 4; st.rerun()

elif st.session_state.step == 4:
    st.markdown("### 💎 妳是米寶的新朋友嗎？")
    opts = ["是的，我是新朋友", "不是，我是老朋友了（已有隨行杯）"]
    choice = st.radio("", opts, index=None, key="v37_choice", label_visibility="collapsed")
    if st.button("前往專屬的陪伴 ➔"):
        if choice == opts[0]: st.session_state.is_first_time = "是的"; st.session_state.step = 5; st.rerun()
        elif choice == opts[1]: st.session_state.is_first_time = "不是"; st.session_state.custom_name = "老朋友回購驚喜"; st.session_state.step = 6; st.rerun()

elif st.session_state.step == 5:
    st.markdown("### 💎 鐫刻妳的專屬溫柔")
    st.markdown("<div style='background-color: #FFFFFF; padding: 10px; border-radius: 10px; border: 1px solid #E9EDC9; font-size:0.85rem; text-align:center;'>首購禮遇：為妳在木蓋上，鐫刻專屬的名字。</div>", unsafe_allow_html=True)
    user_name = st.text_input("輸入名字 (最多12字)", max_chars=12, placeholder="例如：Mila")
    if st.button("查看我的質感陪伴配比 ➔"):
        if user_name: st.session_state.custom_name = user_name; st.session_state.step = 6; st.rerun()

elif st.session_state.step == 6:
    ans, name, first = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time
    if "晨光" in ans[0]: diag, m_tea, a_tea = "暖陽系", "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
    elif "微風" in ans[0]: diag, m_tea, a_tea = "微風系", "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
    else: diag, m_tea, a_tea = "清泉系", "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"

    show_leaves() 
    gift = f"精品首購禮：專屬刻名隨行杯 ({name})" if first=="是的" else "老朋友回饋禮：加贈驚喜茶包 3 包"
    
    st.markdown(f"""
    <div style="background-color: #FFFFFF; padding: 15px; border-radius: 20px; border: 1px solid #E9EDC9;">
        <h3 style='margin:0; font-size:1.3rem !important;'>✨ 妳是：{diag}女子</h3>
        <p class="quote" style='margin-bottom:10px;'>「這份月度陪伴，是送給妳的時光禮物。」</p>
        <hr style='border: 0.5px solid #E9EDC9; margin: 8px 0;'>
        <p style='font-size:0.9rem; margin-bottom:5px;'>☀️ 晨曦：{m_tea}</p>
        <p style='font-size:0.9rem; margin-bottom:5px;'>🌙 午後：{a_tea}</p>
        <hr style='border: 0.5px solid #E9EDC9; margin: 8px 0;'>
        <p style='font-size:0.85rem; line-height:1.6;'>
            • 40 入深度節律漢方茶組 (全月份份量)<br>
            • 植感生活語錄收藏卡<br>
            • {gift}<br>
            <b>月度質感陪伴價 $1,980</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("預約這份溫柔時光 ➔"): st.session_state.step = 7; st.rerun()

elif st.session_state.step == 7:
    ans, name, first = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time
    if "晨光" in ans[0]: diag, m_tea, a_tea = "暖陽系", "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
    elif "微風" in ans[0]: diag, m_tea, a_tea = "微風系", "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
    else: diag, m_tea, a_tea = "清泉系", "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"
    
    show_leaves()
    st.markdown("### 📢 預約暖心的相遇")
    msg = f"""Hi 米寶店長！🐢✨

我是【{diag}女子】。想預約月度陪伴計畫。
🌿 {'杯蓋刻名：' + name if first == '是的' else '老朋友回購驚喜'} ✨

☀️ 晨曦：{m_tea}
🌙 午後：{a_tea}

期待與這份草本香氣相遇。🌿🍵"""

    st.code(msg, language=None)
    st.markdown(f'<a href="https://line.me/R/ti/p/@716osfvq" style="text-decoration:none;"><div style="background-color: #06C755; color: white; text-align: center; padding: 15px; border-radius: 15px; font-weight: bold;">✨ 領取妳的專屬溫柔陪伴 ➔</div></a>', unsafe_allow_html=True)
    if st.button("重新探索"): st.session_state.clear(); st.rerun()

st.markdown("<p style='text-align:center; font-size:0.75rem; color:#8B8B7A; margin-top:20px;'>慶和蔘藥行研製 © 2026 Mibao Herbal</p>", unsafe_allow_html=True)
