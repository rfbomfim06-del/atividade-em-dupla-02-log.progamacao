import os
os.system('cls')

renda_mensal = float(input('Digite a sua renda mensal: R$'))
emprestimo = float(input('Digite o valor do empréstimo pedido: R$'))
parcelas = int(input('Digite a quantidade de parcelas: '))

max_emprestimo = renda_mensal * 10
max_parcelas = renda_mensal * 0.3

print(f'O valor da prestração é: {parcelas}')

if emprestimo <= max_emprestimo:
    print('Valor aceito!')
else:
    print('Valor inválido.')

if parcelas <= max_parcelas:
    print('Parcelas aceitas!')
else:
    print('Quantidade de parcelas negadas!')
