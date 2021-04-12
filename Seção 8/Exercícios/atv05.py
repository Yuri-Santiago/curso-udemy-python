"""
5 - Faça uma função que receba um vetor de inteiros e retorne quantos valores pares ele possui.
"""


def pares(numeros):
    contador = 0
    for x in numeros:
        if x % 2 == 0:
            contador += 1
    return contador


print(pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(pares(lista))
