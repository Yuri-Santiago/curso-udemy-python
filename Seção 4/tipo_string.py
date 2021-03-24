"""
Tipo String

Em Python um dado é considerado do tipo Stirng sempre que:
- Estiver em aspas simples
- Estiver em aspas duplas
- Estiver em aspas simples triplas
- Estiver em aspas duplas triplas

"""
nome = 'Yuri Mateus Santiago'
print(nome)
print(type(nome))

lugar = "john's pub"
print(lugar)

lugar = 'john\'s pub'
print(lugar)

# Métodos
print(lugar.upper())
print(lugar.split())
print(lugar.split()[1])
print(nome.replace('M', 'N'))

# Slicing
print(nome[0:11])
print(nome[::-1])  # Comece do primeiro elemento vá até o último elemento e inverta
