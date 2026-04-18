# ==========================================
# 第一步：環境設定與 CSS 視覺靈魂 (裝潢與地基)
# ==========================================
import streamlit as st  # 引入架設網頁的核心工具
import os               # 引入檢查檔案的工具 (用來確認 Logo 圖片在不在)

# 設定瀏覽器分頁的標題，以及將網頁限制在正中間 (適合手機觀看)
st.set_page_config(page_title="米寶漢方｜您的植感陪伴", layout="centered")

# 寫入 CSS 語法，覆蓋掉系統預設的醜樣式，換成妳最愛的 V74 美學
st.markdown("""
    <style>
    /* 全域設定：所有文字變成深橄欖綠色，強制使用思源黑體 */
    * { color: #4A4E31 !important; font-family: 'Noto Sans TC', sans-serif !important; }
    /* 整個網頁的背景色：米寶的暖米白 */
    .stApp { background-color: #FDFBF7 !important; }
    
    /* 容器間距：保留 V74 舒適的上下呼吸空間，不會太擠 */
    .block-container { padding-top: 1.5rem !important; padding-bottom: 80px !important; }

    /* 標題與引導語的字體大小與顏色設定 */
    h3 { font-size: 1.1rem !important; font-weight: 700 !important; margin: 10px 0 !important; text-align: center !important; color: #7A8450 !important; }
    .question-text { font-size: 1.05rem !important; font-weight: bold !important; text-align: center !important; margin-bottom: 12px !important; line-height: 1.4 !important; }
    .quote { font-style: italic; color: #8B8B7A !important; text-align: center; margin-bottom: 15px !important; font-size: 0.8rem !important; }

    /* 控制頂部 Logo 圖片大小，不要超過 50px */
    [data-testid="stImage"] img { max-height: 50px !important; width: auto !important; margin: 0 auto !important; display: block; }
    [data-testid="stImage"] { margin-bottom: 5px !important; }

    /* 【V74 核心】選項卡片的設計：隱藏醜醜圓點，加上圓角、邊框與間距 */
    [data-testid="stRadio"] div[role="radiogroup"] input { display: none !important; }
    [data-testid="stRadio"] div[role="radiogroup"] { gap: 8px !important; } 
    [data-testid="stRadio"] label {
        border-radius: 12px !important; padding: 10px 18px !important;
        width: 100% !important; border: 1.5px solid rgba(0,0,0,0.05) !important;
        display: flex !important; justify-content: flex-start !important; 
        text-align: left !important; transition: all 0.2s ease !important; cursor: pointer !important;
        font-size: 0.95rem !important; line-height: 1.4 !important;
    }

    /* 為第一、二、三個選項分別設定 淡綠、淡橙、淡藍的網底 */
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(1) label { background-color: #F1F4E8 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(2) label { background-color: #FDF2E9 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(3) label { background-color: #EBF5FB !important; } 

    /* 【V74 核心】當選項被「選中」時，字體瞬間放大 (1.1rem) 並加粗 (900)，外框變粗變綠 */
    div[data-testid="stRadio"] div[role="radiogroup"] div[aria-checked="true"] label {
        font-size: 1.1rem !important; font-weight: 900 !important;   
        color: #2D301D !important; border: 2.5px solid #7A8450 !important;
        background-color: #E9EDC9 !important;
    }

    /* 底部橄欖綠按鈕設計：包含長度、圓角，以及點擊時的「變色微縮」觸感特效 */
    .stButton > button {
        width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important;
        border-radius: 25px !important; height: 3em !important; font-weight: bold !important; border: none !important;
        margin-top: 10px !important; transition: all 0.2s ease !important;
    }
    .stButton > button p { color: #FFFFFF !important; font-size: 1rem !important; }
    .stButton > button:hover { background-color: #8B8B7A !important; } /* 滑過去變灰綠 */
    .stButton > button:active { background-color: #4A4E31 !important; transform: scale(0.98) !important; } /* 按下去變深且縮小 */

    /* 溫暖提示語 (沒選選項時跑出來的文字) 的樣式 */
    .warm-tip { font-size: 0.85rem !important; color: #B08968 !important; text-align: center !important; margin-top: 5px !important; font-weight: bold !important; }

    /* 防深色模式干擾：強制把最後的複製文字框變成白底綠框 */
    [data-testid="stCodeBlock"], [data-testid="stCodeBlock"] > div, pre, code {
        background-color: #F8F9F1 !important; border: 1px solid #E9EDC9 !important; border-radius: 12px !important;
    }
    .price-text { font-size: 1.45rem !important; font-weight: bold !important; color: #7A8450 !important; margin-top: 15px; display: block; text-align: center !important; }

    /* 森林落葉的動畫語法 */
    @keyframes falling {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .leaf { position: fixed; top: -10vh; font-size: 18px; pointer-events: none; z-index: 9999; animation: falling 12s linear infinite; }

    /* 隱藏網頁預設的頂部選單和底部浮水印 */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)


# ==========================================
# 第二步：系統記憶 (Session State) 與頂部佈置
# ==========================================

# 定義一個呼叫落葉特效的函數
def show_leaves():
    leaves_html = "".join([f'<div class="leaf" style="left:{i*15}vw; animation-delay:{i*1.5}s;">🍃</div>' for i in range(7)])
    st.markdown(leaves_html, unsafe_allow_html=True)

# 系統記憶體：用來記住客人現在走到第幾步 (step)、選了什麼 (answers)
for key in ['step', 'answers', 'custom_name', 'is_first_time', 'plan', 'warn']:
    if key not in st.session_state:
        if key == 'step': st.session_state[key] = 1 # 預設從第 1 步開始
        elif key == 'answers': st.session_state[key] = []
        else: st.session_state[key] = ""

# 放置頂部 Logo：如果有圖就放圖，沒圖就放文字
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)
else: st.markdown("<h4 style='text-align:center;'>🌿 米寶漢方</h4>", unsafe_allow_html=True)
# 放置固定在每頁最上面的溫暖引言
st.markdown('<p class="quote">「在忙碌中，給您留一刻鐘的溫暖。」</p>', unsafe_allow_html=True)


# ==========================================
# 第三步：測驗引擎 (第 1 ~ 3 步)
# ==========================================
# 如果現在是前 3 步，就顯示對應的測驗題
if st.session_state.step <= 3:
    # 題庫設定
    qs = ["當您靜下心，您的身體正低聲說著...？", "關於這段日子的作息，您的狀態是...？", "在最需要喘息的午後，您想感受到的是...？"]
    opts = [
        ["我有些疲累，渴望溫潤透亮的晨光", "我有些沉重，想找回輕盈自在的微風", "我有些燥熱，想念山間清澈甘甜的泉水"],
        ["長時間待在冷氣房，手腳冰冷循環差", "生活忙碌常熬夜，作息不規律隨意吃", "壓力大節奏快，心神緊繃難入眠"],
        ["感覺臉龐恢復紅潤元氣，重新出發", "感覺身體找回輕盈律動，不再束縛", "感覺內心恢復安靜穩定，從容自在"]
    ]
    # 動態按鈕文字與溫柔防呆提示語
    btns = ["緩緩走向下一步 ➔", "傾聽日常的節奏 ➔", "遇見您的專屬植感陪伴 ➔"]
    warns = ["🌿 請先聽聽身體的聲音，再告訴米寶喔。", "☕️ 沒關係，深呼吸，選一個最接近您的狀態吧。", "✨ 您的嚮往對米寶很重要，請讓我們知道您的心情。"]
    
    # 顯示題目
    st.markdown(f"### 第 {st.session_state.step} 步")
    st.markdown(f'<p class="question-text">{qs[st.session_state.step-1]}</p>', unsafe_allow_html=True)
    # 顯示選項
    ans = st.radio("", opts[st.session_state.step-1], index=None, key=f"q{st.session_state.step}", label_visibility="collapsed")
    
    # 判斷按鈕是否被按下
    if st.button(btns[st.session_state.step-1]):
        if ans: # 如果有選選項，記錄答案並進入下一步
            st.session_state.answers.append(ans)
            st.session_state.step += 1
            st.session_state.warn = ""
            st.rerun() # 重新整理網頁以顯示下一頁
        else: # 如果沒選選項，觸發警告提示
            st.session_state.warn = warns[st.session_state.step-1]
    
    # 如果有警告，顯示出溫暖的提示文字
    if st.session_state.warn:
        st.markdown(f'<p class="warm-tip">{st.session_state.warn}</p>', unsafe_allow_html=True)


# ==========================================
# 第四步：商業邏輯與防呆 (第 4 ~ 5 步：新老朋友與方案)
# ==========================================
elif st.session_state.step == 4:
    # 詢問是否為新朋友
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
    # 邏輯判斷：新朋友看 1980，老朋友看 1880
    if "新朋友" in st.session_state.is_first_time:
        p_list = ["首購限定組合 (40入) $1,980", "一週輕體驗組 (10入) $680"]
    else:
        p_list = ["老友回購組合 (40入) $1,880", "一週輕體驗組 (10入) $680"]
        
    p_choice = st.radio("", p_list, index=None, key="plan_v115", label_visibility="collapsed")
    if st.button("查看您的專屬配比 ➔"):
        if p_choice:
            st.session_state.plan = p_choice
            # 【關鍵邏輯】只有新朋友選 $1,980，才會去第 5 步填寫雷刻文字
            if "新朋友" in st.session_state.is_first_time and "$1,980" in p_choice: st.session_state.step = 5
            else: st.session_state.custom_name = "老友回購禮遇" if "40入" in p_choice else "植感體驗方案"; st.session_state.step = 6
            st.session_state.warn = ""; st.rerun()
        else: st.session_state.warn = "🥣 請選擇一個組合，讓溫暖精準送達。"
    if st.session_state.warn: st.markdown(f'<p class="warm-tip">{st.session_state.warn}</p>', unsafe_allow_html=True)

elif st.session_state.step == 5:
    # 填寫隨行杯雷刻文字
    st.markdown("### 💎 鐫刻您的專屬風格")
    st.markdown("<div style='background-color: #FFFFFF; padding: 15px; border-radius: 12px; border: 1px solid #E9EDC9; font-size:0.95rem; text-align:center;'>為您準備一只質感的玻璃隨行杯。<br>木蓋上將鐫刻您的專屬風格。<br>陪伴您渡過植感健康每一天。</div>", unsafe_allow_html=True)
    u_name = st.text_input("雷刻文字 (最多12字)", max_chars=12, placeholder="例如：米寶漢方")
    if st.button("查看您的專屬配方 ➔"):
        if u_name: st.session_state.custom_name = u_name; st.session_state.step = 6; st.rerun()


# ==========================================
# 第五步：最終結帳與跳轉 (第 6 ~ 7 步：植感卡片與 LINE 預約)
# ==========================================
elif st.session_state.step == 6:
    show_leaves() # 呼叫落葉特效
    ans, plan, name, first = st.session_state.answers, st.session_state.plan, st.session_state.custom_name, st.session_state.is_first_time
    
    # 決定顯示的最終價格
    price_val = "$1,980" if "$1,980" in plan else "$1,880" if "$1,880" in plan else "$680"
    
    # 根據用戶第一步的答案，分配相對應的茶包比例
    if "40入" in plan:
        amt_t = "40 入深度植感漢方茶組"
        m_t, a_t = ("黃耆元氣茶 (14入) + 金菊牛蒡茶 (6入)", "當歸紅棗茶 (12入) + 黑豆漢方茶 (8入)") if "晨光" in ans[0] else ("洛神山楂茶 (12入) + 金菊牛蒡茶 (8入)", "玫瑰決明茶 (10入) + 黑豆漢方茶 (10入)") if "微風" in ans[0] else ("金菊牛蒡茶 (15入) + 黃耆元氣茶 (5入)", "玫瑰決明茶 (14入) + 當歸紅棗茶 (6入)")
        gift = f"• 首購禮：專屬刻名隨行杯 ({name})" if "新朋友" in first else "• 老朋友禮：加贈驚喜茶包 3 包"
    else:
        amt_t = "10 入一週輕體驗茶組"
        m_t, a_t = ("黃耆元氣茶 (4入) + 金菊牛蒡茶 (1入)", "當歸紅棗茶 (3入) + 黑豆漢方茶 (2入)") if "晨光" in ans[0] else ("洛神山楂茶 (3入) + 金菊牛蒡茶 (2入)", "玫瑰決明茶 (3入) + 黑豆漢方茶 (2入)") if "微風" in ans[0] else ("金菊牛蒡茶 (4入) + 黃耆元氣茶 (1入)", "玫瑰決明茶 (4入) + 當歸紅棗茶 (1入)")
        gift = "• 體驗方案：初探草本植感相遇"
    
    # 診斷結果氣質
    dg = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    
    # 畫出最終配方卡片 (使用自定義 HTML 以防黑化)
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
    show_leaves() # 呼叫落葉特效
    ans, plan, name, first = st.session_state.answers, st.session_state.plan, st.session_state.custom_name, st.session_state.is_first_time
    dg = "暖陽系" if "晨光" in ans[0] else "微風系" if "微風" in ans[0] else "清泉系"
    
    # 準備給客戶複製的純文字訊息 (換行、全名、確保不漏字)
    if "40入" in plan:
        m_v, a_v = ("黃耆元氣茶(14)+金菊牛蒡茶(6)", "當歸紅棗茶(12)+黑豆漢方茶(8)") if "晨光" in ans[0] else ("洛神山楂茶(12)+金菊牛蒡茶(8)", "玫瑰決明茶(10)+黑豆漢方茶(10)") if "微風" in ans[0] else ("金菊牛蒡茶(15)+黃耆元氣茶(5)", "玫瑰決明茶(14)+當歸紅棗茶(6)")
        eng = f"🌿 杯蓋刻字：{name}" if "新朋友" in first else "🌿 老友回購贈茶"
    else:
        m_v, a_v = ("黃耆元氣茶(4)+金菊牛蒡茶(1)", "當歸紅棗茶(3)+黑豆漢方茶(2)") if "晨光" in ans[0] else ("洛神山楂茶(3)+金菊牛蒡茶(2)", "玫瑰決明茶(3)+黑豆漢方茶(2)") if "微風" in ans[0] else ("金菊牛蒡茶(4)+黃耆元氣茶(1)", "玫瑰決明茶(4)+當歸紅棗茶(1)")
        eng = "🌿 方案：一週輕體驗組"

    msg = f"Hi 米寶！🐢✨\n預約：{plan}\n我是：【{dg}】\n☀️ 晨：{m_v}\n🌙 午：{a_v}\n{eng}\n期待這份草本溫暖。🌿🍵"
    
    st.markdown('<p style="font-size:0.9rem; text-align:center; margin-bottom:5px;">點擊☆右上角☆複製後貼給米寶：</p>', unsafe_allow_html=True)
    st.code(msg, language=None) # 顯示複製框
    
    # 【核心跳轉修正】使用 LINE 官方萬用跳轉連結，防止內建瀏覽器攔截
    line_url = "https://line.me/R/ti/p/@716osfvq"
    st.markdown(f'''<a href="{line_url}" target="_top" style="text-decoration:none;"><div style="background-color: #06C755; color: white; text-align: center; padding: 14px; border-radius: 15px; font-weight: bold; font-size: 1rem; transition: background-color 0.2s;">🌿 前往 LINE@ 貼上專屬配方與米寶相遇吧！ ➔</div></a>''', unsafe_allow_html=True)
    
    if st.button("重新探索"): st.session_state.clear(); st.rerun()

# 網頁最底部的固定宣告語
st.markdown("""<div class="custom-footer"><p class="footer-text">米寶漢方｜慶和蔘藥行研製｜© 2026 Mibao Herbal</p></div>""", unsafe_allow_html=True)
