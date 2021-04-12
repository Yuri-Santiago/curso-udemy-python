"""
10 - Foi realizada uma pesquisa de algumas características físicas de cinco habitantes de certa região.
De cada habitante foram coletados os seguintes dados: sexo, cor dos olhos (A - Azuis ou C - Castanhos),
cor dos cabelos (L - Louros, P - Pretos ou C - Castanhos) e idade.
- Faça uma função que leia esses dados em um vetor
- Faça uma função que determine a média de idade das pessoas com olhos castanhos e cabelos pretos.
- Faça uma função que determine e devolva ao programa principal a maior idade entre os habitantes
- Faça uma função que determine e devolva ao programa principal a quantidade de indivíduos do sexo feminino cuja idade
está entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros
"""


def leitura(sexo, cor_olhos, cor_cabelos, idade):
    vetor = []
    sexo = sexo.upper()
    cor_olhos = cor_olhos.upper()
    cor_cabelos = cor_cabelos.upper()
    vetor.extend([sexo, cor_olhos, cor_cabelos, idade])
    return vetor


def idade_media_castanho_preto(pessoas):
    idades = 0
    contagem = 0
    for pessoa in pessoas:
        if 'C' in pessoa and 'P' in pessoa:
            idades += pessoa[3]
            contagem += 1
    if contagem != 0:
        return idades / contagem
    return 0


def maior_idade(pessoas):
    maior = 0
    individuo = 0
    for pessoa in pessoas:
        if pessoa[3] > maior:
            maior = pessoa[3]
            individuo = pessoas.index(pessoa) + 1
    return maior, individuo


def feminino_azul_loiro(pessoas):
    quantidade = 0
    for pessoa in pessoas:
        if 'A' in pessoa and 'L' in pessoa and 18 <= pessoa[3] <= 35:
            quantidade += 1
    return quantidade


lista = [leitura('f', 'A', 'l', 25), leitura('M', 'c', 'c', 20), leitura('m', 'C', 'p', 18), leitura('F', 'C', 'C', 18),
         leitura('m', 'C', 'l', 30)]

for x in range(len(lista)):
    print(f'A pessoa número {x + 1} tem as características: {lista[x]}')
print(f'A média de idade das pessoas com olhos castanhos e cabelos pretos é: {idade_media_castanho_preto(lista)}')
print(f'A maior idade entre os habitantes é: {maior_idade(lista)[0]}, da pessoa de número {maior_idade(lista)[1]}')
print(f'A quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que tenham olhos azuis '
      f'e cabelos louros é: {feminino_azul_loiro(lista)}')
