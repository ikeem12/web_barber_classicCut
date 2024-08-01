from flask import Flask
from flask import render_template,redirect,Response
from flask_mysqldb import MySQL,MySQLdb

app = Flask(__name__, static_folder='src/static', template_folder='src/template')  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def login():
    return render_template('auth/login.html')

if __name__ == '__main__':
    app.run()