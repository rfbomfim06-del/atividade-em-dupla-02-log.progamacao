import os
os.system('cls')

preco = float(input('Digite o valor do produto: R$'))
print('''
== Formas de Pagamento ==

1 - À vista
2 - À prazo

''')
pagamento = int(input('Digite a forma de pagamento: '))

desconto = preco * 0.10
valor_desconto = preco - desconto

match pagamento:
    case 1:
        avista = desconto
    case _:
        parcela = int(input('\nDigite a quantidade de parcelas que deseja pagar(até 6x): '))
        conta = preco / parcela


match pagamento:
    case 1:
        print(f'Valor do produto: R${preco}')
        print(f'Forma de pagamento: {pagamento}')
        print(f'Valor com desconto: R${desconto}')
        print(f'Total a pagar: R${valor_desconto}')
    case _:
        print(f'Valor do produto: R${preco}')
        print(f'Forma de pagamento: {pagamento}')
        print(f'Quantidade de parcelas: {parcela}')
        print(f'Valor por parcelas: R${conta}')
        print(f'Total à prazo: R${preco}')