print('\033[1;31m-\033[m'*20)
print('  \033[1;34mNÚMERO DE VOGAIS\033[m')
print('\033[1;31m-\033[m'*20)
while True:
    palavra = str(input('\033[0;33mDigite uma palavra:\033[m '))
    cont = 0
    for letra in palavra:
        if letra in 'aâeéíiouãAEÉÍIOUÃÂ':
            cont += 1
    print(f'A palavra \033[1;36m{palavra}\033[m tem \033[1;32m{cont}\033[m vogais.')
    while True:
        print('\033[1;31m-\033[m'*20)
        res = str(input('\033[0;33mQuer continuar? [S/N]\033[m ')).strip().upper()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
    print('\033[1;31m-\033[m'*20)
print('\033[1;31m-\033[m'*20)
print('\033[1;34mFIM!\033[m')



