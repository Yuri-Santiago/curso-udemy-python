"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável

# Sintaxe da List Comprehension
[ dado for dado in iterável ]

Nós podemos adicionar estruturas condicionais lógicas na List Comprehension
"""

# Exemplo
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)

res2 = [numero / 2 for numero in numeros]
print(res2)


def funcao(valor):
    return valor * valor


res3 = [funcao(numero) for numero in numeros]
print(res3)

# Outros Exemplos

nome = 'Yuri Santiago'
print([letra.upper() for letra in nome])

amigos = ['raquel', 'israel', 'kelvin', 'pablo', 'yuri']
print([amigo.title() for amigo in amigos])

print([numero * 3 for numero in range(1, 11)])

print([bool(valor) for valor in [0, 1, [], 'True', '']])

print([str(numero) for numero in [1, 2, 3, 4, 5]])

# Exemplos com estruturas lógicas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

resultado = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(resultado)
