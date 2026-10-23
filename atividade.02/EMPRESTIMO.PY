import os
os.system('cls')

renda_mensal = float(input('Digite a sua renda mensal: R$'))
emprestimo = float(input('Digite o valor do empréstimo pedido: R$'))
parcelas = int(input('Digite a quantidade de parcelas: '))

prestacao = emprestimo / parcelas
max_emprestimo = renda_mensal * 10
max_prestacao = renda_mensal * 0.3

print(f'O valor da prestação é: R${prestacao:.3f}')

if emprestimo <= max_emprestimo and prestacao <= max_prestacao:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado.')