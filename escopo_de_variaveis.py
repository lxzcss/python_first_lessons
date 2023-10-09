"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco aonde foi delcarada.

Para declara variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor à mesma

Exemplo em C:
int num = 42;

Exemplo em Java:
int num = 42;
"""

num = 42
print(num)
print(type(num))

num = "Lucas"
print(num)
print(type(num))

num = 42

if num > 10:
    novo = num +10  # A varaiável "novo" está declarada dentro do bloco do if, portanto, é local
    print(novo)

