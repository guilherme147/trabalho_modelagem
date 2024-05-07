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

query = '''
    CREATE TABLE moeda (
        id_moeda INT PRIMARY KEY, 
        moeda VARCHAR(50),
        valor_moeda DOUBLE
    )
'''
cursor = connection.cursor()
cursor.execute(query)

query = '''
    CREATE TABLE conversao (
        id_conversao INT PRIMARY KEY, 
        valor_real    DOUBLE,
        valor_convertido DOUBLE,
        data_hora DATETIME,
        MOEDA_idMOEDA INT NOT NULL,
        FOREIGN KEY (MOEDA_idMOEDA)
	    REFERENCES MOEDA (idMOEDA)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    )
'''
cursor = connection.cursor()
cursor.execute(query)


query = '''
    INSERT INTO moeda VALUES
        (1, 'Dolar', '7'),
        (2, 'Bitcoin', '2'),
        (3, 'Etherium', '4'),
        (4, 'Euro', '1),
        (5, 'Libra', '3'),
        (6, 'Iene', '3')
'''
cursor = connection.cursor()
cursor.execute(query)
connection.commit()

query = '''
    SELECT * FROM moedas
'''
cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchall()
for row in result:

