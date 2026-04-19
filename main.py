import streamlit as st
import os

# ==========================================
# 第一步：環境設定與 CSS 視覺靈魂 (極致壓縮排版)
# ==========================================
st.set_page_config(page_title="米寶漢方｜您的植感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 1. 全域品牌設定 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    /* 縮減頂部與底部邊距以塞入一頁 */
    .block-container { padding-top: 0.5rem !important; padding-bottom: 2rem !important; }

    /* 2. 標題與引導語 (壓縮間距) */
    h3 { font-size: 1.1rem !important; font-weight: 700 !important; margin: 5px 0 !important; text-align: center !important; color: #7A8450 !important; }
    .question-text { font-size: 1rem !important; font-weight: bold !important; text-align: center !important; margin-bottom: 8px !important; }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 10px !important; font-size: 0.75rem !important; }

    /* 3. Logo 尺寸 */
    [data-testid="stImage"] img { max-height: 40px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: 2px !important; }

    /* 4. 選項卡片與烏龜特效 (不變動) */
    [data-testid="stRadio"] div[role="radiogroup"] input { display: none !important; }
    [data-testid="stRadio"] div[role="radiogroup"] { gap: 6px !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] label {
        border-radius: 10px !important; padding: 8px 15px !important;
        width: 100% !important; border: 1.5px solid rgba(0,0,0,0.05) !important;
        display: flex !important; text-align: left !important; transition: all 0.2s ease !important; cursor: pointer !important; font-size: 0.9rem !important;
    }
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(1) label { background-color: #F1F4E8 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(2) label { background-color: #FDF2E9 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(3) label { background-color: #EBF5FB !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
        font-size: 1rem !important; font-weight: 900 !important; border: 2.5px solid #7A8450 !important; background-color: #E9EDC9 !important;
    }
    [data-testid="stRadio"] div[role="radiogroup"] label:not(:has(input:checked)) > div:first-of-type { 
        background-color: transparent !important; border: 2px solid #C2C7A7 !important; 
    }
    [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) > div:first-of-type::after { 
        content: '🐢' !important; font-size: 1.2rem !important;
    } 

    /* 5. 配送資訊與輸入框 (壓縮高度) */
    div[data-baseweb="input"] { height: 40px !important; background-color: #FFFFFF !important; border: 1.5px solid #E9EDC9 !important; border-radius: 8px !important; }
    input { color: #4A4E31 !important; -webkit-text-fill-color: #4A4E31 !important; font-size: 0.9rem !important; }
    
    /* 6. LINE 按鈕與代碼框 (壓縮高度) */
    [data-testid="stLinkButton"] a {
        width: 100% !important; background-color: #06C755 !important; border-radius: 12px !important; height: 2.8em !important; 
        display: flex !important; justify-content: center !important; align-items: center !important;
    }
    [data-testid="stLinkButton"] a * { color: #FFFFFF !important; font-size: 0.95rem !important; font-weight: 900 !important; }
    [data-testid="stCodeBlock"] { background-color: #F8F9F1 !important; border-radius: 10px !important; padding: 5px !important; }

    /* 7. 落葉特效 (不變動) */
    @keyframes falling { 0% { transform: translateY(-10vh) rotate(0deg); opacity: 0; } 10% { opacity: 1; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
    .leaf { position: fixed; top: -10vh; font-size: 18px; pointer-events: none; z-index: 9999; animation: falling 12s linear infinite; }

    /* 8. 隱藏頁尾以騰出空間 */
    #MainMenu, footer, header { visibility: hidden; }
    .footer-hide { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 第二步：系統記憶 (Session State)
# ==========================================
def show_leaves():
    leaves_html = "".join([f'<div class="leaf" style="left:{i*15}vw; animation-delay:{i*1.5}s;">🍃</div>' for i in range(7)])
    st.markdown(leaves_html, unsafe_allow_html=True)

for key in ['step', 'answers', 'custom_name', 'is_first_time', 'plan', 'warn']:
    if key not in st.session_state:
        st.session_state[key] = 1 if key == 'step' else [] if key == 'answers' else ""

img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
st.markdown('<p class="quote">「在忙碌中，給您留一刻鐘的溫暖。」</p>', unsafe_allow_html=True)

# ==========================================
# 第三步：測驗流程 (不變動)
# ==========================================
if st.session_state.step <= 3:
    titles = ["### 壹｜傾聽・身體的低語", "### 貳｜梳理・日常的軌跡", "### 參｜遇見・嚮往的自己"]
    qs = ["當您靜下心，您的身體正低聲說著...？", "關於這段日子的作息，您的狀態是...？", "在最需要喘息的午後，您想感受到的是...？"]
    opts = [
        ["我有些疲累，渴望溫潤透亮的晨光", "我有些沉重，想找回輕盈自在的微風", "我有些燥熱，想念山間清澈甘甜的泉水"],
        ["長時間待在冷氣房，手腳冰冷循環差", "生活忙碌常熬夜，作息不規律隨意吃", "壓力大節奏快，心神緊繃難入眠"],
        ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，從容自在"]
    ]
    btns = ["下一步 ➔", "下一步 ➔", "遇見專屬植感 ➔"]
    
    st.markdown(titles[st.session_state.step-1])
    st.markdown(f'<p class="question-text">{qs[st.session_state.step-1]}</p>', unsafe_allow_html=True)
    ans = st.radio("", opts[st.session_state.step-1], index=None, key=f"q{st.session_state.step}", label_visibility="collapsed")
    
    if st.button(btns[st.session_state.step-1]):
        if ans:
            st.session_state.answers.append(ans); st.session_state.step += 1; st.rerun()

elif st.session_state.step == 4:
    st.markdown("### 💎 您是米寶的新朋友嗎？")
    choice = st.radio("", ["是的，我是新朋友 👋", "我是老朋友 🤗"], index=None, label_visibility="collapsed")
    if st.button("開啟專屬禮遇 ➔"):
        if choice: st.session_state.is_first_time = choice; st.session_state.step = 4.5; st.rerun()

elif st.session_state.step == 4.5:
    st.markdown("### 🌿 選擇您的陪伴方案")
    p_list = ["首購限定組合 (40入) $1,980", "一週輕體驗組 (10入) $680"] if "新朋友" in st.session_state.is_first_time else ["老友回購組合 (40入) $1,880", "一週輕體驗組 (10入) $680"]
    p_choice = st.radio("", p_list, index=None, label_visibility="collapsed")
    if st.button("查看您的植感配方 ➔"):
        if p_choice:
            st.session_state.plan = p_choice
            if "新朋友" in st.session_state.is_first_time and "$1,980" in p_choice: st.session_state.step = 5
            else: st.session_state.custom_name = "老朋友贈茶" if "40入" in p_choice else "輕體驗"; st.session_state.step = 6
            st.rerun()

elif st.session_state.step == 5:
    st.markdown("### 💎 鐫刻您的專屬風格")
    u_name = st.text_input("雷刻文字 (最多12字)", max_chars=12, placeholder="例如：米寶漢方")
    if st.button("查看專屬配方 ➔"):
        if u_name: st.session_state.custom_name = u_name; st.session_state.step = 6; st.rerun()

# ==========================================
# 第四步：最終結果與壓縮結帳區
# ==========================================
elif st.session_state.step == 6:
    show_leaves()
    ans, plan, c_name, first = st.session_state.answers, st.session_state.plan, st.session_state.custom_name, st.session_state.is_first_time
    dg = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    
    st.markdown(f'<div style="background-color: #E9EDC9; padding: 10px; border-radius: 12px; text-align:center; margin-bottom:10px;"><b>✨ 您是：{dg}氣質</b><br><small>{plan}</small></div>', unsafe_allow_html=True)
    
    # --- 壓縮排版：姓名與電話並排 ---
    st.markdown("<h4 style='text-align:center; color:#7A8450; margin:0;'>📝 配送資訊</h4>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1: o_name = st.text_input("姓名", placeholder="姓名...", label_visibility="collapsed")
    with col2: o_phone = st.text_input("電話", placeholder="電話...", label_visibility="collapsed")
    o_addr = st.text_input("地址", placeholder="請填寫收件地址...", label_visibility="collapsed")

    # --- 溫馨提示邏輯 ---
    if not o_name or not o_phone or not o_addr:
        missing = []
        if not o_name: missing.append("姓名")
        if not o_phone: missing.append("電話")
        if not o_addr: missing.append("地址")
        st.markdown(f"<p style='color:#C38D5E; font-size:0.8rem; text-align:center; margin:0;'>🐢 溫馨小提醒：請補齊「{'、'.join(missing)}」米寶才能配送喔！</p>", unsafe_allow_html=True)

    # 組合訊息
    m_v, a_v = ("黃耆元氣茶+金菊牛蒡茶", "當歸紅棗茶+黑豆漢方茶") if "晨光" in ans[0] else ("洛神山楂茶+金菊牛蒡茶", "玫瑰決明茶+黑豆漢方茶") if "微風" in ans[0] else ("金菊牛蒡茶+黃耆元氣茶", "玫瑰決明茶+當歸紅棗茶")
    info = f"👤 姓名：{o_name if o_name else '(未填)'}\n📱 電話：{o_phone if o_phone else '(未填)'}\n📍 地址：{o_addr if o_addr else '(未填)'}"
    msg = f"Hi 米寶！🐢✨\n預約：{plan}\n我是：【{dg}】\n☀️ 晨曦：{m_v}\n🌙 午後：{a_v}\n---\n{info}\n期待這份溫暖。🌿🍵"

    st.code(msg, language=None)
    st.link_button("🌿 前往 LINE@ 貼上預約資訊 ➔", "https://line.me/R/ti/p/@716osfvq", use_container_width=True)
    if st.button("重新測驗"): st.session_state.clear(); st.rerun()