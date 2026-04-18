import streamlit as st
import os

# 1. 究極視覺與跳轉鎖定：V74 質感、去黑底、茶包換行、LINE 強效跳轉
st.set_page_config(page_title="米寶漢方｜您的植感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域品牌色與字體鎖定 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 容器邊距校準 */
    .block-container { padding-top: 0.5rem !important; padding-bottom: 60px !important; }

    /* 標題與題目 */
    h3 { font-size: 1.1rem !important; font-weight: 700 !important; margin: 10px 0 !important; text-align: center !important; color: #7A8450 !important; }
    .question-text { font-size: 1.05rem !important; font-weight: bold !important; text-align: center !important; margin-bottom: 15px !important; }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 10px; font-size: 0.8rem; }

    /* Logo 尺寸 */
    [data-testid="stImage"] img { max-height: 50px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: -10px !important; }

    /* 選項卡片：左對齊、黑點縮小 */
    [data-testid="stRadio"] div[role="radiogroup"] { gap: 8px !important; } 
    [data-testid="stRadio"] label {
        border-radius: 10px !important; padding: 12px 18px !important;
        width: 100% !important; border: 1px solid rgba(0,0,0,0.05) !important;
        display: flex !important; justify-content: flex-start !important; 
        text-align: left !important; font-size: 0.95rem !important; 
    }
    [data-testid="stRadio"] div[role="radiogroup"] [data-testid="stRadioButton"] > div:first-child { transform: scale(0.7) !important; }

    /* 選中後效果：V74 核心肯定感 */
    div[data-testid="stRadio"] div[role="radiogroup"] div[aria-checked="true"] label {
        font-size: 1.1rem !important; font-weight: 900 !important;   
        color: #2D301D !important; border: 2px solid #7A8450 !important;
        background-color: #E9EDC9 !important;
    }

    /* 價格置中與結果框 */
    .price-text { font-size: 1.45rem !important; font-weight: bold !important; color: #7A8450 !important; margin-top: 15px; display: block; text-align: center !important; }

    /* 徹底去黑底、自動換行、防止左右滑動 */
    [data-testid="stCodeBlock"], [data-testid="stCodeBlock"] pre, [data-testid="stCodeBlock"] code {
        background-color: #F8F9F1 !important; color: #4A4E31 !important;
        white-space: pre-wrap !important; word-wrap: break-word !important; word-break: break-all !important;
        font-size: 0.85rem !important; padding: 12px !important; border: 1px solid #E9EDC9 !important; border-radius: 12px !important;
    }
    [data-testid="stCodeBlock"] button { opacity: 1 !important; visibility: visible !important; background-color: #E9EDC9 !important; scale: 0.8; }
    code span { background-color: transparent !important; color: #4A4E31 !important; }

    /* LINE 按鈕技術修復：強制 block display 與高 z-index */
    .line-fix-container {
        margin-top: 15px !important;
        position: relative !important;
        z-index: 9999 !important;
    }
    .line-cta-link {
        display: block !important;
        text-decoration: none !important;
        cursor: pointer !important;
    }
    .line-btn-body {
        background-color: #06C755 !important;
        color: white !important;
        text-align: center !important;
        padding: 16px;
        border-radius: 15px;
        font-weight: 900;
        font-size: 1rem;
        box-shadow: 0 4px 12px rgba(6, 199, 85, 0.3);
    }

    /* 按鈕樣式 */
    .stButton > button { width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important; border-radius: 25px !important; height: 3em !important; font-weight: bold !important; }
    .stButton > button p { color: #FFFFFF !important; font-size: 1rem !important; }

    /* 頁尾 */
    .custom-footer { position: fixed; left: 0; bottom: 8px; width: 100%; text-align: center; background-color: transparent; z-index: 99; pointer-events: none; }
    .footer-text { font-size: 0.65rem !important; color: #8B8B7A !important; line-height: 1.3 !important; }
    #MainMenu, footer, header { visibility: hidden !important; }
    </style>
    """, unsafe_allow_html=True)

# ----------------- 邏輯初始化 -----------------
for k in ['step','answers','custom_name','bundle']:
    if k not in st.session_state: st.session_state[k] = 1 if k=='step' else [] if k=='answers' else ""

# 頂部 Logo
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
st.markdown('<p class="quote">「在忙碌中，給您留一刻鐘的溫暖。」</p>', unsafe_allow_html=True)

# ----------------- 流程 -----------------
if st.session_state.step <= 3:
    qs = [
        "當您靜下心，您的身體正低聲說著...？",
        "關於這段日子的作息，您的狀態是...？",
        "在最需要喘息的午後，您想感受到的是...？"
    ]
    opts = [
        ["我有些疲累，渴望溫潤透亮的晨光", "我有些沉重，想找回輕盈自在的微風", "我有些燥熱，想念山間清澈甘甜的泉水"],
        ["長時間待在冷氣房，手腳冰冷循環差", "生活忙碌常熬夜，作息不規律隨意吃", "壓力大節奏快，心神緊繃難入眠"],
        ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，從容自在"]
    ]
    st.markdown(f"### 第 {st.session_state.step} 步")
    st.markdown(f'<p class="question-text">{qs[st.session_state.step-1]}</p>', unsafe_allow_html=True)
    ans = st.radio("", opts[st.session_state.step-1], index=None, key=f"q{st.session_state.step}", label_visibility="collapsed")
    if st.button("緩緩走向下一步 ➔"):
        if ans: st.session_state.answers.append(ans); st.session_state.step += 1; st.rerun()

elif st.session_state.step == 4:
    st.markdown("### ✨ 選擇您的植感預約組合")
    bundles = [
        "首購限定組合 $1,980 [贈：精品刻名隨行杯 👋]",
        "老友回購組合 $1,880 [贈：驚喜茶包 3 入 🤗]",
        "一週輕體驗組合 $680 [初次邂逅草本 🍵]"
    ]
    selected = st.radio("", bundles, index=None, key="bundle_v88", label_visibility="collapsed")
    engraving = ""
    if selected == bundles[0]:
        st.markdown("<p style='font-size:0.85rem; margin:10px 0 5px; text-align:center;'>雷刻文字 (12字內)：</p>", unsafe_allow_html=True)
        engraving = st.text_input("", placeholder="例如：Mila", label_visibility="collapsed")
    if st.button("查看我的專屬配比 ➔"):
        if selected:
            st.session_state.bundle = selected
            st.session_state.custom_name = engraving if selected == bundles[0] else "熟客禮遇"
            st.session_state.step = 5; st.rerun()

elif st.session_state.step == 5:
    ans, bundle, name = st.session_state.answers, st.session_state.bundle, st.session_state.custom_name
    price_val = 1980 if "$1,980" in bundle else 1880 if "$1,880" in bundle else 680
    diag = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"

    if price_val >= 1880:
        if diag == "暖陽系": m_t, a_t = "黃耆元氣茶 (14入)<br>+ 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入)<br>+ 黑豆漢方茶 (8入)"
        elif diag == "微風系": m_t, a_t = "洛神山楂茶 (12入)<br>+ 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入)<br>+ 黑豆漢方茶 (10入)"
        else: m_t, a_t = "金菊牛蒡茶 (15入)<br>+ 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入)<br>+ 當歸紅棗茶 (6入)"
        gift = f"• 首購禮：專屬刻名隨行杯 ({name})" if price_val == 1980 else "• 老友禮：加贈驚喜茶包 3 入"
        amt = "40 入深度植感漢方茶組"
    else:
        if diag == "暖陽系": m_t, a_t = "黃耆元氣茶 (4入)<br>+ 金菊牛蒡茶 (1入)", "當歸紅棗茶 (3入)<br>+ 黑豆漢方茶 (2入)"
        elif diag == "微風系": m_t, a_t = "洛神山楂茶 (3入)<br>+ 金菊牛蒡茶 (2入)", "玫瑰決明茶 (3入)<br>+ 黑豆漢方茶 (2入)"
        else: m_t, a_t = "金菊牛蒡茶 (4入)<br>+ 黃耆元氣茶 (1入)", "玫瑰決明茶 (4入)<br>+ 當歸紅棗茶 (1入)"
        gift = "• 體驗方案：初探草本植感相遇"
        amt = "10 入一週輕體驗茶組"

    st.markdown(f"""<div style="background-color: #FFFFFF; padding: 15px; border-radius: 15px; border: 1px solid #E9EDC9;">
        <h3 style='margin:0;'>✨ 您是：{diag}氣質</h3>
        <hr style='border: 0.5px solid #E9EDC9; margin: 8px 0;'>
        <p style='font-size:1rem; margin:0; font-weight:bold;'>☀️ 晨曦：<br>{m_t}</p>
        <p style='font-size:1rem; margin:8px 0 0; font-weight:bold;'>🌙 午後：<br>{a_t}</p>
        <hr style='border: 0.5px solid #E9EDC9; margin: 8px 0;'>
        <p style='font-size:0.95rem; margin:0; font-weight:bold; color:#7A8450;'>• {amt}<br>{gift}</p>
        <span class="price-text">方案預約價 ${price_val}</span></div>""", unsafe_allow_html=True)
    if st.button("預約這份植感時光 ➔"): st.session_state.step = 6; st.rerun()

elif st.session_state.step == 6:
    ans, bundle, name = st.session_state.answers, st.session_state.bundle, st.session_state.custom_name
    diag = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    price_val = 1980 if "$1,980" in bundle else 1880 if "$1,880" in bundle else 680
    
    if price_val >= 1880:
        m_v, a_v = ("黃耆元氣茶 (14)\n+ 金菊牛蒡茶 (6)", "當歸紅棗茶 (12)\n+ 黑豆漢方茶 (8)") if diag=="暖陽系" else ("洛神山楂茶 (12)\n+ 金菊牛蒡茶 (8)", "玫瑰決明茶 (10)\n+ 黑豆漢方茶 (10)") if diag=="微風系" else ("金菊牛蒡茶 (15)\n+ 黃耆元氣茶 (5)", "玫瑰決明茶 (14)\n+ 當歸紅棗茶 (6)")
        eng = f"🌿 杯蓋刻字：{name}" if price_val == 1980 else "🌿 熟客回購加贈禮"
    else:
        m_v, a_v = ("黃耆元氣茶 (4)\n+ 金菊牛蒡茶 (1)", "當歸紅棗茶 (3)\n+ 黑豆漢方茶 (2)") if diag=="暖陽系" else ("洛神山楂茶 (3)\n+ 金菊牛蒡茶 (2)", "玫瑰決明茶 (3)\n+ 黑豆漢方茶 (2)") if diag=="微風系" else ("金菊牛蒡茶 (4)\n+ 黃耆元氣茶 (1)", "玫瑰決明茶 (4)\n+ 當歸紅棗茶 (1)")
        eng = "🌿 方案：一週輕體驗"

    msg = f"Hi 米寶！🐢✨\n預約：{bundle}\n我是：【{diag}】\n\n☀️ 晨曦：\n{m_v}\n\n🌙 午後：\n{a_v}\n\n{eng}\n期待這份草本溫暖。🌿🍵"
    st.markdown('<p style="font-size:0.9rem; text-align:center; margin-bottom:5px;">點擊☆右上角☆複製後貼給米寶吧：</p>', unsafe_allow_html=True)
    st.code(msg, language=None)
    
    # 【關鍵技術修復】強效 LINE 跳轉連結
    st.markdown(f'''
        <div class="line-fix-container">
            <a href="https://line.me/R/ti/p/@716osfvq" target="_blank" class="line-cta-link">
                <div class="line-btn-body">🌿 前往 LINE@ 貼上專屬配方給米寶 ➔</div>
            </a>
        </div>
    ''', unsafe_allow_html=True)
    
    if st.button("重新探索"): st.session_state.clear(); st.rerun()

st.markdown("""<div class="custom-footer"><p class="footer-text">慶和蔘藥行研製｜本產品屬一般食品。 © 2026 Mibao Herbal</p></div>""", unsafe_allow_html=True)
