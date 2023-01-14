from pprint import pprint
from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)

time_slots = [
    ["09:00 - 09:20"],
    ["09:20 - 09:40"],
    ["09:40 - 10:00"],

    ["10:00 - 10:20"],
    ["10:20 - 10:40"],
    ["10:40 - 11:00"],

    ["11:00 - 11:20"],
    ["11:20 - 11:40"],
    ["11:40 - 12:00"],

    ["12:00 - 12:20"],
    ["12:20 - 12:40"],
    ["12:40 - 13:00"],

    ["13:00 - 13:20"],
    ["13:20 - 13:40"],
    ["13:40 - 14:00"]
]


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_doctors():
    conn = get_db_connection()
    doctors = conn.execute('SELECT * FROM users WHERE role="Doctor" ORDER BY fname, mname, lname').fetchall()
    conn.close()
    return doctors


def get_appointments(doctor_id):
    conn = get_db_connection()
    appointments = conn.execute('SELECT * FROM appointments WHERE doctor_id=' + doctor_id).fetchall()
    conn.close()
    return appointments


def get_appointments(doctor_id, dt):
    conn = get_db_connection()
    appointments = conn.execute('SELECT * FROM appointments '
                                'WHERE doctor_id=' + doctor_id +
                                ' AND appointment_date=' + dt).fetchall()
    conn.close()
    return appointments


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_post():
    role = request.form['role']
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
    qualification = request.form['qualification']
    expertise = request.form['expertise']
    pprint(role)
    pprint(email)
    pprint(password)
    pprint(fname)
    pprint(mname)
    pprint(lname)
    conn = get_db_connection()
    cur = conn.cursor()
    if role == 'Patient':
        cur.execute(
            "INSERT INTO users (role, email, password, cnic, fname, mname, lname, postal_code, father_name, blood_group, gender, emergency_mobile, payment_mode) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (role, email, password, cnic, fname, mname, lname, postal_code, father_name, blood_group, gender,
             emergency_mobile,
             payment_mode)
        )
    else:
        cur.execute(
            "INSERT INTO users (role, email, password, cnic, fname, mname, lname, postal_code, father_name, blood_group, gender, emergency_mobile, payment_mode, qualification, expertise) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                role, email, password, cnic, fname, mname, lname, postal_code, father_name, blood_group, gender,
                emergency_mobile,
                payment_mode, qualification, expertise)
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
    if user is None:
        pprint('user not found')
        message = 'Wrong email/password'
        return redirect(url_for('login', message=message))

    pprint('user found')
    message = 'User logged-in successfully'
    session.__setitem__('login_status', True)
    session.__setitem__('role', user["role"])
    session.__setitem__('email', user["email"])
    return redirect(url_for('index', message=message, role=user["role"], email=user["email"]))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login', message='User logged out'))


@app.route('/schedule_appointment', methods=['GET'])
def schedule_appointment():
    pprint('schedule_appointment')
    login_status = session.get('login_status')
    if login_status is None:
        return render_template('login.html')
    doctor_id = request.args['doctor_id']
    conn = get_db_connection()
    doctor = conn.execute('SELECT * FROM users WHERE id=' + doctor_id).fetchone()
    conn.close()
    return render_template('schedule_appointment.html', doctor=doctor, time_slots=time_slots)


@app.route('/schedule_appointment', methods=['POST'])
def schedule_appointment_post():
    login_status = session.get('login_status')
    if login_status is None:
        return render_template('login.html')
    doctor_id = request.form["doctor_id"]


@app.route('/')
def index():
    login_status = session.get('login_status')
    if login_status is None:
        return render_template('login.html')
    role = session.get('role')
    email = session.get('email')
    if role == 'Patient':
        doctors = get_doctors()
        return render_template('home_patient.html', role=role, email=email, doctors=doctors)
    return render_template('home_doctor.html', role=role, email=email)


if __name__ == '__main__':
    app.secret_key = '84736uidhgfudgty7et'
    # session.init_app(app)
    app.run()
