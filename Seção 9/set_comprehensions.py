"""
Set Comprehensions

Sintaxe:
set = {1, 2, 3, 4, 5}
"""

# Exemplos
numeros = {num for num in range(11)}
print(numeros)

valores = {x ** 2 for x in range(11)}
print(valores)

letras = {letra for letra in "Banana"}
print(letras)
