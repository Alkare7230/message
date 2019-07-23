#coding:utf-8
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PWD'] = 'shadow72'
app.config['MYSQL_DB'] = 'cbddmanuel'

mysql = MySQL(app)
#__________________________________________________________________________________________________#

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form.redirect
        user_pseudo = details['user_pseudo']
        user_pwd = details['user_pwd']

        cur = mysql.connection.cursor()
        cur.execute(""" INSERT INTO users(user_id, name_user, user_psw) 
        VALUES(?, ?, ?); 
        """,
        (user_id, name_user, user_psw)
        )
        redirect(url_for('http://127.0.0.1:5000/'))
        mysql.connection.commit()
        cur.close()

    return render_template("index.html")





#____________________________________________________________________________________________________#

if __name__ == '__main__':
    app.run(debug=True)
