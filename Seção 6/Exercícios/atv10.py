"""
10 - Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros números primos.
"""

n = int(input('Digite um número para calcularmos a soma dos números primos dessa quantidade: '))
primos = {2}
x = 3

while len(primos) < n:
    for y in range(2, x):
        if x % y == 0:
            break
        else:
            primos.add(x)
    x += 1
print(primos)
