import mysql.connector
from mysql.connector import Error
def criarConexao(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
def criarDatabase(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
connection = criarConexao("localhost", "root", "root")
criarDatabase_query = "CREATE DATABASE cotacao"
criarDatabase(connection, criarDatabase_query)