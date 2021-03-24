"""
Recebendo dados do usuário

input() -> Todos os dados recebidos via input são do tipo String

Em Python, strinf é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;
"""

# Entrada de dados
print('Qual seu nome? ')
nome = input()  # input -> entrada

# Exemplo de print antigo
# print('Seja bem vindo(a) %s' % nome)

# Exemplo de print moderno
# print('Seja bem vindo(a) {0}'.format(nome))


# Exemplo moderno
print(f'Seja bem vindo(a) {nome}')

print('Qual a sua idade? ')
idade = int(input())

# Processamento

# Saída de Dados
# print('A %s tem %d anos' % (nome, idade))

# print('O {0} tem {1} anos'.format(nome, idade))

print(f'O {nome} tem {idade} anos!')

print(f'O {nome} nasceu em {2021 - idade}')
