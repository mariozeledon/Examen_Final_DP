class Multiplicar:
    #atributos
    val1=0
    i=0

    #metodos
    def asignarVal1(self,v1):
        self.val1 = v1

    def tablaMultiplicar(self):
        for i in range(11):
            print(i," X ",self.val1," = ",self.val1*i)
