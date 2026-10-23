import os
os.system('cls')

while True:
    primeiro_numero = float(input('Digite o 1º número: '))
    segundo_numero = float(input('Digite o 2º número: '))
    operador = str(input('Digite o operador escolhido: '))

    match operador:

        case '+':
            resultado = primeiro_numero + segundo_numero
            break
        case '-':
            resultado = primeiro_numero - segundo_numero
        case '*':
            resultado = primeiro_numero * segundo_numero
            break
        case '/':
            resultado = primeiro_numero / segundo_numero
            break
        case _:
            print('Opção inválida!')
            break


    print(f'O 1º número é: {primeiro_numero}')
    print(f'O 2º número é: {segundo_numero}')
    print(f'O operador escolhido é: {operador}')
    print(f'O resultado é: {resultado}')