"""
1 - Faça um programa peça ao usuário para digitar 10 valores e some-os.
"""

x = 0
soma = 0
while x < 10:
    print('Digite um número para ser somado: ')
    num = int(input(f'Número {x+1}: '))
    soma += num
    x += 1
print(f'A soma total é igual a: {soma}')
