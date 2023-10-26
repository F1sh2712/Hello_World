from flask import Flask, render_template,request

like = Flask(__name__)

data = [
    {'id':1,'name':'元旦','num':0},
    {'id':2,'name':'春节','num':0},
    {'id':3,'name':'国庆','num':0},
]

@like.route('/like')
def index():
    return render_template('like.html', data=data)

@like.route('/dianzan')
def dianzan():
    id = request.args.get('id')
    print(f'想要给{id}点赞！！')
    data[int(id)-1]['num'] += 1
    return render_template('like.html', data=data)

like.run(debug=True)