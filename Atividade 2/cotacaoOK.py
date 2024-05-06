import mysql.connector
<<<<<<< HEAD
from mysql.connector import Error
import pandas as pd
=======
>>>>>>> 63c1f20bc7226733b386432a73e4ae5bcc819e59
import PySimpleGUI as sg

# Conectar ao banco de dados
mydb = mysql.connector.connect(
  host="localhost",
  user="seu_usuario",
  password="sua_senha",
  database="COTACAO"
)
cursor = mydb.cursor()

# Função para buscar cotação no banco de dados
def buscar_cotacao(moeda):
    query = f"SELECT valor_moeda FROM MOEDA WHERE moeda = '{moeda}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

# Função para atualizar cotação no banco de dados
def atualizar_cotacao(moeda, valor):
    query = f"UPDATE MOEDA SET valor_moeda = '{valor}' WHERE moeda = '{moeda}'"
    cursor.execute(query)
    mydb.commit()

# Tema do PySimpleGUI
sg.theme('Reddit')
<<<<<<< HEAD
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
        if(event == 'USD'):
            moeda = 'Dólar'
            cotacao_dolar = #\request valor my sql
            cotacao = cotacao_dolar
            cotacao = str(cotacao).replace('.',',')
            window['moeda'].update(moeda)
            window['cotacao'].update("R$"+cotacao)
        if(event == 'BTC'):
            moeda = 'Bitcoin'
            cotacao_bitcoin = #\request valor my sql
            cotacao = float(cotacao_bitcoin)
            cotacao = f'{cotacao:_.3f}'
            cotacao = cotacao.replace('.',',').replace('_','.')
            window['moeda'].update(moeda)
            window['cotacao'].update("R$"+cotacao)
        if(event == 'ETH'):
            moeda = 'Etherium'
            cotacao_etherium = #\request valor my sql
            cotacao = float(cotacao_etherium)
            cotacao = f'{cotacao:_.2f}'
            cotacao = cotacao.replace('.',',').replace('_','.')
            window['moeda'].update(moeda)
            window['cotacao'].update("R$"+cotacao)
        if(event == 'EUR'):
            moeda = 'Euro'
            cotacao_euro = #\request valor my sql
            cotacao = cotacao_euro
            cotacao = str(cotacao).replace('.',',')
            window['moeda'].update(moeda)
            window['cotacao'].update("R$"+cotacao)
        if(event == 'GBP'):
            moeda = 'Libra'
            cotacao_libra = #\request valor my sql
            cotacao = cotacao_libra
            cotacao = str(cotacao).replace('.',',')
            window['moeda'].update(moeda)
            window['cotacao'].update("R$"+cotacao)
        if(event == 'JPY'):
            moeda = 'Iene'
            cotacao_iene = #\request valor my sql
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
        valorReais = float(values[0])
        if(event == sg.WIN_CLOSED):
            window.close()
            break
        if(event == 'USD'):
            moeda = 'Dólar'
            cotacao_dolar = #\request valor my sql
            valorConversao = float(valorReais) / float(cotacao_dolar)  
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("$"+valorConversao)
        if(event == 'BTC'):
            moeda = 'Bitcoin'
            cotacao_bitcoin = #\request valor my sql
            valorConversao =  float(valorReais) / float(cotacao_bitcoin)
            valorConversao = str(valorConversao)  
            window['moeda'].update(moeda)
            window['cotacao'].update("BTC "+valorConversao)
        if(event == 'ETH'):
            moeda = 'Etherium'
            cotacao_etherium = #\request valor my sql
            valorConversao =  float(valorReais) / float(cotacao_etherium)
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("ETH "+valorConversao)
        if(event == 'EUR'):
            moeda = 'Euro'
            cotacao_euro = #\request valor my sql
            valorConversao =  float(valorReais) / float(cotacao_euro)
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("€"+valorConversao)
        if(event == 'GBP'):
            moeda = 'Libra'
            cotacao_libra = #\request valor my sql
            valorConversao =  float(valorReais) / float(cotacao_libra)
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("£"+valorConversao)
        if(event == 'JPY'):
            moeda = 'Iene'
            cotacao_iene = #\request valor my sql
            valorConversao =  float(valorReais) / float(cotacao_iene)
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("¥"+valorConversao)
connection = criarConexao("localhost", "root", "root")
paginaInicial()
=======

# Layout
layout = [
    [sg.Text(("Valor das moedas atualizado"), font=('Arial', 25), border_width=5, text_color='grey')],
    [sg.HorizontalSeparator()],
    [sg.Text('', pad=(0,10))],
    [sg.Button('Dolar', size=(15,3), key='USD'), sg.Text('', pad=(2,0)), sg.Button('Euro', size=(15,3), key='EUR'), sg.Text('', pad=(2,0)), sg.Button('Libra', size=(15,3), key='GBP')],
    [sg.Text('', pad=(0,10))],
    [sg.Button('Iene', size=(15,3), key='JPY'),sg.Text('', pad=(2,0)), sg.Button('Bitcoin', size=(15,3), key='BTC'),sg.Text('', pad=(2,0)), sg.Button('Etherium', size=(15,3), key='ETH')],
    [sg.Text('', pad=(0,10))],
    [sg.HorizontalSeparator()],
    [sg.Text((f"Valor da moeda"), font=('Arial', 25), border_width=5, key='moeda', text_color='grey')],
    [sg.Text((""), font=('Arial', 25), border_width=5, key='cotacao', text_color='grey')]
]

# Janela
window = sg.Window('registro', layout, size=(500,500), element_justification='center')

# Funcionamento
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
>>>>>>> 63c1f20bc7226733b386432a73e4ae5bcc819e59
