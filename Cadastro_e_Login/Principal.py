import Funcao
from time import sleep

Funcao.Cabeçalho('\033[1;36mFAÇA CADASTRO OU LOGIN: \033[m')
while True:
    try:
        print('\033[1;34m~\033[m'*30)
        print('\033[0;36m1 => Informações\n2 => Cadastro\n3 => Login\n4 => Finalizar\033[m')
        print('\033[1;34m~\033[m'*30)
        opc = int(input('\033[1;33mDigite sua opção: \033[m'))
        if opc != 1 and opc != 2 and opc != 3 and opc != 4:
            print('\033[1;31mERRO: opção excolhida não existe!\033[m')
        if opc == 1:
            print('\033[1;36mInformações: \033[m')
            Funcao.Informar()
        if opc == 2:
            print('\033[1;36mFaça seu cadastro!\033[m')
            Funcao.Cadastro()
        if opc == 3:
            print('\033[1;36mFaça seu login!\033[m')
            Funcao.Login()
        if opc == 4:
            print('\033[1;36mFinalizando...\033[m')
            sleep(3)
            print('\033[1;32mConcluído!\033[m')
            break
    except KeyboardInterrupt:
        print('\033[1;33mExecução interrompida pelo usuário.\033[m')
        break

