"""
2 - Crie uma Classe Agenda que pode armazenar 10 pessoas e seja capaz de realizar as seguintes operações:
    - armazenar_pessoa(nome, idade, altura)
    - remover_pessoa(nome)
    - buscar_pessoa(nome)  # informa em que posição da agenda está a pessoa
    - imprimir_agenda()  # imprime os dados de todas as pessoas da agenda
    - imprimir_pessoa(indice)  # imprime os dados da pessoa que está na posição 'i' da agenda
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


class Agenda:
    def __init__(self, pessoa):
        self.__dono = self.set_dono(pessoa)
        self.__lista = []

    def get_dono(self):
        return self.__dono

    def set_dono(self, pessoa):
        if isinstance(pessoa, Pessoa):
            self.__dono = pessoa
            retorno = pessoa
        else:
            retorno = None
        return retorno

    def armazenar_pessoa(self, pessoa):
        if isinstance(pessoa, Pessoa):
            self.__lista.append(pessoa)

    def remover_pessoa(self, nome):
        for pessoa in self.__lista:
            if pessoa.get_nome() == nome.title():
                self.__lista.remove(pessoa)

    def buscar_pessoa(self, nome):
        for indice, pessoa in enumerate(self.__lista):
            if pessoa.get_nome() == nome.title():
                return indice + 1
        return -1

    def imprimir_agenda(self):
        resultado = f'Olá {self.get_dono().get_nome()}!\nPessoas da sua Agenda:\n'
        for pessoa in self.__lista:
            resultado += 'Nome: %40s    Idade: %4d anos    Altura: %5s centímetros\n' % \
                         (pessoa.get_nome(), pessoa.get_idade(), pessoa.get_altura())
        resultado += f'Total de {len(self.__lista)} Pessoas na Agenda.\n'
        print(resultado)

    def imprimir_pessoa(self, indice):
        resultado = f'Olá {self.get_dono().get_nome()}!\nPessoa de número {indice} da Agenda:\n'
        for i, pessoa in enumerate(self.__lista):
            if i == indice - 1:
                resultado += 'Nome: %40s    Idade: %4d anos    Altura: %5s centímetros\n' % \
                             (pessoa.get_nome(), pessoa.get_idade(), pessoa.get_altura())
        resultado += f'Total de {len(self.__lista)} Pessoas na Agenda.\n'
        print(resultado)


if __name__ == '__main__':
    pessoa1 = Pessoa('yuri mateus santiago', 18, 176)
    pessoa2 = Pessoa('raquel maciel', 18, 165)
    pessoa3 = Pessoa('kelvin de lima', 17, 180)
    pessoa4 = Pessoa('israel leite filho', 18, 172)

    agenda = Agenda(pessoa1)

    agenda.armazenar_pessoa(pessoa2)
    agenda.armazenar_pessoa(pessoa3)
    agenda.armazenar_pessoa(pessoa4)

    agenda.imprimir_agenda()
    agenda.remover_pessoa('kelvin dE lima')
    agenda.buscar_pessoa('IsraEl leitE Filho')
    agenda.imprimir_pessoa(2)
    agenda.imprimir_agenda()
