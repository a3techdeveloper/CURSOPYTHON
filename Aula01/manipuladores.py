#Manipulando string (cadeia de caracteres)
curso = 'Curso de Python'

print(curso)
print(curso[0])
print(curso[9])
print(curso[0:5])
print(curso[9:15])
print("----------------------------")

frase = '    Estudando programacao Python      '
#Elimina os espaçamentos 
print(frase)
print(frase.strip())
print("----------------------------")

#Converte caracteres em maiúsculo e minúsculo
print(curso.upper())
print(curso.lower())
#Converte a primeira letra em maiúscula
print(curso.capitalize())

torcida = 'Eu torço pro Corinthians, porque o Corinthians é o melhor'
time = 'Corinthians'
#Substitui um caractere-string-palavra
print(torcida.replace(time,'Grêmio'))
print(torcida.replace(' ','_'))
print("----------------------------")

#Tamanho ou comprimento
print('Comprimento da String:'+str(len(torcida)))
print("----------------------------")

#Tokenização (quebrar em pedaços)
token = curso.split(' ')
print(type(token))
print("----------------------------")

print(token[0])
print(token[1])
print(token[2])

#Verifica se contém a string
palavra = 'Corinthians'
res = palavra in torcida
print(res) #True/False
print("----------------------------")

#Verifica se não contém a string
res = palavra not in torcida
print(res) #True/False
print("----------------------------")

#Utilizando o format()
cidade = 'Águas Lindas'
dia = 2
mes = 'Novembro'
ano = 2024
canal = 'A3Tech'
data = "{}, {} de {} de {}.\n\"{}\""
print(data.format(cidade,dia,mes,ano,canal))
print("----------------------------")

#Caracteres de escape
"""
 \n - quebra de linha
 \t - tabulação
 \r - retorno de carro
 \\ - imprime uma \
 \' - imprime '
 \" - imprime "
"""

#Manipulando o tipo boolean (True [1]/False [0])
aula = True #booleano
expr = 10 > 15 #booleano
curso = 'Curso de Python'
vazio = ''

num1 = 0
num2 = 1

#Estrutura de decisão if/else (se/senão)
if aula:
    print('É verdadeiro')
    print('Fim do Programa')
else:
    print('É falso')
    print('Acabou')

print("----------------------------")
print(aula) #True
print(expr) #False
print(bool(curso)) #True
print(bool(vazio)) #False
print(bool(num1)) #False
print(bool(num2)) #True
print("----------------------------")