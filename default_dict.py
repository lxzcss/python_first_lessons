"""
Módulo Collections - Default Dict

https://doc.python.org/3/library/collections.html#collections.defaultdict

# Recap Dicionários

dic = {'curso': 'Programação em Python: Essencial'}

print(dic)
print(dic['curso'])
print(dic['outro'])  # Keyerror

Default Dict -> Ao criar um dicionário utilizando-o, nós informarmos um valor default.
podendo utilizar um lambda para isso. Este valores será utilizado sempre que houverr
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome, que podem ou não recbeer parâmetros de entrada
e retornar valores.
"""

# Fazendo import
from collections import defaultdict

dic = defaultdict(lambda: 0)

print(dic)

dic['curso'] = 'Programação em Python: Essencial'

print(dic)

print(dic['outro'])  # KeyError no dicionoário comum, mas aqui não

print(dic)
