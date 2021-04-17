"""
Dictionary Comprehension

Se quisermos criar um Dictionary fazemos:
{chave:valor for valor in iterável}
"""
# Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrados = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrados)

numero = [1, 2, 3, 4, 5]
quadrado = {valor: valor ** 2 for valor in numero}
print(quadrado)

chaves = 'abcde'
valores = 1, 2, 3, 4, 5
mistura = {chaves[i]: valores[i] for i in range(len(chaves))}
print(mistura)

# Exemplo com Lógica condicional
lista = [1, 2, 4, 5, 6, 7, 8, 9, 10]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in lista}
print(res)
