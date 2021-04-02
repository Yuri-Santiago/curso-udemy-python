"""
8 - Faça um programa que receba três números e mostre-os em ordem crescente
"""

print('Digite 3 números para verificarmos a sua ordem.')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2:
    if num2 > num3:
        print(num3, num2, num1)
    else:
        if num1 > num3:
            print(num2, num3, num1)
        else:
            print(num2, num1, num3)
else:
    if num2 < num3:
        print(num1, num2, num3)
    else:
        if num1 > num3:
            print(num3, num1, num2)
        else:
            print(num1, num3, num2)
