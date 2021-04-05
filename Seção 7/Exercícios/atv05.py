"""
5 - Leia uma matriz 5 x 5. Leia também um valor X. O prorama deverá fazer uma busca desse valor na matriz e, ao final,
escrever a localização (linha e coluna) ou uma mensagem de "não encontrado".
"""


matriz = []
for x in range(5):
    matriz.append([])
    for i in range(5):
        num = int(input(f'Digite o valor [{x}][{i}]: '))
        matriz[x].append(num)

nao = 0
x = int(input('Digite o valor que você quer buscar na matriz: '))
for y in range(len(matriz)):
    for z in range(len(matriz[y])):
        if x == matriz[y][z]:
            print(f'Valor na posição [{y}][{z}]')
        else:
            nao += 1
if nao == 25:
    print('Valor não encontrado.')
[print(matriz[a]) for a in range(len(matriz))]
