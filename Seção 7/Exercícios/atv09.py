"""
9 - Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores, guardando-os numa
lista. Ordene o valor assim que ele for digitado. Mostre ao final na tela os valores em ordem.
"""

print('Você terá que digitar 10 números para mim ordená-los.')
lista = []
for x in range(10):
    num = int(input(f'Digite o número {x+1}: '))
    lista.append(num)
    lista.sort()

print(f'A lista completa ordenada é: {lista}')
