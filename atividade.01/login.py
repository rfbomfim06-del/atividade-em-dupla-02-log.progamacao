import os
import time
os.system('cls')

login = 'cliente vidaplena'
senha = 'vidaplenaporvoce'

while True:
    print('BEM VINDO OU NOSSO SITE ')
    login = (input('digite o seu login corretamente: '))
    senha = (input('digite sua senha corretamente: '))
    if login == 'cliente vidaplena' and senha == 'vidaplenaporvoce':
        print('login e senha correto')
        break
    else:
        print('login ou senha incorreta! ')
        print(' reiniciando... ')
        time.sleep(1)
        os.system('cls')