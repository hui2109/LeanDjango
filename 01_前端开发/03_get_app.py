from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/get_register", methods=["get"])
def get_register():
    return render_template("get_register.html")


@app.route("/get/register", methods=["get"])
def get_info():
    print(request.args)
    return "注册成功!"


if __name__ == "__main__":
    app.run()
