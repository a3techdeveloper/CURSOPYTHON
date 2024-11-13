import os
"""
Condicional Composta - Avalia um teste lógico, se o teste retornar
True, executa as instruções no bloco if, senão ele executa as
instruções no bloco else
"""
#verifica se o gênero é masculino ou feminino
genero = input('Digite [M] para Masculino: ')
genero = genero.upper() #converter em maiúsculo

# igualdade ==, diferença !=, maior >, menor <, maior igual >=, menor igual <=
if genero == 'M':
    print('É Masculino') #True
else:
    print('É Feminino') #False
print('Fim do Programa \n')

"""
Condicional Encadeada - Avalia um teste lógico, se o teste retornar
True, executa as instruções no bloco if, senão ele avalia outro teste
lógico, se o teste retornar True, executa as instruções no bloco elif,
senão executa as instruções do bloco else
"""
media = float(input('Digite a média do aluno: '))
if media >= 7:
    print('Aprovado') #True
elif media >= 4:
    print('Recuperação') #True
else:
    print('Reprovado') #False
print('Fim do Programa \n')