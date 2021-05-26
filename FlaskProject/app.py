from flask import Flask, redirect, url_for ,render_template
from random import getrandbits

app = Flask(__name__)

@app.route('/')
def Main_Page():
    return render_template('FinalPageCV.html')

@app.route('/assignment8')
def Home_Page():
    return render_template('assignment8.html',
                           name={'guest'},
                           user={'firstname': 'Assaf', 'lastname': 'Oren'},
                           contact={'whatsapp': '+972545894707', 'email': 'assafore@post.bgu.ac.il',
                                    'facebook': 'look for Assaf Oren'},
                           gender=['boy'])

@app.route('/customers')
def Welcome_Customer():
    IsSign = bool(getrandbits(1))
    if IsSign:
        return redirect(url_for('Welcome_Home'))
    else:
        return 'Signup Please!'

if __name__ == '__main__':
    app.run()