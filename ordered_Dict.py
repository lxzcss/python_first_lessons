"""
Móduloo Colletctions - Ordered Dict

https://docs.python.org/3/library/collections.html#collections.OrderedDict

# Em um dicionário, a ordem de inserção dos elementos não é garantida.
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dic.items():
    print(f'Chave = {chave}; Valor = {valor}')

print(dic)

OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.

# Fazendo o Import
from collections import OrderedDict

dic = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dic.items():
    print(f'Chave = {chave}; Tem o Valor = {valor}')
"""
from collections import OrderedDict

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True -> Já que a ordem dos elementos não importa para o dicionário

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False -> Já que a ordem dos elementos importa para o OrderedDict
