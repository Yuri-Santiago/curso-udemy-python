"""
8 - Escreva uma função que compare e retorne verdadeiro, caso uma string seja anagrama da outra, e falso, caso contrário
"""


def anagrama(primeira, segunda):
    letras1 = []
    for x in range(len(primeira)):
        letras1.append(primeira[x].upper())
    letras1.sort()

    letras2 = []
    for x in range(len(segunda)):
        letras2.append(segunda[x].upper())
    letras2.sort()

    if letras1 == letras2:
        return True
    return False


print(anagrama('Yuri', 'Riyu'))
print(anagrama('Banana', 'Nabnaa'))
print(anagrama('Falso', 'Laso'))
