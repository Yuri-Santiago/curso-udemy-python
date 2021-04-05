"""
Módulo Collections - Default Dict

# Recap Dicionários:
dicionario = {'nome': 'Yuri Santiago'}

print(dicionario)
print(dicionario['nome'])
print(dicionario['nada'])  # KeyError

Default Dict -> Ao criar um dicionário usando default dict, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um valor definido.
Caso tentamos acessar uma chave que não existe, essa chave será criada e o valor default será atribuído.
"""

# Importando o Collections
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['nome'] = 'Yuri Santiago'
print(dicionario)

print(dicionario['nada'])  # Aqui nã teremos o KeyError do dicionário comum
print(dicionario)
