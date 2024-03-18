---- -- We specify our primary key here to be as repeatable as possible
-- INSERT INTO users ( firstname, lastname, username, password, email)
-- VALUES('Bharathi','pandurangan','bp6191', '','bharathi@gmail.com');

-- -- Restart our primary key sequences here so inserting id=DEFAULT won't collide
-- ALTER SEQUENCE example_table_id_seq RESTART 1000;
 INSERT INTO users ( firstname, lastname, username, password, email)
 VALUES('Bharathi','pandurangan','bp6191', 'bp6191','bharathi@gmail.com');

