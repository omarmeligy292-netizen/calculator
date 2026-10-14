import tkinter as tk

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("آلة حاسبة")
root.geometry("360x480")
root.configure(bg="#0d1117")  # الخلفية الداكنة الخارجية

# متغير لتخزين النص الحالي في الحاسبة
expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        # استبدال الرموز لكي تفهمها لغة بايثون أثناء الحساب
        total = str(eval(expression.replace('×', '*').replace('÷', '/')))
        equation.set(total)
        expression = total
    except:
        equation.set(" Error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("0")

def backspace():
    global expression
    expression = expression[:-1]
    if expression == "":
        equation.set("0")
    else:
        equation.set(expression)

# متغير نصي لتحديث الشاشة ديناميكياً
equation = tk.StringVar()
equation.set("0")

# شاشة العرض (Display)
display = tk.Entry(
    root, 
    textvariable=equation, 
    font=('Segoe UI', 24), 
    bg="#0d1117", 
    fg="#ffffff", 
    bd=0, 
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=25, padx=20, pady=20, sticky="nsew")

# إعدادات الأزرار (النص، السطر، العمود)
buttons = [
    ('AC', 1, 0), ('(', 1, 1), ('%', 1, 2), ('÷', 1, 3),
    ('7', 2, 0),  ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
    ('4', 3, 0),  ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0),  ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0),  ('.', 5, 1), ('⌫', 5, 2), ('=', 5, 3)
]

# تنسيق الألوان للأزرار بناءً على نوعها
for (text, row, col) in buttons:
    if text == '=':
        action = equalpress
    elif text == 'AC':
        action = clear
    elif text == '⌫':
        action = backspace
    else:
        action = lambda x=text: press(x)
        
    # تحديد ألوان الخلفية والنص بناءً على تصميم الصورة
    bg_color = "#21262d" # لون الأزرار الافتراضي الداكن
    fg_color = "#ffffff"
    
    # إنشاء الزر وضبط خصائصه
    btn = tk.Button(
        root, 
        text=text, 
        font=('Segoe UI', 14, 'bold'),
        bg=bg_color, 
        fg=fg_color, 
        activebackground="#30363d", 
        activeforeground="#ffffff",
        bd=0, 
        relief="flat",
        command=action
    )
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# ضبط تمدد الصفوف والأعمدة لكي تتناسب الأزرار عند تكبير النافذة
root.grid_rowconfigure(0, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# تشغيل البرنامج
root.mainloop()
