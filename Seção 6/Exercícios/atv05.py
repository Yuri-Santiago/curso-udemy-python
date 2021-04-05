"""
4 - Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20?
Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.
"""

passe = 0
divisivel = 0
x = 1
numeros = list(range(1, 21))
while passe < 1:
    for i in range(0, len(numeros)):
        if x % numeros[i] == 0:
            divisivel += 1
        else:
            divisivel = 0
    if divisivel == len(numeros):
        passe = 2
        print(f'O número é {x}')
    x += 1
