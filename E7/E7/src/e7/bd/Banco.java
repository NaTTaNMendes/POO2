package e7.bd;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.PreparedStatement;

public class Banco {
    
    // JDBC driver name and database URL
    final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
    final String DB_URL = "jdbc:mysql://localhost/e7";

    // Database credentials
    final String USER = "aaaa";
    final String PASS = "aaaa";
    
    Connection conn = null;
    PreparedStatement stmt = null;
    
    public Boolean abrirConexao() {
        try {
            // Register JDBC driver
            Class.forName(JDBC_DRIVER);

            // Open a connection
            System.out.println("Connecting to database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }      
    }

    public Boolean fecharConexao() {
        try {
            if (stmt != null) {
                stmt.close();
            }
             
            if (conn != null) {
                conn.close();
            }            
            return true;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }
}
