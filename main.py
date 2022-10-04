from pprint import pprint
from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form['email']
    password = request.form['password']
    fname = request.form['fname']
    mname = request.form['mname']
    lname = request.form['lname']
    cnic = request.form['cnic']
    postal_code = request.form['postal_code']
    father_name = request.form['father_name']
    blood_group = request.form['blood_group']
    gender = request.form['gender']
    emergency_mobile = request.form['emergency_mobile']
    payment_mode = request.form['payment_mode']
    pprint(email)
    pprint(password)
    pprint(fname)
    pprint(mname)
    pprint(lname)
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (email, password, cnic, fname, mname, lname, postal_code, father_name, blood_group, gender, emergency_mobile, payment_mode) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (email, password, cnic, fname, mname, lname, postal_code, father_name, blood_group, gender, emergency_mobile,
         payment_mode)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('index', message='User registered successfully'))


@app.route('/login')
def login():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email=? AND password=?',
                        (email, password)).fetchone()
    conn.close()
    result = False
    if user == None:
        pprint('user not found')
        message = 'Wrong email/password'
    else:
        pprint('user found')
        message = 'User logged-in successfully'
        session.__setitem__('login_status', True)
    return redirect(url_for('index', message=message))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login', message='User logged out'))


@app.route('/')
def index():
    login_status = session.get('login_status')
    if login_status is None:
        return render_template('login.html')
    return render_template('home.html')


if __name__ == '__main__':
    app.secret_key = '84736uidhgfudgty7et'
    # session.init_app(app)
    app.run()
