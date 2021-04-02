"""
Tuplas

Tuplas são bastante parecidas com listas

Existem duas diferenças básicas:
- As tuplas são representadas por parênteses ()
- As tuplas são imutáveis, ou seja, ao se criar uma tupla ela não muda. Toda operação em uma tuplas gera uma nova tupla

Por quê utilizar Tuplas?
- Tuplas são mais rápidas do que listas
- Tuplas deixam seu código mais seguro, pois trabalhar com elementos imutáveis traz esse benefício
"""

# Cuidado 1: As tuplas são representadas por parênteses, mas veja:
tupla1 = (1, 2, 3, 4, 5)
print(type(tupla1))

tupla2 = 6, 7, 8, 9, 10
print(type(tupla2))

print(tupla1)
print(tupla2)

# Cuidado 2: Tuplas com 1 elemento
tupla3 = (2)  # Isso não é uma tupla
print(type(tupla3))

tupla4 = (2, )  # Isso é um tupla
print(type(tupla4))

print(tupla3)
print(tupla4)
# Podemos definir que tuplas são definidas pela vírgula e não pelo parênteses.

# Podemos usar o range para criar uma tupla
tupla = tuple(range(1, 11))
print(tupla)

# Desempacotamento de tupla
nome_completo = ('Yuri', 'Santiago')
nome, sobrenome = nome_completo
print(nome)
print(sobrenome)
# Obs: Gera erro se colocarmos um número diferente de elementos e variáveis

# Métodos para adição e remoção de elementos nas tuplas não existem, pois elas são imutáveis
# Os metodos de soma, valor máximo, mínimo e tamanho são válidos nos inteiros
print(sum(tupla1))
print(min(tupla1))
print(max(tupla1))
print(len(tupla1))

# Concatenação de Tuplas
print(tupla1 + tupla2)  # Tuplas são imutáveis
# Obs: estou imprimindo as duas tuplas juntas, mas não estou mudando o valor delas

tupla1 = tupla1 + tupla2  # Tuplas são imutáveis, mas podemos sobescrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla
print(2 in tupla1)

# Iterando sobre uma tupla
for n in tupla2:
    print(n)

for indice, numero in enumerate(tupla1):
    print(indice, numero)

# Contando elementos dentro de uma tupla
letras = ('a', 'b', 'c', 'a', 'd', 'a', 'b')
print(letras.count('a'))

# Dicas na utilização de Tuplas
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
# Exemplo
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
# Não faz sentido um novo mês poder ser modificado

# O acesso a elementos de uma tupla também é semelhante a de uma lista
print(meses[11])

# Iterar com o while
i = 0
while i < len(meses):
    print(meses[1])
    i += 1

# Verificamos em qual índice um elemento está na Tupla
print(meses.index('Julho'))
# Obs: Caso o elemento não exista será gerado um erro

# Slicing
print(meses[6:11])

# Copiando uma Tupla para outra
print(tupla2)

nova = tupla2  # Na tupla não existe o Shallow Copy
print(nova)
print(tupla2)

nova = nova + tupla1
print(nova)
print(tupla2)
