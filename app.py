from flask import Flask
from flask import render_template,redirect,Response,request
from flask_mysqldb import MySQL,MySQLdb
import config

app = Flask(__name__, static_folder='src/static', template_folder='src/template')  

app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    return render_template('auth/login.html')

if __name__ == '__main__':
    app.run()