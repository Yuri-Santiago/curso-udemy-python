"""
3 - Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro. Se o código
for zero, finalize o programa: se for 1, mostre o vetor na ordem direta, se for 2, mostre o vetor na ordem inversa.
Caso, o código for diferente de 1 e 2 escreva uma mensagem informando que o código é inválido.
"""

print('Nesse programa você deverá digitar 5 números reais e um código.')
lista = []
for x in range(5):
    num = float(input(f'Digite o valor de número {x+1}: '))
    lista.append(num)

cod = int(input('Digite o código (0 = sair, 1 = lista normal, 2 = lista inversa): '))
while True:
    if cod == 0:
        print('Fechando o progama!')
        break
    elif cod == 1:
        print(f'A lista é: {lista}')
        break
    elif cod == 2:
        lista.reverse()
        print(f'A lista inversa é: {lista}')
        break
    else:
        print('Número inválido. Tente novamente.')
        cod = int(input('Digite o código (0 = sair, 1 = lista normal, 2 = lista inversa): '))
