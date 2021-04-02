"""
3 - Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova
tem peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado
ou reprovado. A nota para a aprovação deve ser igual ou superior a 60 pontos.
"""

print('Digite suas 3 notas de prova para saber se foi aprovado ou não.')
prova1 = float(input('Digite a nota 1: '))
prova2 = float(input('Digite a nota 2: '))
prova3 = float(input('Digite a nota 3: '))

media = (prova1 * 1 + prova2 * 1 + prova3 * 2) / 4

if media >= 6:
    print(f'Sua média foi: {media}. Você está aprovado!')
else:
    print(f'Sua média foi: {media}. Você está reprovado!')
