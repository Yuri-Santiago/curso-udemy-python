"""
Escopo de Variáveis

Dois casos de escopo:
- Variáveis globais: são reconhecidas, ou  seja, seu escopo compreende toodo o programa

- Variáveis locais: são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco
foi declarado.

Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de
dado dela. Esse tipo é inferido ao atribuírmos o valor à mesma

"""

numero = 42  # Exemplo de variável Global
print(numero)
print(type(numero))

numero = 'yuri'
print(numero)
print(type(numero))

numero = 11

if numero > 10:
    novo = numero + 10  # Exemplo de variável Local, dentro do bloco if
    print(novo)
print(novo)
