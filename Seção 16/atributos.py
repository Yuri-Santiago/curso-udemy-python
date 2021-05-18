"""
POO - Atributos

Atributos: Representam as características do objeto. Ou seja, pelos atributos nós conseguimos representear
computacionalmente os estados de um objetos.

Em Python, dividimos os atributos em 3 grupos?
    - Atributos de Instância: são declarados dentro do método construtor
    - Atributos de Classe
    - Atributos Dinâmicos

Por Convenção todos os atributos de uma classe são públicos, ou seja, pode ser acessado fora da classe.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser
acessado/utilizado somente dentro da própria classe onde está declarado, utiliza o duplo underline no nome.
Isso é conhecido como Name Mangling, pois isso é apenas uma convenção, ou seja, o python não irá impedir que façamos
acesso aos atributos sinalizados como privados fora da classe.
"""

# Atributos de Instância significa que ao criarmos um objeto de uma classe, todas as instâncias terão estes atributos.


class Lampada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligada(self):
        return self.__ligada


# Atributos de Classe são atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já
# inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Assim ao invés de casa
# instância da classe ter seus valores, os atributos de classe terão o mesmo valor para tosas as instâncias.


class Produto:

    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador += 1


# Atributos Dinâmicos é um atributo de instância que pode ser criado em tempo de execução, o atributo dinâmico será
# exclusivo da instância que o criou


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


if __name__ == '__main__':
    lamp = Lampada(220, 'branca')
    print(lamp.cor)
    # print(lamp._Lampada__cor)  # Aqui ainda temos o acesso, mas não deveríamos fazer esse acesso

    # Atributos de Classe
    p1 = Produto('Playstation 4', 'Video Game', 2570)
    p2 = Produto('Xbox S', 'Video Game', 3100)

    print(p1.valor)
    print(p2.id)
    print(p1.id)
    print(Produto.imposto)  # nós podemos acessar um atributo de classe sem criar um objeto

    # Criando um atributo em tempo de execução
    p2.peso = 5
    print(p2.peso * 2)

    # Deletando atributos
    print(p1.__dict__)
    print(p2.__dict__)

    del p2.peso

    print(p1.__dict__)
    print(p2.__dict__)
