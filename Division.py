class Division:
    #atributos
    val1=0
    val2=0

    #metodos
    def asignarVal1(self,v1):
        self.val1=v1

    def asignarVal2(self,v2):
        self.val2=v2

    def dividirValores(self):
        if (self.val1>self.val2):
            print("El resultado de la división es: ",self.val1/self.val2)

        if (self.val2>self.val1):
            print("El resultado de la división es: ",self.val2/self.val1)