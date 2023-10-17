from flask import Flask, render_template
from random import randint

draw = Flask(__name__)

hero = ['Annie', 'Olaf', 'Galio', 'Twisted Fate', 'Xin', 'Jhin', 'Urgot', 'Leblenc',
        'Vlad', 'Fiddlestick', 'Kyle', 'Yi', 'Alista', 'Ryze', 'Sion', 'Silver']

@draw.route('/index')
def index():
    return render_template('/index.html', hero = hero)

@draw.route('/drawAction')
def drawAction():
    num = randint(0,len(hero)-1)
    return render_template('index.html', hero = hero, h = hero[num])

draw.run(debug=True)
