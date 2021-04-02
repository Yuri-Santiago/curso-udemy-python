"""
8 - Escreva um programa para ajudar vendedores. A partir de um valor total lido, mostre:
- O toral a pagar com desconto de 10%
- O valor de cada parcela, no parcelamento de 3x sem juros
- A comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto)
- A comissão do vendedor, no caso da venda ser parcelada(5% sobre o valor total)
"""

valor = int(input('Qual o valor total? '))
com_desconto = valor - valor * 0.1
parcelado = valor / 3
comissao_a_vista = com_desconto * 0.05
comissao_parcelado = valor * 0.05

print(f'Valor com desconto: {com_desconto}\nValor parcelado em 3x: {parcelado}\n'
      f'Comissão a vista: {comissao_a_vista}\nComissão parcelado: {comissao_parcelado}')
