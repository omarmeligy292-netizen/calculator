import streamlit as st

# إعدادات الصفحة والتصميم المظلم
st.set_page_config(page_title="آلة حاسبة مظلمة", layout="centered")

# إضافة كود CSS مخصص لضبط ألوان الأزرار والخلفية لتطابق التصميم المظلم
st.markdown("""
    <style>
    /* تغيير لون خلفية التطبيق */
    .stApp {
        background-color: #0d1117;
    }
    /* تنسيق شاشة العرض */
    .calc-display {
        background-color: #0d1117;
        color: #ffffff;
        font-size: 2.5rem;
        text-align: right;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #21262d;
        margin-bottom: 20px;
        font-family: monospace;
    }
    /* تنسيق أزرار الآلة الحاسبة */
    div.stButton > button {
        background-color: #21262d !important;
        color: #ffffff !important;
        border: none !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        padding: 20px 0px !important;
        width: 100% !important;
        border-radius: 8px !important;
        transition: background 0.2s;
    }
    div.stButton > button:hover {
        background-color: #30363d !important;
        color: #ffffff !important;
    }
    div.stButton > button:active {
        background-color: #3f4650 !important;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التطبيق (Session State) لتخزين النص الحالي
if "expression" not in st.session_state:
    st.session_state.expression = ""

# دوال التحكم بالآلة الحاسبة باستخدام دوال عادية بدلاً من Lambda لتجنب مشاكل التحديث
def press(char):
    st.session_state.expression += str(char)

def clear():
    st.session_state.expression = ""

def backspace():
    st.session_state.expression = st.session_state.expression[:-1]

def calculate():
    try:
        # استبدال العلامات ليفهمها البايثون أثناء الحساب
        expr = st.session_state.expression.replace('×', '*').replace('÷', '/')
        if expr:
            st.session_state.expression = str(eval(expr))
    except:
        st.session_state.expression = "Error"

# عرض الشاشة (إذا كانت فارغة تعرض 0)
display_text = st.session_state.expression if st.session_state.expression else "0"
st.markdown(f'<div class="calc-display">{display_text}</div>', unsafe_allow_html=True)

# تقسيم الأزرار إلى صفوف وأعمدة مع ربطها بالدوال مباشرة
buttons = [
    [("AC", clear), ("(", lambda: press("(")), ("%", lambda: press("%")), ("÷", lambda: press("/"))],
    [("7", lambda: press("7")), ("8", lambda: press("8")), ("9", lambda: press("9")), ("×", lambda: press("*"))],
    [("4", lambda: press("4")), ("5", lambda: press("5")), ("6", lambda: press("6")), ("-", lambda: press("-"))],
    [("1", lambda: press("1")), ("2", lambda: press("2")), ("3", lambda: press("3")), ("+", lambda: press("+"))],
    [("0", lambda: press("0")), (".", lambda: press(".")), ("⌫", backspace), ("=", calculate)]
]

# رسم الأزرار داخل واجهة Streamlit باستخدام ترقيم فريد وصحيح للـ key يمنع حدوث ValueError
for row_idx, row in enumerate(buttons):
    cols = st.columns(4)
    for col_idx, (label, action) in enumerate(row):
        with cols[col_idx]:
            # استخدام row_idx و col_idx يضمن صناعة معرف فريد لكل زر على حدة
            st.button(label, key=f"btn_r{row_idx}_c{col_idx}", on_click=action)
