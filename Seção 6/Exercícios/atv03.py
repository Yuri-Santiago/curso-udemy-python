"""
3 - Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número
foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""

print('Você deverá digitar uma quantidade de números e mostrarei o maior deles e quantas vezes ele aparece.')
n = int(input('Digite o número de vezes que você quer digitar os números: '))
print('Agora vamos para os números.')

x = 0
numeros = []
while x < n:
    num = int(input(f'Digite o número {x+1}: '))
    numeros.append(num)
    x += 1

maior = max(numeros)
print(f'O maior valor foi: {maior}')
print(f'A quantidade de vezes que o número apareceu foi: {numeros.count(maior)}')
