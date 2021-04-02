"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem dinâmico,
também podermos colocar qualquer tipo de dado e as listas aceitam repetições.

- Dinâmico: Não possui tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando elementos.
- Qualquer tipo de dado? Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.

As listas em Python são representadas por colchetes: []
As listas são mutáveis, ou seja, podem mudar constantemente
"""

print(type([1, 2, 3]))

lista_um = [5, 9, 20, 14, 22, 27, 33, 2, 1, 12, 0, 2]

lista_dois = ['Y', 'u', 'r', 'i', ' ', 'S', 'a', 'n', 't', 'i', 'a', 'g', 'o']

lista_tres = []

lista_quatro = list(range(11))

lista_cinco = list('Yuri Mateus')

# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista_quatro:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Métodos #

# Podemos ordenar uma lista
lista_um.sort()
print(lista_um)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista_um.count(2))
print(lista_dois.count('i'))

# Podemos adicionar elementos em listas, nós utilizamos a função append, mas só podemos adicionar um elemento por vez.
print(lista_um)
lista_um.append(25)
print(lista_um)

lista_um.append([7, 4, 6])  # Coloca a lista como elementos único (sublista)
print(lista_um)
if [7, 4, 6] in lista_um:
    print('Encontrei na lista')
else:
    print("Não encontrei na lista")

lista_um.extend([122, 42, 50])  # Coloca elementos da lista como valor adicional à lista
print(lista_um)

# Podemos inserir um novo elemento na lista informando a posição do índice
lista_um.insert(2, 99)
print(lista_um)

# Podemos facilmente juntar duas listas
lista_um += lista_quatro
print(lista_um)

# Podemos facilmente inverter uma lista
lista_um.reverse()
print(lista_um)

# Podemos copias uma lista
lista_seis = lista_cinco.copy()
print(lista_seis)

# Podemos contar a lista
print(len(lista_um))

# Podemos remover o último elemento de uma lista
# Obs: o pop remove e retorna o último elemento da lista
lista_seis.pop()
print(lista_seis)

# Podemos remover um elemento pelo índice
# Obs: Os elementos à direita deste indíce serão deslocados para a esquerda, se não tiver elemento no indíce dará erro
lista_seis.pop(4)
print(lista_seis)

# Podemos remover todos os elementos da lista
lista_um.clear()
print(lista_um)

# Podemos facilmente repetir elementos em uma lista
lista_um = [1, 2, 3]
lista_um *= 3
print(lista_um)

# Podemos converter uma String para uma lista
#   Exemplo 1
curso = 'Programação em Python essencial'
curso = curso.split()
print(curso)
# Obs: por padrão o split separa as palavras pelo espaço

#   Exemplo 2
curso = 'Programação,em,Python,essencial'
curso = curso.split(',')

# Convertendo uma lista em uma String
curso = ' '.join(curso)  # Aqui nós estamos pegando a lista curso e colocando um espaço entre cada elemento.
print(curso)

# Iterando sobre listas
#   Exemplo 1
soma = ''
for elemento in lista_dois:
    soma += elemento
print(soma)

#   Exemplo 2
carrinho = []
produto = ''
while produto != 'sair':
    print('Adicione um produto ou digite "sair" para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

print(f'O seu carrinho de compras é {carrinho}')

# Adicionando variáveis em listas
num_um = 1
num_dois = 2
num_tres = 3

numeros = [num_um, num_dois, num_tres]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
cores = ['azul', 'vermelho', 'amarelo', 'verde']
print(cores[2])
print(cores[1])

# Fazer acesso aos elementos de forma indexada inversa
print(cores[-1])
print(cores[-4])

# Encontrar o indíce de um elemento da lista
print(lista_um.index(3))
#   Obs: caso não tenha esse número na lista ocorrerá um erro
print(lista_um.index(3, 4))
#   Podemos buscar a partir de um index inicial e não do começo da lista
print(lista_um.index(2, 3, 5))
#   Podemos colocar valor inicial e final da busca

# Também podemos utilizar o slice em listas
print(lista_um[1:7:2])

# Trocando valores de uma lista
nomes = ['Santiago', 'Yuri']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

# Obter soma, valor mínimo, máximo e tamanho de uma lista númerica
print(sum(lista_um))
print(min(lista_um))
print(max(lista_um))
print(len(lista_um))

# Transformar uma lista em tupla
tupla = tuple(lista_um)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
lista_um = [1, 2, 3]
num1, num2, num3 = lista_um
print(num1, num2, num3)
# Obs: se tivermos valore diferentes de elementos e variavéis ocorre um erro

# Copiando uma lista para outra: Shallow Copy e Deep Copy
print('Exemplo 1: Deep Copy')
lista = [1, 2, 3]
print(lista)

lista_copia = lista.copy()
print(lista_copia)

lista_copia.append(4)

print(lista)
print(lista_copia)
# Veja que ao utilizarmos o copy nós copiamos os dados da lista para uma nova lista, mas elas ficaram totalmente
# independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python é chamado Deep Copy.
print('Exemplo 2: Shallow Copy')
lista = [1, 2, 3]
print(lista)

lista_copia = lista
print(lista_copia)

lista_copia.append(4)

print(lista)
print(lista_copia)
# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas após realizar
# modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.
