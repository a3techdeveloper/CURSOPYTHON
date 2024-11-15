"""
Estrutura de repetição for - ele percorre todo array[](list)
buscando as informações dessa lista
"""
nomes = ['Aline','Beto','Carlos','Paula','Anderson']

#Para cada "nome" dentro do array "nomes"
for nome in nomes:
    print('Nome: '+nome)
print('\n')

#Para cada "nome" de array "nomes"
for nome in nomes:
    #Verifica se o nome é igual a Carlos
    if nome == 'Carlos':
        break #interrompe o laço
    #Imprime o nome
    print('Nome: '+nome)
print('\n')


numeros = [1,2,3,4,5,6,7,8,9,10]

#Para cada "numero" dentro do array "numeros"
for numero in numeros:
    #Verifica se o numero é igual 8
    if(numero == 8):
        break #interrompe o laço
    print('Número: '+str(numero))
print('\n')

for numero in numeros:
    #Verifica se o número é maior que 4 E número é menor que 8 [5,6,7]
    if(numero > 4) & (numero < 8):
        continue #continua a contagem
    print('Número: '+str(numero)) # imprime quem está fora da condição
print('\n')

