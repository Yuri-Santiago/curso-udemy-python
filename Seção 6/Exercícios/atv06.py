"""
5 - Faça um  programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o
quadrado da soma.
"""

x = 1
soma = 0
quadrados = 0
while x <= 100:
    soma += x
    quadrados += x**2
    x += 1

total = soma**2 - quadrados
print(f'O valor total é {total}')
