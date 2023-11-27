"""
Método chr()

- Retorna um número como um caractere

Unicode - É como um tradutor para padronizar os código no mundo, utilizando números

- O método chr() aceita apenas um inteiro como argumento.
- O intervalo pode variar de 0 a 1.1141.111 (0x10FFFF na base 16).
- O método chr() retorna um caractere cujo ponto unicode é num, um inteiro.
- Se um inteiro for passado fora do intervalo, o método retornará um ValueError.

Exemplo

x=65
chr(x)

Resultado 1

'A'

x=65
chr((x) + 32)

Resultado 2

'a'

- Sempre que somarmos/subtrairmos '32' teremos o mesmo caractere
em tamanho (maiusculo/minusculo) diferente.

"""