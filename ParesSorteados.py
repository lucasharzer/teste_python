from random import randint
from time import sleep

print('\033[1;33mSoma dos valores pares sorteados:\033[m')

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True) # obriga a liberar o buffer (buffer: guarda os dados que recebe sem mostrá-los)
        sleep(0.5)
    print('\033[1;33mPRONTO!\033[m')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
