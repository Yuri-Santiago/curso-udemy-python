"""
1 - Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes desse vetor,
armazenando o resultado em outro vetor, Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.
"""

print('Você deverá digitar 10 números para o vetor a seguir.')
lista = []
for x in range(10):
    num = int(input(f'Digite o número {x+1}: '))
    lista.append(num)

nova_lista = []
for x in range(len(lista)):
    nova_lista.append(lista[x]**2)

print(f'A lista inicial é: {lista}')
print(f'A nova lista é {nova_lista}')
