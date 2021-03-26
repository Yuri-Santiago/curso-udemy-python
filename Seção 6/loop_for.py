"""
Loop For

loop -> Estrutura de Repetição
for -> Uma dessas Estruturas

Usando o for
for item in interavel
    execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
- Listas
- Range
"""

# Exemplo de for 1: iterando em uma String
nome = 'Yuri Santiago'
for letra in nome:
    print(letra, end=' ')
print()

# Exemplo de for 2: iterando em uma Lista
lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(numero)

# Exemplo de for 3: iterando em um Range
for numero in range(1, 10):  # Obs: o valor final não é incluso no range
    print(numero)

# Trabalhando com índices em Strings
for i, v in enumerate(nome):
    print(nome[i])
