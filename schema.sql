DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fname TEXT NULL,
    mname TEXT NULL,
    lname TEXT NULL,
    email TEXT NULL,
    password TEXT NULL,
    cnic TEXT NULL,
    postal_code TEXT NULL,
    father_name TEXT NULL,
    blood_group TEXT NULL,
    gender TEXT NULL,
    emergency_mobile TEXT NULL,
    payment_mode TEXT NULL
);
