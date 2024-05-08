import mysql.connector
from mysql.connector import Error
from datetime import datetime
import PySimpleGUI as sg
sg.theme('Reddit')
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
        idCONVERSAO INT AUTO_INCREMENT PRIMARY KEY, 
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

# Função para buscar cotação no banco de dados
def buscar_cotacao(moeda):
    query = f"SELECT valor_moeda FROM moeda WHERE moeda = '{moeda}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None
# Função para atualizar cotação no banco de dados
def atualizar_cotacao(moeda, valor):
    query = f"UPDATE moeda SET valor_moeda = '{valor}' WHERE moeda = '{moeda}'"
    cursor.execute(query)
    mydb.commit()

def paginaValor():
    moeda = ''
    cotacao = 0.0
    layout = [
        [sg.Text(("Valor das moedas atualizado"), font=('Arial', 25), border_width=5, text_color='grey')],
        [sg.HorizontalSeparator()],
        [sg.Text('', pad=(0,10))],
        [sg.Button('Dolar', size=(15,3), key='USD'), sg.Text('', pad=(2,0)), sg.Button('Euro', size=(15,3), key='EUR'), sg.Text('', pad=(2,0)), sg.Button('Libra', size=(15,3), key='GBP')],
        [sg.Text('', pad=(0,10))],
        [sg.Button('Iene', size=(15,3), key='JPY'),sg.Text('', pad=(2,0)), sg.Button('Bitcoin', size=(15,3), key='BTC'),sg.Text('', pad=(2,0)), sg.Button('Etherium', size=(15,3), key='ETH')],
        [sg.Text('', pad=(0,10))],
        [sg.HorizontalSeparator()],
        [sg.Text((f"Valor da moeda {moeda}"), font=('Arial', 25), border_width=5, key='moeda', text_color='grey')],
        [sg.Text((f"R${cotacao}"), font=('Arial', 25), border_width=5, key='cotacao', text_color='grey')],
    ]
    # janela
    window = sg.Window('registro', layout, size=(500,500), element_justification='center')
    # funcionamento
    while True:
        event, values = window.read()
        if(event == sg.WIN_CLOSED):
            window.close()
            break
        if(event == sg.WIN_CLOSED):
            window.close()
            break
        while True:
            event, values = window.read()
            if(event == sg.WIN_CLOSED):
                window.close()
                break
            if(event in ['USD', 'EUR', 'GBP', 'JPY', 'BTC', 'ETH']):
                moeda = event
                cotacao = buscar_cotacao(moeda)
                if cotacao is not None:
                    window['moeda'].update(f"Valor da moeda {moeda}")
                    window['cotacao'].update(f"R${cotacao}")
                else:
                    sg.popup(f"Cotação da moeda {moeda} não encontrada no banco de dados")

        if(event == 'USD'):
            moeda = 'Dólar'
            cotacao_dolar = buscar_cotacao(moeda)
            print(buscar_cotacao(moeda))
            cotacao = cotacao_dolar
            cotacao = str(cotacao).replace('.',',')
            window['moeda'].update(moeda)
            window['cotacao'].update("R$"+cotacao)
        if(event == 'BTC'):
            moeda = 'Bitcoin'
            cotacao_bitcoin = buscar_cotacao(moeda)
            cotacao = float(cotacao_bitcoin)
            cotacao = f'{cotacao:_.3f}'
            cotacao = cotacao.replace('.',',').replace('_','.')
            window['moeda'].update(moeda)
            window['cotacao'].update("R$"+cotacao)
        if(event == 'ETH'):
            moeda = 'Etherium'
            cotacao_etherium = buscar_cotacao(moeda)
            cotacao = float(cotacao_etherium)
            cotacao = f'{cotacao:_.2f}'
            cotacao = cotacao.replace('.',',').replace('_','.')
            window['moeda'].update(moeda)
            window['cotacao'].update("R$"+cotacao)
        if(event == 'EUR'):
            moeda = 'Euro'
            cotacao_euro = buscar_cotacao(moeda)
            cotacao = cotacao_euro
            cotacao = str(cotacao).replace('.',',')
            window['moeda'].update(moeda)
            window['cotacao'].update("R$"+cotacao)
        if(event == 'GBP'):
            moeda = 'Libra'
            cotacao_libra = buscar_cotacao(moeda)
            cotacao = cotacao_libra
            cotacao = str(cotacao).replace('.',',')
            window['moeda'].update(moeda)
            window['cotacao'].update("R$"+cotacao)
        if(event == 'JPY'):
            moeda = 'Iene'
            cotacao_iene = buscar_cotacao(moeda)
            cotacao = cotacao_iene
            cotacao = str(cotacao).replace('.',',')
            window['moeda'].update(moeda)
            window['cotacao'].update("R$"+cotacao)
def paginaInicial():
    layout1 = [
        [sg.Text(("Valor das moedas atualizado"), font=('Arial', 25), border_width=5, text_color='grey')],
        [sg.Text('', pad=(0,10))],
        [sg.HorizontalSeparator()],
        [sg.Text('', pad=(0,10))],
        [sg.Button('Converter moedas', size=(15,3), key='conversao'),sg.Text('', pad=(20,0)), sg.Button('Valor das moedas', size=(15,3), key='moedas')],
        [sg.Text('', pad=(0,10))],
        [sg.HorizontalSeparator()],
    ]
    window = sg.Window('registro', layout1, size=(500,500), element_justification='center')
    while True:
        event, values = window.read()
        if(event == sg.WIN_CLOSED):
            window.close()
            break
        if(event == 'conversao'):
            window.close()
            paginaConversao()
            break
        if(event == 'moedas'):
            window.close()
            paginaValor()
            break
