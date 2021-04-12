"""
4 - Faça uma função que receba um número N e retorne a soma dos algarismos de N!.
Ex: se N = 4, N! = 24. Logo, a soma de seus algarismos é 2 + 4 = 6
"""


def funcao(n):
    fatorial = 1
    for x in range(2, n+1):
        fatorial *= x

    fatorial = str(fatorial)
    algarismos = []
    for x in range(len(fatorial)):
        algarismos.append(fatorial[x])

    soma = 0
    for x in range(len(algarismos)):
        soma += int(algarismos[x])

    return soma


print(funcao(4))
