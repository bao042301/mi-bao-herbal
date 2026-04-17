import streamlit as st
import time
import os

# 1. UI 專家級視覺鎖定 (一屏全覽設計 + 療癒三色網底)
st.set_page_config(page_title="米寶漢方｜妳的月度質感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域顯色鎖定 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 縮小 Logo 區塊，節省空間 */
    [data-testid="stImage"] {
        text-align: center;
        margin-bottom: -20px !important;
    }
    [data-testid="stImage"] img {
        max-height: 120px !important;
        width: auto !important;
    }

    /* 標題與引言：緊湊化設計 */
    h3 { 
        font-size: 1.2rem !important; 
        font-weight: 700 !important;
        margin-top: 10px !important;
        margin-bottom: 15px !important;
        text-align: center !important;
        color: #7A8450 !important;
    }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 20px; font-size: 0.85rem; }

    /* 【關鍵優化】卡片式選項：縮減間距與三色網底 */
    div[data-baseweb="radio"] input { display: none !important; } /* 隱藏黑點 */
    
    div[data-baseweb="radio"] {
        display: flex;
        flex-direction: column;
        gap: 12px !important; /* 選項兩兩間距縮小，確保不滑動 */
    }

    /* 基本卡片樣式 */
    div[data-baseweb="radio"] label {
        border-radius: 15px !important;
        padding: 12px 20px !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
        border: 1px solid rgba(0,0,0,0.05) !important;
        display: flex !important;
        justify-content: center !important;
        text-align: center !important;
    }

    /* 【三色網底設定】 */
    /* 第一個選項：淡葉綠 */
    div[data-baseweb="radio"] > div:nth-child(1) label { background-color: #F1F4E8 !important; }
    /* 第二個選項：暖陽杏 */
    div[data-baseweb="radio"] > div:nth-child(2) label { background-color: #FDF2E9 !important; }
    /* 第三個選項：清泉藍 */
    div[data-baseweb="radio"] > div:nth-child(3) label { background-color: #EBF5FB !important; }

    /* 被選中時的狀態：加深顏色並加框 */
    div[aria-checked="true"] {
        transform: scale(1.02) !important;
        border: 2px solid #7A8450 !important;
        box-shadow: 0 4px 12px rgba(122, 132, 80, 0.15) !important;
    }
    div[aria-checked="true"] * {
        font-weight: bold !important;
    }

    /* 按鈕優化：緊湊排版 */
    .stButton > button {
        width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important;
        border-radius: 40px !important; height: 3.2em !important; font-weight: bold !important; 
        border: none !important; margin-top: 15px !important;
    }
    .stButton > button p { color: #FFFFFF !important; }

    /* 隱藏頁尾等預設元件 */
    #MainMenu, footer, header { visibility: hidden; }
    
    /* 結果卡片與複製區 */
    .result-card { background-color: #FFFFFF !important; padding: 25px !important; border-radius: 25px !important; border: 1px solid #E9EDC9 !important; }
    .stCodeBlock, pre, code { background-color: #F8F9F1 !important; border-radius: 15px !important; }
    </style>
    """, unsafe_allow_html=True)

# 初始化狀態
if 'step' not in st.session_state: st.session_state.step = 1
if 'answers' not in st.session_state: st.session_state.answers = []
if 'custom_name' not in st.session_state: st.session_state.custom_name = ""
if 'is_first_time' not in st.session_state: st.session_state.is_first_time = ""

# 頂部 Logo
img_path = "29301.jpg"
if os.path.exists(img_path):
    st.image(img_path)
else:
    st.markdown("<h2 style='text-align:center;'>🌿 米寶漢方</h2>", unsafe_allow_html=True)
st.markdown('<p class="quote">「在忙碌中，給自己留一刻鐘的溫柔。」</p>', unsafe_allow_html=True)

# ----------------- 測驗流程 -----------------
if st.session_state.step == 1:
    st.markdown("### 第一步：聽聽身體的低語")
    q1 = st.radio("", ["我有些疲累，渴望溫潤透亮的晨光...", 
                       "我有些沉重，想找回輕盈自在的微風...", 
                       "我有些燥熱，想念山間清徹甘甜的泉水..."], index=None, key="v24_q1")
    if st.button("緩緩走向下個瞬間 ➔"):
        if q1: st.session_state.answers.append(q1); st.session_state.step = 2; st.rerun()
        else: st.warning("請選一個感覺喔")

elif st.session_state.step == 2:
    st.markdown("### 第二步：梳理日常的步調")
    q2 = st.radio("", ["長時間待在冷氣房，循環緩慢且手腳冰冷", 
                       "工作忙碌常熬夜，晚餐不規律導致不適", 
                       "壓力大節奏快，晚上難以入眠且心神不寧"], index=None, key="v24_q2")
    if st.button("傾聽日常的節奏 ➔"):
        if q2: st.session_state.answers.append(q2); st.session_state.step = 3; st.rerun()
        else: st.warning("請選一個狀態喔")

elif st.session_state.step == 3:
    st.markdown("### 第三步：妳嚮往的喘息瞬間")
    q3 = st.radio("", ["感覺臉龐恢復紅潤元氣，重新出發", 
                       "感覺身體找回輕盈律動，不再束縛", 
                       "感覺內心恢復安靜穩定，優雅從容"], index=None, key="v24_q3")
    if st.button("開啟妳的專屬禮遇 ➔"):
        if q3: st.session_state.answers.append(q3); st.session_state.step = 4; st.rerun()
        else: st.warning("選一個畫面吧")

elif st.session_state.step == 4:
    st.markdown("### 💎 妳是米寶的新朋友嗎？")
    choice = st.radio("", ["是的，我是新朋友", "不是，我是老朋友了（已有隨行杯）"], index=None, key="v24_choice")
    if st.button("前往專屬的陪伴 ➔"):
        if choice == "是的，我是新朋友": st.session_state.is_first_time = "是的"; st.session_state.step = 5; st.rerun()
        elif choice == "不是，我是老朋友了": st.session_state.is_first_time = "不是"; st.session_state.custom_name = "老朋友回購"; st.session_state.step = 6; st.rerun()

elif st.session_state.step == 5:
    st.markdown("### 💎 鐫刻妳的專屬溫柔")
    st.markdown("<div style='background-color: #FFFFFF; padding: 20px; border-radius: 15px; border: 1px solid #E9EDC9; font-size:0.9rem;'>首購禮遇：為妳在木蓋上鐫刻專屬的名字。</div>", unsafe_allow_html=True)
    user_name = st.text_input("輸入要雷刻的名字 (最多12字)", max_chars=12, placeholder="例如：Mila")
    if st.button("查看我的質感陪伴配比 ➔"):
        if user_name: st.session_state.custom_name = user_name; st.session_state.step = 6; st.rerun()

elif st.session_state.step == 6:
    ans, name, first = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time
    if "晨光" in ans[0]: diag, m_tea, a_tea = "暖陽系", "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
    elif "微風" in ans[0]: diag, m_tea, a_tea = "微風系", "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
    else: diag, m_tea, a_tea = "清泉系", "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"

    st.markdown(f"""
    <div class="result-card">
        <h3 style='margin:0;'>✨ 妳是：{diag}女子</h3>
        <hr style='margin:10px 0;'>
        <p style='font-size:0.9rem;'>☀️ 晨曦：{m_tea}<br>🌙 午後：{a_tea}</p>
        <p style='font-size:0.85rem;'>包含：40入茶組 + 生活語錄卡 + {"刻名杯" if first == "是的" else "加贈茶包"}</p>
        <p style='text-align:right; font-weight:bold;'>陪伴價 $1,980</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("預約這份溫柔時光 ➔"): st.session_state.step = 7; st.rerun()

elif st.session_state.step == 7:
    ans, name, first = st.session_state.answers, st.session_state.custom_name, st.session_state.is_first_time
    # (配比邏輯重複確保顯示)
    if "晨光" in ans[0]: diag, m_tea, a_tea = "暖陽系", "黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)"
    elif "微風" in ans[0]: diag, m_tea, a_tea = "微風系", "洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)"
    else: diag, m_tea, a_tea = "清泉系", "金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)"
    
    st.write("### 📢 預約暖心的相遇")
    romantic_msg = f"Hi 米寶店長！🐢✨\\n\\n我是【{diag}女子】。想預約月度陪伴計畫。\\n🌿 {'刻名：'+name if first=='是的' else '老朋友回購驚喜'}\\n☀️ 晨曦：{m_tea}\\n🌙 午後：{a_tea}"
    st.code(romantic_msg.replace('\\\\n', '\n'), language=None)
    st.markdown(f'<a href="https://line.me/R/ti/p/@716osfvq" style="text-decoration:none;"><div style="background-color: #06C755; color: white; text-align: center; padding: 15px; border-radius: 12px; font-weight: bold;">✨ 領取妳的專屬溫柔陪伴 ➔</div></a>', unsafe_allow_html=True)
    if st.button("重新探索"): st.session_state.clear(); st.rerun()

st.markdown("<p style='text-align:center; font-size:0.75rem; color:#8B8B7A; margin-top:30px;'>慶和蔘藥行研製 © 2026 Mibao Herbal</p>", unsafe_allow_html=True)
