class Passageiro:
    def __init__ (self, nome="", rg=""):
        self.nome=nome
        self.rg=rg

class Bilhete:
    def __init__(self, poltrona =0, saida=0, chegada=0, passageiro=None, 
                 origem=None, destino=None, onibus=None):
        self.poltrona=poltrona
        self.saida=saida
        self.chegada=chegada
        self.passageiro=passageiro
        self.origem=origem
        self.destino=destino
        self.onibus=onibus

class Rodoviaria:
    def __init__ (self, cidade="", endereco="", guiches=[]):
        self.cidade=cidade
        self.endereco=endereco
        self.guiches=guiches

class Bagagem:
    def __init__(self, bilhete, identificacao="", peso=0.0):
        self.bilhete=bilhete
        self.identificacao=identificacao
        self.pesso=peso

##class Guiche:

        