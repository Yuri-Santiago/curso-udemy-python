"""
Módulo Collections - Deque

Podemos dizer que o Deque é uma lista de alta performance.
"""

from collections import deque

# Criando deques
deq = deque('yuri')
print(deq)

# Adicionando elementos no deque
deq.append('m')  # Adciona no final
print(deq)

deq.appendleft('O')  # Adiciona no começo
print(deq)

# Remover elementos
print(deq.pop())  # Remove e retorna o último elemento
print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento
print(deq)
