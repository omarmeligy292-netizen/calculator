import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="آلة حاسبة مظلمة", layout="centered")

# كود واجهة الآلة الحاسبة مع معالجة ذكية للأقواس في زر واحد
calculator_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: #0b0f17;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 90vh;
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .calculator {
            background-color: #161b22;
            padding: 20px;
            border-radius: 12px;
            width: 340px;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
            border: 1px solid #21262d;
        }
        .display {
            background-color: #0b0f17;
            color: #ffffff;
            font-size: 2.5rem;
            text-align: right;
            padding: 20px 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            min-height: 50px;
            word-wrap: break-word;
            word-break: break-all;
            border: 1px solid #21262d;
        }
        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
        }
        .btn {
            background-color: #21262d;
            color: #ffffff;
            border: none;
            font-size: 1.3rem;
            font-weight: 600;
            height: 70px;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.15s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .btn:hover {
            background-color: #30363d;
        }
        .btn:active {
            background-color: #3f4650;
        }
    </style>
</head>
<body>

    <div class="calculator">
        <div class="display" id="display">0</div>
        <div class="buttons">
            <button class="btn" onclick="clearDisplay()">AC</button>
            <button class="btn" onclick="smartParenthesis()">()</button>
            <button class="btn" onclick="append('%')">%</button>
            <button class="btn" onclick="append('/')">÷</button>

            <button class="btn" onclick="append('7')">7</button>
            <button class="btn" onclick="append('8')">8</button>
            <button class="btn" onclick="append('9')">9</button>
            <button class="btn" onclick="append('*')">×</button>

            <button class="btn" onclick="append('4')">4</button>
            <button class="btn" onclick="append('5')">5</button>
            <button class="btn" onclick="append('6')">6</button>
            <button class="btn" onclick="append('-')">-</button>

            <button class="btn" onclick="append('1')">1</button>
            <button class="btn" onclick="append('2')">2</button>
            <button class="btn" onclick="append('3')">3</button>
            <button class="btn" onclick="append('+')">+</button>

            <button class="btn" onclick="append('0')">0</button>
            <button class="btn" onclick="append('.')">.</button>
            <button class="btn" onclick="backspace()">⌫</button>
            <button class="btn" onclick="calculate()">=</button>
        </div>
    </div>

    <script>
        let currentInput = "";
        const display = document.getElementById("display");

        function updateDisplay(text) {
            let formatted = text.replace(/\\*/g, '×').replace(/\\//g, '÷');
            display.innerText = formatted || "0";
        }

        function append(value) {
            currentInput += value;
            updateDisplay(currentInput);
        }

        // دالة ذكية لتحديد هل نضع قوس فتح ( أم قوس إغلاق )
        function smartParenthesis() {
            let openCount = (currentInput.match(/\\(/g) || []).length;
            let closeCount = (currentInput.match(/\\)/g) || []).length;
            
            // إذا كان آخر رمز رقم أو قوس إغلاق، وهناك قوس مفتوح لم يغلق بعد، نضع قوس إغلاق
            if (openCount > closeCount && (!isNaN(currentInput.slice(-1)) || currentInput.slice(-1) === ')')) {
                currentInput += ")";
            } else {
                currentInput += "(";
            }
            updateDisplay(currentInput);
        }

        function clearDisplay() {
            currentInput = "";
            updateDisplay("0");
        }

        function backspace() {
            currentInput = currentInput.slice(0, -1);
            updateDisplay(currentInput);
        }

        function calculate() {
            try {
                if (!currentInput) return;
                let result = eval(currentInput);
                currentInput = result.toString();
                updateDisplay(currentInput);
            } catch (e) {
                display.innerText = "Error";
                currentInput = "";
            }
        }
    </script>
</body>
</html>
"""

components.html(calculator_html, height=550, scrolling=False)
