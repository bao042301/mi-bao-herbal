import streamlit as st
import os

# ==========================================
# 第一步：視覺靈魂 (精準對抗深色模式，保護字體)
# ==========================================
st.set_page_config(page_title="米寶漢方｜植感氣質測驗", layout="centered")

st.markdown("""
    <style>
    /* 1. 全局淺色底與深綠字 */
    .stApp, header { background-color: #FDFBF7 !important; }
    p, h1, h2, h3, h4, h5, h6, label, li, span { 
        font-family: 'Noto Sans TC', sans-serif !important; 
        color: #4A4E31 !important; 
    }
    .block-container { padding-top: 1.5rem !important; padding-bottom: 90px !important; }

    /* 2. 測驗選項按鈕 (小烏龜) */
    [data-testid="stRadio"] div[role="radiogroup"] label {
        border-radius: 12px !important; padding: 12px 18px !important;
        width: 100% !important; border: 1.5px solid rgba(0,0,0,0.05) !important;
        display: flex !important; transition: all 0.2s ease !important;
    }
    [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
        border: 2.5px solid #7A8450 !important; background-color: #E9EDC9 !important; font-weight: bold;
    }
    [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) > div:first-of-type::after { 
        content: '🐢' !important; margin-left: 8px;
    }

    /* 3. 輸入框樣式 (強制白底綠字) */
    div[data-baseweb="input"], div[data-baseweb="base-input"] { 
        background-color: #FFFFFF !important; 
        border: 1.5px solid #E9EDC9 !important; 
        border-radius: 8px !important; 
    }
    input { 
        background-color: #FFFFFF !important; 
        color: #4A4E31 !important; 
        -webkit-text-fill-color: #4A4E31 !important; 
    }

    /* 4. LINE 按鈕 */
    [data-testid="stLinkButton"] a {
        width: 100% !important; background-color: #06C755 !important; border-radius: 15px !important; height: 3.2em !important; 
        display: flex !important; justify-content: center !important; align-items: center !important;
    }
    [data-testid="stLinkButton"] a p { color: #FFFFFF !important; -webkit-text-fill-color: #FFFFFF !important; font-weight: 900 !important; }

    /* 5. 抹茶綠複製框 */
    [data-testid="stCodeBlock"] { background-color: #8A9A65 !important; border-radius: 12px !important; }
    [data-testid="stCodeBlock"] * { color: #FDFBF7 !important; -webkit-text-fill-color: #FDFBF7 !important; font-family: 'Noto Sans TC' !important; }

    /* 6. 頁尾 */
    .custom-footer { position: fixed; left: 0; bottom: 0; width: 100vw; text-align: center; background-color: #FDFBF7; padding: 8px 0; z-index: 9999; border-top: 1px solid #E9EDC9; }
    #MainMenu, footer, header { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 第二步：測驗邏輯
# ==========================================
img_path = "29301.jpg"
if os.path.exists(img_path): st.image(img_path)

st.markdown("<h3 style='text-align:center;'>🌿 尋找您的植感氣質</h3>", unsafe_allow_html=True)

questions = [
    ("1. 忙碌了一整天，您最嚮往的放鬆時刻是？", ["在陽台澆水，看著植物發芽", "窩在沙發閱讀，配一杯熱茶", "在大自然漫步，呼吸芬多精"]),
    ("2. 如果有一種氣味能代表今天的您，那是？", ["暖陽曬過的乾爽棉花", "微風帶來的清甜花香", "雨後清泉的冷冽草木"]),
    ("3. 在與人互動時，朋友最常形容您是？", ["像太陽一樣充滿活力與溫潤", "像微風一樣體貼且細膩", "像清泉一樣冷靜且獨立"])
]

scores = []
for i, (q, options) in enumerate(questions):
    ans = st.radio(q, options, index=None, key=f"q{i}")
    if ans:
        scores.append(options.index(ans))

if len(scores) == len(questions):
    total = sum(scores)
    
    # 診斷結果
    if total <= 2:
        res, tea = "暖陽系氣質", "暖陽茶組 (黃耆金菊/當歸黑豆)"
    elif total <= 5:
        res, tea = "微風系氣質", "微風茶組 (洛神金菊/玫瑰黑豆)"
    else:
        res, tea = "清泉系氣質", "清泉茶組 (金菊黃耆/玫瑰當歸)"

    st.markdown(f"""
    <div style='background-color:#E9EDC9; padding:20px; border-radius:15px; margin-top:20px; text-align:center;'>
        <h4 style='margin:0;'>您的診斷結果：<b>{res}</b></h4>
        <p style='margin-top:10px;'>最適合您的專屬配方是：<br><b>{tea}</b></p>
    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # 第三步：新增訂購人資訊 (此次更新重點)
    # ==========================================
    st.markdown("<br><h4 style='text-align:center;'>🛍️ 預約我的植感配方</h4>", unsafe_allow_html=True)
    
    name = st.text_input("👤 訂購人姓名", placeholder="請輸入姓名...")
    phone = st.text_input("📱 聯絡電話", placeholder="請輸入電話...")
    address = st.text_input("📍 收件地址", placeholder="請輸入地址...")

    if st.button("生成預約明細 ➔"):
        if name and phone and address:
            msg = f"Hi 米寶！🐢✨\n我完成氣質測驗囉！\n---\n🔮 測驗結果：{res}\n🍵 專屬配方：{tea}\n---\n👤 姓名：{name}\n📱 電話：{phone}\n📍 地址：{address}\n---\n我想預約「首購深度方案(40入)」，請幫我確認訂單。🌿"
            
            st.markdown("<p style='text-align:center; font-size:0.9rem;'>點擊右上方複製訂單：</p>", unsafe_allow_html=True)
            st.code(msg, language=None)
            
            st.link_button("🌿 前往 LINE@ 貼上預約資訊", "https://line.me/R/ti/p/@716osfvq")
        else:
            st.warning("🐢 記得幫米寶填寫完整的姓名、電話與地址喔！")

st.markdown("""<div class="custom-footer"><p style="font-size:0.65rem; color:#8B8B7A; margin:0;">米寶漢方｜植感日常｜© 2026 Mibao Herbal</p></div>""", unsafe_allow_html=True)
