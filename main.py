import streamlit as st
import time

# 1. 視覺風格設定 (精品卡片化、強烈字體對比)
st.set_page_config(page_title="米寶漢方｜專屬植感語錄測驗", layout="centered")
st.markdown("""
    <style>
    /* 全域背景 */
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 1. 導覽文字：小而淡 */
    .q-index {
        font-size: 0.85rem !important;
        color: #A0A880 !important;
        margin-bottom: 10px !important;
        letter-spacing: 1px;
    }

    /* 2. 題目區：深色底板 + 大白字 */
    .stRadio > label { 
        background-color: #556B2F !important;
        color: #FFFFFF !important;
        padding: 25px 20px !important;
        border-radius: 15px !important;
        font-size: 1.8rem !important; /* 超大題目字體 */
        font-weight: bold !important;
        line-height: 1.3 !important;
        margin-bottom: 20px !important;
        box-shadow: 0 4px 12px rgba(85, 107, 47, 0.2) !important;
    }
    
    /* 3. 選項區：淺色底板 + 邊框 */
    div[data-baseweb="radio"] label {
        background-color: #FFFFFF !important;
        border: 1.5px solid #E9EDC9 !important;
        padding: 15px 20px !important;
        border-radius: 12px !important;
        margin-bottom: 10px !important;
        font-size: 1.3rem !important; /* 選項字體加大 */
        transition: all 0.3s ease !important;
        color: #556B2F !important;
    }

    /* 選項點擊後的視覺回饋 */
    div[data-baseweb="radio"] label:hover {
        background-color: #F0F4E8 !important;
        border-color: #556B2F !important;
    }

    /* 按鈕美化 */
    .stButton > button {
        width: 100% !important;
        background-color: #556B2F !important;
        color: #FFFFFF !important;
        border-radius: 30px !important;
        height: 3.8em !important;
        font-size: 1.25rem !important;
        font-weight: bold !important;
        border: none !important;
        margin-top: 20px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
    }
    .stButton > button p { color: #FFFFFF !important; }
    
    .result-box { background-color: #FFFFFF; padding: 25px; border-radius: 20px; border: 2px solid #E9EDC9; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 品牌頭部
st.title("🌿 米寶漢方")
st.subheader("尋找妳的專屬植感語錄")

if 'step' not in st.session_state:
    st.session_state.step = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

questions = [
    ("剛起床的妳，感覺今天的身體能量像？", ["剛充飽電，但總覺得少了點光澤", "有點重重的，像吸飽水的海綿", "沒電的鬧鐘，需要一點推動力"]),
    ("午餐過後，妳的身體最想對妳說的一句話是...？", ["「我想找回紅潤的好氣色。」", "「我想變輕盈，帶走多餘的沉重。」", "「我需要冷靜，幫我趕走煩燥火氣。」"]),
    ("結束這一天前，妳最想給自己什麼樣的擁抱？", ["溫潤且紮實的暖意", "清新且無負擔的自在", "穩定且平和的守護"])
]

# 測驗進程
if st.session_state.step < len(questions):
    q_text, opts = questions[st.session_state.step]
    
    st.markdown(f'<p class="q-index">STEP {st.session_state.step + 1} / 3</p>', unsafe_allow_html=True)
    
    # 選項，index=None 保持初始空心
    selection = st.radio(q_text, opts, index=None, key=f"mibao_v4_{st.session_state.step}")
    
    btn_label = "下一題 ➔" if st.session_state.step < 2 else "查看專屬漢方調配 ➔"
    
    if st.button(btn_label):
        if selection is not None:
            st.session_state.answers.append(opts.index(selection))
            st.session_state.step += 1
            st.rerun()
        else:
            st.warning("請選一個最貼近妳現在心情的答案喔！")
else:
    with st.spinner('✨ 正在幫您調配專屬漢方中...'):
        time.sleep(2)
    
    ans = st.session_state.answers
    counts = [ans.count(0), ans.count(1), ans.count(2)]
    result_idx = counts.index(max(counts))
    line_link = "https://line.me/R/ti/p/@716osfvq"
    
    st.divider()
    with st.container():
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        if result_idx == 0:
            st.header("☀️ 妳是：暖陽系女子")
            st.write("「妳是溫潤的暖陽，但別忘了也要溫暖自己。」")
            st.info("**米寶專屬計畫：【暖陽 30 日重啟計畫】**\n\n推薦配方：當歸紅棗茶、黑豆漢方茶、黃耆元氣茶。")
        elif result_idx == 1:
            st.header("🍃 妳是：微風系女子")
            st.write("「願妳的日常，如微風般輕盈自在。」")
            st.info("**米寶專屬計畫：【微風 30 日重啟計畫】**\n\n推薦配方：洛神山楂茶、玫瑰決明茶、金菊牛蒡茶。")
        else:
            st.header("💧 妳是：清泉系女子")
            st.write("「安靜地綻放，就是妳最美的樣子。」")
            st.info("**米寶專屬計畫：【清泉 30 日重啟計畫】**\n\n推薦配方：金菊牛蒡茶、黃耆元氣茶、玫瑰決明茶。")
        
        st.markdown(f'''
            <a href="{line_link}" target="_blank" style="text-decoration:none;">
                <div style="background-color: #06C755; color: white; text-align: center; padding: 15px; border-radius: 10px; font-weight: bold; font-size: 1.2rem; margin-top: 20px;">
                    LINE 領取 $220 首購優惠 ➔
                </div>
            </a>
        ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("重新測驗"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()
    st.balloons()

st.markdown('''
    <div style="font-size: 0.8rem; color: #999; text-align: center; margin-top: 50px;">
        米寶漢方｜三十年慶和蔘藥行經驗監製<br>
        本測驗僅供風格參考，非醫療診斷之用。
    </div>
''', unsafe_allow_html=True)
