"""
9 - Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:
    IMC       //       Classificação
   <18.5               Abaixo do Peso
18.6 - 24.9            Saudável
25.0 - 29.9            Peso em excesso
30.0 - 34.9            Obesidade Grau I
35.0 - 39.9            Obesidade Grau II (severa)
   >40.0               Obesidade Grau III (mórbida)
"""

print('Esse programa calcula seu IMC.')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print('Você está Abaixo do Peso')
elif imc < 24.9:
    print('Você está Saudável')
elif imc < 29.9:
    print('Você está com Peso em excesso')
elif imc < 34.9:
    print('Você está com Obesidade de Grau I')
elif imc < 39.9:
    print('Você está com Obesidade de Grau II (severa)')
else:
    print('Você está com Obesidade de Grau III (mórbida)')
