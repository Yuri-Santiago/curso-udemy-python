"""
2 - Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N
em ordem crescente.
"""

n = int(input('Digite um valor N ímpar e positivo: '))

if n < 0 or n % 2 == 0:
    print('Número inválido')
else:
    x = 1
    while x <= n:
        print(x, end=' ')
        x += 2
