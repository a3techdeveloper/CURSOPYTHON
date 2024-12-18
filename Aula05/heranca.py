"""
Quando temos uma classe-pai, defubuda com suas propriedades
e métodos e criamos uma classe-filha que herda todas as
propriedades e métodos da classe-pai, assim, podemos ter objetos
que aproveitam rotinas e variáveis sem que precisemos reescrevê-las
"""
#Base, Pai, Super
class NPC:
    #construtor
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    #método
    def info(self):
        print('Nome.......: '+self.nome)
        print('Time.......: '+str(self.time))
        print('Força......: '+str(self.forca))
        print('Munição....: '+str(self.municao))
        print('Vivo.......: ' + ('sim' if self.vivo else 'não'))
        print('Energia....: '+str(self.energia))
        print('-----------------------------------------------')

#Filha, Subclasse
class Soldado(NPC):
    #construtor da classe-filha
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)

#Filha, Subclasse
class Guarda(NPC):
    #construtor da classe-filha
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)

#Filha, Subclasse
class Elite(NPC):
    #construtor da classe-filha
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)

    #Sobrescrita do método
    def inf(self):
        #Override
        super().info()

#instanciando os objetos
s1 = Guarda('Tripa-Seca', 1)
s2 = Soldado('Quase-Nada', 1)
s3 = Elite('Racha-Cuca', 1)

s4 = Guarda('Super Atento', 2)
s5 = Soldado('Tiro Certo', 2)
s6 = Elite('Samurai', 2)

#passar valor propriedade vivo
s1.vivo =  False
s6.vivo = False

#executando o método da classe-pai
s1.info()
s2.info()
s3.info()
s4.info()
s5.info()

#executando o método da própria ckasse-filha Elite
s6.inf()