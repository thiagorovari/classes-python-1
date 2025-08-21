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

class Guiche:
    def __init__(self, numero=0,area=0.0, empresas=[]):
        self.numero=numero
        self.area=area
        self.empresas=empresas

class Empresa:
    def __init__(self, nome="", anoFundacao=0, cnpj="", guiches=[]):
        self.nome=nome
        self.anoFundacao=anoFundacao
        self.cnpj=cnpj
        self.guiches=guiches
    

class Onibus:
    def __init__(self, placa="", anoFabricacao=0, bagageiro=0.0, totalAssentos=0, totalLeitos =0, empresa=None):
        self.placa=placa
        self.anoFabricacao=anoFabricacao
        self.bagageiro=bagageiro
        self.totalAssentos=totalAssentos
        self.totalLeitos=totalLeitos
        self.empresa=empresa


if __name__ == "__main__":
    rSp = Rodoviaria(cidade="Sao Paulo")
    rIta = Rodoviaria(cidade="Itajuba")
    o = Onibus(empresa="Passaro Marron")
    p = Passageiro(nome="Thiago")
    b = Bilhete(origem=rSp, destino=rIta, onibus=o,passageiro=p)

    print(b.passageiro.nome , "vai para", b.destino.cidade)