"""
Módulo Collections - Named Tuple

# recap Tupla
tupla = (1, 2, 3)
print(tupla)

Named Tuple -> são tuplas, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros
"""

from collections import namedtuple

# Precisamos definir o nome e parâmetros
# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 - Declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando
toby = cachorro(idade=4, raça='Labrador', nome='Toby')
print(toby)

# Acessando os Dados
# Forma 1
print(toby[0])  # idade
print(toby[1])  # raça
print(toby[2])  # nome

# Forma 2
print(toby.idade)  # idade
print(toby.raça)  # raça
print(toby.nome)  # nome

# Todos os métodos da tupla são válidos aqui
print(toby.index('Labrador'))
print(toby.count('Labrador'))
