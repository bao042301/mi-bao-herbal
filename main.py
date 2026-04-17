import streamlit as st
import time

# 1. 浪漫視覺與細節設定
st.set_page_config(page_title="在忙碌中，給自己留一刻鐘的溫柔", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    h1, h2, h3 { color: #6B705C; font-family: 'Noto Serif TC', serif; }
    .stSelectbox label, .stTextInput label { color: #6B705C; font-weight: bold; }
    .stButton > button {
        width: 100%; border-radius: 30px; background-color: #A5A58D; color: white !important;
        height: 3.5em; font-size: 1.1rem; font-weight: bold; border: none; transition: 0.3s;
    }
    .stButton > button:hover { background-color: #6B705C; }
    .result-card { 
        background-color: #FFFFFF; padding: 30px; border-radius: 25px; 
        border: 1px solid #E9EDC9; box-shadow: 0 10px 20px rgba(0,0,0,0.02);
    }
    .tea-item { display: flex; justify-content: space-between; border-bottom: 1px dashed #DDBEA9; padding: 8px 0; color: #6B705C; }
    .quote { font-style: italic; color: #B7B7A4; text-align: center; margin-bottom: 20px; }
    .tag { background-color: #FFE8D6; color: #A5A58D; padding: 2px 10px; border-radius: 20px; font-size: 0.8rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 米寶漢方")
st.subheader("找尋妳的植感語錄")
st.markdown('<p class="quote">「在忙碌中，給自己留一刻鐘的溫柔。」</p>', unsafe_allow_html=True)

# 2. 浪漫敘事測驗 (隱喻上班，但不強調職場)
st.divider()
st.write("✨ **探尋妳的身體頻率**")
q1 = st.selectbox("當妳靜下心，妳的身體正低聲說著...？", 
                  ["請選擇", "「我有些疲累，渴望一份透亮的晨光...」", "「我有些沉重，想找回輕盈的微風...」", "「我有些燥熱，想念山間的清泉...」"])

q2 = st.selectbox("在最需要喘息的午後，妳最嚮往的瞬間？", 
                  ["請選擇", "感覺臉龐恢復紅潤元氣，重新出發", "感覺身體恢復自在律動，不再束縛", "感覺內心恢復安靜穩定，優雅從容"])

custom_name = st.text_input("💎 **專屬浪漫**：想在木蓋上雷刻的名字（這會是妳的專屬符號）", max_chars=12, placeholder="例如：Mila")

# 3. 動態配比與浪漫呈現
if st.button("開啟我的月度植感練習") and q1 != "請選擇" and q2 != "請選擇":
    with st.spinner('米寶正在為妳揉捻專屬的香氣...'):
        time.sleep(2)
        
        # 浪漫配比邏輯
        if "晨光" in q1 or "紅潤" in q2:
            diag, quote = "暖陽系女子", "「妳是溫潤的暖陽，哪怕忙碌，也要記得為自己發光。」"
            am_formula = {"黃耆元氣茶": 16, "金菊牛蒡茶": 4}
            pm_formula = {"當歸紅棗茶": 14, "黑豆漢方茶": 6}
        elif "微風" in q1 or "律動" in q2:
            diag, quote = "微風系女子", "「願妳的日常，如微風般輕盈，不留負擔。」"
            am_formula = {"洛神山楂茶": 15, "金菊牛蒡茶": 5}
            pm_formula = {"玫瑰決明茶": 12, "黑豆漢方茶": 8}
        else:
            diag, quote = "清泉系女子", "「在紛擾的世界裡，做一池最安靜、最深邃的清泉。」"
            am_formula = {"金菊牛蒡茶": 18, "黃耆元氣茶": 2}
            pm_formula = {"玫瑰決明茶": 16, "當歸紅棗茶": 4}

        st.balloons()
        st.markdown(f"""
        <div class="result-card">
            <p class="quote">{quote}</p>
            <h3 style="text-align:center;">✨ 專屬配置：妳是【{diag}】</h3>
            <br>
            <p>☀️ <b>晨曦啟幕 (AM 節律)</b></p>
            {"".join([f'<div class="tea-item"><span>{k}</span><span class="tag">{v} 回</span></div>' for k,v in am_formula.items()])}
            
            <br>
            <p>🌙 <b>午後拾光 (PM 節律)</b></p>
            {"".join([f'<div class="tea-item"><span>{k}</span><span class="tag">{v} 回</span></div>' for k,v in pm_formula.items()])}
            
            <hr>
            <p style="font-size:0.9rem;"><b>月度陪伴計畫包含：</b><br>
            40 入雙效植感茶組 (四週深度節律) + 生活手札 + 雷刻木蓋隨行杯 (刻名：{custom_name if custom_name else 'Dear'})</p>
            <h3 style="color:#6B705C; text-align:right;">月度陪伴價：$1,980</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # LINE 代碼
        am_str = ", ".join([f"{k}*{v}" for k,v in am_formula.items()])
        pm_str = ", ".join([f"{k}*{v}" for k,v in pm_formula.items()])
        order_msg = f"你好，我想預約【米寶漢方｜月度植感練習】\n我是：{diag}\n晨曦配比：{am_str}\n午後配比：{pm_str}\n雷刻名字：{custom_name}"
        st.code(order_msg)
        st.markdown(f'<a href="https://line.me" target="_blank" style="text-decoration:none;"><div style="background-color: #06C755; color: white; text-align: center; padding: 15px; border-radius: 10px; font-weight: bold;">複製這份溫柔，去 LINE 與米寶相遇 ➔</div></a>', unsafe_allow_html=True)

st.markdown('<p style="text-align: center; color: #B7B7A4; font-size: 0.8rem; margin-top: 50px;">米寶漢方｜慶和老店二代轉型練習<br>產品為一般食品，溫柔陪伴妳的日常。</p>', unsafe_allow_html=True)
