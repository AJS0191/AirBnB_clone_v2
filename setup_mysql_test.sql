<<<<<<< HEAD
-- Prepares the testing MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY "hbnb_test_pwd";
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
=======
-- Prepares the testing MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY "hbnb_test_pwd";
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
>>>>>>> 1bc002ec0ecad7b93ea946ae73478b51c046d885
