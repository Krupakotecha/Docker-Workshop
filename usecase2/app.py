
from flask import Flask, render_template, request, redirect, url_for
import pymysql
app = Flask(__name__)

@app.route('/')
def home() :
        return render_template('register.html')

@app.route('/result', methods = ['POST', 'GET'])
def result() :
        if request.method == 'POST' :
                u = request.form['userid']
                p = request.form['password']
                con = pymysql.connect(host='172.17.0.2', user='root', password='root', cursorclass=pymysql.cursors.DictCursor)
                cur = con.cursor()
                cur.execute("CREATE DATABASE IF NOT EXISTS test")
                cur.execute("USE test")
                cur.execute("CREATE TABLE IF NOT EXISTS register(user_id varchar(20), password varchar(20)) ")
                sql = "INSERT INTO register(user_id,password) VALUES(\'"+u+"\',\'"+p+"\')"
                cur.execute(sql)
                sql="SELECT * FROM register WHERE user_id=\'"+u+"\'"
                cur.execute(sql)
                result=cur.fetchall()
                outp = str(result[0])
                con.commit()
                con.close()
                return outp

if __name__ == '__main__' :
        app.run(debug = True, host = '0.0.0.0')

