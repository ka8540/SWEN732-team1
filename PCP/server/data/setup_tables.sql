DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    id VARCHAR(50) PRIMARY KEY NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    session_key VARCHAR(128) DEFAULT NULL
);
