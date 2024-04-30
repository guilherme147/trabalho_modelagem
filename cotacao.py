import requests as rq
import pandas as pd
import PySimpleGUI as sg
sg.theme('Reddit')
moeda = ''
cotacao = 0.0
    # layout
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
    [sg.Text((f"R${cotacao}"), font=('Arial', 25), border_width=5, key='cotacao', text_color='grey')]
]

# janela
window = sg.Window('registro', layout, size=(500,500), element_justification='center')
# funcionamento
while True:
    event, values = window.read()
    requisicao = rq.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL,BTC-BRL,JPY-BRL,ETH-BRL")
    requisicao_dic = requisicao.json()
    if(event == sg.WIN_CLOSED):
        window.close()
        break
    if(event == 'USD'):
        moeda = 'Dólar'
        cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
        cotacao = cotacao_dolar
        cotacao = str(cotacao).replace('.',',')
        window['moeda'].update(moeda)
        window['cotacao'].update("R$"+cotacao)
    if(event == 'BTC'):
        moeda = 'Bitcoin'
        cotacao_bitcoin = requisicao_dic["BTCBRL"]["bid"]
        cotacao = float(cotacao_bitcoin)
        cotacao = f'{cotacao:_.3f}'
        cotacao = cotacao.replace('.',',').replace('_','.')
        window['moeda'].update(moeda)
        window['cotacao'].update("R$"+cotacao)
    if(event == 'ETH'):
        moeda = 'Etherium'
        cotacao_etherium = requisicao_dic["ETHBRL"]["bid"]
        cotacao = float(cotacao_etherium)
        cotacao = f'{cotacao:_.2f}'
        cotacao = cotacao.replace('.',',').replace('_','.')
        window['moeda'].update(moeda)
        window['cotacao'].update("R$"+cotacao)
    if(event == 'EUR'):
        moeda = 'Euro'
        cotacao_euro = requisicao_dic["EURBRL"]["bid"]
        cotacao = cotacao_euro
        cotacao = str(cotacao).replace('.',',')
        window['moeda'].update(moeda)
        window['cotacao'].update("R$"+cotacao)
    if(event == 'GBP'):
        moeda = 'Libra'
        cotacao_libra = requisicao_dic["GBPBRL"]["bid"]
        cotacao = cotacao_libra
        cotacao = str(cotacao).replace('.',',')
        window['moeda'].update(moeda)
        window['cotacao'].update("R$"+cotacao)
    if(event == 'JPY'):
        moeda = 'Iene'
        cotacao_iene = requisicao_dic["JPYBRL"]["bid"]
        cotacao = cotacao_iene
        cotacao = str(cotacao).replace('.',',')
        window['moeda'].update(moeda)
        window['cotacao'].update("R$"+cotacao)
