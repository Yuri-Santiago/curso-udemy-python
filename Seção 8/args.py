"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que comece
com asterisco

Exemplo
*xis

Mas por convenção, utilizamos o *args para defini-lo

Mas o que é o *args?
O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
Então desde já lembre-se que tuplas são imutáveis.
"""

# Exemplo


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(5, 6, 7))

# print(soma_todos_numeros(2, 3))  # TypeError
# print(soma_todos_numeros(2, 3, 4, 5))  # TypeError
# Essa função não é legal, pois se quisessemos somar mais elementos, teríamos que ir adicionando parâmetros

# Utilizando o *args


def soma_tudo(*args):
    return sum(args)


print(soma_tudo(1, 2, 3, 4, 5, 6, 7, 8, 9))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(soma_tudo(numeros))  # Aqui teremos um TypeError

# Podemos usar o desempacotamento
print(soma_tudo(*numeros))
# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
# Desta forma, ele saberá que precisará desempacotar antes os dados.

# Outro exemplo de utiização do *args


def verifica_info(*args):
    if 'Yuri' in args and 'Santiago' in args:
        return 'Bem vindo Yuri!'
    return 'Eu não sei quem você é'


print(verifica_info())
print(verifica_info('Yuri'))
print(verifica_info('Yuri Santiago'))
print(verifica_info('Yuri', 'Mateus'))
print(verifica_info('Yuri', 'Mateus', 'Santiago'))
print(verifica_info('Yuri', 'Santiago'))
