from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ \033[0;34m0\033[m ] \033[0;34mPEDRA\033[m
[ \033[0;35m1\033[m ] \033[0;35mPAPEL\033[m
[ \033[0;36m2\033[m ] \033[0;36mTESOURA\033[m''')
jogador = int(input('Qual é a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('\033[1;33mJOGADA INVÁLIDA\033[m')
else:
    print('\033[0;32mJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!\033[m')
    print('-='*10)
    print('O computador escolheu \033[4;37m{}\033[m'.format(itens[computador]))
    print('O jogador escolheu \033[4;37m{}\033[m'.format(itens[jogador]))
    print('-='*10)
    if computador == 0: # computador jogou pedra
        if jogador == 0:
            print('\033[0;33mEMPATE!\033[m')
        elif jogador == 1:
            print('\033[0;32mJOGADOR VENCE!\033[m')
        elif jogador == 2:
            print('\033[0;31mCOMPUTADOR VENCE!\033[m')
    elif computador == 1: # computador jogou papel
        if jogador == 1:
            print('\033[0;33mEMPATE!\033[m')
        elif jogador == 0:
            print('\033[0;31mCOMPUTADOR VENCE!\033[m')
        elif jogador == 2:
            print('\033[0;32mJOGADOR VENCE!\033[m')
    elif computador == 2: # computador jogou tesoura
        if jogador == 2:
            print('\033[0;33mEMPATE!\033[m')
        elif jogador == 1:
            print('\033[0;31mCOMPUTADOR VENCE!\033[m')
        elif jogador == 0:
            print('\033[0;32mJOGADOR VENCE!\033[m')
