"""
Conjuntos

- Conjuntos em qualquer linguagem se programação, estamos fazendo referência a Teoria dos Conjuntos em Matemática

- Aqui no Python os conjuntos são chamados de Sets

Dito isso, da mesmsa forma que na matemática:
- Sets não possuem valores duplicados
- Sets não possuem valores ordenados
- Elementos não são acessados via índice, ou seja, Setss não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos,
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e items duplicados

Os Sets são referenciados em Python com chaves {}

Diferença entres Sets e Dicionários
- Os dicionários são chave/valor
- Os conjuntos são apenas valor
"""

# Definindo um conjunto
# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 1})  # Repare que temos valores repetidos

print(s)
print(type(s))
# Obs: Ao criar um conjunto, caso seja acessando um valor já existente,
# o mesmo será ignorado sem gerar erro e não fará parte do conjunto

# Forma 2 - Mais comum
conjunto = {1, 2, 3, 4, 5, 5}
print(conjunto)
print(type(conjunto))

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem
s = {99, 2, 22, 27, 15, 12, 45, 7}
print(s)  # O conjunto não é exibido em sua ordem

# Nós podemos colocar diferentes tipos de dados em Python
misturado = {1, 'b', True, 22.5, None}
print(misturado)

# Podemos iterar em um set normalmente
for x in misturado:
    print(x)

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade não gera erro, mas não adiciona
print(s)

# Remover elementos de um conjunto
# Forma 1
s.remove(2)  # Não é índice, nós informamos o valor a ser removido
print(s)
# Obs: Caso o valor não seja encontrado será gerado um KeyError, nenhum valor é retornado

# Forma 2
s.discard(1)
print(s)
# Obs: Se o valor não for encontrado, não é gerado erro

# Copiando um conjunto para outro
# Forma 1 - Deep Copy
print('Deep Copy')
novo = s.copy()
print(novo)

novo.add(5)

print(novo)
print(s)

# Forma 2 - Shallow Copy
print('Shallow Copy')
novo = s
print(novo)

novo.add(5)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
misturado.clear()
print(misturado)

# Métodos matemáticos de conjuntos
# Imagine que temos dois conjuntos, um conjunto com os alunos de Pythom e outro com os alunos de Java
estudantes_python = {'Yuri', 'Raquel', 'Kelvin', 'Ruann', 'BV', 'Israel'}
estudantes_java = {'Yuri', 'Raquel', 'Pablo', 'Arthur'}

# Veja que alguns alunos que estudam Python também estudam Java
# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)  # Tanto faz qual conjunto está union com o outro
print(unicos1)

# Forma 2 - Utilizando o caractere pipe
unicos2 = estudantes_java | estudantes_python
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos
# Forma 1 - Utilizando o intersection
ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)

# Forma 2 - Utilizando o caractere &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes de um curso que não estão no outro
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma, Maior valor, Menor valor e Tamanho, se o conjunto dor numérico
print(sum(s))
print(max(s))
print(min(s))
print(len(s))