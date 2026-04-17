import streamlit as st
import time
import os

# 1. 視覺鎖定 (極致壓縮空間、修正標題、去黑底、三色網底)
st.set_page_config(page_title="米寶漢方｜妳的植感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域顯色鎖定 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 【關鍵優化】極致壓縮頂部間距，讓內容上提，防止底部卡到 */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
    }

    /* 標題與題目：強制顯色且緊湊 */
    h3 { 
        font-size: 1rem !important; font-weight: 700 !important;
        margin-top: 0px !important; margin-bottom: 2px !important;
        text-align: center !important; color: #7A8450 !important;
        display: block !important; visibility: visible !important;
    }
    .question-text {
        font-size: 1.1rem !important; font-weight: bold !important;
        text-align: center !important; margin-bottom: 10px !important;
        line-height: 1.3 !important;
    }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 10px; font-size: 0.75rem; }

    /* Logo 極致縮小 */
    [data-testid="stImage"] img { max-height: 60px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: -10px !important; }

    /* 【選項卡片】移除黑點 + 三色網底 + 緊湊間距 */
    [data-testid="stRadio"] div[role="radiogroup"] input { display: none !important; }
    [data-testid="stRadio"] div[role="radiogroup"] { gap: 6px !important; } /* 縮小卡片間距 */
    
    [data-testid="stRadio"] label {
        border-radius: 10px !important; padding: 10px 15px !important;
        width: 100% !important; border: 1px solid rgba(0,0,0,0.03) !important;
        display: flex !important; justify-content: center !important; text-align: center !important;
        transition: all 0.2s ease !important; cursor: pointer !important;
        font-size: 0.95rem !important;
    }

    /* 三色穩定鎖定 */
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(1) label { background-color: #F1F4E8 !important; }
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(2) label { background-color: #FDF2E9 !important; }
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(3) label { background-color: #EBF5FB !important; }
    [data-testid="stRadio"] div[aria-checked="true"] label { border: 1.5px solid #7A8450 !important; }

    /* 去黑底鎖定 */
    .stTextInput input { background-color: #FFFFFF !important; border: 1.5px solid #E9EDC9 !important; border-radius: 10px !important; }
    [data-testid="stCodeBlock"], [data-testid="stCodeBlock"] > div, pre, code {
        background-color: #F8F9F1 !important; border: 1px solid #E9EDC9 !important; border-radius: 12px !important;
    }
    code span { background-color: transparent !important; color: #4A4E31 !important; }

    /* 按鈕扁平化：節省空間 */
    .stButton > button {
        width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important;
        border-radius: 25px !important; height: 2.8em !important; font-weight: bold !important; border: none !important;
        margin-top: 5px !important;
    }
    .stButton > button p { color: #FFFFFF !important; font-size: 0.95rem !important; }

    /* 特效 */
    @keyframes falling {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .leaf { position: fixed; top: -10vh; font-size: 20px; pointer-events: none; z-index: 9999; animation: falling 10s linear infinite; }

    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

def show_leaves():
    leaves_html = "".join([f'<div class="leaf" style="left:{i*15}vw; animation-delay:{i*1.2}s;">🍃</div>' for i in range(7)])
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
st.markdown('<p class="quote">「在忙碌中，給自己留一刻鐘的溫柔。」</p>', unsafe_allow_html=True)

# ----------------- 測驗流程 -----------------
if st.session_state.step == 1:
    st.markdown("### 第一步：聽聽身體的低語")
    st.markdown('<p class="question-text">當妳靜下心，妳的身體正低聲說著...？</p>', unsafe_allow_html=True)
    q1 = st.radio("", ["我有些疲累，渴望溫潤透亮的晨光...", "我有些沉重，想找回輕盈自在的微風...", "我有些燥熱，想念山間清徹甘甜的泉水..."], index=None, key="v39_q1", label_visibility="collapsed")
    if st.button("緩緩走向下個瞬間 ➔"):
        if q1: st.session_state.answers.append(q1); st.session_state.step = 2; st.rerun()

elif st.session_state.step == 2:
    st.markdown("### 第二步：梳理日常的步調")
    st.markdown('<p class="question-text">關於這段日子的作息，妳目前的感受是？</p>', unsafe_allow_html=True)
    q2 = st.radio("", ["長時間待在冷氣房，循環緩慢且手腳冰冷", "工作忙碌常熬夜，晚餐不規律導致不適", "壓力大節奏快，晚上難以入眠且心神不寧"], index=None, key="v39_q2", label_visibility="collapsed")
    if st.button("傾聽日常的節奏 ➔"):
        if q2: st.session_state.answers.append(q2); st.session_state.step = 3; st.rerun()

elif st.session_state.step == 3:
    st.markdown("### 第三步：妳嚮往的喘息瞬間")
    st.markdown('<p class="question-text">在最需要喘息的午後，妳最嚮往的瞬間？</p>', unsafe_allow_html=True)
    q3 = st.radio("", ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，優雅從容"], index=None, key="v39_q3", label_visibility="collapsed")
    if st.button("開啟妳的專屬禮遇 ➔"):
        if q3: st.session_state.answers.append(q3); st.session_state.step = 4; st.rerun()

elif st.session_state.step == 4:
    st.markdown("### 💎 妳是米寶的新朋友嗎？")
    opts = ["是的，我是新朋友", "不是，我是老朋友了（已有隨行杯）"]
    choice = st.radio("", opts, index=None, key="v39_choice", label_visibility="collapsed")
    if st.button("前往專屬的陪伴 ➔"):
        if choice == opts[0]: st.session_state.is_first_time = "是的"; st.session_state.step = 5; st.rerun()
        elif choice == opts[1]: st.session_state.is_first_time = "不是"; st.session_state.custom_name = "老朋友回購驚喜"; st.session_state.step = 6; st.rerun()

elif st.session_state.step == 5:
    st.markdown("### 💎 鐫刻妳的專屬溫柔")
    st.markdown("""<div style='background-color: #FFFFFF; padding: 12px; border-radius: 10px; border: 1px solid #E9EDC9; font-size:0.85rem; text-align:center;'>為妳準備一只質感的玻璃隨行杯。讓我們在木蓋上，鐫刻專屬的名字，陪伴妳每一天。</div>""", unsafe_allow_html=True)
    user_name = st.text_input("雷刻名字 (最多12字)", max_chars=12, placeholder="例如：Mila")
    if st.button("查看我的質感陪伴配比 ➔"):
        if user_name: st.session_state.custom_name = user_name; st.session_state.step = 6; st.rerun()

elif st.session_state.step == 6:
    ans, name, first = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time
    if "晨光" in ans[0]: diag, m, a = "暖陽系", "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
    elif "微風" in ans[0]: diag, m, a = "微風系", "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
    else: diag, m, a = "清泉系", "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"

    show_leaves() 
    gift = f"• 精品首購禮：專屬刻名玻璃隨行杯 ({name})" if first=="是的" else "• 老朋友回饋禮：加贈驚喜茶包 3 包"
    
    st.markdown(f"""
    <div style="background-color: #FFFFFF; padding: 12px; border-radius: 15px; border: 1px solid #E9EDC9;">
        <h3 style='margin:0; font-size:1.2rem !important;'>✨ 妳是：{diag}女子</h3>
        <hr style='border: 0.5px solid #E9EDC9; margin: 5px 0;'>
        <p style='font-size:0.9rem; margin:0;'>☀️ 晨曦：{m}</p>
        <p style='font-size:0.9rem; margin:0;'>🌙 午後：{a}</p>
        <hr style='border: 0.5px solid #E9EDC9; margin: 5px 0;'>
        <p style='font-size:0.8rem; line-height:1.5; margin:0;'>
            • 40 入深度節律漢方茶組 (全月份份量)<br>• 植感生活語錄收藏卡 (暖心鼓勵)<br>{gift}<br>
            <b>月度質感陪伴價 $1,980</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("預約這份溫柔時光 ➔"): st.session_state.step = 7; st.rerun()

elif st.session_state.step == 7:
    ans, name, first = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time
    if "晨光" in ans[0]: diag, m, a = "暖陽系", "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
    elif "微風" in ans[0]: diag, m, a = "微風系", "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
    else: diag, m, a = "清泉系", "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"
    
    show_leaves()
    st.markdown("### 📢 預約暖心的相遇")
    engrave = f"杯蓋想悄悄刻上：{name} ✨" if first == "是的" else "我是老朋友了，想領取回購驚喜 🐢🎁"
    msg = f"""Hi 米寶店長！🐢✨

我剛剛完成植感測驗了，我是【{diag}女子】。
想預約這份月度陪伴，讓這份溫柔陪我度過每一天。

🌿 {engrave}

我的專屬配比：
☀️ 晨曦：{m}
🌙 午後：{a}

期待與這份草本香氣相遇。🌿🍵"""
    st.write("最後一步，完成暖心的約定。點擊右上角複製文字並交給米寶店長：")
    st.code(msg, language=None)
    st.markdown(f'<a href="https://line.me/R/ti/p/@716osfvq" style="text-decoration:none;"><div style="background-color: #06C755; color: white; text-align: center; padding: 12px; border-radius: 12px; font-weight: bold;">✨ LINE 領取專屬陪伴 ➔</div></a>', unsafe_allow_html=True)
    if st.button("重新探索"): st.session_state.clear(); st.rerun()

st.markdown("<p style='text-align:center; font-size:0.7rem; color:#8B8B7A; margin-top:15px;'>慶和蔘藥行研製 © 2026 Mibao Herbal</p>", unsafe_allow_html=True)
