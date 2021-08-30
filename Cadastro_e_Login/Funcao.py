import Arquivo
import PySimpleGUI as sg
from time import sleep
from datetime import date

def Cadastro():
    
    arq = 'Banco.txt'

    if not Arquivo.ArquivoExiste(arq):
        Arquivo.CriarArquivo(arq)

    # Tema
    sg.theme('DarkAmber')

    # Layout
    layout1 = [
        [sg.Text('Preencha os campos abaixo:')],
        [sg.Text('Nome:'),sg.Input(key='nome',size=(42,4))],
        [sg.Text('Usuario:'),sg.Input(key='usuario',size=(41,4))],
        [sg.Text('Ano de Nascimento:'), sg.Input(key='anonascimento',size=(31,4))],
        [sg.Text('Senha:'), sg.Input(key='senha',size=(42,4))],
        [sg.Button('Cadastro'), sg.Button('Sair')]
    ]

    # Janela
    janela1 = sg.Window('Cadastro', layout1)

    # Eventos
    while True:
        evento1, valores1 = janela1.read()
        if evento1 == sg.WIN_CLOSED or evento1 == 'Sair': 
            print('\033[1;32mConcluído!\033[m')
            break
        if evento1 == 'Cadastro':
            user = BuscarUsuario(valores1['usuario'], valores1['senha'])
            if user == True:
                print('\033[1;31mERRO: usuário cadastrado já existe\033[m')
                break
            anoatual = date.today().year
            idade = anoatual - int(valores1['anonascimento'])
            Arquivo.Cadastrar(arq, valores1['nome'], valores1['usuario'], idade, valores1['senha'])
    janela1.close()

def Linha(tam = 30):
    return '\033[1;34m-\033[m'*tam

def Cabeçalho(txt):
    print(Linha())
    print(txt.center(30))
    print(Linha())

def BuscarUsuario(login, senha):
    usuarios = []
    try:
        with open('Banco.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                usuarios.append(linha.split())
            for usuario in usuarios:
                nome = usuario[1]
                password = usuario[3]
                if login == nome and senha == password:
                    return True
    except FileNotFoundError:
        return False

def Login():
  # Tema
    sg.theme('DarkAmber')
    # Layout
    layout2 = [
        [sg.Text('Preencha os campos abaixo:')],
        [sg.Text('Usuario:'),sg.Input(key='usuario',size=(41,4))],
        [sg.Text('Senha:'), sg.Input(key='senha',size=(42,4))],
        [sg.Button('Login'), sg.Button('Sair')]
    ]

    # Janela
    janela2 = sg.Window('Login', layout2)

    # Eventos
    while True:
        evento2, valores2 = janela2.read()
        if evento2 == sg.WIN_CLOSED or evento2 == 'Sair': 
            print('\033[1;32mConcluído!\033[m')
            break
        if evento2 == 'Login':
            user = BuscarUsuario(valores2['usuario'], valores2['senha'])
            if user == True:
                print('\033[1;32mLogado com SUCESSO, Bem-Vindo!\033[m')
            else:
                print('\033[1;31musuário ou senha INCORRETOS!\033[m')
    janela2.close()

def Informar():
    # Tema
    sg.theme('DarkAmber')

    # Layout
    layout3 = [
        [sg.Text('Sistema de Cadastro e Login:')],
        [sg.Text('Nesse sistema é possível efetuar o cadastro de usuários;')],
        [sg.Text('Fazer o login do usuário cadastrado;')],
        [sg.Text('Sair do sistema.')],
        [sg.Checkbox('entendi', default=False, key='verificar')],
        [sg.Button('Ok')]
    ]

    # Janela
    janela3 = sg.Window('Informações', layout3)

    # Eventos
    while True:
        evento3, valores3 = janela3.read()
        if valores3['verificar'] == False:
            print('\033[0;36mMarque o campo "entendi" para avançar.\033[m')
        else:
            if evento3 == sg.WIN_CLOSED or evento3 == 'Ok':
                print('\033[1;32mConcluído!\033[m')
                break
    janela3.close()
