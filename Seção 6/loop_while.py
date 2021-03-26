"""
Loop While

Forma geral:
while expressão_booleana:
    // execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso

"""

# Exemplo 1
numero = 1

while numero <= 10:
    print(numero)
    numero += 1
# OBS: Em um loop While é importante que cuidemos do critério de parada para não causar um loop infinito.

# Exemplo 2
resposta = ''

while resposta != 'sim':
    resposta = input('Digite "sim"')
