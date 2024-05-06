import PySimpleGUI as sg
numero_pessoas = 1
valor = 0
percent_gorjeta = 0
soma = 0
verificador = True
def calcula_gorjeta(valor, numero_pessoas, total_extra):
    valor_total = (valor / numero_pessoas) + total_extra
    return valor_total
    verificador = input("Você deseja pagar algum percentual de gorjeta? s/n")
    if(verificador == 's'):
        percent_gorjeta = input("Qual o percentual que voce deseja passar?")
    verificador = input("Você deseja pagar algum extra? s/n")
    if(verificador == 's'):
        extra = input("Qual o total extra que voce deseja passar?")
    total_extra = valor * (percent_gorjeta / 100) + extra
    valor_total = calcula_gorjeta(valor, numero_pessoas, total_extra)
    print(valor_total)

def tabelaComanda():
    # layout
    layout = [
        [sg.Text('Qual o valor da sua comanda?')],
        [sg.Text('Digite O valor'), sg.InputText()],
        [sg.Button('OK'), sg.Button('Sair')]
    ]
    # janela
    window = sg.Window('registro', layout)
    # funcionamento
    while True:
        event, values = window.read()
        valorComanda = float(values[0])
        if(event == sg.WIN_CLOSED or event == 'Sair'):
            window.close()
            break
        if(event == 'OK'):
            window.close()
            break
    window.close()
    return valorComanda
def tabelaDividir():
    # layout
    layout = [
        [sg.Text('Você deseja dividir com quantas pessoas?')],
        [sg.Combo(['Somente eu', '2', '3', '4', '5', '6', '7', '8'])],
        [sg.Button('OK'), sg.Button('Sair')]
    ]
    # janela
    window = sg.Window('registro', layout)
    # funcionamento
    while True:
        event, values = window.read()
        numero_pessoas = int(values[0])
        print(numero_pessoas)
        if(event == sg.WIN_CLOSED or event == 'Sair'):
            window.close()
            break
        if(event == 'OK'):
            window.close()
            break
    return numero_pessoas
def tabelaGorjeta():
    # layout
    layout = [
        [sg.Text('Qual o percentual que você deseja pagar de gorjeta?')],
        [sg.Text('Digite a porcentagem'), sg.InputText()],
        [sg.Button('OK'), sg.Button('Sair')]
    ]
    # janela
    window = sg.Window('registro', layout)
    # funcionamento
    while True:
        event, values = window.read()
        percent_gorjeta = int(values[0])
        print(percent_gorjeta)
        if(event == sg.WIN_CLOSED or event == 'Sair'):
            window.close()
            break
        if(event == 'OK'):
            window.close()
            break
    return percent_gorjeta
def tabelaExtra():
    # layout
    layout = [
        [sg.Text('Deseja pagar algum extra?')],
        [sg.Text('Digite o valor que deseja pagar de extra, se quiser pagar extra.'), sg.InputText()],
        [sg.Button('OK'), sg.Button('Sair')]
    ]
    # janela
    window = sg.Window('registro', layout)
    # funcionamento
    while True:
        event, values = window.read()
        extra = int(values[0])
        print(percent_gorjeta)
        if(event == sg.WIN_CLOSED or event == 'Sair'):
            window.close()
            break
        if(event == 'OK'):
            window.close()
            break  
    return extra
def tabelaValor(valor, extra, valor_total, pessoas):
    # layout
    layout = [
        [sg.Text((f"O valor total da comanda deu R${valor}"), font=('Arial', 25), border_width=5, background_color='grey')],
        [sg.Text((f"O valor dos acrecimos R$ {extra}"), font=('Arial', 25), border_width=5, background_color='grey')],
        [sg.Text((f"O valor total foi R${valor_total}"), font=('Arial', 25), border_width=5, background_color='grey')],
        [sg.Text((f"Cada um devera pagar R${pessoas}"), font=('Arial', 25), border_width=5, background_color='grey')],
        [sg.Button('Pagar')]
    ]
    # janela
    window = sg.Window('registro', layout)
    # funcionamento
    while True:
        event, values = window.read()
        if(event == sg.WIN_CLOSED):
            window.close()
            break
        if(event == 'Pagar'):
            window.close()
            break  
def tabelaVerificacao():
        # layout
    layout = [
        [sg.Text('Deseja fazer outro pagamento?')],
        [sg.Button('Sim'), sg.Button('Não')]
    ]
    # janela
    window = sg.Window('registro', layout)
    # funcionamento
    while True:
        event, values = window.read()
        if(event == sg.WIN_CLOSED or event == 'Não'):
            verificador = False
            window.close()
            break
        if(event == 'Sim'):
            verificador = True
            window.close()
            break  
    return verificador
while verificador == True:
    valor = tabelaComanda()
    numero_pessoas = tabelaDividir()
    percent_gorjeta = tabelaGorjeta()
    extra = tabelaExtra()
    total_extra = valor * (percent_gorjeta / 100) + extra
    valor_total = valor + total_extra
    total_por_pessoa = valor_total / numero_pessoas
    tabelaValor(valor,total_extra, valor_total, total_por_pessoa)
    verificador = tabelaVerificacao()
    

