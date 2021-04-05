"""
8 - Leia um número positivo do usuário, então, calcule e imprima a sequência Finonacci
até o primeiro número syperior ao número lido. Exemplo: se o usuário informou o número 30,
a sequência a ser impressa será 0 1 1 2 3 5 8 13 21 34.
"""

num = int(input('Digite um número para ser a parada da nossa sequência Fibonacci: '))
x = 0
y = 1

while True:
    print(f'{x} ', end=' ')
    if x > num:
        break
    x = x + y

    print(f'{y} ', end=' ')
    if y > num:
        break
    y = y + x
