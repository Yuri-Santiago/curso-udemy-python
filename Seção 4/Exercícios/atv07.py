"""
7 - Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite o número
de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga,
sabendo-se que são descontados 8% para imposto de renda.
"""

dias = int(input('Quantos dias o encanador trabalhará? '))
total = (30 * dias) - (30 * dias * 0.08)

print(f'Ele irá receber, calculando o imposto de renda, {total} reais')
