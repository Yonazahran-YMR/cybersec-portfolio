DELIMITER //
CREATE TRIGGER trg_brute_force
AFTER INSERT ON events
FOR EACH ROW
BEGIN
    DECLARE fail_count INT;
    DECLARE existing_alert INT;

    IF NEW.event_id = 4625 THEN
        SELECT COUNT(*) INTO fail_count
        FROM events
        WHERE event_id = 4625
          AND source_ip = NEW.source_ip
          AND event_time >= (NEW.event_time - INTERVAL 10 MINUTE)
          AND event_time <= NEW.event_time;

        SELECT COUNT(*) INTO existing_alert
        FROM alerts
        WHERE related_ip = NEW.source_ip
          AND alert_type = 'Brute Force Suspected'
          AND triggered_at >= (NEW.event_time - INTERVAL 10 MINUTE);

        IF fail_count >= 5 AND existing_alert = 0 THEN
            INSERT INTO alerts (triggered_at, alert_type, related_account, related_ip, details)
            VALUES (NEW.event_time, 'Brute Force Suspected', NEW.account, NEW.source_ip,
                    CONCAT(fail_count, ' failed logons in 10 min window'));
        END IF;
    END IF;
END//
DELIMITER ;
