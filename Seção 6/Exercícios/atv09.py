"""
9 - Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas
do chamado Triangulo de Floyd. Para n = 6, temos:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""

print('Nesse programa será impresso o Triângulo de Floyd')
linhas = int(input('Digite o número de linhas do triângulo a ser expresso: '))

vezes = 1
num = 1
while vezes <= linhas:
    for x in range(1, vezes+1):
        print(f'{num} ', end=' ')
        num += 1
    print()
    vezes += 1
