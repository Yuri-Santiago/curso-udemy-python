"""
Funções com Retorno

OBS:
- Em Python, quando  uma função não retorna nenhum valor, o retorno é None
- Funções Python que retornam valores, devem retornar estes valores com a palavra reservada 'return'
- Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução
da função para outras funções

- Sobre a palavra reservada return
1 - Ela finaliza a funções, ou seja, ela sai da execução da função
2 - Podemos ter, em uma função, diferentes returns
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores
"""

from random import random

numeros = [1, 2, 3]
ret = numeros.pop()

print(f'Retorno de pop: {ret}')

# ret_errado = print(numeros)  # Print não retorna nada
# print(f'Retorno de print: {ret_errado}')

# Exemplo função


def quadrado_de_7():
    print(7 * 7)


quadrado_de_7()  # Essa função não está sendo retornada, mas só printada

# ret = quadrado_de_7()  # Não há retorno
# print(f'Retorno: {ret}')

# Vamos fazer uma função que retorna algo


def quadrado_de_8():
    return 8*8


# Criamos uma variável para receber o retorno da função
ret = quadrado_de_8()
print(f'O Retorno é: {ret}')

# Sem precisar da variável
print(f'O Retorno é: {quadrado_de_8()}')


# Refatorando a função diz_oi da outra aula


def diz_oi():
    return 'Oi '


# Vantagem do return
alguem = 'Yuri!'
print(diz_oi() + alguem)


# Exemplo de múltiplos returns


def nova_funcao():
    variavel = False
    if variavel:
        return 1
    elif variavel is None:
        return 0
    return -1


print(nova_funcao())

# Exemplo de múltiplos valores no return


def outra_funca():
    return 1, 2, 3


num1, num2, num3 = outra_funca()
print(num1 + num2 + num3)
print(outra_funca())

# Função para jogar uma moeda
# importamos o módulo random


def jogar_moeda():
    valor = random()  # Gera um valor randomico entre 0 e 1
    if valor > 0.5:
        return 'cara'
    return 'coroa'


print(jogar_moeda())

# Erros comuns na utilização do return, que nem é um erro, mas codificação desnecessária


def is_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False  # Aqui não precisamos de um Else, pois não há necessidade


print(is_impar())
