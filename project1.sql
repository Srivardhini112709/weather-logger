CREATE DATABASE weather_project;
show databases;
USE weather_project;
show tables;
CREATE TABLE weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    description VARCHAR(100),
    observation_time DATETIME
);
SELECT * FROM weather_data ORDER BY observation_time DESC;







