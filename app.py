from flask import Flask, render_template_string

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Gửi Phương Anh</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #fff0f5;
            color: #333;
            text-align: center;
            padding: 50px;
        }
        .container {
            max-width: 700px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
        }
        h1 {
            color: #ff69b4;
        }
        p {
            font-size: 1.2em;
            line-height: 1.6;
        }
        .footer {
            margin-top: 40px;
            font-size: 0.9em;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Gửi đến Phương Anh</h1>
        <p>
            Tớ không biết cậu có bao giờ vào trang này không, nhưng nếu cậu thấy được thì...<br>
            Cảm ơn cậu vì đã tồn tại, vì đã khiến ai đó muốn cố gắng mỗi ngày.<br>
            Tớ xin lỗi nếu món quà quá nhiều, tớ chỉ... lỡ thích cậu hơi nhiều thôi 😳
        </p>
        <div class="footer">- Một người đã luôn lặng lẽ dõi theo cậu -</div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)