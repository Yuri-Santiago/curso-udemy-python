"""
7 - Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100.
Escolha números aleatórios entre 1 e 100, e mostra na tela a pergunta: qual é a soma de a+b, onde a e b são números
aleatórios. Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as repostas correstas,
além de quantas vezes o aluno acertou
"""

import random

x = 0
acertos = 0
certas = []
perguntas = []
respostas = []
while x < 5:
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    print(f'Qual a soma de {a} + {b}?')
    perguntas.append((a, b))

    resposta = int(input('Resposta: '))
    respostas.append(resposta)

    certa = a + b
    certas.append(certa)

    if resposta == certa:
        acertos += 1

    x += 1
print()

x = 0
while x < 5:
    print(f'A pegunta número {x+1} foi: {perguntas[x][0]} + {perguntas[x][1]} = {certas[x]}.'
          f'\nSua resposta foi: {respostas[x]}')
    x += 1

print()
print(f'Você acertou {acertos} perguntas.')
