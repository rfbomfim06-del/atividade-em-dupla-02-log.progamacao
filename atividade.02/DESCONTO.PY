import os
os.system('cls')

total = 0

produto = str(input('Digite o produto escolhido: '))
quantidade = int(input('Digite a quantidade comprada: '))
preco = float(input('Digite o preço do produto: R$'))

if quantidade <= 5:
    desconto = preco * 0.2
elif quantidade <= 10 :
    desconto = preco * 0.3
elif quantidade > 10:
    desconto = preco * 0.5
else:
    print('Inválido!')

total = quantidade * preco

print(f'\nO produto selecionado é: {produto}')
print(f'A quantidade selecionada é: {quantidade}')
print(f'O preço do produto selecionado é: R${preco:.2f}')
print(f'O total é: R${total:.2f}')
print(f'O desconto fornecido é: {desconto:.1f}%')