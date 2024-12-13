"""
Funções que não são identificadas por um nome, mas que podem executar
rotinas úteis no sistema

A sintaxe: lambda arg:expr
"""

soma = lambda a, b : a + b
mult = lambda a, b, c : (a + b) * c

print(soma(10, 20)) #30
print(mult(2, 5, 3)) #21

#sem associar com variáveis
print((lambda a, b : a - b)(20, 7)) #13

#passar função como arg
result = lambda x, func : x + func(x)
r = result(2, lambda x : x * x) #6
print(r)
r = result(2, lambda x : x + 3) #7
print(r)