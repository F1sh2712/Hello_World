from flask import Flask,render_template,request

login = Flask(__name__)

@login.route('/login')
def loginPage():
    return render_template('login.html')

@login.route('/homepage')
def homePage():
    userName = request.args.get('username')
    return f"这里是主页！你好，用户{userName}！"

login.run(debug=True)

