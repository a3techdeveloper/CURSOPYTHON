#Coleção List - arrays indexados
carros = ['HRV','Golf','Argo','Focus']
#índice 3 alterar o valor 'Fusion'
carros[3] = 'Fusion'

print(carros) #Imprime a lista de carros

#Adiciona itens na lista
carros.append('Fit')
carros.append('Polo')

print(carros) #Imprime os itens

#Remove da lista, remove último, remove pelo índice
carros.remove('Fit')
carros.pop() #Polo
del carros[2] #Argo

print(carros) #Imprime os itens

print(str(len(carros))+' carros na lista') #quantidade de itens

carros.clear() #Limpa a lista
print(carros) #Imprime os itens

#2 listas
frutas1 = ['morango','laranja','uva','goiaba']
frutas2 = ['banana','maca','melancia']

#copia os itens da lista para outra lista
frutas_cop = list(frutas1)
print(frutas_cop)

#Mescla duas ou mais listas
frutas_merg = frutas1 + frutas2
print(frutas_merg)