import Funcao

def ArquivoExiste(nome):
    try: 
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True

def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[1;31mHouve um ERRO ao tentar criar arquivo!\033[m')
    else:
        print(f'\033[1;32mArquivo {nome} criado com sucesso!\033[m')

def LerArquivo(nome):
    try:
        a = open(nome, 'rt') 
    except:
        print('Erro ao ler o arquivo')
    else:
        Funcao.Cabeçalho('Pessoas Cadastradas')
        #print(a.read())  readLines coloca tudo dentro de uma lista
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[2]:>3} anos')
    finally:
        a.close()

def Cadastrar(arq, nome, usuario, idade, senha):
    try:
        a = open(arq, 'at')
    except:
        print('\033[1;31mHouve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome} {usuario} {idade} {senha}\n')
        except:
            print('\033[1;31mHouve um ERRO ao escrever os dados!\033[m')
        else:
            print(f'\033[1;32mRegistro de {nome} cadastrado com sucesso!\033[m')
            a.close()