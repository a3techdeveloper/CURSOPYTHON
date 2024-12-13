"""
Funções que retornam valores, utilizando a palavra-chave return.
"""
#lista
valores = [1,5,3,2,10,4,8] #33

#cria a função
def somarlista(listaNumeros):
    #valor inicial
    result = 0
    #percorre todos os itens
    for numero in listaNumeros:
        result += numero
    return result

#chama a função
r = somarlista(valores)
print(str(valores)+': Soma = '+str(r))