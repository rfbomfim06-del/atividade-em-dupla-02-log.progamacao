import os
os.system('cls')

produto = str(input('Digite o nome do produto: '))
preco = float(input('Digite o valor do produto: '))
pagamento = int(input('Digite a forma de pagamento(1/2): '))

match preco:
    case 1:
        0.10 * preco
    case 2:
        