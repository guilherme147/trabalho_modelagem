import mysql.connector
from mysql.connector import Error

def criarDatabase(host_name, user_name, user_password, db_name):
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute(f"USE {db_name}")
        print("Database created successfully")
        return connection
    except Error as err:
        print(f"Error: '{err}'")

def criarTabela(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print("Table created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
# Criar o banco de dados 'cotacao' se ele não existir
connection = criarDatabase("localhost", "root", "root", "cotacao")

# Criação da tabela moeda
query = '''
    CREATE TABLE IF NOT EXISTS moeda (
        idMOEDA INT PRIMARY KEY, 
        moeda VARCHAR(50),
        valor_moeda DOUBLE
    )
'''
criarTabela(connection, query)

# Criação da tabela conversao
query = '''
    CREATE TABLE IF NOT EXISTS conversao (
        idCONVERSAO INT PRIMARY KEY, 
        valor_real DOUBLE,
        valor_convertido DOUBLE,
        data_hora DATETIME,
        MOEDA_idMOEDA INT NOT NULL,
        FOREIGN KEY (MOEDA_idMOEDA)
        REFERENCES moeda (idMOEDA)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    )
'''
criarTabela(connection, query)

# Inserção de dados na tabela moeda
query = '''
    INSERT INTO moeda VALUES
        (1, 'Dolar', 7),
        (2, 'Bitcoin', 2),
        (3, 'Etherium', 4),
        (4, 'Euro', 1),
        (5, 'Libra', 3),
        (6, 'Iene', 3)
'''
criarTabela(connection, query)
connection.commit()

# Consulta à tabela moeda
query = '''
    SELECT * FROM moeda
'''
cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchall()
print(result)