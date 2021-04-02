"""
6 - Leia um número inteiro e imprima a soma do seu sucessor de seu triplo com o antecessor de seu dobro
"""

num = int(input('Digite um número para verificar o cálculo: '))
total = (num * 3 + 1) + (num * 2 - 1)
print(f'a soma do sucessor de seu triplo com o antecessor do dobro de {num} é igual a {total}')
