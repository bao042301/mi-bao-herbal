import streamlit as st
import time

# 1. 視覺與動畫設定 (維持高淨值品牌感)
st.set_page_config(page_title="米寶漢方｜妳的月度植感練習", layout="centered", page_icon="🌿")
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7 !important; }
    h1, h2, h3 { color: #4A4E31 !important; font-family: 'Noto Serif TC', serif !important; text-align: center !important; }
    
    /* 強制所有段落、單選框文字顏色為深橄欖綠，絕不變白 */
    p, span, label, .stMarkdown p { color: #4A4E31 !important; }
    
    /* 單選框選項文字樣式 */
    .stRadio > label { font-size: 1.25rem !important; color: #4A4E31 !important; font-weight: bold !important; margin-bottom: 20px !important; }
    div[data-baseweb="radio"] label { font-size: 1.15rem !important; padding: 10px 0 !important; }

    /* 按鈕樣式 (綠底白字) */
    .stButton > button {
        width: 100% !important; border-radius: 30px !important; background-color: #6B705C !important; color: white !important;
        height: 3.8em !important; font-size: 1.1rem !important; font-weight: bold !important; border: none !important;
        margin-top: 30px !important; display: flex !important; align-items: center !important; justify-content: center !important;
    }
    .stButton > button p { color: #FFFFFF !important; } /* 鎖定按鈕文字為白 */
    
    /* 文字輸入框樣式 */
    .stTextInput > div > div > input {
        border-radius: 15px !important;
        border: 2px solid #E9EDC9 !important;
        height: 3.5em !important;
        font-size: 1.1rem !important;
        background-color: #FFFFFF !important;
        color: #4A4E31 !important;
    }
    .stTextInput > label { font-size: 1.2rem !important; color: #4A4E31 !important; font-weight: bold !important; }

    /* 結果卡片樣式 */
    .result-card { 
        background-color: #FFFFFF; padding: 30px; border-radius: 25px; 
        border: 1px solid #E9EDC9; box-shadow: 0 10px 30px rgba(0,0,0,0.06);
        margin-top: 20px;
    }
    .tea-item { display: flex; justify-content: space-between; border-bottom: 1px dashed #DDBEA9; padding: 12px 0; color: #4A4E31; font-size: 1.05rem; }
    .quote { font-style: italic; color: #8B8B7A; text-align: center; margin-bottom: 20px; font-size: 1rem; line-height: 1.6; }
    .tag { background-color: #FFE8D6; color: #6B705C; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: bold; }
    
    /* 儀式感文字 */
    .ritual-text {
        color: #6B705C !important; font-size: 1.1rem !important; line-height: 1.8 !important; text-align: center !important;
        padding: 20px; background-color: #FFFFFF; border-radius: 15px; border: 1px solid #E9EDC9; margin-bottom: 30px;
    }
    
    /* 隱藏標頭與選單 */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# 初始化 Session State (V2 流程修復)
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'custom_name' not in st.session_state:
    st.session_state.custom_name = "Dear"

# 標題區 (全域顯示)
st.title("🌿 米寶漢方")

# 2. 分步測驗邏輯
if st.session_state.step == 1:
    st.markdown('<p class="quote">「在忙碌中，給自己留一刻鐘的溫柔。」</p>', unsafe_allow_html=True)
    
    # 加入品牌圖片：Roselle Tea (微風系代表圖) 建立精品感
    st.image("uploaded:29301.jpg", caption="🌸 精品漢方，源自庆和蔘藥行三十年研製", use_container_width=True)
    st.divider()
    
    st.write("### 第一步：聽聽身體的低語")
    q1 = st.radio("當妳靜下心，妳的身體正低聲說著...？", 
                  ["我有些疲累，渴望一份溫潤透亮的晨光...", 
                   "我有些沉重，想找回輕盈自在的微風...", 
                   "我有些燥熱，想念山間清徹甘甜的泉水..."])
    if st.button("下一頁：梳理日常 ➔"):
        st.session_state.answers.append(q1)
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.write("### 第二步：梳理日常的步調")
    q2 = st.radio("關於這段日子的作息，妳目前的感受是？", 
                  ["長時間待在冷氣房，循環緩慢且手腳冰冷", 
                   "工作忙碌常熬夜，晚餐不規律導致消化不適", 
                   "壓力大節奏快，晚上難以入眠且心神不寧"])
    if st.button("下一頁：嚮往的瞬間 ➔"):
        st.session_state.answers.append(q2)
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    # 優化第三題：側重結果渴望，更有情感連結
    st.write("### 第三步：妳嚮往的喘息瞬間")
    q3 = st.radio("在最需要喘息的午後，妳最嚮往什麼樣的瞬間？", 
                  ["感覺臉龐恢復紅潤元氣，身體溫暖舒適", 
                   "感覺身體找回律動，全身輕盈無束縛", 
                   "感覺內心安靜穩定，趕走燥熱煩悶"])
    
    if st.button("最後一步：鐫刻溫柔 ➔"):
        st.session_state.answers.append(q3)
        st.session_state.step = 4
        st.rerun()

# 3. 獨立雷刻專屬頁 (強化儀式感與浪漫文案)
elif st.session_state.step == 4:
    st.write("### 💎 鐫刻妳的專屬溫柔")
    
    st.markdown("""
        <div class="ritual-text">
            「在忙碌日常中，為自己留下一個空白。<br>
            鐫刻上妳的名字，或是那句提醒妳的溫柔。<br>
            讓這個隨行杯，陪妳渡過每一天，提醒妳值得被溫柔對待。」
        </div>
        """, unsafe_allow_html=True)
    
    # 浪漫文字與儀式感引導
    custom_name = st.text_input("想要鐫刻在杯蓋上的文字 (最多12字)", placeholder="例如：Mila 或 Quiet", max_chars=12)
    st.markdown("<p style='font-size:0.9rem; color:#8B8B7A; text-align:right;'>建議 6-8 字，清晰透亮</p>", unsafe_allow_html=True)
    
    if st.button("開啟我的月度植感練習 ➔"):
        if custom_name: # 防呆機制：必須輸入名字
            st.session_state.custom_name = custom_name
            st.session_state.step = 5
            st.rerun()
        else:
            st.warning("💎 留下一個名字吧，讓它陪妳度過每一天。")

# 4. 結果與配比 (修復邏輯計算與動畫)
elif st.session_state.step == 5:
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<p class="quote">正在為妳揉捻專屬的草本香氣...</p>', unsafe_allow_html=True)
        time.sleep(1.5)
        st.markdown('<p class="quote">正在鐫刻妳的專屬溫柔印記...</p>', unsafe_allow_html=True)
        time.sleep(1.5)
    placeholder.empty()

    ans = st.session_state.answers
    name = st.session_state.custom_name
    
    # V5 邏輯計算 (修正索引問題)
    if "晨光" in ans[0] or "紅潤" in ans[2]:
        diag, quote = "暖陽系女子", "「妳是溫潤的暖陽，哪怕忙碌，也要記得為自己發光。」"
        morning_tea, morning_count = "黃耆元氣茶", 14
        afternoon_tea, afternoon_count = "當歸紅棗茶", 12
        side_tea1, side1_count = "金菊牛蒡茶", 6
        side_tea2, side2_count = "黑豆漢方茶", 8
        result_special_effect = "☀️"
    elif "微風" in ans[0] or "律動" in ans[2]:
        diag, quote = "微風系女子", "「願妳的日常，如微風般輕盈自在，不留任何負擔。」"
        morning_tea, morning_count = "洛神山楂茶", 12
        afternoon_tea, afternoon_count = "玫瑰決明茶", 10
        side_tea1, side1_count = "金菊牛蒡茶", 8
        side_tea2, side2_count = "黑豆漢方茶", 10
        result_special_effect = "🍂"
    else:
        diag, quote = "清泉系女子", "「在紛擾的世界裡，做一池最安靜、最深邃的清泉。」"
        morning_tea, morning_count = "金菊牛蒡茶", 15
        afternoon_tea, afternoon_count = "玫瑰決明茶", 14
        side_tea1, side1_count = "黃耆元氣茶", 5
        side_tea2, side2_count = "當歸紅棗茶", 6
        result_special_effect = "💧"

    st.balloons()
    
    st.markdown(f'<div class="result-card">', unsafe_allow_html=True)
    st.markdown(f'<p class="quote" style="color:#6B705C;">{result_special_effect} {quote}</p>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="text-align:center; color:#4A4E31;">✨ 妳是：【{diag}】</h3>', unsafe_allow_html=True)
    
    st.markdown("<p style='font-weight:bold; margin-top:20px; color:#4A4E31;'>☀️ 晨曦啟幕配比 (建議早晨飲用)</p>", unsafe_allow_html=True)
    st.markdown(f'<div class="tea-item"><span>{morning_tea}</span><span class="tag">{morning_count} 入</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="tea-item"><span>{side_tea1}</span><span class="tag">{side1_count} 入</span></div>', unsafe_allow_html=True)
        
    st.markdown("<p style='font-weight:bold; margin-top:20px; color:#4A4E31;'>🌙 午後拾光配比 (建議下午飮用)</p>", unsafe_allow_html=True)
    st.markdown(f'<div class="tea-item"><span>{afternoon_tea}</span><span class="tag">{afternoon_count} 入</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="tea-item"><span>{side_tea2}</span><span class="tag">{side2_count} 入</span></div>', unsafe_allow_html=True)
        
    st.divider()
    st.markdown(f"""
        <p style="color:#4A4E31; font-size:1rem; line-height:1.6;"><b>月度陪伴計畫包含：</b><br>
        • <b>40 入</b>深度節律漢方茶組 (四週節律)<br>
        • 生活風格手札<br>
        • <b>雷射刻名</b>精品木蓋隨行杯 (刻上妳的名字：{name if name else 'Dear'})</p>
        <h3 style="color:#4A4E31; text-align:right; margin-top:15px;">月度陪伴價：$1,980</h3>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # LINE 代碼與預約按鈕
    order_msg = f"你好，我想預約【米寶漢方｜月度植感練習】\n我是：{diag}\n晨曦配比：{morning_tea}*{morning_count}, {side_tea1}*{side1_count}\n午後配比：{afternoon_tea}*{afternoon_count}, {side_tea2}*{side2_count}\n雷刻文字：{name}"
    
    st.write("👇 請複製下方預約文字，並告知米寶，即刻開啟溫柔日常：")
    st.code(order_msg)
    
    line_link = "https://line.me/R/ti/p/@716osfvq"
    st.markdown(f'<a href="{line_link}" target="_blank" style="text-decoration:none;"><div style="background-color: #06C755; color: white !important; text-align: center; padding: 18px; border-radius: 12px; font-weight: bold; font-size: 1.2rem;">複製內容，去 LINE 完成預約 ➔</div></a>', unsafe_allow_html=True)
    
    if st.button("重新探索新的練習"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# 頁尾
st.markdown('<p style="text-align: center; color: #8B8B7A; font-size: 0.8rem; margin-top: 60px;">米寶漢方｜慶和蔘藥行研製<br>產品為一般食品，溫柔陪伴妳的日常。© 2026 Mibao Herbal</p>', unsafe_allow_html=True)
