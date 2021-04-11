"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas específicas.
- Pode ou não receber entradas de dados e retornar uma saída de dados.
- Muito úteis para executar procedimentos similares por repetidas vezes.

OBS: Se você escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que iniciamos o curso:
- print()
- len()
- max()
- count()
- etc

Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada)
    bloco_da_funcao

Onde: nome_da_funcao -> Sempre, com letras minúsculas, e se for nome composto, separado por underlinde (Snake Case).
      parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opicionais.
      bloco_da_funcao -> Obrigatório, é onde ocorre o processamento da função, neste bloco pode ou não ter o retorno.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def', informando ao Python que estamos definindo
uma função. Também abrimos o bloco de código com o dois pontos ':' que é utilizado para definir os blocos.
"""

# Exemplo de utilização de funções

cores = ['vermelho', 'azul', 'amarelo']

# Utilizando a função integrada (Built-in) do Python print()
print(cores)

curso = 'Programação em Python: Essencial'
print(curso)

# Utilizando uma função das listas
cores.append('verde')
print(cores)
# curso.append('dado')  # Isso é um erro pois as Strings não possuem essa função

# Utilizando uma função das listas que não recebe parâmetros
cores.clear()
print(cores)
# Princípio DRY - Don´t Repeat Yourself, as funções são muito úteis para esse princípio não ocorrer.

# Definindo a primeira função


def diz_oi():
    print('oi')


# OBS: Veja que dentro das nossas funções podemos utilizar outras funções
#      Veja que essa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi
#      Veja que esta função não recebe nenhum parâmetro ou entrada

# Utilizando funções

diz_oi()  # Chamada de Execução

# Exemplo 2:


def cantar_parabens():
    print('Parabéns pra Você')
    print('Nesta Data Querida')
    print('Muitas Felicidades')
    print('Muitos Anos de Vida')
    print('Viva o Aniversariante')


# Utilizando a função
for n in range(3):
    cantar_parabens()

# Em Python podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável

oi = diz_oi
oi()
# Isso não é comum mas é possível em Python
