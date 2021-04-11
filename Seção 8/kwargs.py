"""
Entendendo o **kwargs

Poderíamos chamar esse parâmetro de qualque nome, mas por convenção, chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige que
utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.

# Nas nossas funções, podemos ter NESTA ORDEM:
- Parâmetros obrigatórios
- *Args
- Parâmetros Default (não obrigatórios)
- **Kwargs
"""

# Exemplos


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.capitalize()} é {cor}')


cores_favoritas(yuri='azul', raquel='rosa', kelvin='verde', israel='vermelho')
# OBS: Os parâmetros *args e **kwargs não são obrigatórios
cores_favoritas()

# Exemplo mais complexo


def senha(**kwargs):
    if 'yuri' in kwargs and kwargs['yuri'] == 'Python':
        return 'Você está liberado para acesso.'
    elif 'yuri' in kwargs:
        return f"{kwargs['yuri']} é a senha errada."
    return 'Usuário não reconhecido.'


print(senha())
print(senha(yuri='Java'))
print(senha(joao='Python'))
print(senha(yuri='Python'))

# Exemplo de ordem


def funcao(num, *args, nome='aluno', **kwargs):
    if len(args) != 0 and len(kwargs) != 0:
        return f"Oi {nome} sua colocação é {num}, a soma dos seus pontos é {sum(args)} e seu curso é " \
               f"{list(kwargs.values())[0]}"
    elif len(args) != 0:
        return f"Oi {nome} sua colocação é {num}, a soma dos seus pontos é {sum(args)}"
    elif len(kwargs) != 0:
        return f"Oi {nome} sua colocação é {num}, seu curso é {list(kwargs.values())[0]}"
    return f"Oi {nome} sua colocação é {num}"


print(funcao(2, 1, 2, 3, 4, 5, 6, nome='Raquel', raquel='Python'))
print(funcao(5))
print(funcao(1, 9, 8, 6, yuri='Java'))
print(funcao(3, nome='kelvin'))
print(funcao(4, 7, 7, 4))
print(funcao(6, curso='Python'))

# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Yuri', 'sobrenome': 'Santiago'}
print(mostra_nomes(**nomes))

# Outro Exemplo


def somas(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
nums = dict(a=1, b=2, c=3)

somas(1, 2, 3,)
somas(*lista)
somas(**nums)
# OBS: Os nomes da chave do dicionário devem ser o mesmo dos parâmetros da função
