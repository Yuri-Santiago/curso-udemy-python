"""
4 - Faça um programa que mostra ao usuário um menu com 4 opções de operações
matemáticas (as básicas, por exemplo). O usuário escolhe uma da opções e o seu programa
então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo.
"""

print('Bem vindo à Calculadora\nDigite uma operação para iniciarmos\n"+" - Adição\n"-" - Subtração\n'
      '"*" - Multiplicação\n"/" - Divisão')
operacao = input('Digite o caractere da operação')

print('Agora digite os dois valores para completar a opeação.')
num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))

if operacao == '+':
    print(f'A soma de {num1} + {num2} é: {num1+num2}')
elif operacao == '-':
    print(f'A subtração de {num1} + {num2} é: {num1-num2}')
elif operacao == '*':
    print(f'A multiplicação de {num1} + {num2} é: {num1*num2}')
else:
    print(f'A divisão de {num1} + {num2} é: {num1/num2}')
