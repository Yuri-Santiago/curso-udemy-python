"""
Mapas -> São conhcecidos em Python comoDicionários

Dicionários em Python são representados por chaves {}
"""

receita = {'jan': 100, 'fev': 150, 'mar': 200}
print(receita)

# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi: R${receita[chave]}')

# Agora o modo Pythonico de fazer isso tudo
# Acesso a todas as chaves
print(receita.keys())
for chave in receita.keys():
    print(chave)

# Acessando os valores
print(receita.values())
for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários
print(receita.items())
for chave, valor in receita.items():
    print(f'Em {chave} recebi: R${valor}')

# Soma, Valor Máximo, valor Mínimo, Tamanho
# Só podemos usar os três primeiros se o valor for do tipo numérico

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
