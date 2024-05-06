import mysql.connector
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
