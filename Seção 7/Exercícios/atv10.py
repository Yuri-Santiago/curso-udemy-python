"""
10 - Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado
Triangulo de Pascal
"""

num = int(input('Digite um número para ser a quantidade de linhas do Triangulo de Pascal: '))

linhas = 0
atual = [1]
anterior = []
while linhas < num:
    for x in atual:
        print(x, end=' ')

    anterior = atual.copy()
    atual.clear()
    y = 0
    for i in range(len(anterior)):
        atual.append(y+anterior[i])
        y = anterior[i]
    atual.append(1)
    print()
    linhas += 1
