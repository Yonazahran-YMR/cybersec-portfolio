CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_time DATETIME NOT NULL,
    event_id INT NOT NULL,
    source_ip VARCHAR(45),
    account VARCHAR(100),
    hostname VARCHAR(100)
);

CREATE TABLE alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    triggered_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    alert_type VARCHAR(100),
    related_account VARCHAR(100),
    related_ip VARCHAR(45),
    details TEXT
);