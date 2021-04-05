"""
4 - Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5 * i)%(i + 1), sendo i a posição do elemento no
vetor. Em seguida imprima o vetor na tela.
"""

vetor = []

for i in range(50):
    num = (i + 5 * i) % (i + 1)
    vetor.append(num)

print(f'A lista final é: {vetor}')
