import streamlit as st
import time
import os

# 1. 全方位視覺鎖定
st.set_page_config(page_title="米寶漢方｜妳的月度質感陪伴", layout="centered")

st.markdown("""
    <style>
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    h1, h2, h3 { text-align: center !important; margin-bottom: 10px !important; }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 20px; font-size: 0.95rem; }

    /* 單選框與輸入框 */
    div[data-baseweb="radio"] div { color: #6B705C !important; }
    div[data-baseweb="radio"] div[aria-checked="true"] > div { background-color: #6B705C !important; }
    .stTextInput input { background-color: #FFFFFF !important; border: 2px solid #E9EDC9 !important; border-radius: 12px !important; }

    /* 下一步/重新開始按鈕 */
    .stButton > button {
        width: 100% !important; background-color: #6B705C !important; color: #FFFFFF !important;
        border-radius: 25px !important; height: 3.5em !important; font-weight: bold !important; border: none !important;
    }
    .stButton > button p { color: #FFFFFF !important; }

    /* 訂單信箋風格 */
    .order-box {
        background-color: #F8F9F1 !important; padding: 20px !important; border-radius: 15px !important;
        border: 1px solid #E9EDC9 !important; margin: 15px 0 !important; font-size: 1rem !important; line-height: 1.6 !important;
    }
    .result-card { background-color: #FFFFFF !important; padding: 25px !important; border-radius: 25px !important; border: 2px solid #E9EDC9 !important; }
    
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    
    <script>
    function copyText(text) {
        if (navigator.clipboard && window.isSecureContext) {
            navigator.clipboard.writeText(text).then(() => {
                alert("✅ 訊息已複製！\\n請在下一步點擊開啟 LINE 後，長按貼上發送給米寶。");
            });
        } else {
            const el = document.createElement('textarea');
            el.value = text;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            alert("✅ 訊息已複製！\\n請在下一步點擊開啟 LINE 後，長按貼上發送給米寶。");
        }
    }
    </script>
    """, unsafe_allow_html=True)

# 初始化 Session State
if 'step' not in st.session_state: st.session_state.step = 1
if 'answers' not in st.session_state: st.session_state.answers = []
if 'custom_name' not in st.session_state: st.session_state.custom_name = ""
if 'is_first_time' not in st.session_state: st.session_state.is_first_time = ""

# 頂部品牌區 (米樂龜 Logo)
img_path = "29301.jpg"
if os.path.exists(img_path):
    st.image(img_path, use_container_width=True)
else:
    st.markdown("<h1 style='font-size: 2rem;'>🌿 米寶漢方</h1>", unsafe_allow_html=True)
st.markdown('<p class="quote">「在忙碌中，給自己留一刻鐘的溫柔。」</p>', unsafe_allow_html=True)

# ----------------- 測驗流程 -----------------
if st.session_state.step == 1:
    st.write("### 第一步：聽聽身體的低語")
    q1 = st.radio("當妳靜下心，妳的身體正低聲說著...？", ["我有些疲累，渴望溫潤透亮的晨光...", "我有些沉重，想找回輕盈自在的微風...", "我有些燥熱，想念山間清徹甘甜的泉水..."], index=None, key="v9_q1")
    if st.button("下一步：梳理日常 ➔"):
        if q1: st.session_state.answers.append(q1); st.session_state.step = 2; st.rerun()
        else: st.warning("請選一個最貼近妳的感覺喔")

elif st.session_state.step == 2:
    st.write("### 第二步：梳理日常的步調")
    q2 = st.radio("關於這段日子的作息，妳目前的感受是？", ["長時間待在冷氣房，循環緩慢且手腳冰冷", "工作忙碌常熬夜，晚餐不規律導致不適", "壓力大節奏快，晚上難以入眠且心神不寧"], index=None, key="v9_q2")
    if st.button("下一步：嚮往的瞬間 ➔"):
        if q2: st.session_state.answers.append(q2); st.session_state.step = 3; st.rerun()
        else: st.warning("請選一個妳的日常狀態喔")

