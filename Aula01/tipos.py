#importanto biblioteca
import random

#Em python podemos trabalhar com diversos tipos de dados

x = 1 #int -> integer
x = 'Curso de Python' #string -> cadeia de caracteres
x = 15.6 #float -> ponto flutuante
x = False #boolean True/False

#Complex
n1 = 5; n2 = 2; x = complex(n1, n2)
print(x)

#Listas (list/array)
x = ['carro','avião','navio',1,58.3,True]
print(x)

#Tuplas (tuple)
x = ('carro','avião','navio',1,58.3,True)

#Dictionary 
x = {
    'canal':'Curso de Python',
    'curso':'Django 3.0',
    'aluno':'Anderson Henrique'
}
print(x)

#Podemos trabalhar com o tipo set
x = {5,7,4,5,7,4,8}
x = frozenset({5,7,4,5,7,4,8})
#Imprime o tipo de dados
print(str(type(x)))
#Imprime o valor
print(x)

#Numéricos, Random e Casting (conversão de tipos)
num_i = 10
num_f = 5.2
num_c = 1j

#cast
x = int(num_f)
y = float(num_i)

print(x, y)  

#Podemos gerar números aleatórios, utilizando o random
num_r = [
    random.randrange(0, 59), #índice 0
    random.randrange(0, 59), #índice 1
    random.randrange(0, 59), #índice 2
    random.randrange(0, 59), #índice 3
    random.randrange(0, 59), #índice 4
    random.randrange(0, 59)  #índice 5
]

#método cast str(), int(), flot()
print('Valor 1:'+str(num_r[0]))
print('Valor 2:'+str(num_r[1]))
print('Valor 3:'+str(num_r[2]))
print('Valor 4:'+str(num_r[3]))
print('Valor 5:'+str(num_r[4]))
print('Valor 6:'+str(num_r[5]))