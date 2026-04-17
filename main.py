import streamlit as st
import time
import os

# 1. 全方位視覺鎖定 (穩定顯色與植感調色)
st.set_page_config(page_title="米寶漢方｜妳的月度質感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域鎖定深橄欖綠文字 */
    * {
        color: #4A4E31 !important;
        font-family: 'Noto Sans TC', sans-serif !important;
    }
    .stApp { background-color: #FDFBF7 !important; }
    
    h1, h2, h3 { text-align: center !important; margin-bottom: 10px !important; }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 20px; font-size: 0.95rem; }

    /* 選項 (Radio) 顏色：質感橄欖綠 */
    div[data-baseweb="radio"] div { color: #6B705C !important; }
    div[data-baseweb="radio"] div[aria-checked="true"] > div { background-color: #6B705C !important; }

    /* 雷刻輸入框：強制白底綠邊 */
    .stTextInput input {
        background-color: #FFFFFF !important;
        border: 2px solid #E9EDC9 !important;
        border-radius: 12px !important;
        color: #4A4E31 !important;
        padding: 10px !important;
    }

    /* 按鈕樣式 (綠底白字) */
    .stButton > button {
        width: 100% !important; background-color: #6B705C !important; color: #FFFFFF !important;
        border-radius: 25px !important; height: 3.8em !important; font-weight: bold !important; border: none !important;
    }
    .stButton > button p { color: #FFFFFF !important; }

    /* 質感信箋風格 */
    .order-box {
        background-color: #F8F9F1 !important; padding: 20px !important; border-radius: 15px !important;
        border: 1px solid #E9EDC9 !important; margin: 20px 0 !important; font-size: 0.95rem !important;
        line-height: 1.6 !important; white-space: pre-wrap !important;
    }

    .result-card { background-color: #FFFFFF !important; padding: 25px !important; border-radius: 25px !important; border: 2px solid #E9EDC9 !important; }
    
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    
    <script>
    function copyAndJump(text) {
        const el = document.createElement('textarea');
        el.value = text;
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
        window.open("https://line.me/R/ti/p/@716osfvq", "_blank");
    }
    </script>
    """, unsafe_allow_html=True)

# 初始化 Session State
if 'step' not in st.session_state: st.session_state.step = 1
if 'answers' not in st.session_state: st.session_state.answers = []
if 'custom_name' not in st.session_state: st.session_state.custom_name = ""
if 'is_first_time' not in st.session_state: st.session_state.is_first_time = "是的"

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
                  ["我有些疲累，渴望溫潤透亮的晨光...", "我有些沉重，想找回輕盈自在的微風...", "我有些燥熱，想念山間清徹甘甜的泉水..."], index=None, key="v71_q1")
    if st.button("下一頁：梳理日常 ➔"):
        if q1: st.session_state.answers.append(q1); st.session_state.step = 2; st.rerun()
        else: st.warning("請選一個最貼近妳的感覺喔")

elif st.session_state.step == 2:
    st.write("### 第二步：梳理日常的步調")
    q2 = st.radio("關於這段日子的作息，妳目前的感受是？", 
                  ["長時間待在冷氣房，循環緩慢且手腳冰冷", "工作忙碌常熬夜，晚餐不規律導致不適", "壓力大節奏快，晚上難以入眠且心神不寧"], index=None, key="v71_q2")
    if st.button("下一頁：嚮往的瞬間 ➔"):
        if q2: st.session_state.answers.append(q2); st.session_state.step = 3; st.rerun()
        else: st.warning("請選一個妳的日常狀態喔")

elif st.session_state.step == 3:
    st.write("### 第三步：妳嚮往的喘息瞬間")
    q3 = st.radio("在最需要喘息的午後，妳最嚮往什麼樣的瞬間？", 
                  ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，優雅從容"], index=None, key="v71_q3")
    if st.button("最後一步：確認陪伴方式 ➔"):
        if q3: st.session_state.answers.append(q3); st.session_state.step = 4; st.rerun()
        else: st.warning("選一個妳最嚮往的畫面吧")

elif st.session_state.step == 4:
    st.write("### 💎 確認妳的陪伴方式")
    is_first = st.radio("這是妳第一次預約米寶的「月度質感陪伴」嗎？", ["是的，我是新朋友", "不是，我是老朋友了（已有隨行杯）"], key="is_first_v71")
    
    if is_first == "是的，我是新朋友":
        st.markdown("<div style='background-color: #FFFFFF; padding: 20px; border-radius: 15px; border: 1px solid #E9EDC9; margin: 15px 0;'><b>首購禮遇：</b>我們將為妳在隨行杯木蓋上，鐫刻專屬的文字。<br>讓它提醒妳，每一天都值得被溫柔對待。</div>", unsafe_allow_html=True)
        user_name = st.text_input("輸入要雷刻的名字 (最多12字)", max_chars=12, placeholder="例如：Mila 或 Quiet")
        st.session_state.custom_name = user_name
        st.session_state.is_first_time = "是的"
    else:
        st.markdown("<div style='background-color: #F8F9F1; padding: 20px; border-radius: 15px; border: 1px solid #E9EDC9; margin: 15px 0;'><b>歡迎回來，老朋友！</b><br>這次我們將專注於為妳補充月度所需的漢方茶組，持續守護妳的日常步調。</div>", unsafe_allow_html=True)
        st.session_state.custom_name = "老朋友回購"
        st.session_state.is_first_time = "不是"

    if st.button("開啟我的月度質感陪伴 ➔"):
        if st.session_state.is_first_time == "是的" and not st.session_state.custom_name:
            st.warning("留下一個名字吧，讓首購禮物專屬於妳。")
        else:
            st.session_state.step = 5
            st.rerun()

elif st.session_state.step == 5:
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<p class="quote">正在為妳揉捻專屬的草本香氣...</p>', unsafe_allow_html=True); time.sleep(1.2)
    placeholder.empty()

    ans, name, first = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time
    if "晨光" in ans[0]:
        diag = "暖陽系"; m_tea = "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)"; a_tea = "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
    elif "微風" in ans[0]:
        diag = "微風系"; m_tea = "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)"; a_tea = "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
    else:
        diag = "清泉系"; m_tea = "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)"; a_tea = "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"

    st.balloons()
    gift_text = f"• <b>首購禮：</b>雷刻刻名隨行杯 (刻名：{name})" if first == "是的" else "• <b>回購方案：</b>月度漢方茶組補充包"
    
    st.markdown(f"""<div class="result-card"><h3 style='text-align:center;'>✨ 妳是：{diag}女子</h3><p class="quote">「這份月度陪伴計畫，是送給妳的時光禮物。」</p><hr style='border: 0.5px solid #E9EDC9;'><p><b>☀️ 晨曦啟幕配比：</b><br>{m_tea}</p><br><p><b>🌙 午後拾光配比：</b><br>{a_tea}</p><hr style='border: 0.5px solid #E9EDC9;'><p style='font-size:0.9rem;'><b>陪伴包含：</b> 40入茶組 + 生活手札<br>{gift_text}</p><h3 style='text-align:right; color:#6B705C !important;'>月度陪伴價 $1,980</h3></div>""", unsafe_allow_html=True)
    
    # 預約訊息 (含自動複製邏輯)
    engrave_msg = f"雷刻文字：{name}" if first == "是的" else "回購方案：已有隨行杯"
    order_msg = f"你好，我想預約【米寶漢方｜月度質感陪伴】\\n我是：{diag}女子\\n{engrave_msg}\\n\\n專屬配比內容：\\n晨曦：{m_tea}\\n午後：{a_tea}\\n\\n我已完成測驗，想預約月度陪伴計畫。"
    
    st.write("👇 點擊下方按鈕自動複製訊息，並開啟 LINE：")
    st.markdown(f'<div class="order-box">{order_msg.replace("\\\\n", "<br>")}</div>', unsafe_allow_html=True)
    
    html_button = f"""<button onclick="copyAndJump('{order_msg}')" style="width: 100%; background-color: #06C755; color: white; border: none; padding: 18px; border-radius: 12px; font-weight: bold; font-size: 1.2rem; cursor: pointer; box-shadow: 0 4px 10px rgba(6,199,85,0.2);">點我開啟 LINE，與米寶見面 ➔</button>"""
    st.components.v1.html(html_button, height=100)

    if st.button("重新探索新的陪伴"):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

# 頁尾文字更新：慶和蔘藥行研製
st.markdown("<p style='text-align:center; font-size:0.8rem; color:#8B8B7A; margin-top:60px;'>米寶漢方｜慶和蔘藥行研製<br>產品為一般食品。 © 2026 Mibao Herbal</p>", unsafe_allow_html=True)
