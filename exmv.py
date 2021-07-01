print('\033[1;34mMAIORES, MENORES VALORES E POSIÇÕES\033[m')
print('\033[0;32m=-\033[m'*40)
valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('\033[0;32m=-\033[m'*40)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == max(valores):
        print(f'{pos}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == min(valores):
        print(f'{pos}... ', end='')
