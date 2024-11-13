import os

"""
Condicional Simples - Avalia um teste lógico, se o teste retornar
True, executa as instruções no bloco if, senão ele não executa nada
e abandona a estrutura
"""
a = True #boolean

if a:
    print('Curso de Python') #True
print('Fim do Programa \n')

#pedir para usuario digitar a idade
idade = int(input('Por favor, informe a sua idade: '))

#verificar se a idade digitada é maior ou igual a 18
if idade >= 18:
   print('Tem maioridade') #True
print('Fim do programa \n')

#verifica a idade e retorna a situação
if idade < 13:
    print('É criança') #true
if (idade > 12) & (idade < 18):
    print('É adolescente') #true
if idade > 17:
    print('É adulto') #true
print('Fim do Programa \n')