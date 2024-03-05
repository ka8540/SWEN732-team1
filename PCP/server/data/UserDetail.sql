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

INSERT INTO user_authentication ( firstname, lastname, username, hashed_password, email,session_key) VALUES('Kush','Ahir','kush_ahir', '5775c5782a9e218ebd3c971f689cfccb45fde0560db23aa4b4057e08', 'kay@gmail.com',NULL);