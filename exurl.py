import urllib
import urllib.request
from time import sleep
import webbrowser

print('\033[0;36m~\033[m'*30)
print('\033[0;34mSITE PUDIM...\033[m'.center(40))
print('\033[0;36m~\033[m'*30)
sleep(3)
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('\033[1;31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[1;32mConsegui acessar o site Pudim com sucesso!\033[m')
    print('\033[1;32mInformações: \033[m')
    sleep(3)
    print(site.read())
    print('\033[1;32mAbrindo o site em 3, 2, 1...\033[m')
    sleep(3)
    webbrowser.open('http://www.pudim.com.br/', new=2)
    print('\033[1;32;40mPronto!\033[m')
finally:
    print('\033[1;33mMuito Obrigado!\033[m')