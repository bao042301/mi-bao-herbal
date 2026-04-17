import streamlit as st
import time
import os

# 1. 全方位視覺鎖定 (極致穩定顯色與植感調色)
st.set_page_config(page_title="米寶漢方｜妳的月度質感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域鎖定深橄欖綠文字，防止深色模式干擾 */
    * {
        color: #4A4E31 !important;
        font-family: 'Noto Sans TC', sans-serif !important;
    }
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 標題與引言 */
    h1, h2, h3 { text-align: center !important; margin-bottom: 10px !important; }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 20px; font-size: 0.95rem; }

    /* 選項 (Radio) 顏色：質感橄欖綠 */
    div[data-baseweb="radio"] div {
        color: #6B705C !important;
    }
    div[data-baseweb="radio"] div[aria-checked="true"] > div {
        background-color: #6B705C !important;
    }

    /* 雷刻輸入框：強制白底綠邊，絕不變黑 */
    .stTextInput input {
        background-color: #FFFFFF !important;
        border: 2px solid #E9EDC9 !important;
        border-radius: 12px !important;
        color: #4A4E31 !important;
        padding: 10px !important;
    }
    .stTextInput div[data-baseweb="input"] {
        background-color: transparent !important;
        border: none !important;
    }

    /* 按鈕樣式 (綠底白字) */
    .stButton > button {
        width: 100% !important;
        background-color: #6B705C !important;
        color: #FFFFFF !important;
        border-radius: 25px !important;
        height: 3.8em !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    }
    .stButton > button p { color: #FFFFFF !important; }

    /* 質感訂單訊息框 (淺草色信箋風格，移除黑底) */
    .order-box {
        background-color: #F8F9F1 !important;
        padding: 20px !important;
        border-radius: 15px !important;
        border: 1px solid #E9EDC9 !important;
        margin: 20px 0 !important;
        font-size: 0.95rem !important;
        line-height: 1.6 !important;
        white-space: pre-wrap !important;
    }

    /* 結果卡片區塊 */
    .result-card { 
        background-color: #FFFFFF !important; 
        padding: 25px !important; 
        border-radius: 25px !important; 
        border: 2px solid #E9EDC9 !important;
    }
    
    /* 隱藏預設選單 */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# 初始化 Session State
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'custom_name' not in st.session_state:
    st.session_state.custom_name = ""

# ----------------- 頂部品牌區 -----------------

img_path = "29301.jpg"
if os.path.exists(img_path):
    st.image(img_path, use_container_width=True)
else:
    st.markdown("<h1 style='font-size: 2rem;'>🌿 米寶漢方</h1>", unsafe_allow_html=True)

st.markdown('<p class="quote">「在忙碌中，給自己留一刻鐘的溫柔。」</p>', unsafe_allow_html=True)

# ----------------- 測驗流程 -----------------

if st.session_state.step == 1:
    st.write("### 第一步：聽聽身體的低語")
    q1 = st.radio("當妳靜下心，妳的身體正低聲說著...？", 
                  ["我有些疲累，渴望溫潤透亮的晨光...", 
                   "我有些沉重，想找回輕盈自在的微風...", 
                   "我有些燥熱，想念山間清徹甘甜的泉水..."], index=None, key="v5_q1")
    if st.button("下一頁：梳理日常 ➔"):
        if q1:
            st.session_state.answers.append(q1)
            st.session_state.step = 2
            st.rerun()
        else:
            st.warning("請選一個最貼近妳的感覺喔")

elif st.session_state.step == 2:
    st.write("### 第二步：梳理日常的步調")
    q2 = st.radio("關於這段日子的作息，妳目前的感受是？", 
                  ["長時間待在冷氣房，循環緩慢且手腳冰冷", 
                   "工作忙碌常熬夜，晚餐不規律導致不適", 
                   "壓力大節奏快，晚上難以入眠且心神不寧"], index=None, key="v5_q2")
    if st.button("下一頁：嚮往的瞬間 ➔"):
        if q2:
            st.session_state.answers.append(q2)
            st.session_state.step = 3
            st.rerun()
        else:
            st.warning("請選一個妳的日常狀態喔")

elif st.session_state.step == 3:
    st.write("### 第三步：妳嚮往的喘息瞬間")
    q3 = st.radio("在最需要喘息的午後，妳最嚮往什麼樣的瞬間？", 
                  ["感覺臉龐恢復紅潤元氣，重新出發", 
                   "感覺身體找回輕盈律動，不再束縛", 
                   "感覺內心恢復安靜穩定，優雅從容"], index=None, key="v5_q3")
    if st.button("最後一步：鐫刻溫柔 ➔"):
        if q3:
            st.session_state.answers.append(q3)
            st.session_state.step = 4
            st.rerun()
        else:
            st.warning("想像一下那個畫面，選一個吧")

elif st.session_state.step == 4:
    st.write("### 💎 鐫刻妳的專屬溫柔")
    st.markdown("""
        <div style='background-color: #FFFFFF; padding: 25px; border-radius: 15px; border: 1px solid #E9EDC9; margin-bottom: 20px;'>
            「在忙碌日常中，為自己留下一個空白。鐫刻上妳的名字，或是那句提醒妳的溫柔。<br><br>
            讓這個隨行杯陪伴妳度過每一天，提醒妳值得被溫柔對待。」
        </div>
    """, unsafe_allow_html=True)
    
    user_name = st.text_input("輸入要雷刻在木蓋上的名字 (最多12字)", max_chars=12, placeholder="例如：Mila 或 Quiet")
    
    if st.button("開啟我的月度質感陪伴 ➔"):
        if user_name:
            st.session_state.custom_name = user_name
            st.session_state.step = 5
            st.rerun()
        else:
            st.warning("留下一個名字吧，讓這份禮物專屬於妳。")

elif st.session_state.step == 5:
    # 載入儀式
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<p class="quote">正在為妳揉捻專屬的草本香氣...</p>', unsafe_allow_html=True)
        time.sleep(1.5)
        st.markdown('<p class="quote">正在鐫刻妳的專屬溫柔陪伴...</p>', unsafe_allow_html=True)
        time.sleep(1.5)
    placeholder.empty()

    ans = st.session_state.answers
    name = st.session_state.custom_name
    
    # 配比邏輯鎖定
    if "晨光" in ans[0]:
        diag = "暖陽系"
        m_tea = "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)"
        a_tea = "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
    elif "微風" in ans[0]:
        diag = "微風系"
        m_tea = "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)"
        a_tea = "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
    else:
        diag = "清泉系"
        m_tea = "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)"
        a_tea = "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"

    st.balloons()
    
    # 結果頁面佈局
    st.markdown(f"""
    <div class="result-card">
        <h3 style='text-align:center;'>✨ 妳是：{diag}女子</h3>
        <p class="quote">「這份月度陪伴計畫，是送給妳的時光禮物。」</p>
        <hr style='border: 0.5px solid #E9EDC9;'>
        <p style='margin-bottom:5px;'><b>☀️ 晨曦啟幕配比：</b></p>
        <p style='font-size:0.95rem;'>{m_tea}</p>
        <br>
        <p style='margin-bottom:5px;'><b>🌙 午後拾光配比：</b></p>
        <p style='font-size:0.95rem;'>{a_tea}</p>
        <hr style='border: 0.5px solid #E9EDC9;'>
        <p style='font-size:0.9rem;'><b>陪伴包含：</b> 40入茶組 + 生活手札 + 雷刻刻名杯 (刻名：{name})</p>
        <h3 style='text-align:right; color:#6B705C !important;'>月度陪伴價 $1,980</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("👇 請長按複製下方訊息，開啟妳的溫柔陪伴：")
    
    # 完整的預約訊息 (含茶包與包數)
    order_msg = f"你好，我想預約【米寶漢方｜月度質感陪伴】\n我是：{diag}女子\n雷刻文字：{name}\n\n專屬配比內容：\n晨曦：{m_tea}\n午後：{a_tea}\n\n我已完成測驗，想領取專屬杯與月度茶組。"
    
    st.markdown(f'<div class="order-box">{order_msg}</div>', unsafe_allow_html=True)
    
    st.markdown(f'<a href="https://line.me/R/ti/p/@716osfvq" target="_blank" style="text-decoration:none;"><div style="background-color: #06C755; color: white !important; text-align: center; padding: 18px; border-radius: 12px; font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 10px rgba(6,199,85,0.2);">點我開啟 LINE 預約 ➔</div></a>', unsafe_allow_html=True)

    if st.button("重新探索新的陪伴"):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

st.markdown("<p style='text-align:center; font-size:0.8rem; color:#8B8B7A; margin-top:60px;'>米寶漢方｜慶和蔘藥行三十年經驗監製<br>產品為一般食品，溫柔陪伴妳的日常。 © 2026 Mibao Herbal</p>", unsafe_allow_html=True)
