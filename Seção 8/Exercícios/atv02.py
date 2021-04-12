"""
2 - Faça uma função chamada DesenhaLinha. Ela deve desenhar uma linha na tela usando vários símbolos de igual (Ex: =======).
A função recebe por parâmetro quantos sinais de igual serão mostrados
"""


def desenha_linha(vezes):
    linha = ''
    for x in range(1, vezes + 1):
        linha += '='
    return linha


for vez in range(11):
    print(desenha_linha(vez))
print(desenha_linha(100))
