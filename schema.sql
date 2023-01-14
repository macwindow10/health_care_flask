DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS appointments;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    role TEXT NOT NULL,
    fname TEXT NULL,
    mname TEXT NULL,
    lname TEXT NULL,
    email TEXT NULL,
    password TEXT NULL,
    cnic TEXT NULL,
    postal_code TEXT NULL,
    father_name TEXT NULL,
    gender TEXT NULL,
    blood_group TEXT NULL,
    emergency_mobile TEXT NULL,
    payment_mode TEXT NULL,
    qualification TEXT NULL,
    expertise TEXT NULL
);

CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    appointment_date TEXT NOT NULL,
    appointment_time TEXT NOT NULL,
    doctor_id INTEGER NOT NULL,
    patient_id INTEGER NOT NULL
)