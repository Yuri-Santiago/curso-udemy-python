"""
Funções com Parâmetro Padrão (Default Parameters)

Funções onde a passagem de parâmetro seja opcional

Por quê utilizar parâmetros com valor default?
- Nos permite ser mais flexíveis nas funções
- Evita erros com argumentos incorretos
- Nos permite trabalhar com exemplos mais legíveis de código

Quais tipos de dados podemos utilizar como valores default para parâmetros
- Qualquer tipo de dado: Números, Strings, Floats, Booleans, Lists, Tuples, Dicts Funções e Etc
"""

# Exemplo de função onde a passagem de parâmetros seja opcional
print('Yuri Mateus')
print()

# Exemplo de função onde a passagem de parâmetro é obrigatória


def quadrado(numero):
    return numero ** 2


print(quadrado(5))
# print(quadrado()) Type Error

# Criando uma função com parâmetro padrão


def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 5))  # Eleva à potencia informada pelo usuário
print(exponencial(3, 2))

print(exponencial(4))  # Por padrão eleva ao quadrado
# OBS: Se o usuário informar somente um argumento, ele será atribuído ao parâmetro número, e a potência será a padrão,
# se for informado dois valores no argumento, a potência padrão será substituída.

# OBS: Em funções Python, os parâmetros com valores default (padrão) devem sempre estar no final da declaração.
# ERRO:
"""
def teste(num=2, potencia)
    return num ** potencia
"""

# Outro exemplos


def soma(num1=0, num2=0):
    return num1 + num2


print(soma(3, 5))
print(soma(4))
print(soma())

# Exemplo mais complexo


def mostra_informacao(nome='Yuri', aluno=False):
    if nome == 'Yuri' and aluno:
        return 'Bem Vindo aluno Yuri'
    elif nome == 'Yuri':
        return 'Eu pensei que você era o aluno'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(aluno=True))
print(mostra_informacao('João'))

# Exemplo de função como parâmetro


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(5, 3))
print(mat(5, 3, subtracao))

# Escopo - Evitar problemas e confusões
# Variáveis Globais
# Variáveis Locais

nome = 'Yuri'  # Variável Global


def diz_oi():
    nome = 'João'  # Variável Local
    return f'Oi {nome}'


print(diz_oi())
# OBS: se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

# Outri exemplo


def cumprimento():
    prof = 'Serra'  # Variável Local
    return f'Oi {prof}'


print(cumprimento())
# print(prof)  # Name error

# ATENÇÃO com variáveis globais (Se puder evitar, evite!)
"""
total = 0

def incrementa():
    total = total + 1  # A variável local está sendo utilizada para processamento sem ter sido inicializada
    return total


print(incrementa())
"""

total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável Global

    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável
"""
def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()


print(fora())
"""
# OBS: Isso não é nada comum mas existe