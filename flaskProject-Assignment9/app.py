from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/assignment9', methods=["GET", "POST"])
def as9():
    curr_method = request.method
    users = {"ASAF": "BOY", "D": "S", "R": "REEE"}
    user_name = ''
    user_search = ''

    if curr_method == "GET":
        if 'user_search' in request.args:
            user_search = request.args['user_search']
        else:
            user_search = ''

    if curr_method == "POST":
        if 'user_name' in request.form:
            user_name = request.form['user_name']
        else:
            user_name = ''
        if user_name in users:
            session['nickname'] = users[user_name]
        else:
            session['nickname'] = ''

    return render_template("assignment9.html",
                           users=users,
                           user_name=user_name,
                           curr_method=curr_method,
                           user_search=user_search)


@app.route("/logout")
def logout():
    session['nickname'] = ''
    return redirect('/assignment9')


if __name__ == '__main__':
    app.run()
