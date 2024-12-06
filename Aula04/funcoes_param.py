"""
Função com parâmetros - Podemos declarar parâmetros que serão utilizados
dentro do contexto da função. Ex.: def nome_funcao(par1, par2, par3):
"""
def somar(x, y):
    print('Soma deu: '+ str(x+y))

#chamando função e passando os parâmetros
somar(10, 20)
somar(50, 130)
somar(70, 30)
print('\n')

"""
IMC - Índice de Massa Corporal
IMC : peso / altura²
Se o valor do IMC for maior ou igual a 18.5 e menor que 25, PESO IDEAL, 
Senao FORA DO PESO IDEAL
"""
def calculaIMC(peso,altura):
    imc = peso / (altura ** 2)
    if(imc >= 18.5) & (imc < 25):
        result = 'ESTÁ NO PESO IDEAL'
    else:
        result = 'NÃO ESTÁ NO PESO IDEAL'
    print('Com o IMC de '+str(imc)+' você '+result)

#chamar função
calculaIMC(93, 1.80)

#parâmetros arbitrários
def textos(*txt):
    for param in txt:
        print(param)

#chamando a função
textos('Python','Django','Jupiter','SQLite','Pandas')
print('\n')


y = int(input('Digite o valor de y: '))
#parâmetro default (padrão)
def multiplicar(x = 10):
    resultado = x * y
    print('O resultado da multiplicação: '+str(resultado))

#chamando a função
multiplicar()