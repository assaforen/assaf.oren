from flask import Flask, redirect, url_for
from random import getrandbits

app = Flask(__name__)

@app.route('/')
def Main_Page():
    return 'Welcome To the Main Page!'

@app.route('/home')
def Home_Page():
    return redirect('/')

@app.route('/customers')
def Welcome_Customer():
    IsSign = bool(getrandbits(1))
    if IsSign:
        return redirect(url_for('Welcome_Home'))
    else:
        return 'Signup Please!'

if __name__ == '__main__':
    app.run()