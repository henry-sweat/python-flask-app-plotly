from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/press_button')
def do_something():
    dt = datetime.datetime.now()
    res = '{:%Y-%m-%d %H-%M-%S}'.format(dt)
    return res

if __name__ == '__main__':
    app.run()