"""
Ranges

- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada

Formas gerais:

# Forma 1
range(valor final)

obs: valor final não incluso, início padrão 0, passo de 1 em 1

# Forma 2
range(valor inicial, valor final)

obs: valor final não incluso, início especificado, passo de 1 em 1

# Forma 3
range(valor inicial, valor final, passo)

obs: valor final não incluso, início especificado, passo especificado

# Forma 4 (Inverso)
range(valor inicial, valor final, passo inverso)

obs: valor final não incluso, início especificado, passo especificado
"""

# Forma 1
for num in range(11):
    print(num)

# Forma 2
for num in range(5, 11):
    print(num)

# Forma 3
for num in range(6, 11, 2):
    print(num)

# Forma 4
for num in range(10, 5, -1):
    print(num)
