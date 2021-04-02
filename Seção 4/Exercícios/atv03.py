"""
3 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é C = 5.0 * (F - 32.0)/9.0, sendo C a temperatura em Celsius
e F em Fahrenheit.
"""

f = float(input('Digite um grau em Fahrenheit: '))
c = 5.0 * (f - 32.0)/9.0

print(f'Esse valor em Celsius é {c}')
