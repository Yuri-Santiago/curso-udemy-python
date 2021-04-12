"""
3 - Escreva uma função que gera um triângulo lateral de altura 2*n-1 e n largura.
Por exemplo, a saída para n = 4 seria:
+
++
+++
++++
+++
++
+
"""


def triangulo(n):
    caractere = ''
    vezes = 0
    while vezes < n:
        caractere += '+'
        print(caractere)
        vezes += 1

    while vezes > 1:
        caractere = ''
        for x in range(1, vezes):
            caractere += '+'
        print(caractere)
        vezes -= 1


triangulo(10)
