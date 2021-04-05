"""
6 - Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da forma:
A[i][j] = 2i + 7j - 2 se i<j
A[i][j] = 3i^2 - 1 se i=j
A[i][j] = 4i^3 - 5j^2 se i>j
"""

matriz = []
for x in range(10):
    matriz.append([])
    for i in range(10):
        matriz[x].append(0)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i < j:
            matriz[i][j] = (2 * i) + (7 * j) - 2
        elif i > j:
            matriz[i][j] = ((4 * i) ** 3) - ((5 * j) ** 2)
        else:
            matriz[i][j] = ((3 * i) ** 2) - 1

[print(matriz[a]) for a in range(len(matriz))]
