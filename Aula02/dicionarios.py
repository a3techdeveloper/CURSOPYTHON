"""
Dictionary são coleções, com a característica de trabalhar
com os pares {key:value} na estrutura
"""
carro = {
    'Fabricante' : 'Honda',
    'Modelo' : 'HRV',
    'Ano':'2016',
    'Cor':'Prata'
}
print(carro['Fabricante'])

carro['Cambio'] = 'Automatico' #adicionar
print(carro)

del carro['Cambio'] #remover
print(carro)

print('Fabricante: '+carro['Fabricante']) #buscar
print('Modelo: '+carro.get('Modelo')) #buscar
print("\n")

carro['Cor'] = 'Preto' #alterar
print("\n")
carro.pop('Cor') #remover

#Laço Loop que percorre toda a lista e retorna as chaves
for chave in carro:
    print('Chave: ' + chave)
print("\n")

#Laço Loop que percorre toda a lista e retorna as chaves
for chave in carro:
    print('Valor: '+ carro[chave]) #carro[Fabricante], carro[Modelo]
print("\n")

#Laço Loop que percorre toda a lista e retorna as chaves e valores
for chave, valor in carro.items():
    print('Chave: '+chave+' - Valor: '+valor)
print("\n")

#Verifica se um determinado valor é uma chave
if 'Modelo' in carro:
    print('SIM, Modelo é uma chave')
else:
    print('NÃO, Modelo não é uma chave')
print("\n")

carro.clear() #remove todos os itens
print(carro)
print("\n")

uf = {
    'DF' : 'Distrito Federal',
    'GO' : 'Goiás',
    'MG' : 'Minas Gerais'
}

print(uf['DF'])