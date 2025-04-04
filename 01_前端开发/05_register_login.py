from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/register_new", methods=['GET', 'POST'])
def register_new():
    if request.method == 'GET':
        return render_template('register_new.html')
    else:
        user = request.form.get('usr')  # 注意: 这里使用form格式, 而不是arg形式
        pwd = request.form.get('pwd')
        gender = request.form.get('gender')
        hobby_list = request.form.getlist('hobby')
        city = request.form.get('usr')
        skill_list = request.form.getlist('skill')
        info = request.form.get('info')
        print(user, pwd, gender, hobby_list, city, skill_list, info)
        return '注册成功'


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('usr')
        pwd = request.form.get('pwd')
        print(user, pwd)
        return '登录成功'


if __name__ == '__main__':
    app.run()
