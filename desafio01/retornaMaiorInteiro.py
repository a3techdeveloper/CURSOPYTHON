"""
Desafio - Usuário vai digitar 03 números inteiros, e independente da
ordem forem inseridos o algoritmo vai verificar qual é o maior número
e imprimir esse número
"""
import os
from time import sleep

os.system('cls')
print('-------------------------------------------')
print('        DESAFIO RETORNA MAIOR INTEIRO      ')
print('-------------------------------------------')

n1 = int(input('Digite o 1º número inteiro: ')) 
n2 = int(input('Digite o 2º número inteiro: ')) 
n3 = int(input('Digite o 3º número inteiro: ')) 

#Verifica se n1 é maior que n2 (verdadeiro)
if n1 > n2:
    n2 = n1 #Pega o valor de n1 e joga no n2
#Verifica se n2 é maior que n3 (verdadeiro)
if n2 > n3:
    n3 = n2 #Pega o valor de n2 e joga no n3

print('--------------- RESPOSTA ------------------')
print("O maior número inteiro digitado foi o "+str(n3))
sleep(5) # aguarda 5s
os.system('cls')