from flask import Flask, render_template, redirect, url_for, request, session, Blueprint
import mysql.connector

assignment10 = Blueprint('assignment10', __name__, static_folder='static',
                          static_url_path='/assignment10', template_folder='templates')


@assignment10.route("/assignment10")
def table_user():
    query = "select * from table_user"
    query_result = interact_DB(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


@assignment10.route("/assignment10Insert", methods=['GET', 'POST'])
def insertuserstoDB():
    USER_NAME = request.form['USER_NAME']
    NICK_NAME = request.form['NICK_NAME']
    query = "insert into users(USER_NAME, NICK_NAME) values ('%s', '%s')" % (USER_NAME, NICK_NAME)
    interact_DB(query=query, query_type='commit')
    return redirect('/assignment10')


@assignment10.route("/assignment10delete", methods=['POST'])
def deleteuserstoDB():
    USER_NAME = request.form['USER_NAME']
    query = "delete from USER_NAME where name='%s';" % USER_NAME
    interact_DB(query, query_type='commit')
    return redirect("/assignment10")


@assignment10.route("/assignment10update", methods=['POST'])
def updateusersinDB():
    USER_NAME = request.form['USER_NAME']
    NICK_NAME = request.form['NICK_NAME']
    query = "update users set NICK_NAME = '%s' where name='%s';" % (NICK_NAME, USER_NAME)
    interact_DB(query, query_type='commit')
    return redirect("/assignment10")


def interact_DB(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='assaf8193OREN',
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

