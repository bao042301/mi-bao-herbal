import streamlit as st
import os

# ==========================================
# 第一步：環境設定與 CSS 視覺靈魂 (五次校對：極致壓縮版)
# ==========================================
st.set_page_config(page_title="米寶漢方｜您的植感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域品牌與背景 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 🚀 壓縮邊距：為了「塞入一頁」，將上下留白縮到最小 */
    .block-container { padding-top: 0.5rem !important; padding-bottom: 30px !important; }
    
    /* 標題與引導語壓縮 */
    h3 { font-size: 1.1rem !important; font-weight: 700 !important; margin: 5px 0 !important; text-align: center !important; color: #7A8450 !important; }
    .question-text { font-size: 1rem !important; font-weight: bold !important; text-align: center !important; margin-bottom: 5px !important; }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 10px !important; font-size: 0.75rem !important; }

    /* Logo 壓縮 */
    [data-testid="stImage"] img { max-height: 40px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: 2px !important; }

    /* 烏龜選項 (保持原樣) */
    [data-testid="stRadio"] div[role="radiogroup"] input { display: none !important; }
    [data-testid="stRadio"] div[role="radiogroup"] label {
        border-radius: 10px !important; padding: 8px 15px !important;
        width: 100% !important; border: 1.5px solid rgba(0,0,0,0.05) !important;
        display: flex !important; transition: all 0.2s ease !important; cursor: pointer !important; font-size: 0.9rem !important;
    }
    [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
        border: 2.5px solid #7A8450 !important; background-color: #E9EDC9 !important; font-weight: 900 !important;
    }
    [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) > div:first-of-type::after { 
        content: '🐢' !important; font-size: 1.2rem !important;
    } 

    /* 輸入框與按鈕 (並排優化) */
    div[data-baseweb="input"] { height: 42px !important; background-color: #FFFFFF !important; border: 1.5px solid #E9EDC9 !important; border-radius: 8px !important; }
    input { color: #4A4E31 !important; -webkit-text-fill-color: #4A4E31 !important; }
    
    .stButton > button { width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important; border-radius: 20px !important; height: 2.8em !important; border: none !important; }
    [data-testid="stLinkButton"] a { width: 100% !important; background-color: #06C755 !important; border-radius: 12px !important; height: 3em !important; display: flex !important; justify-content: center !important; align-items: center !important; text-decoration: none !important; }
    [data-testid="stLinkButton"] a * { color: #FFFFFF !important; font-weight: 900 !important; font-size: 1rem !important; }

    /* 落葉特效 */
    @keyframes falling { 0% { transform: translateY(-10vh) rotate(0deg); opacity: 0; } 10% { opacity: 1; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
    .leaf { position: fixed; top: -10vh; font-size: 18px; pointer-events: none; z-index: 9999; animation: falling 12s linear infinite; }

    /* 抹茶綠複製框 */
    [data-testid="stCodeBlock"] { background-color: #F8F9F1 !important; border: 1px solid #E9EDC9 !important; border-radius: 12px !important; padding: 5px !important; }
    
    /* 隱藏選單 */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 第二步：系統記憶與落葉
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
# 第三步：測驗流程 (1~5 步)
# ==========================================
if st.session_state.step <= 3:
    qs = ["當您靜下心，您的身體正低聲說著...？", "關於這段日子的作息，您的狀態是...？", "在最需要喘息的午後，您想感受到的是...？"]
    opts = [["我有些疲累，渴望溫潤透亮的晨光", "我有些沉重，想找回輕盈自在的微風", "我有些燥熱，想念山間清澈甘甜的泉水"],
            ["長時間待在冷氣房，手腳冰冷循環差", "生活忙碌常熬夜，作息不規律隨意吃", "壓力大節奏快，心神緊繃難入眠"],
            ["感覺臉龐恢復紅紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，從容自在"]]
    st.markdown(f"### {['壹','貳','參'][st.session_state.step-1]}｜探尋")
    ans = st.radio(qs[st.session_state.step-1], opts[st.session_state.step-1], index=None, label_visibility="collapsed")
    if st.button("下一步 ➔"):
        if ans: st.session_state.answers.append(ans); st.session_state.step += 1; st.rerun()

elif st.session_state.step == 4:
    choice = st.radio("### 💎 身分確認", ["是的，我是新朋友 👋", "我是老朋友 🤗"], index=None, label_visibility="collapsed")
    if st.button("開啟專屬禮遇 ➔"):
        if choice: st.session_state.is_first_time = choice; st.session_state.step = 4.5; st.rerun()

elif st.session_state.step == 4.5:
    p_list = ["首購限定組合 (40入) $1,980", "一週輕體驗組 (10入) $680"] if "新朋友" in st.session_state.is_first_time else ["老友回購組合 (40入) $1,880", "一週輕體驗組 (10入) $680"]
    p_choice = st.radio("### 🌿 陪伴方案", p_list, index=None, label_visibility="collapsed")
    if st.button("查看您的配方 ➔"):
        if p_choice:
            st.session_state.plan = p_choice
            st.session_state.step = 5 if ("新朋友" in st.session_state.is_first_time and "$1,980" in p_choice) else 6
            st.session_state.custom_name = "老朋友驚喜贈茶" if "40入" in p_choice else "輕體驗方案"; st.rerun()

elif st.session_state.step == 5:
    st.markdown("### 💎 刻名玻璃杯")
    u_name = st.text_input("雷刻文字 (最多12字)", placeholder="例如：米寶漢方")
    if st.button("查看專屬配方 ➔"):
        if u_name: st.session_state.custom_name = u_name; st.session_state.step = 6; st.rerun()

# ==========================================
# 第四步：最終結果頁 (五次校對之核心：並排、提示、無標題、一頁)
# ==========================================
elif st.session_state.step == 6:
    show_leaves()
    ans, plan, c_name, first = st.session_state.answers, st.session_state.plan, st.session_state.custom_name, st.session_state.is_first_time
    dg = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    
    # 1. 診斷卡片
    st.markdown(f"""<div style="background-color: #E9EDC9; padding: 10px; border-radius: 12px; text-align:center; border: 1px solid rgba(0,0,0,0.05);">
        <h4 style='margin:0; font-size:1rem;'>✨ 診斷結果：{dg}氣質</h4>
        <p style='margin:2px 0; font-size:0.85rem;'>{plan}</p></div>""", unsafe_allow_html=True)

    # 2. 🚀 並排輸入框 (無標題)
    col1, col2 = st.columns(2)
    with col1: o_name = st.text_input("姓名", placeholder="👤 您的姓名...", label_visibility="collapsed")
    with col2: o_phone = st.text_input("電話", placeholder="📱 聯絡電話...", label_visibility="collapsed")
    o_addr = st.text_input("地址", placeholder="📍 完整收件地址...", label_visibility="collapsed")

    # 3. 🚀 溫馨提示邏輯
    missing = []
    if not o_name: missing.append("姓名")
    if not o_phone: missing.append("電話")
    if not o_addr: missing.append("地址")
    
    if missing:
        st.markdown(f"<p style='color:#C38D5E; font-size:0.75rem; text-align:center; margin:0;'>🐢 溫馨小提醒：請補填「{'、'.join(missing)}」</p>", unsafe_allow_html=True)

    # 4. 訊息整合
    if "40入" in plan:
        m_v, a_v = ("黃耆元氣茶(14入)+金菊牛蒡茶(6入)", "當歸紅棗茶(12入)+黑豆漢方茶(8入)") if "晨光" in ans[0] else ("洛神山楂茶(12入)+金菊牛蒡茶(8入)", "玫瑰決明茶(10入)+黑豆漢方茶(10入)") if "微風" in ans[0] else ("金菊牛蒡茶(15入)+黃耆元氣茶(5入)", "玫瑰決明茶(14入)+當歸紅棗茶(6入)")
        eng = f"🌿 杯蓋刻字：{c_name}" if "新朋友" in first else "🌿 老友回購贈茶"
    else:
        m_v, a_v = ("黃耆元氣茶(4入)+金菊牛蒡茶(1入)", "當歸紅棗茶(3入)+黑豆漢方茶(2入)") if "晨光" in ans[0] else ("洛神山楂茶(3入)+金菊牛蒡茶(2入)", "玫瑰決明茶(3入)+黑豆漢方茶(2入)") if "微風" in ans[0] else ("金菊牛蒡茶(4入)+黃耆元氣茶(1入)", "玫瑰決明茶(4入)+當歸紅棗茶(1入)")
        eng = "🌿 方案：一週輕體驗組"

    info = f"👤 姓名：{o_name if o_name else '(未填)'}\n📱 電話：{o_phone if o_phone else '(未填)'}\n📍 地址：{o_addr if o_addr else '(未填)'}"
    msg = f"Hi 米寶！🐢✨\n預約：{plan}\n我是：【{dg}】\n☀️ 晨曦：{m_v}\n🌙 午後：{a_v}\n{eng}\n---\n{info}\n期待這份草本溫暖。🌿🍵"

    # 5. 代碼框與按鈕
    st.code(msg, language=None)
    st.link_button("🌿 前往 LINE@ 貼上預約資訊 ➔", "https://line.me/R/ti/p/@716osfvq", use_container_width=True)
    if st.button("重新測驗"): st.session_state.clear(); st.rerun()

st.markdown("""<div style="text-align:center; padding-top:10px;"><p style="font-size:0.6rem; color:#8B8B7A;">米寶漢方｜慶和蔘藥行研製｜© 2026 Mibao Herbal</p></div>""", unsafe_allow_html=True)
