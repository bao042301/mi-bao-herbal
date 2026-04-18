import streamlit as st

# 1. 視覺與風格
st.set_page_config(page_title="米樂漢方｜專屬植感語錄測驗", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    h1, h2, h3 { color: #556B2F; }
    .stButton > button {
        width: 100%; border-radius: 30px; background-color: #556B2F; color: white !important;
        height: 3.5em; font-size: 1.2rem; font-weight: bold;
    }
    .result-box { background-color: #FFFFFF; padding: 25px; border-radius: 20px; border: 2px solid #E9EDC9; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 米樂漢方")
st.subheader("尋找妳的專屬植感語錄")
st.write("忙碌的日子裡，妳好嗎？讓我們為妳找尋此時此刻，最溫柔的漢方陪伴。")

# 2. 情境問題
questions = [
    ("Q1. 剛起床的妳，感覺今天的身體能量像？", ["剛充飽電，但總覺得少了點光澤", "有點重重的，像吸飽水的海綿", "沒電的鬧鐘，需要一點推動力"]),
    ("Q2. 午餐過後，妳的身體最想對妳說的一句話是...？", ["「我想找回紅潤的好氣色。」", "「我想變輕盈，帶走多餘的沉重。」", "「我需要冷靜，幫我趕走煩燥火氣。」"]),
    ("Q3. 結束這一天前，妳最想給自己什麼樣的擁抱？", ["溫潤且紮實的暖意", "清新且無負擔的自在", "穩定且平和的守護"])
]

responses = []
for i, (q_text, opts) in enumerate(questions):
    res = st.radio(q_text, opts, key=f"q{i}")
    responses.append(opts.index(res))

# 3. 查看結果與正確 LINE 連結
if st.button("查看我的專屬陪伴計畫"):
    counts = [responses.count(0), responses.count(1), responses.count(2)]
    result_idx = counts.index(max(counts))
    
    # 正確的 LINE 連結
    line_link = "https://line.me/R/ti/p/@716osfvq  "
    
    st.divider()
    if result_idx == 0:
        st.header("☀️ 妳是：暖陽系女子")
        st.info("**專屬計畫：【暖陽 30 日重啟計畫】**\n\n陪伴內容：當歸紅棗茶、黑豆漢方茶、黃耆元氣茶。")
    elif result_idx == 1:
        st.header("🍃 妳是：微風系女子")
        st.info("**專屬計畫：【微風 30 日重啟計畫】**\n\n陪伴內容：洛神山楂茶、玫瑰決明茶、金菊牛蒡茶。")
    else:
        st.header("💧 妳是：清泉系女子")
        st.info("**專屬計畫：【清泉 30 日重啟計畫】**\n\n陪伴內容：金菊牛蒡茶、黃耆元氣茶、玫瑰決明茶。")
    
    st.markdown(f'<a href="{line_link}" target="_blank"><div style="background-color: #06C755; color: white; text-align: center; padding: 15px; border-radius: 10px; font-weight: bold; font-size: 1.1rem;">LINE 領取 $220 首購優惠 ➔</div></a>', unsafe_allow_html=True)
    st.balloons()

st.markdown('<p style="font-size: 0.8rem; color: #999; text-align: center; margin-top: 50px;">本測驗為生活風格參考，不具醫療診斷功能。產品為一般食品。</p>', unsafe_allow_html=True)