"""
Tipo Float

Tipo Real, Decimal
Possui casas decimais

Obs: O separador de casas decimais na programação é o ponto e não a vírgula
"""

# Errado
valor_errado = 1, 55
print(valor_errado)  # Isso é um tuple

# Certo
valor = 1.55
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 55
print(valor1)
print(valor2)

# Podemos converter um float para int
convertido = int(valor)
print(convertido)  # Obs: ao converter valores perdemos precisão
print(type(convertido))

# Podemos trabalhar com números complexos
complexo = 3j
print(type(complexo))
