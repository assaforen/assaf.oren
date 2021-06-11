from flask import Flask, render_template, redirect, url_for, request, session,jsonify
from random import getrandbits
import mysql.connector
from Pages.assignment10.assignment10 import assignment10
app = Flask(__name__)
app.secret_key = '123'
app.register_blueprint(assignment10)

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


@app.route("/assignment11/table_user")
def assignment11_users():
    query = "select * from table_user"
    query_result = interact_db(query=query, query_type='fetch')
    response = "There is no data"
    if len(query_result) != 0:
        response = query_result
    response = jsonify(response)

    return response


@app.route("/assignment11/table_user/selected", defaults={'ID': 1})
@app.route("/assignment11/table_user/selected/<int:ID>")
def assignment11_select_user(ID):
    query = "select * from table_user where ID='%s';" % ID
    query_result = interact_db(query=query, query_type='fetch')
    response = "Wrong ID, Insert correct ID"
    if len(query_result) != 0:
        response = query_result
    response = jsonify(response)

    return response


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='assaf8193',
                                         database='cv')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value



@app.route("/logout")
def logout():
    session['nickname'] = ''
    return redirect('/assignment9')



if __name__ == '__main__':
    app.run()