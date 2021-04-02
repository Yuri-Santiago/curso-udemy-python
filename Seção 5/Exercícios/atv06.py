"""
6 - Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente
de importo sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor
e o estado de destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado
em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
"""

estados = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}

valor = float(input('Digite o valor do produto: '))
estado = input('Digite o estado ("MG", "SP", "RJ", "MS") que irá comprar: ')

if estado in estados.keys():
    imposto = valor * estados[estado]
    print(f'O valor total foi: {valor + imposto}')
else:
    print('Estado inválido, tente novamente.')
