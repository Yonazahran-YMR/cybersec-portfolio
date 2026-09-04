import java.io.BufferedReader;
import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class LogParser {
    static final String DB_URL = "jdbc:mysql://localhost:3306/soc_pipeline";
    static final String USER = "root";
    static final String PASS = "";

    public static void main(String[] args) {
        String csvFile = "sample_logs.csv";

        try (Connection conn = DriverManager.getConnection(DB_URL, USER, PASS);
               BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            
            String insertSQL = "INSERT INTO events (event_time, event_id, source_ip, account, hostname) VALUES (?, ?, ?, ?, ?)";
            PreparedStatement pstmt = conn.prepareStatement(insertSQL);

            String line;
            br.readLine(); //Skip header row

            int count = 0;
            while ((line = br.readLine()) != null) {
                if (line.trim().isEmpty()) continue;

                System.out.println("Processing line: [" + line + "]");
                String[] fields = line.split(",");

                pstmt.setString(1, fields[0]);
                pstmt.setInt(2, Integer.parseInt(fields[1]));
                pstmt.setString(3, fields[2]);
                pstmt.setString(4, fields[3]);
                pstmt.setString(5, fields[4]);

                pstmt.executeUpdate();
                count++;
            }

            System.out.println("Inserted " + count + " events.");
        
        } catch (Exception e) {
            System.err.println("Error parsing log file: " + e.getMessage());
            e.printStackTrace(System.err);
        }
    }
}
