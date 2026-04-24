from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Docker Python App</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .card {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.2);
        }

        h1 {
            margin-bottom: 10px;
        }

        p {
            font-size: 18px;
            opacity: 0.9;
        }

        .btn {
            margin-top: 20px;
            padding: 10px 20px;
            border: none;
            background: white;
            color: #333;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }

        .btn:hover {
            background: #ddd;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Hello Aftab!</h1>
        <p>Your Dockerized Python App is Running Successfully</p>
        <p>Powered by Flask + Docker</p>
        <a href="/about">
            <button class="btn">About</button>
        </a>
    </div>
</body>
</html>
"""

ABOUT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>About</title>
    <style>
        body {
            margin: 0;
            font-family: Arial;
            background: #1e1e2f;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }

        .box {
            padding: 40px;
        }

        a {
            color: #00d4ff;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>📦 About This App</h1>
        <p>This is a beautifully styled Python Flask app running inside Docker.</p>
        <p>It is served via a container and can be scaled easily.</p>
        <a href="/">⬅ Back to Home</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/about')
def about():
    return render_template_string(ABOUT_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
