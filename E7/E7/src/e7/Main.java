package e7;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.PreparedStatement;

public class Main {

    public static void main(String[] args) {
        
        // JDBC driver name and database URL
        final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
        final String DB_URL = "jdbc:mysql://localhost/e7";

        // Database credentials
        final String USER = "aaaa";
        final String PASS = "aaaa";
        
        Connection conn = null;
        PreparedStatement stmt = null;

      try {
         // Register JDBC driver
         Class.forName(JDBC_DRIVER);

         // Open a connection
         System.out.println("Connecting to database...");
         conn = DriverManager.getConnection(DB_URL, USER, PASS);

         String sql = "INSERT INTO carro (placa, cor) VALUES (?, ?)";
         stmt = conn.prepareStatement(sql);
         
         stmt.setString(1, "aaaaa");
         stmt.setString(2, "preto");

         System.out.println("Inserting data into table...");
         int rowsInserted = stmt.executeUpdate();

         if (rowsInserted > 0) {
            System.out.println(rowsInserted + " row(s) inserted.");
         } else {
            System.out.println("No rows inserted.");
         }

      } catch (SQLException se) {
         // Handle errors for JDBC
         se.printStackTrace();
      } catch (Exception e) {
         // Handle errors for Class.forName
         e.printStackTrace();
      } finally {
         // Finally block to close resources
         try {  
             if (stmt != null) {
                stmt.close();
             }
             
             if (conn != null) {
               conn.close();
            }
         } catch (SQLException se) {
            se.printStackTrace();
         }
      }
    }
    
}
