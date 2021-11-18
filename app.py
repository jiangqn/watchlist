from flask import Flask
from flask import escape, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return u'<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user(name):
    return 'hello, %s' % escape(name)

@app.route('/test')
def test():
    return url_for('user', name='jiangqn')