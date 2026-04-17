import streamlit as st
import time

# 1. 視覺與動畫設定 (強化文字對比度)
st.set_page_config(page_title="在忙碌中，給自己留一刻鐘的溫柔", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    h1, h2, h3 { color: #4A4E31; font-family: 'Noto Serif TC', serif; }
    .stRadio > label { font-size: 1.2rem; color: #4A4E31; font-weight: bold; }
    p, span, div { color: #4A4E31 !important; }
    .stButton > button {
        width: 100%; border-radius: 30px; background-color: #6B705C; color: white !important;
        height: 3.5em; font-size: 1.1rem; font-weight: bold; border: none;
    }
    .result-card { 
        background-color: #FFFFFF; padding: 30px; border-radius: 25px; 
        border: 1px solid #E9EDC9; box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }
    .tea-item { display: flex; justify-content: space-between; border-bottom: 1px dashed #DDBEA9; padding: 8px 0; color: #4A4E31; }
    .quote { font-style: italic; color: #8B8B7A; text-align: center; margin-bottom: 15px; }
    .tag { background-color: #FFE8D6; color: #6B705C; padding: 2px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 初始化狀態
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = []

# 標題區
st.markdown("<h1 style='text-align: center;'>🌿 米寶漢方</h1>", unsafe_allow_html=True)
st.markdown('<p class="quote">「在忙碌中，給自己留一刻鐘的溫柔。」</p>', unsafe_allow_html=True)

# 2. 分步測驗邏輯
if st.session_state.step == 1:
    st.markdown('<h3 style="text-align: center;">第一步：聽聽身體的低語</h3>', unsafe_allow_html=True)
    q1 = st.radio("當妳靜下心，妳的身體正低聲說著...？", 
                  ["我有些疲累，渴望一份透亮的晨光...", 
                   "我有些沉重，想找回輕盈的微風...", 
                   "我有些燥熱，想念山間的清泉..."])
    if st.button("下一頁：梳理步調 ➔"):
        st.session_state.answers.append(q1)
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.markdown('<h3 style="text-align: center;">第二步：梳理日常的步調</h3>', unsafe_allow_html=True)
    q2 = st.radio("關於這段日子的作息，妳目前的感受是？", 
                  ["長時間待在冷氣房，感覺循環緩慢", 
                   "工作忙碌常熬夜，晚餐不規律", 
                   "壓力大節奏快，晚上難以入眠"])
    if st.button("最後一頁：嚮往的瞬間 ➔"):
        st.session_state.answers.append(q2)
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.markdown('<h3 style="text-align: center;">第三步：留下的專屬標記</h3>', unsafe_allow_html=True)
    q3 = st.radio("在最需要喘息的午後，妳最嚮往的瞬間？", 
                  ["感覺臉龐恢復紅潤元氣，重新出發", 
                   "感覺身體恢復自在律動，不再束縛", 
                   "感覺內心恢復安靜穩定，優雅從容"])
    custom_name = st.text_input("💎 想要雷刻在木蓋上的名字", max_chars=12, placeholder="例如：Mila")
    
    if st.button("開啟我的月度植感練習 ➔"):
        st.session_state.answers.append(q3)
        st.session_state.custom_name = custom_name
        st.session_state.step = 4
        st.rerun()

# 3. 結果與配比 (移除 AM/PM)
elif st.session_state.step == 4:
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<p class="quote">正在為妳揉捻專屬的草本香氣...</p>', unsafe_allow_html=True)
        time.sleep(1.5)
        st.markdown('<p class="quote">正在刻印妳的專屬溫柔...</p>', unsafe_allow_html=True)
        time.sleep(1.5)
    placeholder.empty()

    ans = st.session_state.answers
    name = st.session_state.custom_name
    
    # 邏輯計算
    if "晨光" in ans[0] or "紅潤" in ans[2]:
        diag, quote = "暖陽系女子", "「妳是溫潤的暖陽，哪怕忙碌，也要記得為自己發光。」"
        morning_tea, morning_count = "黃耆元氣茶", 14
        afternoon_tea, afternoon_count = "當歸紅棗茶", 12
        side_tea1, side1_count = "金菊牛蒡茶", 6
        side_tea2, side2_count = "黑豆漢方茶", 8
    elif "微風" in ans[0] or "律動" in ans[2]:
        diag, quote = "微風系女子", "「願妳的日常，如微風般輕盈，不留負擔。」"
        morning_tea, morning_count = "洛神山楂茶", 12
        afternoon_tea, afternoon_count = "玫瑰決明茶", 10
        side_tea1, side1_count = "金菊牛蒡茶", 8
        side_tea2, side2_count = "黑豆漢方茶", 10
    else:
        diag, quote = "清泉系女子", "「在紛擾的世界裡，做一池最安靜、最深邃的清泉。」"
        morning_tea, morning_count = "金菊牛蒡茶", 15
        afternoon_tea, afternoon_count = "玫瑰決明茶", 14
        side_tea1, side1_count = "黃耆元氣茶", 5
        side_tea2, side2_count = "當歸紅棗茶", 6

    st.balloons()
    
    st.markdown(f'<div class="result-card">', unsafe_allow_html=True)
    st.markdown(f'<p class="quote" style="color:#6B705C;">{quote}</p>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="text-align:center; color:#4A4E31;">✨ 專屬配置：妳是【{diag}】</h3>', unsafe_allow_html=True)
    
    st.markdown("<p style='font-weight:bold; margin-top:20px;'>☀️ 晨曦啟幕配比</p>", unsafe_allow_html=True)
    st.markdown(f'<div class="tea-item"><span>{morning_tea}</span><span class="tag">{morning_count} 入</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="tea-item"><span>{side_tea1}</span><span class="tag">{side1_count} 入</span></div>', unsafe_allow_html=True)
        
    st.markdown("<p style='font-weight:bold; margin-top:20px;'>🌙 午後拾光配比</p>", unsafe_allow_html=True)
    st.markdown(f'<div class="tea-item"><span>{afternoon_tea}</span><span class="tag">{afternoon_count} 入</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="tea-item"><span>{side_tea2}</span><span class="tag">{side2_count} 入</span></div>', unsafe_allow_html=True)
        
    st.divider()
    st.markdown(f"""
        <p style="color:#4A4E31; font-size:0.95rem;"><b>月度陪伴計畫包含：</b><br>
        40 入雙效植感茶組 (四週深度節律) + 生活手札 + 雷刻木蓋隨行杯 (刻名：{name if name else 'Dear'})</p>
        <h3 style="color:#4A4E31; text-align:right;">月度陪伴價：$1,980</h3>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # LINE 代碼與正確連結
    order_msg = f"你好，我想預約【米寶漢方｜月度植感練習】\n我是：{diag}\n晨曦配比：{morning_tea}*{morning_count}, {side_tea1}*{side1_count}\n午後配比：{afternoon_tea}*{afternoon_count}, {side_tea2}*{side2_count}\n雷刻名字：{name}"
    
    st.write("👇 請複製下方文字，與米寶相遇：")
    st.code(order_msg)
    
    line_link = "https://line.me/R/ti/p/@716osfvq"
    st.markdown(f'<a href="{line_link}" target="_blank" style="text-decoration:none;"><div style="background-color: #06C755; color: white !important; text-align: center; padding: 15px; border-radius: 10px; font-weight: bold; font-size: 1.1rem;">複製內容，去 LINE 領取專屬杯 ➔</div></a>', unsafe_allow_html=True)
    
    if st.button("重新探索"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

st.markdown('<p style="text-align: center; color: #8B8B7A; font-size: 0.8rem; margin-top: 50px;">米寶漢方｜慶和蔘藥行研製<br>產品為一般食品，溫柔陪伴妳的日常。</p>', unsafe_allow_html=True)