def paginaConversao():
    cotacao = 0.0
    moeda = ''
    layout = [
        [sg.Text('Digite o valor a converter em reais', text_color='grey' ,font=('Arial', 20))],
        [sg.Text('R$',text_color='grey', font=('Arial', 12)),sg.InputText(background_color='grey', text_color='white')],
        [sg.Text('', pad=(0,10))],
        [sg.HorizontalSeparator()],
        [sg.Text('', pad=(0,10))],
        [sg.Button('Dolar', size=(15,3), key='USD'), sg.Text('', pad=(2,0)), sg.Button('Euro', size=(15,3), key='EUR'), sg.Text('', pad=(2,0)), sg.Button('Libra', size=(15,3), key='GBP')],
        [sg.Text('', pad=(0,10))],
        [sg.Button('Iene', size=(15,3), key='JPY'),sg.Text('', pad=(2,0)), sg.Button('Bitcoin', size=(15,3), key='BTC'),sg.Text('', pad=(2,0)), sg.Button('Etherium', size=(15,3), key='ETH')],
        [sg.Text('', pad=(0,10))],
        [sg.HorizontalSeparator()],
        [sg.Text((f"{moeda}"), font=('Arial', 25), border_width=5, key='moeda', text_color='grey')],
        [sg.Text((f"{cotacao}"), font=('Arial', 25), border_width=5, key='cotacao', text_color='grey')],
    ]
    window = sg.Window('registro', layout, size=(500,500), element_justification='center')
    while True:
        event, values = window.read()
        valorReais = values[0]
        if(event == sg.WIN_CLOSED):
            window.close()
            break
        if(event == 'USD'):
            moeda = 'Dólar'
            data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(data_atual)
            cotacao_dolar = buscar_cotacao(moeda)
            valorConversao = float(valorReais) / float(cotacao_dolar)  
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("$"+valorConversao)
            query = f'''
                INSERT INTO conversao (valor_real, valor_convertido, data_hora, MOEDA_idMOEDA) VALUES
                ({valorReais}, {valorConversao}, '{data_atual}', 1)
                '''
            criarTabela(connection, query)
            connection.commit()
        if(event == 'BTC'):
            moeda = 'Bitcoin'
            data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cotacao_bitcoin = buscar_cotacao(moeda)
            valorConversao =  float(valorReais) / float(cotacao_bitcoin)
            valorConversao = str(valorConversao)  
            window['moeda'].update(moeda)
            window['cotacao'].update("BTC "+valorConversao)
            query = f'''
                INSERT INTO conversao (valor_real, valor_convertido, data_hora, MOEDA_idMOEDA) VALUES
                ({valorReais}, {valorConversao}, '{data_atual}', 2)
                '''
            criarTabela(connection, query)
            connection.commit()
        if(event == 'ETH'):
            moeda = 'Etherium'
            data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cotacao_etherium = buscar_cotacao(moeda)
            valorConversao =  float(valorReais) / float(cotacao_etherium)
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("ETH "+valorConversao)
            query = f'''
                INSERT INTO conversao (valor_real, valor_convertido, data_hora, MOEDA_idMOEDA) VALUES
                ({valorReais}, {valorConversao}, '{data_atual}', 3)
                '''
            criarTabela(connection, query)
            connection.commit()
        if(event == 'EUR'):
            moeda = 'Euro'
            data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cotacao_euro = buscar_cotacao(moeda)
            valorConversao =  float(valorReais) / float(cotacao_euro)
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("€"+valorConversao)
            query = f'''
                INSERT INTO conversao (valor_real, valor_convertido, data_hora, MOEDA_idMOEDA) VALUES
                ({valorReais}, {valorConversao}, '{data_atual}', 4)
                '''
            criarTabela(connection, query)
            connection.commit()
        if(event == 'GBP'):
            moeda = 'Libra'
            data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cotacao_libra = buscar_cotacao(moeda)
            valorConversao =  float(valorReais) / float(cotacao_libra)
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("£"+valorConversao)
            query = f'''
                INSERT INTO conversao (valor_real, valor_convertido, data_hora, MOEDA_idMOEDA) VALUES
                ({valorReais}, {valorConversao}, '{data_atual}', 5)
                '''
            criarTabela(connection, query)
            connection.commit()
        if(event == 'JPY'):
            moeda = 'Iene'
            data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cotacao_iene = buscar_cotacao(moeda)
            valorConversao =  float(valorReais) / float(cotacao_iene)
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("¥"+valorConversao)
            query = f'''
                INSERT INTO conversao (valor_real, valor_convertido, data_hora, MOEDA_idMOEDA) VALUES
                ({valorReais}, {valorConversao}, '{data_atual}', 6)
                '''
            criarTabela(connection, query)
            connection.commit()
# Tema do PySimpleGUI


# while True:
#     event, values = window.read()
#     if(event == sg.WIN_CLOSED):
#         window.close()
#         break
#     if(event in ['USD', 'EUR', 'GBP', 'JPY', 'BTC', 'ETH']):
#         moeda = event
#         cotacao = buscar_cotacao(moeda)
#         if cotacao is not None:
#             window['moeda'].update(f"Valor da moeda {moeda}")
#             window['cotacao'].update(f"R${cotacao}")
#         else:
#             sg.popup(f"Cotação da moeda {moeda} não encontrada no banco de dados")


paginaInicial()
