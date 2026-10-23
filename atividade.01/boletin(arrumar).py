import os
os.system('cls')

QUANTIDADE_DE_REPETICAO = 3
soma = 0
for i in range(QUANTIDADE_DE_REPETICAO):
    while True:
        nota =float(input("digite a sua nota: "))
        if nota >= 0 or nota <= 10:
            print()
            break
        else:
            print()
            print(' NOTA INVALIDA! ')
            soma = soma = soma + nota

media = nota / QUANTIDADE_DE_REPETICAO

print(f'media:{media}')
