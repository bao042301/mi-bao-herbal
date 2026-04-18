import streamlit as st
import os

# 1. 配置與極致樣式鎖定
st.set_page_config(page_title="米寶漢方｜您的植感陪伴", layout="centered")

st.markdown("""
    <style>
    /* 全域鎖定 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    .stApp { background-color: #FDFBF7 !important; }
    .block-container { padding-top: 0.5rem !important; padding-bottom: 50px !important; }

    /* 隱藏原生組件 */
    #MainMenu, footer, header { visibility: hidden !important; }

    /* 標題比例 */
    h3 { font-size: 1.1rem !important; font-weight: 700 !important; text-align: center !important; margin: 10px 0 !important; }
    .question-text { font-size: 1rem !important; font-weight: bold !important; text-align: center !important; margin-bottom: 10px !important; }

    /* 選項點點極致微縮 */
    [data-testid="stRadioButton"] div[role="radiogroup"] [data-testid="stRadioButton"] > div:first-child { 
        transform: scale(0.5) !important; 
        margin-top: 3px !important;
    }
    [data-testid="stRadio"] label {
        border-radius: 12px !important; padding: 10px 15px !important;
        border: 1px solid rgba(0,0,0,0.05) !important; font-size: 0.9rem !important;
    }

    /* 選中後字體加粗放大 */
    div[data-testid="stRadio"] div[role="radiogroup"] div[aria-checked="true"] label {
        font-size: 1.05rem !important; font-weight: 900 !important;   
        background-color: #E9EDC9 !important; border: 2.5px solid #7A8450 !important;
    }

    /* 自定義配方框 (取代原生的 st.code) */
    .custom-recipe-box {
        background-color: #F8F9F1 !important;
        border: 1.5px solid #E9EDC9 !important;
        border-radius: 15px !important;
        padding: 15px !important;
        font-size: 0.9rem !important;
        line-height: 1.5 !important;
        white-space: pre-wrap !important; /* 自動換行 */
        word-wrap: break-word !important;
        margin-bottom: 10px !important;
    }

    /* 按鈕與 LINE 跳轉 */
    .stButton > button { width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important; border-radius: 30px !important; height: 3em !important; font-weight: bold !important; border: none !important; }
    .line-cta-button {
        display: block !important;
        background-color: #06C755 !important;
        color: white !important;
        text-align: center !important;
        padding: 15px !important;
        border-radius: 15px !important;
        text-decoration: none !important;
        font-weight: 900 !important;
        margin-top: 10px !important;
        font-size: 1rem !important;
    }

    /* 頁尾 */
    .custom-footer { position: fixed; left: 0; bottom: 8px; width: 100%; text-align: center; font-size: 0.6rem; color: #8B8B7A; }
    </style>
    """, unsafe_allow_html=True)

# ----------------- 邏輯初始化 -----------------
if 'step' not in st.session_state: st.session_state.step = 1
if 'answers' not in st.session_state: st.session_state.answers = []
if 'bundle' not in st.session_state: st.session_state.bundle = ""
if 'engraving' not in st.session_state: st.session_state.engraving = ""

# 頂部 Logo
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)

# ----------------- 流程控制 -----------------
if st.session_state.step <= 3:
    questions = [
        {"q": "當您靜下心，您的身體正低聲說著...？", "opts": ["我有些疲累，渴望溫潤透亮的晨光", "我有些沉重，想找回輕盈自在的微風", "我有些燥熱，想念山間清澈甘甜的泉水"]},
        {"q": "關於這段日子的作息，您的狀態是...？", "opts": ["長時間待在冷氣房，手腳冰冷循環差", "生活忙碌常熬夜，作息不規律隨意吃", "壓力大節奏快，心神緊繃難入眠"]},
        {"q": "在最需要喘息的午後，您想感受到的是...？", "opts": ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，從容自在"]}
    ]
    curr = questions[st.session_state.step - 1]
    st.markdown(f"### 第 {st.session_state.step} 步")
    st.markdown(f'<p class="question-text">{curr["q"]}</p>', unsafe_allow_html=True)
    ans = st.radio("", curr["opts"], index=None, key=f"q{st.session_state.step}", label_visibility="collapsed")
    if st.button("繼續 ➔"):
        if ans: 
            st.session_state.answers.append(ans)
            st.session_state.step += 1
            st.rerun()

elif st.session_state.step == 4:
    st.markdown("### ✨ 選擇您的專屬陪伴方案")
    bundles = ["首購組 $1,980 (贈：刻名隨行杯)", "老友組 $1,880 (贈：驚喜茶包 3 入)", "體驗組 $680 (一週輕體驗)"]
    choice = st.radio("", bundles, index=None, key="bundle_select", label_visibility="collapsed")
    eng = ""
    if choice == bundles[0]:
        eng = st.text_input("雷刻文字 (12字內)", placeholder="例如：Mila")
    if st.button("查看測驗結果 ➔"):
        if choice:
            st.session_state.bundle = choice
            st.session_state.engraving = eng
            st.session_state.step = 5
            st.rerun()

elif st.session_state.step == 5:
    ans, bundle, eng = st.session_state.answers, st.session_state.bundle, st.session_state.engraving
    diag = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    
    # 配比邏輯
    if "$680" in bundle:
        m_t, a_t = ("黃耆元氣茶(4)+金菊牛蒡茶(1)", "當歸紅棗茶(3)+黑豆漢方茶(2)") if diag=="暖陽系" else ("洛神山楂茶(3)+金菊牛蒡茶(2)", "玫瑰決明茶(3)+黑豆漢方茶(2)") if diag=="微風系" else ("金菊牛蒡茶(4)+黃耆元氣茶(1)", "玫瑰決明茶(4)+當歸紅棗茶(1)")
        gift = "體驗方案"
    else:
        m_t, a_t = ("黃耆元氣茶(14)+金菊牛蒡茶(6)", "當歸紅棗茶(12)+黑豆漢方茶(8)") if diag=="暖陽系" else ("洛神山楂茶(12)+金菊牛蒡茶(8)", "玫瑰決明茶(10)+黑豆漢方茶(10)") if diag=="微風系" else ("金菊牛蒡茶(15)+黃耆元氣茶(5)", "玫瑰決明茶(14)+當歸紅棗茶(6)")
        gift = f"雷刻杯：{eng}" if "$1,980" in bundle else "老友禮：加贈 3 包茶包"

    st.markdown(f"### ✨ 您是：{diag}氣質")
    recipe_msg = f"Hi 米寶！🐢✨\n預約組合：{bundle}\n☀️ 晨：{m_t}\n🌙 午：{a_t}\n🌿 備註：{gift}\n期待草本的溫暖。"
    
    # 這裡使用 HTML 容器取代 st.code，徹底解決黑底與左右滑動問題
    st.markdown(f'<div class="custom-recipe-box">{recipe_msg}</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:center; font-size:0.8rem;">長按上方框框文字即可全選複製</p>', unsafe_allow_html=True)
    
    # LINE@ 強效按鈕
    st.markdown(f'<a href="https://line.me/R/ti/p/@716osfvq" target="_blank" class="line-cta-button">🌿 前往 LINE@ 貼上配方預約 ➔</a>', unsafe_allow_html=True)
    
    if st.button("重新探索"):
        st.session_state.clear()
        st.rerun()

st.markdown('<div class="custom-footer">慶和蔘藥行監製｜本產品屬一般食品。 © 2026 Mibao Herbal</div>', unsafe_allow_html=True)
