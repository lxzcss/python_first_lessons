"""
Módulo Colletctions - Counter (Contador)

https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento

# Realizando o import

from collections import Counter

# Exemeplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Couter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Geek University'))
#  Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})


"""

from collections import Counter

# Exemplo 3
texto = """Inicialmente os integrantes viajavam numa caravana composta por veículos clássicos ou alterados para um 
estilo pós-apocalíptico, que foi crescendo progressivamente. Mantendo uma génese nómada nos primeiros anos, 
instalaram-se mais tarde em Oeiras, Portugal, e fundaram o centro cultural Nirvana Studios. As actividades desta 
companhia iniciaram-se em 1992, e à excepção do ano de 1995, realizou todos os anos diversas actividades até à sua 
fundação oficial em 2002 com o nome Custom Circus"""

palavras = texto.split()
#  print(palavras)

res = Counter(palavras)
print(res)

print(res.most_common(5))

