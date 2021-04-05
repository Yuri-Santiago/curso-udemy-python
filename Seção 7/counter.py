"""
Módulo Collections - Counter (Contador)

Collections -> High-Performance Container Datatypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.
"""

# Importando o módulo collections
from collections import Counter

# Utilizando o Counter
# Podemos utilizar qualquer iterável, aqui está uma lista
lista = [1, 2, 2, 1, 3, 1, 1, 2, 3, 2, 2, 3, 4, 5, 5, 5, 1, 2, 4, 5, 6]

# Exemplo 1 - Criando um Counter
res = Counter(lista)

print(type(res))
print(res)
# Para cada elemento da lista o counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2 - Utilizando em Strings
print(Counter('Yuri Mateus Santiago'))

# Exemplo 3
texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eleifend aliquet tempus. Aliquam lacinia ' \
        'vitae erat vitae interdum. Praesent lacinia faucibus lectus, sit amet fringilla augue dictum non. Mauris ' \
        'malesuada sem in convallis ultrices. Vivamus a lectus non metus facilisis placerat. Mauris odio eros, ' \
        'vehicula id vestibulum eget, molestie at tellus. In semper aliquet mi, eu mattis neque sollicitudin vitae.' \
        ' Fusce finibus ac mauris eu ultrices. Phasellus blandit magna vitae turpis fringilla, nec accumsan est ' \
        'facilisis. Cras id dui vel massa suscipit ornare. Vivamus ornare leo nibh, hendrerit efficitur lorem gravida' \
        ' ut. Donec viverra, arcu sed scelerisque egestas, odio dolor rhoncus purus, in efficitur mi nulla nec mi.' \
        ' Etiam tempor nibh convallis lacus lacinia, id ullamcorper ligula vehicula. Sed lacinia felis ut sodales ' \
        'eleifend. Cras mattis elementum dolor, non hendrerit neque imperdiet vitae. Sed tempus leo erat, sed ' \
        'ullamcorper lorem faucibus in.'

palavras = texto.split()
ex = Counter(palavras)
print(ex)

# Encontrando as 5 palavras com mais ocorrências no texto
print(ex.most_common(5))
