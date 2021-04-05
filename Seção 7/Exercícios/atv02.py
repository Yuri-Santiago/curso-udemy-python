"""
2 - Faça um programa que leia dois números a e b (positivos menores que 10000) e:
    - Crie um vetor onde cada posição é um algarismo do número. A primeira posição é o algarismo menos significativo
    - Crie um vetor que seja a soma de a e b, mas faça-o usando apenas os vetores construídos anteriormente.
"""

a = input('Digite o número a: ')
b = input('Digite o número b: ')

vetor_a = list(a)
vetor_b = list(b)

for x in range(len(vetor_a)):
    vetor_a[x] = int(vetor_a[x])

for x in range(len(vetor_b)):
    vetor_b[x] = int(vetor_b[x])

vetor_a.reverse()
vetor_b.reverse()

while len(vetor_a) != 4:
    vetor_a.append(0)

while len(vetor_b) != 4:
    vetor_b.append(0)

resultado = []
ad = 0
for x in range(4):
    num = vetor_a[x] + vetor_b[x]
    num += ad
    if num >= 10:
        num -= 10
        ad = 1
    else:
        ad = 0
    resultado.append(num)
if ad == 1:
    resultado.append(1)

resultado.reverse()
vetor_a.reverse()
vetor_b.reverse()

print(f'O valor de {vetor_a} + {vetor_b} = {resultado}')
