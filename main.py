import streamlit as st
import time

# 1. 救援級視覺設定 (白底黑字，最穩定顯色)
st.set_page_config(page_title="米寶漢方｜專屬測驗", layout="centered")
st.markdown("""
    <style>
    /* 1. 強制背景為米白色 */
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 2. 強制所有文字為深綠色，絕不變白 */
    h1, h2, h3, p, span, li, label, div {
        color: #2D3A1B !important; 
        font-family: 'Noto Sans TC', sans-serif !important;
    }

    /* 3. 特別針對題目：字體加大且加粗 */
    .stRadio > label p {
        font-size: 1.5rem !important;
        font-weight: bold !important;
        color: #2D3A1B !important;
        line-height: 1.5 !important;
        padding: 10px 0 !important;
    }
    
    /* 4. 特別針對選項：字體適中 */
    div[data-testid="stMarkdownContainer"] p {
        font-size: 1.2rem !important;
        color: #2D3A1B !important;
    }

    /* 5. 按鈕：維持深綠色底，白字 */
    .stButton > button {
        width: 100% !important;
        background-color: #556B2F !important;
        color: #FFFFFF !important;
        border-radius: 15px !important;
        height: 3.5em !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border: none !important;
        margin-top: 20px !important;
    }
    
    /* 確保按鈕文字一定是白的 */
    .stButton > button p { color: #FFFFFF !important; }

    /* 隱藏不必要的組件避免干擾 */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# 品牌頭部
st.title("🌿 米寶漢方")
st.write("### 尋找妳的專屬植感語錄")

if 'step' not in st.session_state:
    st.session_state.step = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

questions = [
    ("剛起床的妳，感覺今天的身體能量像？", ["剛充飽電，但總覺得少了點光澤", "有點重重的，像吸飽水的海綿", "沒電的鬧鐘，需要一點推動力"]),
    ("午餐過後，妳的身體最想對妳說的一句話是...？", ["「我想找回紅潤的好氣色。」", "「我想變輕盈，帶走多餘的沉重。」", "「我需要冷靜，幫我趕走煩燥火氣。」"]),
    ("結束這一天前，妳最想給自己什麼樣的擁抱？", ["溫潤且紮實的暖意", "清新且無負擔的自在", "穩定且平和的守護"])
]

if st.session_state.step < len(questions):
    q_text, opts = questions[st.session_state.step]
    st.write(f"**STEP {st.session_state.step + 1} / 3**")
    
    # 題目與選項
    selection = st.radio(q_text, opts, index=None, key=f"mibao_rescue_{st.session_state.step}")
    
    btn_label = "下一題 ➔" if st.session_state.step < 2 else "查看我的專屬陪伴計畫 ➔"
    
    if st.button(btn_label):
        if selection is not None:
            st.session_state.answers.append(opts.index(selection))
            st.session_state.step += 1
            st.rerun()
        else:
            st.warning("請選一個選項再繼續喔！")
else:
    with st.spinner('✨ 正在調配中...'):
        time.sleep(1.5)
    
    ans = st.session_state.answers
    counts = [ans.count(0), ans.count(1), ans.count(2)]
    result_idx = counts.index(max(counts))
    line_link = "https://line.me/R/ti/p/@716osfvq"
    
    st.divider()
    if result_idx == 0:
        st.header("☀️ 妳是：暖陽系女子")
        st.info("推薦配方：當歸紅棗茶、黑豆漢方茶、黃耆元氣茶。")
    elif result_idx == 1:
        st.header("🍃 妳是：微風系女子")
        st.info("推薦配方：洛神山楂茶、玫瑰決明茶、金菊牛蒡茶。")
    else:
        st.header("💧 妳是：清泉系女子")
        st.info("推薦配方：金菊牛蒡茶、黃耆元氣茶、玫瑰決明茶。")
    
    st.markdown(f'''
        <a href="{line_link}" target="_blank" style="text-decoration:none;">
            <div style="background-color: #06C755; color: white; text-align: center; padding: 15px; border-radius: 10px; font-weight: bold; font-size: 1.2rem; margin-top: 10px;">
                LINE 領取首購優惠 ➔
            </div>
        </a>
    ''', unsafe_allow_html=True)

    if st.button("重新測驗"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()
    st.balloons()
