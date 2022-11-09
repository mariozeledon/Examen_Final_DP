class Sumar:
    #atributos
    val1=0
    val2=0
    resultado=0

    #metodos
    def asginarVal1(self,v1):
        self.val1 = v1

    def asignarVal2(self,v2):
        self.val2 = v2

    def sumarValores(self):
        self.resultado = self.val1 + self.val2
        print("El resultado de la suma es ",self.resultado)