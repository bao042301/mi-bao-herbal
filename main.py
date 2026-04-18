# 引入 streamlit 套件，這是我們架設網頁的核心工具
import streamlit as st
# 引入 os 套件，用來檢查圖片檔案存不存在
import os

# 【網頁基礎設定】
# page_title: 網頁在瀏覽器分頁上顯示的名稱
# layout="centered": 讓畫面維持在正中間，不會因為螢幕太大而往兩邊擴散，適合手機版
st.set_page_config(page_title="米寶漢方｜您的植感陪伴", layout="centered")

# 【全域 CSS 樣式設定】
# 這裡使用 HTML/CSS 來強行覆蓋 Streamlit 預設的醜醜樣式
st.markdown("""
    <style>
    /* 1. 全域品牌設定 */
    * { 
        color: #4A4E31 !important; /* 所有文字預設為深橄欖綠 */
        font-family: 'Noto Sans TC', sans-serif !important; /* 強制使用思源黑體，確保質感 */
    }
    .stApp { 
        background-color: #FDFBF7 !important; /* 整個網頁的背景色：米寶專屬的暖米白色 */
    }
    
    /* 2. 容器與呼吸感 (V74 核心) */
    .block-container { 
        padding-top: 1.5rem !important; /* 畫面上方的留白，不要太擠 */
        padding-bottom: 80px !important; /* 畫面下方的留白，避免內容被頁尾擋住 */
    }

    /* 3. 隱藏系統預設的垃圾資訊 */
    #MainMenu, footer, header { 
        visibility: hidden; /* 把右上角選單、預設的頁首頁尾全部藏起來 */
    }

    /* 4. 標題與引導文字的排版 */
    h3 { 
        font-size: 1.1rem !important; font-weight: 700 !important; 
        margin: 10px 0 !important; text-align: center !important; color: #7A8450 !important; 
    }
    .question-text { 
        font-size: 1.05rem !important; font-weight: bold !important; 
        text-align: center !important; margin-bottom: 12px !important; line-height: 1.4 !important; 
    }

    /* 5. Logo 圖片大小控制 */
    [data-testid="stImage"] img { 
        max-height: 50px !important; /* 限制 Logo 最高只能 50px，才不會太大 */
        width: auto !important; margin: 0 auto !important; display: block; 
    }

    /* 6. 選項按鈕 (Radio) 的三色卡片設計 (V74 核心) */
    [data-testid="stRadio"] div[role="radiogroup"] input { display: none !important; } /* 把原本醜醜的圓形按鈕藏起來 */
    [data-testid="stRadio"] div[role="radiogroup"] { gap: 8px !important; } /* 選項之間的間距 */
    [data-testid="stRadio"] label {
        border-radius: 12px !important; padding: 10px 18px !important; /* 讓選項變成圓角矩形的卡片 */
        width: 100% !important; border: 1.5px solid rgba(0,0,0,0.05) !important;
        display: flex !important; justify-content: flex-start !important; 
        transition: all 0.2s ease !important; cursor: pointer !important; /* 加入點擊的滑順轉場動畫 */
    }

    /* 針對第 1, 2, 3 個選項分別給予 淡綠、淡橙、淡藍 的背景色 */
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(1) label { background-color: #F1F4E8 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(2) label { background-color: #FDF2E9 !important; } 
    [data-testid="stRadio"] div[role="radiogroup"] > div:nth-of-type(3) label { background-color: #EBF5FB !important; } 

    /* 7. 【重點】選中後的放大爆粗體特效 */
    div[data-testid="stRadio"] div[role="radiogroup"] div[aria-checked="true"] label {
        font-size: 1.1rem !important; /* 字體放大 */
        font-weight: 900 !important;  /* 字體極度加粗 */
        color: #2D301D !important;    /* 字體顏色變得更深 */
        border: 2.5px solid #7A8450 !important; /* 加上明顯的綠色粗邊框 */
        background-color: #E9EDC9 !important; /* 背景變成統一的鮮綠色 */
    }

    /* 8. 底部導購按鈕的動態特效 */
    .stButton > button {
        width: 100% !important; background-color: #7A8450 !important; color: #FFFFFF !important;
        border-radius: 25px !important; height: 3em !important; font-weight: bold !important; 
        border: none !important; margin-top: 10px !important; 
        transition: all 0.2s ease !important; /* 讓變色不突兀 */
    }
    .stButton > button:hover { background-color: #8B8B7A !important; } /* 滑鼠游標移過去時變灰綠色 */
    .stButton > button:active { 
        background-color: #4A4E31 !important; /* 手指按下去時變成深色 */
        transform: scale(0.98) !important; /* 按下去時縮小 0.98 倍，製造真實按壓感 */
    }

    /* 9. 森林落葉特效動畫 */
    @keyframes falling {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .leaf { 
        position: fixed; top: -10vh; font-size: 18px; pointer-events: none; /* 讓落葉不能被點擊，才不會干擾操作 */
        z-index: 9999; animation: falling 12s linear infinite; /* 動畫持續 12 秒，不斷循環 */
    }
    </style>
    """, unsafe_allow_html=True)
