"""
8 - Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 > ... A11, ou seja, está ordenado em ordem
crescente até o sexto elemento, e a partir desse elemento está ordenado em ordem decrescente. Dado o vetor da questão
anterior, proponha um algoritmo para ordenar os elementos.
"""

lista = [10, 6, 7, 2, 9, 5, 1, 11, 3, 8, 4]
lista.sort()
lista.extend(list([lista.pop(x) for x in range(len(lista)-1, 4, -1)]))
print(lista)
