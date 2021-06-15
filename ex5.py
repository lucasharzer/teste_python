import random, time
print('\033[0;36m=~\033[m'*20)
print('\033[1;34mTente adivinhar um número:\033[m')
print('\033[0;36m=~\033[m'*20)
computador = random.randint(0, 10)
print('Escolha um número aleatório entre \033[0;32m0\033[m e \033[0;32m10\033[m: ')
jogador = int(input('Qual foi o número \033[4;mescolhido?\033[m '))
print('\033[4;30;47mContando...\033[m ')
time.sleep(4)
if jogador > 10:
    print('\033[1;33mNÚMERO INVÁLIDO!\033[m (somente entre 0 e 10), considerando 10: ')
    jogador = 10
if jogador < 0:
    print('\033[1;33mNÚMERO INVÁLIDO\033[m (somente entre 0 e 10), considerando 0: ')
    jogador = 0
if jogador == computador:
    print('\033[0;32mMUITO BEM!\033[m você acertou o número!')
else:
    print('\033[0;31mERROOOOOOOUU!\033[m o número digitado foi \033[0;31;40m{}\033[m e o certo é \033[0;32;40m{}\033[m!'.format(jogador, computador))
print('\033[0;36m=~\033[m'*20)
