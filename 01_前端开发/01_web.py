from flask import Flask

app = Flask(__name__)


# 创建了网址 /show/info 和函数 index 的对应关系
# 以后用户在浏览器上访问 /show/info 时, 就会自动调用 index 函数

@app.route('/show/info')
def index():
    return "中国<span style='color:red;'>联通</span>"


if __name__ == '__main__':
    app.run()  # http://127.0.0.1:5000/show/info
