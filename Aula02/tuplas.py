#Tuplas são listas, sendo que não podem ser alteradas

t_carros = ('Verona','Marea','Stilo')
#colocando a tupla dentro de uma lista
l_carros = list(t_carros)

l_carros[1] = 'Focus'
#colocando a lista dentro de uma tupla
t_carros = tuple(l_carros)

#laço for iterar os itens
for c in t_carros:
    print('Modelo: '+c)
