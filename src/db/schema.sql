-- DROP TABLE IF EXISTS example_table;
-- DROP DATABASE IF EXISTS swen732;
-- CREATE DATABASE swen732;

DROP TABLE IF EXISTS users;
CREATE TABLE users(
    user_id uuid PRIMARY KEY DEFAULT 
    uuid_generate_v4(),
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
    -- session_key VARCHAR(255) UNIQUE
);

