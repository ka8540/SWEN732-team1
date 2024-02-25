CREATE TABLE user_authentication (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(50) NOT NULL,
);

INSERT INTO user_authentication (username, hashed_password, email, role) VALUES('kush_ahir', 'kush1234', 'kay@gmail.com', 'USER');