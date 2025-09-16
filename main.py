import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="prova56__"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
