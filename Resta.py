class Restar:
    #atributos
    val1=0
    Val2=0
    resultado=0

    #metodos
    def asignarVal1(self,v1):
        self.val1 = v1
    
    def asignarVal2(self,v2):
        self.val2 = v2

    def restarValores(self):
        if (self.val1>self.val2):
            self.resultado = self.val1-self.val2
            print("El resultado de la resta es ",self.resultado)

        if (self.val2>self.val1):
            self.resultado = self.val2-self.val1
            print("El resultado de la resta es ",self.resultado)