"""
O sistema vai sortear um número[0 a 10], e tentamos adivinhar qual número foi
sorteado
"""
import random
import os

print('-------------------------------------')
print('          JOGO DA ADIVINHAÇÃO        ')
print('-------------------------------------')

tentativas = 0 
sorteado = random.randrange(0, 10)
jogador = int(input('Digite o seu número: '))

#Enquanto o número sorteado for diferente do nosso
while(sorteado != jogador):
    #Limpar a tela
    os.system('cls')
    #verifica se o número sorteado é maior do que o nosso
    if(sorteado > jogador):
        print('ERRO, o numero e maior')
    #verifica se o número sorteado é menor do que o nosso
    elif(sorteado < jogador):
        print('ERRO, o numero e menor')
    tentativas += 1 #incrementa
    jogador = int(input('Digite o seu número: '))

print('Numero: '+str(jogador)+', voce acertou em '+str(tentativas+1)+' tentativas')