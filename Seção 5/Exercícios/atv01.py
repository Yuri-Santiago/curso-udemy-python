"""
1 - Leia um número forrnecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""

import math

num = int(input('Digite um número'))

if num > 0:
    print(f'A raiz quadrada do número é: {math.sqrt(num)}')
else:
    print('Número inválido, tente novamente')
