class Avaliacao :
    def __init__(self, matricula=0, presenca=0.1, nota1=0, nota2=0, substitutiva=0, nota_minima=6.0):
        self.matricula = matricula
        self._presenca = presenca
        self.nota1 = nota1
        self.nota2 = nota2
        self.substitutiva = substitutiva
        self.nota_minima = nota_minima

    @property
    def presenca(self):
        return self._presenca

    @presenca.setter
    def presenca(self, presenca):
        if(presenca<=1.0):
            self._presenca=presenca
        

if __name__ == "__main__":
    a1 = Avaliacao(123, substitutiva=10.0)
    a1.presenca = 10.0
    print(a1.matricula, a1.presenca)

   