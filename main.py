from random import *

class chuteonumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_max = 100
        self.valor_min = 1
        self.tentarnovamente = True

    def Iniciar(self):
        self.GerarAleatorio()
        self.PedirValor()
        while self.tentarnovamente == True:
            if int(self.valor_chute) > self.valor_aleatorio:
                print('Chute um valor mais baixo!')
                self.PedirValor()
            elif int(self.valor_chute) < self.valor_aleatorio:
                print('Chute um valor mais alto!')
                self.PedirValor()
            elif int(self.valor_chute) == self.valor_aleatorio:
                print('Parabéns! Você acertou!')
                self.tentarnovamente = False

    def PedirValor(self):
        self.valor_chute = input('Chute um número: ')

    def GerarAleatorio(self):
        self.valor_aleatorio = randint(self.valor_min, self.valor_max)


chute = chuteonumero()
chute.Iniciar()
