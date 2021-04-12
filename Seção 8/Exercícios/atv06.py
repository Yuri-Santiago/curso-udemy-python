"""
6 - Crie um programa que receba três valores (obrigatoriamente maiores que zero), representando as medidas dos três
lados de um triângulo. Elabore funções para:
a) Determinar se esses lados formam um triângulo, sabendo que:
- O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados
b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo. Sendo que:
- Chama-se equilátero o triângulo que tem três lados iguais
- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais
- Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""


def verifica_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    return False


def tipo_triangulo(a, b, c):
    if a == b and b == c:
        return 'Triângulo Equilátero'
    elif a == b or a == c or b == c:
        return 'Triângulo Isósceles'
    return 'Trângulo Escaleno'


triangulo = [6, 8, 10]
verificacao = verifica_triangulo(*triangulo)

if verificacao:
    print(f'O tipo do seu Triângulo é: {tipo_triangulo(*triangulo)}')
else:
    print('Esses valores não formam um Triângulo')
