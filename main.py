import streamlit as st
import os

# ==========================================
# 第一步：環境設定與 CSS 視覺靈魂 
# ==========================================
st.set_page_config(page_title="米寶漢方｜您的植感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 1. 全域品牌設定 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    .block-container { padding-top: 1.5rem !important; padding-bottom: 90px !important; }

    /* 2. 標題與引導語 */
    h3 { font-size: 1.15rem !important; font-weight: 700 !important; margin: 10px 0 !important; text-align: center !important; color: #7A8450 !important; letter-spacing: 1px; }
    .question-text { font-size: 1.05rem !important; font-weight: bold !important; text-align: center !important; margin-bottom: 12px !important; line-height: 1.4 !important; }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 15px !important; font-size: 0.8rem !important; }

    /* 3. Logo 尺寸 */
    [data-testid="stImage"] img { max-height: 50px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: 5px !important; }

    /* 4. 選項卡片與極致選中特效 */
    [data-testid="stRadio"] div[role="radiogroup"] input { display: none !important; }
    [data-testid="stRadio"] div[role="radiogroup"] { gap: 8px !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] label {
        border-radius: 12px !important; padding: 10px 18px !important;
        width: 100% !important; border: 1.5px solid rgba(0,0,0,0.05) !important;
        display: flex !important; justify-content: flex-start !important; 
        text-align: left !important; transition: all 0.2s ease !important; cursor: pointer !important; font-size: 0.95rem !important;
    }
    
    /* 三色網底精準套用 */
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(1) label { background-color: #F1F4E8 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(2) label { background-color: #FDF2E9 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(3) label { background-color: #EBF5FB !important; } 
    
    [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
        font-size: 1.1rem !important; font-weight: 900 !important;   
        color: #2D301D !important; border: 2.5px solid #7A8450 !important; background-color: #E9EDC9 !important;
    }
    [data-testid="stRadio"] div[role="radiogroup"] label:not(:has(input:checked)) > div:first-of-type > div { display: none !important; }
    [data-testid="stRadio"] div[role="radiogroup"] label:not(:has(input:checked)) > div:first-of-type { 
        background-color: transparent !important; border: 2px solid #C2C7A7 !important; 
    }
    [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) > div:first-of-type > div { display: none !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) > div:first-of-type { 
        background-color: transparent !important; border: none !important; overflow: visible !important; 
        display: flex !important; justify-content: center !important; align-items: center !important;
    } 
    [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) > div:first-of-type::after { 
        content: '🐢' !important; font-size: 1.3rem !important; display: block !important;
    } 

    /* 5. 一般按鈕特效 */
    .stButton > button {
        width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important;
        border-radius: 25px !important; height: 3em !important; font-weight: bold !important; border: none !important; margin-top: 10px !important; transition: all 0.2s ease !important;
    }
    .stButton > button p { color: #FFFFFF !important; font-size: 1rem !important; }
    .stButton > button:hover { background-color: #8B8B7A !important; }
    .stButton > button:active { background-color: #4A4E31 !important; transform: scale(0.98) !important; }

    /* 6. LINE 原生跳轉按鈕樣式鎖定 */
    [data-testid="stLinkButton"] a {
        width: 100% !important; background-color: #06C755 !important; 
        border-radius: 15px !important; height: 3.2em !important; 
        border: none !important; transition: transform 0.2s ease !important;
        display: flex !important; justify-content: center !important; align-items: center !important; text-decoration: none !important;
    }
    [data-testid="stLinkButton"] a * { color: #FFFFFF !important; font-size: 1.05rem !important; font-weight: 900 !important; }

    /* 7. 溫暖提示語與價格 */
    .warm-tip { font-size: 0.85rem !important; color: #B08968 !important; text-align: center !important; margin-top: 5px !important; font-weight: bold !important; }
    .price-text { font-size: 1.45rem !important; font-weight: bold !important; color: #7A8450 !important; margin-top: 15px; display: block; text-align: center !important; }

    /* 8. 程式碼框 */
    [data-testid="stCodeBlock"], [data-testid="stCodeBlock"] > div, pre, code { background-color: #F8F9F1 !important; border: 1px solid #E9EDC9 !important; border-radius: 12px !important; }
    [data-testid="stCodeBlock"] button { opacity: 1 !important; background-color: rgba(233, 237, 201, 1) !important; scale: 0.8; }
    
    /* 雷刻填字區與同行輸入框防黑底 */
    [data-testid="stTextInput"] div[data-baseweb="input"], 
    [data-testid="stTextInput"] div[data-baseweb="base-input"] { 
        background-color: #FFFFFF !important; 
        border: 1.5px solid #E9EDC9 !important; 
        border-radius: 8px !important; 
    }
    [data-testid="stTextInput"] input { 
        color: #4A4E31 !important; 
        -webkit-text-fill-color: #4A4E31 !important; 
        background-color: #FFFFFF !important; 
    }

    /* 9. 森林落葉 */
    @keyframes falling { 0% { transform: translateY(-10vh) rotate(0deg); opacity: 0; } 10% { opacity: 1; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
    .leaf { position: fixed; top: -10vh; font-size: 18px; pointer-events: none; z-index: 9999; animation: falling 12s linear infinite; }

    /* 10. 絕對固定頁尾 */
    .custom-footer {
        position: fixed; left: 0; bottom: 0; width: 100vw; text-align: center; 
        background-color: #FDFBF7; padding: 8px 0; z-index: 9999; box-shadow: 0 -2px 10px rgba(0,0,0,0.03); 
    }
    .footer-text { font-size: 0.65rem !important; color: #8B8B7A !important; line-height: 1.2 !important; margin: 0 !important; }
    #MainMenu, footer, header { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 第二步：系統記憶 (Session State) 與頂部佈置
# ==========================================
def show_leaves():
    leaves_html = "".join([f'<div class="leaf" style="left:{i*15}vw; animation-delay:{i*1.5}s;">🍃</div>' for i in range(7)])
    st.markdown(leaves_html, unsafe_allow_html=True)

for key in ['step', 'answers', 'custom_name', 'is_first_time', 'plan', 'warn']:
    if key not in st.session_state:
        st.session_state[key] = 1 if key == 'step' else [] if key == 'answers' else ""

img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
st.markdown('<p class="quote">「在忙碌中，給您留一刻鐘的溫暖。」</p>', unsafe_allow_html=True)

# ==========================================
# 第三步：測驗引擎 (第 1 ~ 3 步) - 浪漫 A 文案
# ==========================================
if st.session_state.step <= 3:
    titles = ["### 壹｜傾聽・身體的低語", "### 貳｜梳理・日常的軌跡", "### 參｜遇見・嚮往的自己"]
    qs = ["當您靜下心，您的身體正低聲說著...？", "關於這段日子的作息，您的狀態是...？", "在最需要喘息的午後，您想感受到的是...？"]
    opts = [
        ["我有些疲累，渴望溫潤透亮的晨光", "我有些沉重，想找回輕盈自在的微風", "我有些燥熱，想念山間清澈甘甜的泉水"],
        ["長時間待在冷氣房，手腳冰冷循環差", "生活忙碌常熬夜，作息不規律隨意吃", "壓力大節奏快，心神緊繃難入眠"],
        ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，從容自在"]
    ]
    btns = ["緩緩走向下一步 ➔", "傾聽日常的節奏 ➔", "遇見您的專屬植感陪伴 ➔"]
    warns = ["🌿 請先聽聽身體的聲音，再告訴米寶喔。", "☕️ 沒關係，深呼吸，選一個最接近您的狀態吧。", "✨ 您的嚮往對米寶很重要，請讓我們知道您的心情。"]
    
    st.markdown(titles[st.session_state.step-1])
    st.markdown(f'<p class="question-text">{qs[st.session_state.step-1]}</p>', unsafe_allow_html=True)
    
    ans = st.radio("", opts[st.session_state.step-1], index=None, key=f"q{st.session_state.step}", label_visibility="collapsed")
    
    if st.button(btns[st.session_state.step-1]):
        if ans:
            st.session_state.answers.append(ans)
            st.session_state.step += 1
            st.session_state.warn = ""
            st.rerun()
        else:
            st.session_state.warn = warns[st.session_state.step-1]
    
    if st.session_state.warn:
        st.markdown(f'<p class="warm-tip">{st.session_state.warn}</p>', unsafe_allow_html=True)

# ==========================================
# 第四步：商業邏輯與防呆 (第 4 ~ 5 步：新老朋友與方案)
# ==========================================
elif st.session_state.step == 4:
    st.markdown("### 💎 您是米寶的新朋友嗎？")
    choice = st.radio("", ["是的，我是新朋友 👋", "我是老朋友 🤗"], index=None, key="id_v115", label_visibility="collapsed")
    if st.button("開啟您的專屬禮遇 ➔"):
        if choice:
            st.session_state.is_first_time = choice
            st.session_state.step = 4.5; st.session_state.warn = ""; st.rerun()
        else: st.session_state.warn = "💎 選擇一個身分，讓米寶準備專屬驚喜。"
    if st.session_state.warn: st.markdown(f'<p class="warm-tip">{st.session_state.warn}</p>', unsafe_allow_html=True)

elif st.session_state.step == 4.5:
    st.markdown("### 🌿 選擇您的陪伴方案")
    p_list = ["首購限定組合 (40入) $1,980", "一週輕體驗組 (10入) $680"] if "新朋友" in st.session_state.is_first_time else ["老友回購組合 (40入) $1,880", "一週輕體驗組 (10入) $680"]
    p_choice = st.radio("", p_list, index=None, key="plan_v115", label_visibility="collapsed")
    if st.button("查看您的植感配方 ➔"):
        if p_choice:
            st.session_state.plan = p_choice
            if "新朋友" in st.session_state.is_first_time and "$1,980" in p_choice: st.session_state.step = 5
            else: st.session_state.custom_name = "老朋友驚喜贈茶" if "40入" in p_choice else "輕體驗方案"; st.session_state.step = 6
            st.session_state.warn = ""; st.rerun()
        else: st.session_state.warn = "🥣 請選擇一個組合，讓溫暖精準送達。"
    if st.session_state.warn: st.markdown(f'<p class="warm-tip">{st.session_state.warn}</p>', unsafe_allow_html=True)

elif st.session_state.step == 5:
    st.markdown("### 💎 鐫刻您的專屬風格")
    st.markdown("<div style='background-color: #FFFFFF; padding: 15px; border-radius: 12px; border: 1px solid #E9EDC9; font-size:0.95rem; text-align:center;'>為您準備一只質感的玻璃隨行杯。<br>木蓋上將鐫刻您的專屬風格。<br>陪伴您渡過植感健康每一天。</div>", unsafe_allow_html=True)
    u_name = st.text_input("雷刻文字 (最多12字)", max_chars=12, placeholder="例如：米寶漢方")
    if st.button("查看您的專屬配方 ➔"):
        if u_name: st.session_state.custom_name = u_name; st.session_state.step = 6; st.rerun()

# ==========================================
# 第五步：最終結帳與跳轉 (第 6 ~ 7 步：植感卡片與 LINE 預約)
# ==========================================
elif st.session_state.step == 6:
    show_leaves()
    ans, plan, name, first = st.session_state.answers, st.session_state.plan, st.session_state.custom_name, st.session_state.is_first_time
    price_val = "$1,980" if "$1,980" in plan else "$1,880" if "$1,880" in plan else "$680"
    
    if "40入" in plan:
        amt_t = "40 入深度植感漢方茶組"
        m_t, a_t = ("黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)") if "晨光" in ans[0] else ("洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)") if "微風" in ans[0] else ("金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)")
        gift = f"• 首購禮：專屬刻名隨行杯 ({name})" if "新朋友" in first else "• 老朋友禮：加贈驚喜茶包 3 包"
    else:
        amt_t = "10 入一週輕體驗茶組"
        m_t, a_t = ("黃耆元氣茶 (4入) + 金菊牛蒡茶 (1入)", "當歸紅棗茶 (3入) + 黑豆漢方茶 (2入)") if "晨光" in ans[0] else ("洛神山楂茶 (3入) + 金菊牛蒡茶 (2入)", "玫瑰決明茶 (3入) + 黑豆漢方茶 (2入)") if "微風" in ans[0] else ("金菊牛蒡茶 (4入) + 黃耆元氣茶 (1入)", "玫瑰決明茶 (4入) + 當歸紅棗茶 (1入)")
        gift = "• 體驗方案：初探草本植感相遇"
    
    dg = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    st.markdown(f"""<div style="background-color: #FFFFFF; padding: 15px; border-radius: 15px; border: 1px solid #E9EDC9;">
        <h3 style='margin:0;'>✨ 您是：{dg}氣質</h3>
        <hr style='border: 0.5px solid #E9EDC9; margin: 8px 0;'>
        <p style='font-size:1.05rem; margin:0; font-weight:bold;'>☀️ 晨曦：{m_t}</p>
        <p style='font-size:1.05rem; margin:8px 0 0; font-weight:bold;'>🌙 午後：{a_t}</p>
        <hr style='border: 0.5px solid #E9EDC9; margin: 8px 0;'>
        <p style='font-size:0.95rem; margin:0; font-weight:bold; color:#7A8450;'>• {amt_t}<br>{gift}</p>
        <span class="price-text">方案預約價 {price_val}</span></div>""", unsafe_allow_html=True)
    if st.button("預約這份植感時光 ➔"): st.session_state.step = 7; st.rerun()

elif st.session_state.step == 7:
    show_leaves()
    ans, plan, name, first = st.session_state.answers, st.session_state.plan, st.session_state.custom_name, st.session_state.is_first_time
    dg = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    
    if "40入" in plan:
        m_v, a_v = ("黃耆元氣茶(14入)+金菊牛蒡茶(6入)", "當歸紅棗茶(12入)+黑豆漢方茶(8入)") if "晨光" in ans[0] else ("洛神山楂茶(12入)+金菊牛蒡茶(8入)", "玫瑰決明茶(10入)+黑豆漢方茶(10入)") if "微風" in ans[0] else ("金菊牛蒡茶(15入)+黃耆元氣茶(5入)", "玫瑰決明茶(14入)+當歸紅棗茶(6入)")
        eng = f"🌿 杯蓋刻字：{name}" if "新朋友" in first else "🌿 老友回購贈茶"
    else:
        m_v, a_v = ("黃耆元氣茶(4入)+金菊牛蒡茶(1入)", "當歸紅棗茶(3入)+黑豆漢方茶(2入)") if "晨光" in ans[0] else ("洛神山楂茶(3入)+金菊牛蒡茶(2入)", "玫瑰決明茶(3入)+黑豆漢方茶(2入)") if "微風" in ans[0] else ("金菊牛蒡茶(4入)+黃耆元氣茶(1入)", "玫瑰決明茶(4入)+當歸紅棗茶(1入)")
        eng = "🌿 方案：一週輕體驗組"

    # --- 👇 這是保證「不換行、圖示在左、框在右」的最新版 ---
    
    # 建立第一行：圖示與姓名
    c1, c2 = st.columns([1, 8])
    with c1: st.markdown("<p style='margin-top:8px; font-size:1.1rem; text-align:center;'>👤</p>", unsafe_allow_html=True)
    with c2: order_name = st.text_input("name", placeholder="請填寫收件人姓名", label_visibility="collapsed")
    
    # 建立第二行：圖示與電話
    c3, c4 = st.columns([1, 8])
    with c3: st.markdown("<p style='margin-top:8px; font-size:1.1rem; text-align:center;'>📱</p>", unsafe_allow_html=True)
    with c4: order_phone = st.text_input("phone", placeholder="請填寫手機號碼", label_visibility="collapsed")
    
    # 建立第三行：圖示與地址
    c5, c6 = st.columns([1, 8])
    with c5: st.markdown("<p style='margin-top:8px; font-size:1.1rem; text-align:center;'>📍</p>", unsafe_allow_html=True)
    with c6: order_address = st.text_input("addr", placeholder="請填寫完整收件地址", label_visibility="collapsed")

    # 溫暖小提醒邏輯
    missing = []
    if not order_name: missing.append("姓名")
    if not order_phone: missing.append("電話")
    if not order_address: missing.append("地址")
    
    if missing:
        st.markdown(f"<p style='color:#C38D5E; font-size:0.85rem; text-align:center; font-weight:bold; margin-top:5px;'>🐢 溫馨小提醒：請補填「{'、'.join(missing)}」米寶才能配送喔！</p>", unsafe_allow_html=True)

    # 組合顧客資訊字串
    info_str = f"👤 姓名：{order_name if order_name else '(未填寫)'}\n📱 電話：{order_phone if order_phone else '(未填寫)'}\n📍 地址：{order_address if order_address else '(未填寫)'}"

    # 把 info_str 放進 msg 裡面
    msg = f"Hi 米寶！🐢✨\n預約：{plan}\n我是：【{dg}】\n☀️ 晨曦：{m_v}\n🌙 午後：{a_v}\n{eng}\n---\n{info_str}\n---\n期待這份草本溫暖。🌿🍵"
    # --- 👆 新增結束 ---

    st.code(msg, language=None)
    
    st.markdown('<p style="font-size:0.9rem; text-align:center; margin-top:10px; margin-bottom:5px;">點擊☆上框右上角☆複製</p>', unsafe_allow_html=True)
    
    line_url = "https://line.me/R/ti/p/@716osfvq"
    st.link_button("🌿 前往 LINE@ 貼上專屬方案與米寶相遇吧！ ➔", line_url, use_container_width=True)
    
    if st.button("重新探索"): st.session_state.clear(); st.rerun()

st.markdown("""<div class="custom-footer"><p class="footer-text">米寶漢方｜慶和蔘藥行研製｜© 2026 Mibao Herbal</p></div>""", unsafe_allow_html=True)