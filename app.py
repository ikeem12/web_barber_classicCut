from flask import Flask
from flask import render_template,redirect,request,session,url_for,flash
from flask_mysqldb import MySQL,MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash
import config

app = Flask(__name__, static_folder='src/static', template_folder='src/template')
app.secret_key = config.SECRET_KEY    

app.config.from_object('config')
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/panelControl',methods=['GET', 'POST'])
def panelControl():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE userName = %s',(user,))
        account = cur.fetchone()

        if account and check_password_hash(account['password'],password):
            session['loggedin'] = True
            session['user'] = account['role']
            return redirect(url_for(account['role']))
        else:
            flash('Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.', 'danger')
  
    return render_template('auth/login.html')

@app.route('/admin')
def admin():
    if 'loggedin' in session:
        return render_template('admin.html')
    else:
        return redirect(url_for('panelControl'))

@app.route('/employee')
def employee():
    if 'loggedin' in session:
        return render_template('employee.html')
    else:
        return redirect(url_for('panelControl'))

if __name__ == '__main__':
    app.run()