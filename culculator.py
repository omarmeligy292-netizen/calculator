import streamlit as st

st.title("آلة حاسبة بسيطة 🧮")

num1 = st.number_input("أدخل الرقم الأول:", value=0.0)
num2 = st.number_input("أدخل الرقم الثاني:", value=0.0)

operation = st.selectbox("اختر العملية الحسابية:", ["الجمع (+)", "الطرح (-)", "الضرب (×)", "القسمة (÷)"])

if st.button("احسب النتيجة"):
    if operation == "الجمع (+)":
        result = num1 + num2
    elif operation == "الطرح (-)":
        result = num1 - num2
    elif operation == "الضرب (×)":
        result = num1 * num2
    elif operation == "القسمة (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "خطأ: لا يمكن القسمة على صفر!"
    
    st.success(f"النتيجة: {result}")