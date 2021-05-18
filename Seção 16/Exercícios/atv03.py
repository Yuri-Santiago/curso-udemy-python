"""
3 - Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio. A classe deve
armazenar o andar atual (térreo = 0), total de andares do prédio, excluindo o térreo, capacidade do elevador, e quantas
pessoas estão presentes nele.

A classe deve também disponibilizar os seguintes métodos:
- inicializar: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores
sempre começam no térreo e vazio)
- entrar: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço)
- sair: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele)
- subir: para subir um andar (não deve subir se já estiver no último andar)
- descer: para descer um andar (não deve descer se já estiver no térreo)
- Encapsular todos os atributos da classe (criar os métodos get e set)
"""


class Elevador:
    def __init__(self, capacidade, total_andares):
        self.__andar_atual = 0
        self.__quantidade_atual = 0
        self.__capacidade = capacidade
        self.__total_andares = total_andares

    def get_andar_atual(self):
        return self.__andar_atual

    def get_quantidade_atual(self):
        return self.__quantidade_atual

    def get_capacidade(self):
        return self.__capacidade

    def get_total_andares(self):
        return self.__total_andares

    def set_andar_atual(self, andar):
        self.__andar_atual = andar

    def set_quantidade_atual(self, quantidade):
        self.__quantidade_atual = quantidade

    def set_capacidade(self, capacidade):
        self.__capacidade = capacidade

    def set_total_andares(self, total_andares):
        self.__total_andares = total_andares

    def entrar(self):
        if self.__quantidade_atual < self.__capacidade:
            self.__quantidade_atual += 1

    def sair(self):
        if self.__quantidade_atual > 0:
            self.__quantidade_atual -= 1

    def subir(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1

    def descer(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1


if __name__ == '__main__':
    elevador = Elevador(5, 3)

    for _ in range(6):
        elevador.entrar()
    print(elevador.get_quantidade_atual())

    for _ in range(4):
        elevador.subir()
    print(elevador.get_andar_atual())

    for _ in range(10):
        elevador.sair()
    print(elevador.get_quantidade_atual())

    for _ in range(6):
        elevador.descer()
    print(elevador.get_andar_atual())
