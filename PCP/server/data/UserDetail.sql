DROP TABLE IF EXISTS user_authentication;


CREATE TABLE user_authentication (
    user_id SERIAL PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    session_key VARCHAR(255) UNIQUE
);