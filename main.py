import streamlit as st
import time
import os

# 1. UI 專家級視覺設定 (極致留白與呼吸感)
st.set_page_config(page_title="米寶漢方｜妳的月度質感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 1. 全域背景與文字 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 2. 標題與引言：精緻、平衡、不壓迫 */
    h1 { font-size: 2rem !important; margin-bottom: 10px !important; }
    h3 { 
        font-size: 1.25rem !important; /* 縮小題目尺寸，與答案達成平衡 */
        font-weight: 700 !important;
        letter-spacing: 0.1rem !important;
        margin-top: 40px !important;
        margin-bottom: 50px !important; /* 題目與第一個答案的間距 */
        text-align: center !important;
        color: #7A8450 !important;
    }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 50px; font-size: 0.9rem; }

    /* 3. 【關鍵修正】卡片式選項 (徹底移除黑點 + 極致 120px 間距) */
    div[data-baseweb="radio"] input { display: none !important; } /* 隱藏原生黑點 */
    
    div[data-baseweb="radio"] {
        display: flex;
        flex-direction: column;
        gap: 120px !important; /* 選項與選項之間的「兩兩間距」設定為 120px */
    }

    div[data-baseweb="radio"] label {
        background-color: #FFFFFF !important;
        border: 1px solid #E9EDC9 !important;
        border-radius: 20px !important;
        padding: 22px 25px !important;
        width: 100% !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 4px 15px rgba(122, 132, 80, 0.05) !important;
        display: flex !important;
        justify-content: center !important;
        text-align: center !important;
    }

    /* 被選中時的華麗轉變 */
    div[aria-checked="true"] {
        background-color: #7A8450 !important;
        border-color: #7A8450 !important;
        transform: translateY(-5px) !important;
        box-shadow: 0 12px 30px rgba(122, 132, 80, 0.2) !important;
    }
    div[aria-checked="true"] * {
        color: #FFFFFF !important;
    }

    /* 4. 按鈕優化 (質感圓潤) */
    .stButton > button {
        width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important;
        border-radius: 40px !important; height: 3.8em !important; font-weight: bold !important; 
        border: none !important; margin-top: 60px !important;
        font-size: 1.1rem !important;
    }
    .stButton > button p { color: #FFFFFF !important; }

    /* 5. 複製區與輸入框：徹底去黑 */
    .stTextInput input {
        background-color: #FFFFFF !important; border: 2px solid #E9EDC9 !important;
        border-radius: 15px !important; color: #4A4E31 !important; padding: 15px !important;
    }
    .stCodeBlock, pre, code, div[data-testid="stCodeBlock"] {
        background-color: #F8F9F1 !important; border: 1px solid #E9EDC9 !important;
        border-radius: 18px !important;
    }
    div[data-testid="stCodeBlock"] > div { background-color: #F8F9F1 !important; }
    code span { color: #4A4E31 !important; }

    /* 6. 結果卡片與落葉特效 */
    .result-card { 
        background-color: #FFFFFF !important; padding: 35px !important;
        border-radius: 30px !important; border: 1px solid #E9EDC9 !important;
        box-shadow: 0 20px 50px rgba(74, 78, 49, 0.08) !important;
    }
    @keyframes falling {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .leaf { position: fixed; top: -10vh; font-size: 24px; pointer-events: none; z-index: 9999; animation: falling 12s linear infinite; }
    
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

def show_leaves():
    leaves_html = ""
    for i in range(15):
        left, delay = i * 7, i * 0.7
        leaves_html += f'<div class="leaf" style="left:{left}vw; animation-delay:{delay}s;">🍃</div>'
        leaves_html += f'<div class="leaf" style="left:{left+3}vw; animation-delay:{delay+2}s;">🌿</div>'
    st.markdown(leaves_html, unsafe_allow_html=True)

# 初始化狀態
if 'step' not in st.session_state: st.session_state.step = 1
if 'answers' not in st.session_state: st.session_state.answers = []
if 'custom_name' not in st.session_state: st.session_state.custom_name = ""
if 'is_first_time' not in st.session_state: st.session_state.is_first_time = ""

# 頂部 Logo (米寶旗艦感)
img_path = "29301.jpg"
if os.path.exists(img_path):
    st.image(img_path, use_container_width=True)
else:
    st.markdown("<h1 style='text-align:center;'>🌿 米寶漢方</h1>", unsafe_allow_html=True)
st.markdown('<p class="quote">「在忙碌中，給自己留一刻鐘的溫柔。」</p>', unsafe_allow_html=True)

# ----------------- 測驗流程 -----------------
if st.session_state.step == 1:
    st.markdown("### 第一步：聽聽身體的低語")
    q1 = st.radio("", ["我有些疲累，渴望溫潤透亮的晨光...", "我有些沉重，想找回輕盈自在的微風...", "我有些燥熱，想念山間清徹甘甜的泉水..."], index=None, key="v23_q1")
    if st.button("緩緩走向下個瞬間 ➔"):
        if q1: st.session_state.answers.append(q1); st.session_state.step = 2; st.rerun()
        else: st.warning("請選一個妳現在最真實的感覺喔")

elif st.session_state.step == 2:
    st.markdown("### 第二步：梳理日常的步調")
    q2 = st.radio("", ["長時間待在冷氣房，循環緩慢且手腳冰冷", "工作忙碌常熬夜，晚餐不規律導致不適", "壓力大節奏快，晚上難以入眠且心神不寧"], index=None, key="v21_q2")
    if st.button("傾聽日常的節奏 ➔"):
        if q2: st.session_state.answers.append(q2); st.session_state.step = 3; st.rerun()
        else: st.warning("請選一個妳的日常狀態喔")

elif st.session_state.step == 3:
    st.markdown("### 第三步：妳嚮往的喘息瞬間")
    q3 = st.radio("", ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，優雅從容"], index=None, key="v21_q3")
    if st.button("開啟妳的專屬禮遇 ➔"):
        if q3: st.session_state.answers.append(q3); st.session_state.step = 4; st.rerun()
        else: st.warning("想像一下那個畫面吧")

elif st.session_state.step == 4:
    st.markdown("### 💎 妳是米寶的新朋友嗎？")
    choice = st.radio("", ["是的，我是新朋友", "不是，我是老朋友了（已有隨行杯）"], index=None, key="v21_choice")
    if st.button("前往專屬的陪伴 ➔"):
        if choice == "是的，我是新朋友": st.session_state.is_first_time = "是的"; st.session_state.step = 5; st.rerun()
        elif choice == "不是，我是老朋友了（已有隨行杯）": st.session_state.is_first_time = "不是"; st.session_state.custom_name = "老朋友回購驚喜"; st.session_state.step = 6; st.rerun()
        else: st.warning("請選擇妳的身份喔")

elif st.session_state.step == 5:
    st.markdown("### 💎 鐫刻妳的專屬溫柔")
    st.markdown("<div style='background-color: #FFFFFF; padding: 25px; border-radius: 15px; border: 1px solid #E9EDC9; margin-bottom: 20px;'>「首購禮遇：為妳在隨行杯木蓋上，鐫刻專屬的名字。<br><br>讓它陪伴妳度過每一天，提醒妳值得被溫柔對待。」</div>", unsafe_allow_html=True)
    user_name = st.text_input("輸入要雷刻的名字 (最多12字)", max_chars=12, placeholder="例如：Mila 或 Quiet")
    if st.button("查看我的質感陪伴配比 ➔"):
        if user_name: st.session_state.custom_name = user_name; st.session_state.step = 6; st.rerun()
        else: st.warning("留下名字，讓溫柔專屬於妳。")

elif st.session_state.step == 6:
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<p class="quote">正在為妳揉捻專屬的草本香氣...</p>', unsafe_allow_html=True); time.sleep(1.2)
    placeholder.empty()

    ans, name, first = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time
    if "晨光" in ans[0]: diag, m_tea, a_tea = "暖陽系", "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
    elif "微風" in ans[0]: diag, m_tea, a_tea = "微風系", "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
    else: diag, m_tea, a_tea = "清泉系", "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"

    show_leaves() 
    gift_detail = f"• <b>精品首購禮：</b>專屬刻名木蓋隨行杯 (刻名：{name})" if first == "是的" else "• <b>老友回饋禮：</b>額外加贈 3 包驚喜茶包"
    
    st.markdown(f"""
    <div class="result-card">
        <h3 style='text-align:center; font-size: 1.5rem !important; color: #4A4E31 !important;'>✨ 妳是：{diag}女子</h3>
        <p class="quote">「這份月度陪伴，是送給妳的時光禮物。」</p>
        <hr style='border: 0.5px solid #E9EDC9;'>
        <p style='margin-bottom:8px;'><b>☀️ 晨曦啟幕配比：</b><br>{m_tea}</p>
        <p style='margin-bottom:8px;'><b>🌙 午後拾光配比：</b><br>{a_tea}</p>
        <hr style='border: 0.5px solid #E9EDC9;'>
        <p style='font-size:0.95rem; line-height:1.7;'>
            <b>本月陪伴清單包含：</b><br>
            • <b>40 入</b> 深度節律漢方茶組 (全月份份量)<br>
            • <b>植感生活語錄收藏卡</b> (給妳暖心的鼓勵)<br>
            {gift_detail}
        </p>
        <p style='text-align:right; color:#7A8450; font-size: 1.05rem; font-weight: bold; margin-top:15px;'>
            月度質感陪伴價 $1,980
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(" ")
    if st.button("預約這份溫柔時光 ➔"):
        st.session_state.step = 7
        st.rerun()

elif st.session_state.step == 7:
    ans, name, first = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time
    if "晨光" in ans[0]: diag, m_tea, a_tea = "暖陽系", "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
    elif "微風" in ans[0]: diag, m_tea, a_tea = "微風系", "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
    else: diag, m_tea, a_tea = "清泉系", "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"

    st.markdown("### 📢 預約一場暖心的相遇")
    st.write("最後兩步，開啟妳的植感日常：")
    
    engrave_part = f"杯蓋想悄悄刻上：{name} ✨" if first == "是的" else "我是老朋友了，想領取回購驚喜 🐢🎁"
    romantic_msg = f"""Hi 米寶店長！🐢✨

我剛剛完成植感測驗了，我是【{diag}女子】。
想預約這份月度陪伴，讓這份溫柔陪我度過每一天。

🌿 {engrave_part}

我的專屬配比：
☀️ 晨曦：{m_tea}
🌙 午後：{a_tea}

期待與這份草本香氣相遇。🌿🍵"""

    st.write("Step 1：點擊下方框框右上角的圖示「複製文字」")
    st.code(romantic_msg, language=None)

    line_link = "https://line.me/R/ti/p/@716osfvq"
    st.markdown(f'''
        <a href="{line_link}" target="_blank" style="text-decoration:none;">
            <div style="background-color: #06C755; color: white !important; text-align: center; padding: 18px; border-radius: 12px; font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 10px rgba(6,199,85,0.2);">
                ✨ 領取妳的專屬溫柔陪伴 ➔
            </div>
        </a>
    ''', unsafe_allow_html=True)

    st.write("---")
    if st.button("重新探索新的陪伴"):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

st.markdown("<p style='text-align:center; font-size:0.8rem; color:#8B8B7A; margin-top:60px;'>米寶漢方｜慶和蔘藥行研製<br>產品為一般食品。 © 2026 Mibao Herbal</p>", unsafe_allow_html=True)
