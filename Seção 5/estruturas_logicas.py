"""
Estruturas Lógicas
and(E), or(OU), not(NÃO), is(É)

Operadores unários: not
Operadores binários: and, or, is

Para o and ambos os valores precisam ser True para retornar True
Para o or um dos valores precisa ser True para retornar True
O not inverte o valor booleano
O is verifica se o valor é aquilo
"""

logado = False
ativo = False

if ativo and logado:
    print('Bem vindo usuário')
elif ativo and not logado:
    print('Você precisa logar na sua conta')
elif ativo or logado:
    print('Você possui uma conta')
elif ativo is False:
    print('Você precisa ativar sua conta')
