import requests as rq
import pandas as pd
import PySimpleGUI as sg
sg.theme('Reddit')
def criaCotacao():
    layout = [
    [sg.Button('jogo', key='jogo')]
    ]      
    return layout    
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
        requisicao = rq.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL,BTC-BRL,JPY-BRL,ETH-BRL")
        requisicao_dic = requisicao.json()
        if(event == sg.WIN_CLOSED):
            window.close()
            break
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
        requisicao = rq.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL,BTC-BRL,JPY-BRL,ETH-BRL")
        requisicao_dic = requisicao.json()
        if(event == sg.WIN_CLOSED):
            window.close()
            break
        if(event == 'USD'):
            moeda = 'Dólar'
            cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
            valorConversao = float(valorReais) / float(cotacao_dolar)  
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("$"+valorConversao)
        if(event == 'BTC'):
            moeda = 'Bitcoin'
            cotacao_bitcoin = requisicao_dic["BTCBRL"]["bid"]
            valorConversao =  float(valorReais) / float(cotacao_bitcoin)
            valorConversao = str(valorConversao)  
            window['moeda'].update(moeda)
            window['cotacao'].update("BTC "+valorConversao)
        if(event == 'ETH'):
            moeda = 'Etherium'
            cotacao_etherium = requisicao_dic["ETHBRL"]["bid"]
            valorConversao =  float(valorReais) / float(cotacao_etherium)
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("ETH "+valorConversao)
        if(event == 'EUR'):
            moeda = 'Euro'
            cotacao_euro = requisicao_dic["EURBRL"]["bid"]
            valorConversao =  float(valorReais) / float(cotacao_euro)
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("€"+valorConversao)
        if(event == 'GBP'):
            moeda = 'Libra'
            cotacao_libra = requisicao_dic["GBPBRL"]["bid"]
            valorConversao =  float(valorReais) / float(cotacao_libra)
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("£"+valorConversao)
        if(event == 'JPY'):
            moeda = 'Iene'
            cotacao_iene = requisicao_dic["JPYBRL"]["bid"]
            valorConversao =  float(valorReais) / float(cotacao_iene)
            valorConversao = str(valorConversao)
            window['moeda'].update(moeda)
            window['cotacao'].update("¥"+valorConversao)
paginaInicial()