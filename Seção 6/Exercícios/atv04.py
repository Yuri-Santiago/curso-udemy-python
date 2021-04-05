"""
4 - Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção
dele próprio. Ex: a soma dos divisores do números 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""

n = int(input('Digite um número para calcularmos a soma dos seus divisores: '))

x = 1
divisores = []
while x < n:
    if n % x == 0:
        divisores.append(x)
    x += 1

numeros = []
for x in range(0, len(divisores)):
    numeros.append(str(divisores[x]))

print(' + '.join(numeros))
print(f'= {sum(divisores)}')
