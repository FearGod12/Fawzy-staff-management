-- Create database, Create user and Grant privileges

CREATE DATABASE IF NOT EXISTS fsm_dev_db;
CREATE USER IF NOT EXISTS 'fsm_dev'@'localhost' IDENTIFIED BY 'fsm_dev_pwd';
GRANT ALL PRIVILEGES ON `fsm_dev_db`.* TO 'fsm_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'fsm_dev'@'localhost';
FLUSH PRIVILEGES;
