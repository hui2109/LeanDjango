from flask import Flask, render_template

app = Flask(__name__)


@app.route("/show/info")
def index():
    # Flask内部会自动打开这个文件，并读取内容，将内容给用户返回。
    # 默认：去当前项目目录的templates文件夹中找。
    return render_template("index.html")


@app.route("/get/news")
def get_news():
    return render_template("get_news.html")


@app.route("/show/table")
def show_table():
    return render_template("show_table.html")


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run()  # http://127.0.0.1:5000/show/info
