CREATE DATABASE soc_pipeline;
USE soc_pipeline;

CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_time DATETIME NOT NULL,
    event_id INT NOT NULL,
    source_ip VARCHAR(45) NOT NULL,
    account VARCHAR(100) NOT NULL,
    hostname VARCHAR(100) NOT NULL
);

CREATE TABLE alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    triggered_at DATETIME NOT NULL,
    alert_type VARCHAR(100) NOT NULL,
    related_account VARCHAR(100) NOT NULL,
    related_ip VARCHAR(45) NOT NULL,
    details VARCHAR(255),
    technique_id VARCHAR(10),
    technique_name VARCHAR(100)
);
