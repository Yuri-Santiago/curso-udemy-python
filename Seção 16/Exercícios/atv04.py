"""
4 - Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o volume e trocar os canais da televisão.

- O controle de volume permite aumentar ou diminuir a potência do volume do som em uma unidade de cada vez
- O controle de canal também permite aumentar e diminuir o número do canal em uma unidade, porém, também possibilita
trocar para um canal indicado
- Também devem existir métodos para consultar o valor do volume de som e o canal selecionado
"""


class Televisao:
    def __init__(self, canal_maximo):
        self.__volume_atual = 1
        self.__canal_atual = 1
        self.__volume_maximo = 100
        self.__canal_maximo = canal_maximo

    def get_volume_atual(self):
        return self.__volume_atual

    def get_canal_atual(self):
        return self.__canal_atual

    def get_volume_maximo(self):
        return self.__volume_maximo

    def get_canal_maximo(self):
        return self.__canal_maximo

    def set_volume_atual(self, volume):
        self.__volume_atual = volume

    def set_canal_atual(self, canal):
        self.__canal_atual = canal

    def set_volume_maximo(self, volume):
        self.__volume_maximo = volume

    def set_canal_maximo(self, canal):
        self.__canal_maximo = canal


class ControleRemoto:
    def __init__(self, televisao):
        self.__televisao = televisao

    def aumentar_volume(self):
        if self.__televisao.get_volume_atual() < self.__televisao.get_volume_maximo():
            self.__televisao.set_volume_atual(self.__televisao.get_volume_atual() + 1)

    def diminuir_volume(self):
        if self.__televisao.get_volume_atual() > 0:
            self.__televisao.set_volume_atual(self.__televisao.get_volume_atual() - 1)

    def aumentar_canal(self):
        if self.__televisao.get_canal_atual() < self.__televisao.get_canal_maximo():
            self.__televisao.set_canal_atual(self.__televisao.get_canal_atual() + 1)

    def diminuir_canal(self):
        if self.__televisao.get_canal_atual() > 0:
            self.__televisao.set_canal_atual(self.__televisao.get_canal_atual() - 1)

    def trocar_canal(self, canal):
        if canal <= self.__televisao.get_canal_maximo():
            self.__televisao.set_canal_atual(canal)

    def get_volume(self):
        return self.__televisao.get_volume_atual()

    def get_canal(self):
        return self.__televisao.get_canal_atual()


if __name__ == '__main__':
    tv = Televisao(50)

    controle = ControleRemoto(tv)

    for _ in range(200):
        controle.aumentar_volume()
    print(controle.get_volume())

    for _ in range(55):
        controle.aumentar_canal()
    print(controle.get_canal())

    for _ in range(30):
        controle.diminuir_volume()
    print(controle.get_volume())

    for _ in range(15):
        controle.diminuir_canal()
    print(controle.get_canal())

    controle.trocar_canal(10)
    print(controle.get_canal())
