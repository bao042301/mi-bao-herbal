import streamlit as st
import time

# 1. 視覺風格設定 (精確調整字體大小比例)
st.set_page_config(page_title="米寶漢方｜專屬植感語錄測驗", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 基本文字顯色與字體 */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #556B2F !important;
        font-family: 'Noto Sans TC', sans-serif !important;
    }

    /* 1. 導覽文字：第 X 題 / 共 3 題 (縮小) */
    .q-index {
        font-size: 0.9rem !important;
        color: #8B9467 !important;
        margin-bottom: 5px !important;
        font-weight: normal !important;
    }

    /* 2. 題目字體：radio 的 label (放大) */
    .stRadio > label { 
        font-size: 1.6rem !important; 
        font-weight: bold !important; 
        line-height: 1.4 !important;
        margin-bottom: 25px !important; 
        display: block !important;
    }
    
    /* 3. 選項字體：每個選項的文字 (比題目稍小一點) */
    div[data-baseweb="radio"] label {
        font-size: 1.25rem !important;
        font-weight: 500 !important;
        color: #556B2F !important;
        padding-top: 10px !important;
        padding-bottom: 10px !important;
    }

    /* 修正按鈕樣式 */
    .stButton > button {
        width: 100% !important;
        background-color: #556B2F !important;
        color: #FFFFFF !important;
        border-radius: 30px !important;
        height: 3.8em !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border: none !important;
        margin-top: 30px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    .stButton > button p { color: #FFFFFF !important; }
    
    .result-box { background-color: #FFFFFF; padding: 25px; border-radius: 20px; border: 2px solid #E9EDC9; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 標題區
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

# 測驗邏輯
if st.session_state.step < len(questions):
    q_text, opts = questions[st.session_state.step]
    
    # 使用自定義 CSS 類別顯示「第幾題」，讓字體變小
    st.markdown(f'<p class="q-index">第 {st.session_state.step + 1} 題 / 共 3 題</p>', unsafe_allow_html=True)
    
    # 選項，初始設為 None (空心)
    selection = st.radio(q_text, opts, index=None, key=f"mibao_v3_{st.session_state.step}")
    
    btn_label = "下一題 ➔" if st.session_state.step < 2 else "查看我的專屬陪伴計畫 ➔"
    
    if st.button(btn_label):
        if selection is not None:
            st.session_state.answers.append(opts.index(selection))
            st.session_state.step += 1
            st.rerun()
        else:
            st.warning("請先選一個妳最心儀的選項喔！")
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
            st.info("**米寶專屬計畫：【暖陽 30 日重啟計畫】**\n\n當歸紅棗茶、黑豆漢方茶、黃耆元氣茶。")
        elif result_idx == 1:
            st.header("🍃 妳是：微風系女子")
            st.write("「願妳的日常，如微風般輕盈自在。」")
            st.info("**米寶專屬計畫：【微風 30 日重啟計畫】**\n\n洛神山楂茶、玫瑰決明茶、金菊牛蒡茶。")
        else:
            st.header("💧 妳是：清泉系女子")
            st.write("「安靜地綻放，就是妳最美的樣子。」")
            st.info("**米寶專屬計畫：【清泉 30 日重啟計畫】**\n\n金菊牛蒡茶、黃耆元氣茶、玫瑰決明茶。")
        
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
        米寶漢方｜溫柔陪伴妳的每一天<br>
        本測驗為生活風格參考，不具醫療診斷功能。產品為一般食品。
    </div>
''', unsafe_allow_html=True)
