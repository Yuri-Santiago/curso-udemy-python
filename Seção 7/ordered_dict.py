"""
Módulo Collections - Ordered Dict

Em um dicionário a ordem de inserção não é garantida
No ordered dict você terá a ordem de inserção dos elementos garantida.
"""
# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

# Entendendo a diferença entre Dict e Ordered Dict
# Dicionário comum
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True - já que a ordem dos elementos não importa para o dicionário

# Ordered dict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False - já que a ordem dos elementos impora para o ordered dict
