"""
10 - Faça um programa para ler as dimensões de um terreno (comprimento C e largura L),
bem como o preço do metro de tela P. Imprima o custo para cercar este mesmo terreno com tela.
"""

print('Digite as dimensões do seu terreno: ')
comprimento = int(input('Comprimento: '))
largura = int(input('Largura: '))

preco = float(input('Digite o preço do metro de tela: '))

area = comprimento * largura
total = area * preco
print(f'O preço para telar todo o terreno é {total}')
