"""
9 - Faça uma função que receba duas strings e retorne a intercalação letra a letra da primeira com a segunda string.
A string intercalada deve ser retornada na primeira string.
"""


def funcao(primeira, segunda):
    letras1 = []
    for x in range(len(primeira)):
        letras1.append(primeira[x])

    letras2 = []
    for x in range(len(segunda)):
        letras2.append(segunda[x])

    final = []
    if len(letras1) > len(letras2):
        for x in range(len(letras1)):
            final.append(letras1[x])
            if len(letras2) > x:
                final.append(letras2[x])
    elif len(letras1) < len(letras2):
        for x in range(len(letras2)):
            if len(letras1) > x:
                final.append(letras1[x])
            final.append(letras2[x])
    else:
        for x in range(len(letras1)):
            final.append(letras1[x])
            final.append(letras2[x])
    return ''.join(final)


print(funcao('Yr', 'ui'))
print(funcao('Eecco', 'xríi'))
print(funcao('Maçã', 'Banana'))
