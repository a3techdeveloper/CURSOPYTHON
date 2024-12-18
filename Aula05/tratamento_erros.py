"""
Tratamento de erros com try except
"""
x = 2

try:
    print(x)
except NameError:
    print('variável x não foi definida')

y = 10

try:
    print(y)
except:
    print('ERRO no programa')
else:
    print('Tudo certo')