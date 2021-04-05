"""
7 - Elabore um programa que faça leitura de váriaos números inteiros. até que se digite um número negativo.
O programa tem que retornar o maior e o menor número lido.
"""

print('Nesse programa você poderá inserir vários números até que se digite um número negativo para sair.')
num = int(input('Digite o primerio número para começarmos: '))
maior = num
menor = num

while num >= 0:
    num = int(input('Digite um número qualquer, e um negativo para sair: '))
    if num >= 0:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'O maior número digitado foi: {maior}\nO menor número digitado foi: {menor}')
