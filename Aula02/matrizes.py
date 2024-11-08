#Listas são arrays unidimensionais[linha]
carros = ['Fusca','Belina','Variante','Fiat 147']
#imprimir Belina

"""
Uma Lista
Linhas 0 - Fusca, Belina, Variante, Fiat 147
"""
print(carros[1])

#Matrizes são arrays bidimensionais[linha][coluna] 

"""
Uma Matriz
            Coluna 0         Coluna 1      Coluna 2         Coluna  3
Linha 0 -  Fusca[0][0]        VW           1978            Preto
Linha 1 -  Belina[1][0]       Ford         1972            Verde

"""
veiculos = [
    ['Modelo','HRV'],
    ['Fabricante','Honda'],
    ['Ano', 2015]
]

print(veiculos[0][0]) # Modelo
print(veiculos[0][1]) # HRV
print(veiculos[1][0]) # Fabricante
print(veiculos[1][1]) # Honda
print(veiculos[2][0]) # Ano
print(veiculos[2][1]) # 2015

veiculos[2][1] = 2019 #alterando o valor do ano
veiculos.append(['Cor', 'Prata']) #adicionando

for linha, coluna in veiculos:
    print('Linha: '+linha+' - Coluna: '+ str(coluna))
print('\n')
