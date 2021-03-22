"""
PEP8 - Python Enhancement Proposal

São proposals de melhorias para a linguagem Python

The zen of Python
import this

A ideia da PEP8 é que possamos escrever códigos Python de forma agradável

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:

class CalculadoraCientifica:

[2] - Utilize nomes em minúsculo, separados por underline para funções ou varoáveis

def soma():

def soma_dois():

numero = 4

numero_impar - 3

[3] - Utilize 4 espaços para identação!

if 'a' in 'banana':
    print('Tem')

[4] - Linhas em Branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separadas com uma única linha em branco;

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas;
- Imports devem ser colocados no topo do arquivo, logo depois dos comentários e antes de variáveis;


import numpy
import pandas

from types import StringType,ListType

from tpes import (
    StringType,
    ListType,
    SetType,
    OutroType,
)

[6] - Espaços em expressões e instruções
- Não faça
funcao( algo[ 1 ], { outro: 2 } )
Faça
funcao(algo[1], {outro: 2})

-Não faça
algo (1)
Faça
algo(1)

-Não Faça
x              = 1
y              = 2
variavel_longa = 3
Faça
x = 1
y = 2
variavel_longa = 3

[7] - Termine sempre uma instrução com uma nova linha

"""


import this
