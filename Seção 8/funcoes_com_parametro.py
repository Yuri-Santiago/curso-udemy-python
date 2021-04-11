"""
Funções com Parâmetro (de Entrada)

Funções que recebem dados para serem processados dentro da mesma.

Se a gente pensar em um programa qualquer, geralmente temos:
Entrada -> Processamento -> Saída

Se a gente pensar em uma função, já sabemos que temos funções que:
= Não possuem entrada
- Não possuem saída
- Possuem entrada mas não possuem saída
- Não possuem entrada mas possuem saída
- Possuem entrada e saída
"""

# Refatorando a função quadrado_de_7


def quadrado(num):
    return num ** 2


print(quadrado(7))
print(quadrado(8))
ret = quadrado(9)
print(ret)

# Refatorando a função cantar parabéns


def cantar_parabens(aniversaiante):
    print('Parabéns pra Você')
    print('Nesta Data Querida')
    print('Muitas Felicidades')
    print('Muitos Anos de Vida')
    print(f'Viva o/a {aniversaiante}')


print(cantar_parabens('Yuri'))

# Funções podem ter n parâmetros de entradd. Ou seja, podemos receber como entrada e uma função quantos parâmetros forem
# necessários. Eles são separados por vírgula.

# Exemplos


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(5, 6))
print(soma(10, 11))

print(multiplica(4, 5))
print(multiplica(7, 8))

print(outra(3, 2, 'Yuri '))
print(outra(1, 2, 'Python '))
# OBS: Se a informarmos um número errado de parâmetros ou argumentos, teremos TypeErroe

# Nomeando parâmetros


def nome_completo(nome, sobrenome):  # Mais fácil de identificar do que somente String1 e String2
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Yuri', 'Mateus'))

# A diferença entre parâmetros e argumentos
# Parâmetros são variáveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função

# A ordem dos parâmetros importa!
nome1 = 'Yuri'
sobrenome1 = 'Mateus'

print(nome_completo(sobrenome1, nome1))

# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.

print(nome_completo(nome=nome1, sobrenome=sobrenome1))
print(nome_completo(sobrenome='Mateus', nome='Yuri'))

# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for x in numeros:
        if x % 2 != 0:
            total += x
    return total  # Se esse return estivesse dentro do for, iria terminar a função antes do fim do loop


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(soma_impares(tupla))
