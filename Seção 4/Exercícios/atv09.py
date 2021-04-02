"""
9 - Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao
valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu,
o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.
"""

print('Digite quanto cada apostador investiu: ')
num1 = float(input('Apostador 1: '))
num2 = float(input('Apostador 2: '))
num3 = float(input('Apostador 3: '))
aposta_total = num1 + num2 + num3
proporcao1 = num1 / aposta_total
proporcao2 = num2 / aposta_total
proporcao3 = num3 / aposta_total

valor = int(input('Digite o valor total do prêmio: '))
recebe1 = proporcao1 * valor
recebe2 = proporcao2 * valor
recebe3 = proporcao3 * valor

print(f'O primeiro recebeu R${recebe1}\nO segundo recebeu R${recebe2}\nO terceiro recebeu R${recebe3}')
