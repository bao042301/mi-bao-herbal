import streamlit as st
import time

# 1. 視覺風格與顯色鎖死 (增加動畫區域樣式)
st.set_page_config(page_title="米寶漢方｜專屬植感測驗", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 確保所有文字在任何模式下都清晰可見 (深橄欖綠) */
    h1, h2, h3, p, span, label {
        color: #2D3A1B !important; 
        font-family: 'Noto Sans TC', sans-serif !important;
    }

    /* 題目字體 */
    .stRadio > label p {
        font-size: 1.5rem !important;
        font-weight: bold !important;
        line-height: 1.5 !important;
        padding: 10px 0 !important;
    }
    
    /* 選項字體 */
    div[data-testid="stMarkdownContainer"] p {
        font-size: 1.25rem !important;
        font-weight: 500 !important;
    }

    /* 按鈕樣式 (綠底白字) */
    .stButton > button {
        width: 100% !important;
        background-color: #556B2F !important;
        color: #FFFFFF !important;
        border-radius: 20px !important;
        height: 3.8em !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border: none !important;
        margin-top: 20px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
    }
    .stButton > button p { color: #FFFFFF !important; }

    /* 【關鍵新增】專屬動畫區塊樣式 (置中、放大) */
    .spinner-box {
        text-align: center;
        padding: 40px;
        background-color: #FFFFFF;
        border-radius: 20px;
        border: 1px solid #E9EDC9;
        margin-top: 30px;
        font-size: 1.4rem !important;
        font-weight: bold !important;
        color: #556B2F !important;
    }
    .spinner-emoji {
        font-size: 3rem !important;
        display: block;
        margin-bottom: 15px;
    }

    /* 隱藏標頭與選單 */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# 品牌標題
st.title("🌿 米寶漢方")
st.write("### 尋找妳的專屬植感語錄")

# 初始化狀態
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
    st.write(f"**STEP {st.session_state.step + 1} / 3**")
    
    # 使用動態 key 確保每題開始時為空心狀態
    selection = st.radio(q_text, opts, index=None, key=f"mibao_final_v5_{st.session_state.step}")
    
    btn_label = "下一題 ➔" if st.session_state.step < 2 else "查看專屬漢方調配 ➔"
    
    if st.button(btn_label):
        if selection is not None:
            st.session_state.answers.append(opts.index(selection))
            st.session_state.step += 1
            st.rerun()
        else:
            st.warning("請選一個最貼近妳心情的選項喔！")
else:
    # 建立一個用於顯示動畫的空白區塊
    spinner_placeholder = st.empty()
    
    # 計算分數
    ans = st.session_state.answers
    counts = [ans.count(0), ans.count(1), ans.count(2)]
    result_idx = counts.index(max(counts))
    line_link = "https://line.me/R/ti/p/@716osfvq"
    
    # 【關鍵修改】依據結果顯示分眾專屬動畫
    if result_idx == 0:
        # 暖陽系動畫
        spinner_placeholder.markdown('<div class="spinner-box"><span class="spinner-emoji">☀️✨☀️</span>正在為您凝聚陽光能量，調配暖陽漢方...</div>', unsafe_allow_html=True)
        time.sleep(1.5) # 模擬調配時間
        
    elif result_idx == 1:
        # 微風系動畫
        spinner_placeholder.markdown('<div class="spinner-box"><span class="spinner-emoji">🍃🌬️🍃</span>正在攔截草本微風，調配清新漢方...</div>', unsafe_allow_html=True)
        time.sleep(1.5)
        
    else:
        # 清泉系動畫
        spinner_placeholder.markdown('<div class="spinner-box"><span class="spinner-emoji">🌊💧🌊</span>正在引導清澈泉水，調配滋潤漢方...</div>', unsafe_allow_html=True)
        time.sleep(1.5)

    # 動畫結束後，清除動畫區塊並顯示結果
    spinner_placeholder.empty()
    st.divider()
    
    # 結果卡片顯示
    if result_idx == 0:
        st.header("☀️ 妳是：暖陽系女子")
        st.success("**米寶計畫：【暖陽 30 日重啟】**\n\n推薦配方：當歸紅棗茶、黑豆漢方茶、黃耆元氣茶。")
        st.balloons() # 暖陽系使用氣球
        
    elif result_idx == 1:
        st.header("🍃 妳是：微風系女子")
        st.success("**米寶計畫：【微風 30 日重啟】**\n\n推薦配方：洛神山楂茶、玫瑰決明茶、金菊牛蒡茶。")
        st.snow() # 微風系使用降雪 (模擬飄樹葉感)
        
    else:
        st.header("💧 妳是：清泉系女子")
        st.success("**米寶計畫：【清泉 30 日重啟】**\n\n推薦配方：金菊牛蒡茶、黃耆元氣茶、玫瑰決明茶。")
        st.balloons() # 清泉系使用氣球
        st.toast("🌊 感覺到清涼的泉水正在滋潤身心...")

    # LINE 引導按鈕
    st.markdown(f'''
        <a href="{line_link}" target="_blank" style="text-decoration:none;">
            <div style="background-color: #06C755; color: white; text-align: center; padding: 18px; border-radius: 12px; font-weight: bold; font-size: 1.3rem; margin-top: 20px;">
                LINE 領取專屬首購優惠 ➔
            </div>
        </a>
    ''', unsafe_allow_html=True)

    if st.button("重新測驗"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()

st.markdown('''
    <div style="font-size: 0.8rem; color: #999; text-align: center; margin-top: 50px;">
        米寶漢方｜三十年慶和蔘藥行經驗監製<br>
        本測驗僅供風格參考，非醫療診斷之用。
    </div>
''', unsafe_allow_html=True)
