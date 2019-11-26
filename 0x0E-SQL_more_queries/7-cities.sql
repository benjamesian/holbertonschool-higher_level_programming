-- Create db `hbtn_0d_usa`
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- Create table `cities`
CREATE TABLE IF NOT EXISTS cities (
       id INT NOT NULL AUTO_INCREMENT,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY (state_id)
       	       REFERENCES states(id),
       PRIMARY KEY (id)
);
