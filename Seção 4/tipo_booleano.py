"""
Tio Booleano

Álgebra Booleana, criada por George Boole

2 constantes: Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

A primeira letra precisa ser maiúscula
"""

falso = False
verdadeiro = True
print(falso)
print(verdadeiro)
print(type(verdadeiro))
# Operações
#   Negação(not) : troca do valor atual para o seu contrário
print(not falso)
print(not verdadeiro)

#   Ou(or) : é uma operação binária onde um ou o outro precisa ser verdadeiro para retornar verdadeiro
print(falso or verdadeiro)

#   E(and) : é uma operação binária onde ambos os valores devem ser verdadeiro para retornar verdadeiro
print(falso and verdadeiro)
print(not falso and verdadeiro)

# Você pode comparar valores e variáveis para retornar um valor booleano
print(5 < 6)
print(3 > 4)
