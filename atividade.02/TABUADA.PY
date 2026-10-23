import os
import time
os.system('cls')

print('== TABUADA ==')

tabuada = int(input('Digite um número: '))
for i in range(1, 11):
    time.sleep(1)
    print(f'{tabuada} x {i} = {tabuada * i}')