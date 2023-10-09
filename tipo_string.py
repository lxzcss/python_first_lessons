"""
Tipo string

Relembrand que em python, um dado é considerado do tipo string, sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'true', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "true", "42.3"
- Estiver entre aspas simples triplas -> '''string'''

nome = 'Lucas'
nome2 = "Sthe"
nome3 = '''Stella'''
"""
# nome4 = """Yasmin"""
"""
print(nome)
print(nome2)
print(nome3)
print(nome4)

print(type(nome))
print(type(nome2))
print(type(nome3))
print(type(nome4))

bar = "Luca's Bar"  # Tem de ser com aspas duplas, devido a aspa simples
print(bar)
print(type(bar))

nome = 'lucas \nloiola'
print(nome)
print(type(nome))

nome = 'Lucas \' Loiola'
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split())  # Transforma em uma lista de strings


# [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11 ]
# ['L' 'u' 'c' 'a' 's' ' ' 'L' 'o' 'i' 'o' 'l' 'a']
# Slice de string
nome = "Lucas Loiola"

print(nome[0:5])

print(nome[6:12])

# [    0,       1     ]
# [ 'Lucas', 'Loiola' ]
print(nome.split()[1])

print(nome.split()[0])

"""
# - Estiver entre aspas duplas triplas -> """String"""

nome = "lucas Loiola"

"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
"""
print(nome.title())

print(nome[::-1])  # Inversão da string

print(nome.replace('L', 'b'))

texto = 'socorram me subino onibus em marrocos'  # Palíndromo

print(texto)
print(texto[::-1])

nome = 'ana'  # Palíndromo
print(nome)

print(nome[::-1])