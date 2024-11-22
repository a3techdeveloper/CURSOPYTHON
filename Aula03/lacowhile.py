"""
Estrutura de repetição while -> verifica um teste lógico, enquanto o resultado do teste retornar True, ele permanece no laço.
"""
import os
os.system('cls') #Limpar a tela

i = 0

#Enquanto a condição for verdadeira
while i <= 10:
    print(i) #imprime o valor de i
    i += 1 #incrementa (soma 1)
print('Fim do Loop')

numeros = ['Um','Dois','Três','Quatro','Cinco','Seis','Sete']
x = 0
tamanho = len(numeros) #retorna quantidade de itens
print('\n')

#Enquanto o valor de x for menor que quantidade de itens
while x < tamanho:
    print(numeros[x]) #imprime o item
    x += 1 #incrementa
print('Fim do Loop')

os.system('cls') #Limpar Tela

clientes = [] #Lista de clientes vazia
cliente = input('Digite o nome do cliente: ') #pega o valor e armazena
#Enquanto o valor armazenado for diferente de 'sair'
while cliente != 'sair':
    clientes.append(cliente) #adiciona o cliente na lista clientes
    cliente = input('Digite o nome do cliente: ')
os.system('cls') #Limpar Tela

print('------- Lista de Clientes ---------')
print('-----------------------------------')
#Para cada cliente dentro da lista clientes
for cliente in clientes:
    print(cliente) #imprime o cliente
print('Fim da Listagem')