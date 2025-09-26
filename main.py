import mysql.connector
import time

print("Waiting for MariaDB to be ready...")
time.sleep(3)

try:
    conn = mysql.connector.connect(
        host="localhost",
        password="",  # empty password
        database="WorkHubDB"
    )
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50));")
    conn.commit()

    print("Database 'WorkHubDB' is ready and table 'test_table' created.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()