import streamlit as st
import time

# 1. 視覺風格設定
st.set_page_config(page_title="米寶漢方｜專屬植感語錄測驗", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    h1, h2, h3 { color: #556B2F; font-family: 'Noto Sans TC', sans-serif; }
    .stRadio > label { font-size: 1.2rem; color: #556B2F; padding-bottom: 10px; }
    .stButton > button {
        width: 100%; border-radius: 30px; background-color: #556B2F; color: white !important;
        height: 3.5em; font-size: 1.2rem; font-weight: bold; border: none; margin-top: 20px;
    }
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
    ("Q1. 剛起床的妳，感覺今天的身體能量像？", ["剛充飽電，但總覺得少了點光澤", "有點重重的，像吸飽水的海綿", "沒電的鬧鐘，需要一點推動力"]),
    ("Q2. 午餐過後，妳的身體最想對妳說的一句話是...？", ["「我想找回紅潤的好氣色。」", "「我想變輕盈，帶走多餘的沉重。」", "「我需要冷靜，幫我趕走煩燥火氣。」"]),
    ("Q3. 結束這一天前，妳最想給自己什麼樣的擁抱？", ["溫潤且紮實的暖意", "清新且無負擔的自在", "穩定且平和的守護"])
]

if st.session_state.step < len(questions):
    q_text, opts = questions[st.session_state.step]
    st.write(f"第 {st.session_state.step + 1} 題 / 共 3 題")
    selection = st.radio(q_text, opts, index=None, key=f"q_{st.session_state.step}")
    
    if st.button("下一題" if st.session_state.step < 2 else "查看測驗結果"):
        if selection is not None:
            st.session_state.answers.append(opts.index(selection))
            st.session_state.step += 1
            st.rerun()
        else:
            st.warning("請選擇一個選項再繼續喔！")
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
            st.info("**米寶專屬計畫：【暖陽 30 日重啟計畫】**\n\n內容：當歸紅棗茶、黑豆漢方茶、黃耆元氣茶。")
        elif result_idx == 1:
            st.header("🍃 妳是：微風系女子")
            st.write("「願妳的日常，如微風般輕盈自在。」")
            st.info("**米寶專屬計畫：【微風 30 日重啟計畫】**\n\n內容：洛神山楂茶、玫瑰決明茶、金菊牛蒡茶。")
        else:
            st.header("💧 妳是：清泉系女子")
            st.write("「安靜地綻放，就是妳最美的樣子。」")
            st.info("**米寶專屬計畫：【清泉 30 日重啟計畫】**\n\n內容：金菊牛蒡茶、黃耆元氣茶、玫瑰決明茶。")
        
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
