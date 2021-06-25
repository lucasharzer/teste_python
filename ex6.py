from random import randint
print('=-'*17)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*17)
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    while True:
        e = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        if e in 'PIip':
            break
    computador = randint(1, 10)
    soma = jogador + computador
    print('-'*17)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}: ', end='')
    if soma % 2 == 0:
        print('DEU PAR!')
        print('-'*17)
        if e == 'P':
            v += 1
            print('Você VENCEU!\nVamos jogar novamente...')
        else:
            print('Você PERDEU!')
            break
    else:
        print('DEU ÍMPAR!')
        print('-'*17)
        if e == 'I':
            v += 1
            print('Você VENCEU!\nVamos jogar novamente...')
        else:
            print('Você PERDEU!')
            break
    print('=-'*17)
print('=-'*17)
if v == 1:
    print('GAME OVER! Você venceu \033[1;32m1\033[m vez.')
else:
    print(f'GAME OVER! Você venceu \033[1;32m{v}\033[m vezes.')


