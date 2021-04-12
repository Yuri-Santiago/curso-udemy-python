"""
7 - Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule e retorne a soma dos elementos que estão
na diagonal principal.
"""


def diagonal(matriz):
    soma = 0
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if x == y:
                soma += matriz[x][y]
    return soma


lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(diagonal(lista))
