"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de casa decimais na programção é o ponto(".") e não a vírgula(",").
"""

# Errado do ponto de vista do Float, mas gera uma Tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um Float para um Int
"""
OBS: Ao converter valores Float para valores Inteiros, perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
var = 5j

