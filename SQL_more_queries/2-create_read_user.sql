-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it doesn't exist, with a password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege only on the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply changes immediately
FLUSH PRIVILEGES;
