"""
1 - Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura. Crie os métodos
públicos para sets e gets e também um método para imprimir os dados de uma pessoa.
"""


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = self.set_nome(nome)
        self.__idade = self.set_idade(idade)
        self.__altura = self.set_altura(altura)

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura

    def set_nome(self, nome):
        if isinstance(nome, str) and nome != '':
            retorno = nome.title()
            self.__nome = nome.title()
        else:
            retorno = 'Anônimo'
            self.__nome = 'Anônimo'
        return retorno

    def set_idade(self, idade):
        if isinstance(idade, int) and idade > 0:
            retorno = idade
            self.__idade = idade
        else:
            retorno = 0
            self.__idade = 0
        return retorno

    def set_altura(self, altura):
        if isinstance(altura, int) and altura > 0:
            retorno = altura
            self.__altura = altura
        else:
            retorno = 0
            self.__altura = 0
        return retorno

    def __str__(self):
        return f'{self.get_nome()} tem {self.get_idade()} anos de idade e {self.get_altura()} cm de altura.'


if __name__ == '__main__':
    eu = Pessoa('yuri mateus santiago', 18, 176)
    errada = Pessoa(True, 20.5, -2)

    print(eu)
    print(errada)
