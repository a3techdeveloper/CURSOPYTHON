#Biblioteca 
import os
from time import sleep

os.system('cls') #limpar tela

#o método input permite entrada de dados
nome = input('Digite o seu nome:')
#o método print permite saida de dados
print('O nome digitado foi '+nome)

#aguardar 3 segundos
sleep(3)

os.system('cls') #limpar tela

#pegando o valor string do input convertendo em inteiro e armazenando
num1 = int(input('Digite o primeiro valor:'))
num2 = int(input('Digite o segundo valor:'))
#somando os valores e armazenando  cast -> tipo(var)
resultado = num1 + num2
print('O resulta da soma: '+str(resultado))