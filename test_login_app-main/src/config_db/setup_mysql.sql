CREATE DATABASE IF NOT EXISTS login_db;
USE login_db;
CREATE TABLE IF NOT EXISTS login_table(
    id int auto_increment primary key, 
    email varchar(255) not null unique, 
    password varchar(255) not null);