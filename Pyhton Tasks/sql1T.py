import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="Shalin@2006",
    database="test_db"
)

cursor = conn.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
cursor.execute("CREATE TABLE IF NOT EXISTS test(id INT PRIMARY KEY auto_increment, name VARCHAR(50), age INT)")

cursor.execute("INSERT INTO test ( name, age) VALUES ( 'Sample Name', 30)")
cursor.execute("INSERT INTO test ( name, age) VALUES ( 'Sample Name n', 40)")
cursor.execute("INSERT INTO test ( name, age) VALUES ('Sample Name n', 40)")

# cursor.execute("UPDATE test_db SET age = %s WHERE id = 1", (32,))


# cursor.execute("DROP TABLE IF EXISTS test_db")
conn.commit()

conn.close()