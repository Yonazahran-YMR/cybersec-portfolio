DELIMITER //
CREATE TRIGGER trg_brute_force
AFTER INSERT ON events
FOR EACH ROW
BEGIN
    DECLARE fail_count INT;
    DECLARE existing_alert INT;
    DECLARE prior_bruteforce INT;
 
    -- Rule 1: Brute force (T1110)
    -- 5+ failed logons (4625) from the same source IP within a 10 minute window
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
            INSERT INTO alerts (triggered_at, alert_type, related_account, related_ip, details, technique_id, technique_name)
            VALUES (NEW.event_time, 'Brute Force Suspected', NEW.account, NEW.source_ip,
                    CONCAT(fail_count, ' failed logons in 10 min window'),
                    'T1110', 'Brute Force');
        END IF;
    END IF;
 
    -- Rule 2: Possible persistence (T1136)
    -- Same account that has an active brute force alert creates a new account (4720) within 30 minutes
    IF NEW.event_id = 4720 THEN
        SELECT COUNT(*) INTO prior_bruteforce
        FROM alerts
        WHERE related_account = NEW.account
          AND alert_type = 'Brute Force Suspected'
          AND triggered_at >= (NEW.event_time - INTERVAL 30 MINUTE)
          AND triggered_at <= NEW.event_time;
 
        IF prior_bruteforce > 0 THEN
            INSERT INTO alerts (triggered_at, alert_type, related_account, related_ip, details, technique_id, technique_name)
            VALUES (NEW.event_time, 'Possible Persistence', NEW.account, NEW.source_ip,
                    CONCAT('New account created (event 4720) by ', NEW.account,
                           ' following brute force alert on account ', NEW.account),
                    'T1136', 'Create Account');
        END IF;
    END IF;
END//
DELIMITER ;
