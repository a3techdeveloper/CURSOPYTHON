"""
Funções são estruturas de controle que executam procedimentos
que rotineiramente precisamos no código de programação

Criar -> def nome_funcao(param1, param2):
Invocar -> nome_funcao
"""
import os 

#Usuário insere dois números inteiros
n1 = int(input('Digite o primeiro numero inteiro: '))
n2 = int(input('Digite o segundo numero inteiro: '))

#Criamos a função
def somar():
    soma = n1 + n2
    print('Soma de '+str(n1)+' e '+str(n2)+' = '+str(soma))

def subtrair():
    soma = n1 - n2
    print('Subtração de '+str(n1)+' e '+str(n2)+' = '+str(soma))

def multiplicar():
    soma = n1 * n2
    print('Multiplicação de '+str(n1)+' por '+str(n2)+' = '+str(soma))

#Criar a função que chama todas as funções
def calculos():
    somar()
    subtrair()
    multiplicar()

#chamar a função
calculos()

"""
    Criar uma função que calcula a media de um aluno e retorna o resultado
    de acordo com o seguinte criterio
    SE a media do aluno for maior ou igual a 6, foi APROVADO SENAO foi REPROVADO
    ETAPAS
    1- Entrada de Dados (Nome do aluno, nota 1, nota 2, nota 3, nota 4)
    2- Calcular a media: (soma das notas) e divide por 4
        2.1- Estrutura Decisão Composta: if(teste_logico): valor_se_verdadeiro else:
    valor_se_falso
    3- Imprime: Nome do aluno e a sua situação de acordo com a media que obteve
"""
nome = input('Nome do(a) aluno(a): ')
n1   = float(input('Digite a Nota1: '))
n2   = float(input('Digite a Nota2: '))
n3   = float(input('Digite a Nota3: '))
n4   = float(input('Digite a Nota4: '))

def calculaMedia(): 
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 6:
        resp = 'APROVADO(A)'
    else:
        resp = 'REPROVADO(A)'
    print(nome+' foi '+resp+' com a média '+str(media))

#chamar a função
calculaMedia()
