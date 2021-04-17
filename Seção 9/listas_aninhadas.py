"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays
    - Unidimensionais (Arrays / Vetores)
    - Multidimensionais (Matrizes)

Em Python nós temos as Listas
Mas e as Matrizes?
"""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print(listas)
print(type(listas))

# Como acessamos os dados?
print(listas[0][1])  # Acesso parecido com Matrizes
print(listas[2][0])

# Iterando em uma Lista Aninhada
for lista in listas:
    for numero in lista:
        print(numero, end=', ')
print()

# List Comprehension
[[print(valor, end=', ') for valor in lista] for lista in listas]
print()

# Gerando uma matriz 3x3
tabuleiro = [[numero for numero in range(3)] for valor in range(3)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)
