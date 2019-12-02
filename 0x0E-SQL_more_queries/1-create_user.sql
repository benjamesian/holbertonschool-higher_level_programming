-- Create a user `user_0d_11`
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grand all privileges to newly created user
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
