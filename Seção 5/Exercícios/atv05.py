"""
5 - Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposntar.
As condições para aposentadoria são
- Ter pelo menos 65 anos
- Ou ter trabalhado pelo menos 30 anos
- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos
"""

print('Nesse programa iremos calcular se você pode ou não se aposentar.')
idade = int(input('Digite sua idade: '))
tempo = int(input('Digite o seu tempo de serviço'))

if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
    print('Você pode se aposentar! :)')
else:
    print('Você não pode se aposentar. :(')
