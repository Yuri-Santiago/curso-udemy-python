"""
Documentando Funções com DocStrings

OBS: Podemos ter acesso a documentação de uma função em Python utilizando a propriedade especial __doc__
"""

# Aqui vemos que a função print possui um docstring explicando ela
print(help(print))

# Exemplos


def diz_oi():
    """Uma função que retorna a string 'Oi! '"""
    return 'Oi! '


print(diz_oi())
print(help(diz_oi))
print(diz_oi.__doc__)


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de um número, ou esse número elevado à potência
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que será o expoente da função
    :return: Retorna o exponencial do número pela potência
    """
    return numero ** potencia


print(exponencial(2))
print(help(exponencial))
print(exponencial.__doc__)
