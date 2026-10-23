import os
os.system('cls')

QUANTIDADE_DE_REPEDICAO = (5)
pares = 0
impares = 0
soma = 0
for i in range(QUANTIDADE_DE_REPEDICAO):
    numero = int(input("digite o numero: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    soma = numero + soma
print(f'quatidade de pares:{pares}')
print(f'quatidade de impares:{impares}')
print(f'soma:{soma}')

