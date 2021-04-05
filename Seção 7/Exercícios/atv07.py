"""
7 - Faça um programa para determinar a próxima jogada em um Jogo da Velha. Assumir que o tabuleiro é representado por
uma matriz de 3 x 3, onde cadda posição representa uma das casas do tabuleiro. A matriz pode conter os seguintes valores
1, 0, 2 representando respectivamente uma casa contendo uma peça do jogador 1, uma casa vazia do tabuleiro 0, e uma casa
contendo uma peça do jogador 2.
"""

matriz = []
for x in range(3):
    matriz.append([])
    for i in range(3):
        matriz[x].append(0)
# def jogada_obvia():


def jogada(num):
    linha, coluna = list(input("digite a posicão desejada (ex:21 é 2° linha e 1° coluna): "))
    linha = int(linha)
    coluna = int(coluna)
    if matriz[linha][coluna] == 0:
        matriz[linha][coluna] = num
    else:
        print("jogada inválida")
        jogada(num)


def checa():
    condicao = 0
    for y in matriz:
        if y.count(0) == 0:
            condicao += 1
        else:
            condicao = 0
    if condicao == 3:
        print("!!!deu velha!!!")
        return 1
    else:
        condicao = vitoria()
        return condicao


def vitoria():
    vit = 0
    n = 0
    # vertical
    for m in range(3):
        if matriz[n][m] == matriz[n+1][m] and matriz[n+1][m] == matriz[n+2][m] and matriz[n][m] != 0:
            print(f"bateu vertical jogador {matriz[n][m]}!!!")
            vit += 1

    # horizontal
    for m in matriz:
        if m[0] == m[1] and m[1] == m[2] and m[0] != 0:
            print(f"bateu horizontal jogador  {m[0]}!!!")
            vit += 1

    # diagonal descendente
    if matriz[n][n] == matriz[n+1][n+1] and matriz[n+1][n+1] == matriz[n+2][n+2] and matriz[n][n] != 0:
        print(f"bateu diagonal jogador {matriz[n][n]}!!!")
        vit += 1

    # diagonal ascendente
    if matriz[n][n+2] == matriz[n+1][n+1] and matriz[n+1][n+1] == matriz[n+2][n] and matriz[n][n+2] != 0:
        print(f"bateu diagonal invertida jogador {matriz[n][n+2]}!!!")
        vit += 1
    # checa se venceu
    return 1 if vit >= 1 else 0


print("inicie o jogo")
vez = 1
fim = 0
while fim < 1:
    if vez % 2 == 0:
        papel = 2
    else:
        papel = 1
    print('   0  1  2')
    [print(a, matriz[a]) for a in range(3)]
    jogada(papel)
    vez += 1
    fim = checa()
    # jogada_obvia()

print('   0  1  2')
[print(a, matriz[a]) for a in range(3)]
print('O jogo acabou.')
