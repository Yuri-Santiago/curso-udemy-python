"""
Dicionários
Obs: Em algumas linguagens de programação, os dicioários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}

Obs sobre dicionários
- Chave e valor são separados por dois pontos 'chave': 'valor'
- Tanto chave quanto valor podem ser de qualquer tipo de dado
- Podemos misturar tipos de dados

###
Tipo None

O tipo de dado None em Python representa o tipo sem tipo, ou poderia ser conhecido também como tipo vazio,
porém, falar que é um tipo sem tipo é mais apropriado.

Obs: O tipo None é sempre especificado com a primeira letra Maiúscula
Obs: O tipo None em Python é sempre considerado como False

Quando utilizamos?
- Podemos utilizar None quando queremos criar uma variável e inicializá-la com um tipo sem tipo,
antes de recebermos um valor final
###
"""

# Criação de Dicionários
# Forma 1: mais comum
paises = {'br': 'Brasil', 'us': 'Estados Unidos', 'uk': 'Reino Unido'}
print(paises)
print(type(paises))

# Forma 2: menos comum
estados = dict(ce='Ceará', rj='Rio de Janeiro', sp='São Paulo')
print(estados)
print(type(estados))

# Acessando elementos
# Forma 1: Acessando via chave, da mesma forma que lista/tupla
print(estados['ce'])
print(estados['sp'])
# Caso a chave não exista, teremos uma KeyError

# Forma 2: Acessando via get - recomendado
print(estados.get('rj'))
print(estados.get('rs'))  # Caso não encontra a chave retornará um tipo None, ver mais acima.

# Caso o get não encontre o objeto com a chave informada ele retornará None que é False
estado = estados.get('ce')
if estado:
    print(f'Encontrei o estado {estado}')
else:
    print(f'Não encontrei o estado')

# Podemos definir um valor padrão para caso não encontremos um objeto com a chave informada
estado = estados.get('mg', 'Não encontrado')
print(estado)

# Podemos verificar se determinada chave está em um dicionário
print('rj' in estados)
print('mg' in estados)
print('Rio de Janeiro' in estados)

if 'mg' in estados:
    minas = estados['mg']

# Podemos utilizar qualquer tipo de dado (int, float, boolean, string, listas, tuplas) em um dicionário
entidade = {
    (1, 1): 'João, Python',
    (1, 2): 'João, Java',
    (2, 2): 'Maria, Java'
}
print(entidade)
print(type(entidade))
# Tuplas por exemplo são bastante interessantes de serem utilizadas cmo chaves de dicionários, pois são imutáveis

# Adicionando elementos ao dicionário
receita = {'jan': 100, 'fev': 150, 'mar': 130}
print(receita)

# Forma 1 - Mais comum
receita['abr'] = 200
print(receita)

# Forma 2
novo_dado = {'mai': 180}
receita.update(novo_dado)  # receita.update({'mai': 180})
print(receita)

# Atualizando dados em um dicionário
# Forma 1
receita['mai'] = 500
print(receita)

# Forma 2
receita.update({'mai': 250})
print(receita)
# Concluímos que a forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesa
# E em dicionários NÃO podemos ter chaves repetidas

# Remover dados de um dicionário
# Forma 1 - Mais comum
retirada = receita.pop('jan')
print(retirada)
print(receita)
# Obs: Aqui precisamos sempre informar a chave, sem ela dará erro
# Obs: Ao removermos um objeto, o seu valor é retornado

# Forma 2
del receita['fev']
print(receita)
# Obs: neste caso o valor removido não é retornado

# Métodos de Dicionários
d = dict(a=1, b=2, c=3)
print(d)

# Limpar o dicionário
receita.clear()
print(receita)

# Copiando um dicionário para outro
# Forma 1: Deep Copy
print('Deep Copy')
novo = d.copy()  # Deep Copy
print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2: Shallow Copy
print('Shallow Copy')
novo = d
print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'id'], 'desconhecido')
print(usuario)
print(type(usuario))
# O método formkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar pra cada valor do iterável, uma chave e irá atribuir a essa chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)  # Ele não recebe 5 chaves pois não aceita repetição de chaves

veja = {}.fromkeys(range(1, 6), 'novo')
print(veja)
