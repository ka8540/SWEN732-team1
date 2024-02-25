DROP TABLE IF EXISTS user_authentication;


CREATE TABLE user_authentication (
    user_id SERIAL PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(50) NOT NULL
);

INSERT INTO user_authentication ( firstname, lastname, username, hashed_password, email, role) VALUES('Kush','Ahir','kush_ahir', 'kush1234', 'kay@gmail.com', 'USER');