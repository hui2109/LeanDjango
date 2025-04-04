from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/post_register", methods=["get"])  # 此时还是get请求
def post_register():
    return render_template("post_register.html")


@app.route("/post/register", methods=["post"])
def post_info():
    print(request.form)  # post形式的参数 form
    return "注册成功!!"


if __name__ == "__main__":
    app.run()
