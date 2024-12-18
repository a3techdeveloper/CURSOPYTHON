"""
Criando a classe Carro
"""
class Carro:
    #propriedades
    velMax = 0
    cor = ""
    ligado = False

    #construtor
    def __init__(self, v, l, c):
        self.velMax = v
        self.ligado = l
        self.cor = c

    #métodos
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def andar(self):
        if(self.ligado):
            print('Andando...')
        else:
            print('Carro desligado...')

    def mostrar(self):
        print('Velocidade Máxima: '+str(self.velMax))
        print('Cor..............: '+self.cor)
        estado = 'sim' if self.ligado else 'não'
        print('Ligado...........: '+estado)
        print('--------------------------')

#Instanciando dois objetos do tipo Carro
c1 = Carro(200,False,'Preto')
c2 = Carro(200,False,'Branco')

#Passando valores para as propriedades
#c1.velMax = 200
#c1.cor = 'Preto'
#c1.ligado = False

#Imprime os valores
c1.mostrar()
c1.ligar()
c1.mostrar()

c2.mostrar()

c1.andar()
c2.andar()