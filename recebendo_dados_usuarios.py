"""
Recebendo dados do usuario

input() -> Todo dado recebido via input é do tipo String.

Em Python, String é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Lucas'
- Aspas duplas -> "Lucas"
- Aspas simples triplas -> '''Lucas'''
"""
# - Aspas duplas triplas -> """Lucas"""


# Entrada de dados
# print("Qual seu nome?")
# nome = input()  # Input -> Entrada

nome = input('Qual seu nome?').title()

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja Bem-vindo(a) {nome.title()}')

# print("Qual sua idade? ")
# idade = input()

idade = int(input('Qual sua idade? '))

# Processamento

# Saída
# Exemplo de print 'antigo' 2.x
# print('%s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'{nome} tem {idade} anos')

"""
# int(idade) -> cast

Cast é a 'conversão' de um tipo de dado para outro. 
"""
print(f'O {nome} nasceu em {2023 - idade}')
