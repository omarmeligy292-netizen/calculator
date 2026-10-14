import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="آلة حاسبة مظلمة", layout="centered")

# كود CSS مكثف وصارم لإجبار الأزرار والصفوف على الاندماج وتطابق أبعاد الصورة
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق الإجمالية */
    .stApp {
        background-color: #0b0f17;
    }
    
    /* تحديد عرض الحاوية بالكامل لتبدو كآلة حاسبة ملمومة */
    [data-testid="stMainBlockContainer"] {
        max-width: 400px !important;
        padding-top: 5rem !important;
        margin: auto !important;
    }
    
    /* شاشة العرض العليا */
    .calc-display {
        background-color: #0b0f17;
        color: #ffffff;
        font-size: 3rem;
        text-align: right;
        padding: 20px 15px;
        border-radius: 8px;
        border: 1px solid #1f242c;
        margin-bottom: 10px;
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* تصفير المسافات تماماً بين الصفوف البرمجية */
    [data-testid="stVerticalBlock"] {
        gap: 0px !important;
    }
    
    /* تصفير المسافات تماماً بين الأعمدة في الصف الواحد */
    [data-testid="stHorizontalBlock"] {
        gap: 8px !important;
        margin-bottom: 8px !important;
    }
    
    /* تصفير الحشو الخاص بكل عمود */
    [data-testid="column"] {
        padding: 0px !important;
        width: 100% !important;
    }
    
    /* تحويل الأزرار إلى مربعات عريضة وممتلئة */
    div.stButton > button {
        background-color: #161b22 !important;
        color: #ffffff !important;
        border: none !important;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        height: 75px !important;  /* تحديد طول ثابت ومناسب للزر */
        width: 100% !important;   /* إجبار الزر على ملء كامل عرض العمود */
        border-radius: 8px !important;
        margin: 0px !important;
        padding: 0px !important;
        transition: background-color 0.1s ease;
    }
    
    /* تأثير تمرير الفأرة والضغط */
    div.stButton > button:hover {
        background-color: #21262d !important;
        border: none !important;
        color: #ffffff !important;
    }
    div.stButton > button:active {
        background-color: #30363d !important;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التطبيق (Session State) لتخزين النص الحالي
if "expression" not in st.session_state:
    st.session_state.expression = ""

def press(char):
    st.session_state.expression += str(char)

def clear():
    st.session_state.expression = ""

def backspace():
    st.session_state.expression = st.session_state.expression[:-1]

def calculate():
    try:
        expr = st.session_state.expression.replace('×', '*').replace('÷', '/')
        if expr:
            st.session_state.expression = str(eval(expr))
    except:
        st.session_state.expression = "Error"

# عرض الشاشة (إذا كانت فارغة تعرض 0)
display_text = st.session_state.expression if st.session_state.expression else "0"
st.markdown(f'<div class="calc-display">{display_text}</div>', unsafe_allow_html=True)

# مصفوفة الأزرار والرموز
buttons = [
    [("AC", clear), ("(", lambda: press("(")), ("%", lambda: press("%")), ("÷", lambda: press("/"))],
    [("7", lambda: press("7")), ("8", lambda: press("8")), ("9", lambda: press("9")), ("×", lambda: press("*"))],
    [("4", lambda: press("4")), ("5", lambda: press("5")), ("6", lambda: press("6")), ("-", lambda: press("-"))],
    [("1", lambda: press("1")), ("2", lambda: press("2")), ("3", lambda: press("3")), ("+", lambda: press("+"))],
    [("0", lambda: press("0")), (".", lambda: press(".")), ("⌫", backspace), ("=", calculate)]
]

# رسم الأزرار
for row_idx, row in enumerate(buttons):
    cols = st.columns(4)
    for col_idx, (label, action) in enumerate(row):
        with cols[col_idx]:
            st.button(label, key=f"btn_r{row_idx}_c{col_idx}", on_click=action)
