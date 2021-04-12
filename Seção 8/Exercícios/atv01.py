"""
1 - Faça uma função que receba dois números e retorne qual deles é maior.
"""


def maior(a, b):
    if a > b:
        return 'O primeiro é maior'
    elif b > a:
        return 'O segundo é maior'
    return 'Os números são iguais'


print(maior(3, 4))
print(maior(6, 5))
print(maior(7, 7))