elif st.session_state.step == 3:
    st.write("### 第三步：妳嚮往的喘息瞬間")
    q3 = st.radio("在最需要喘息的午後，妳最嚮往什麼樣的瞬間？", ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，優雅從容"], index=None, key="v9_q3")
    if st.button("下一步：確認身份 ➔"):
        if q3: st.session_state.answers.append(q3); st.session_state.step = 4; st.rerun()
        else: st.warning("想像一下那個畫面，選一個吧")

elif st.session_state.step == 4:
    st.write("### 💎 妳是米寶的新朋友嗎？")
    choice = st.radio("這是妳第一次預約米寶的「月度質感陪伴」嗎？", ["是的，我是新朋友", "不是，我是老朋友了（已有隨行杯）"], index=None, key="v9_choice")
    if st.button("下一步 ➔"):
        if choice == "是的，我是新朋友": st.session_state.is_first_time = "是的"; st.session_state.step = 5; st.rerun()
        elif choice == "不是，我是老朋友了（已有隨行杯）": st.session_state.is_first_time = "不是"; st.session_state.custom_name = "老朋友回購"; st.session_state.step = 6; st.rerun()
        else: st.warning("請選擇妳的身份喔")

elif st.session_state.step == 5:
    st.write("### 💎 鐫刻妳的專屬溫柔")
    st.markdown("<div style='background-color: #FFFFFF; padding: 25px; border-radius: 15px; border: 1px solid #E9EDC9; margin-bottom: 20px;'>「首購禮遇：為妳在隨行杯木蓋上，鐫刻專屬的名字。<br><br>讓它陪伴妳度過每一天，提醒妳值得被溫柔對待。」</div>", unsafe_allow_html=True)
    user_name = st.text_input("輸入要雷刻的名字 (最多12字)", max_chars=12, placeholder="例如：Mila 或 Quiet")
    if st.button("最後一步：查看配比 ➔"):
        if user_name: st.session_state.custom_name = user_name; st.session_state.step = 6; st.rerun()
        else: st.warning("請輸入名字，讓首購禮物專屬於妳。")

elif st.session_state.step == 6:
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
    gift_text = f"• <b>首購禮：</b>雷刻隨行杯 (刻名：{name})" if first == "是的" else "• <b>回購方案：</b>月度補充漢方茶組"
    st.markdown(f"""<div class="result-card"><h3 style='text-align:center;'>✨ 妳是：{diag}女子</h3><p class="quote">「這份月度陪伴計畫，是送給妳的時光禮物。」</p><hr style='border: 0.5px solid #E9EDC9;'><p><b>☀️ 晨曦啟幕配比：</b><br>{m_tea}</p><br><p><b>🌙 午後拾光配比：</b><br>{a_tea}</p><hr style='border: 0.5px solid #E9EDC9;'><p style='font-size:0.9rem;'><b>陪伴包含：</b> 40入茶組 + 生活手札<br>{gift_text}</p><h3 style='text-align:right; color:#6B705C !important;'>月度陪伴價 $1,980</h3></div>""", unsafe_allow_html=True)
    
    # 建立正式的訂單訊息
    engrave_msg = f"雷刻文字：{name}" if first == "是的" else "回購方案：已有隨行杯"
    order_msg = f"""你好，我想預約【米寶漢方｜月度質感陪伴】
我是：{diag}女子
{engrave_msg}

專屬配比內容：
晨曦：{m_tea}
午後：{a_tea}

我已完成測驗，想預約月度陪伴計畫。"""

    st.write("---")
    st.write("### 📢 最後兩步，與米寶相遇：")
    
    # 步驟一：複製
    st.markdown(f'<div class="order-box">{order_msg.replace("\n", "<br>")}</div>', unsafe_allow_html=True)
    js_msg = order_msg.replace("\n", "\\n").replace("'", "\\'")
    
    btn_copy = f"""<button onclick="copyText('{js_msg}')" style="width: 100%; background-color: #E9EDC9; color: #4A4E31; border: 2px solid #6B705C; padding: 15px; border-radius: 12px; font-weight: bold; font-size: 1.1rem; cursor: pointer; margin-bottom: 10px;">Step 1：點我複製預約訊息 ➔</button>"""
    st.components.v1.html(btn_copy, height=75)

    # 步驟二：跳轉
    st.markdown(f'<a href="https://line.me/R/ti/p/@716osfvq" target="_blank" style="text-decoration:none;"><div style="background-color: #06C755; color: white !important; text-align: center; padding: 18px; border-radius: 12px; font-weight: bold; font-size: 1.2rem; box-shadow: 0 4px 10px rgba(6,199,85,0.2);">Step 2：點我開啟 LINE 貼上發送 ➔</div></a>', unsafe_allow_html=True)

    st.write("---")
    if st.button("重新探索新的陪伴"):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

st.markdown("<p style='text-align:center; font-size:0.8rem; color:#8B8B7A; margin-top:60px;'>米寶漢方｜慶和蔘藥行研製<br>產品為一般食品。 © 2026 Mibao Herbal</p>", unsafe_allow_html=True)
