#llamar al archivo y luego importamos la clase
from Suma import Sumar
from Resta import Restar
from Multiplicacion import Multiplicar 
from Division import Division 

#variables
num1=0
num2=0
opcion=0

print("*****MENU*****")
print("[1] Suma")
print("[2] Resta")
print("[3] Multiplicación")
print("[4] División")
print("[5] Salir")

opcion = input("\nDigita una opción ")

if opcion == '1':
    num1 = int(input("Ingrese el 1er. número: "))
    num2 = int(input("Ingrese el 2do. número: "))

    #Instanciamos la clase sumar
    calculadora = Sumar()

    calculadora.asginarVal1(num1)
    calculadora.asignarVal2(num2)
    calculadora.sumarValores()

if opcion == '2':
    num1 = int(input("Ingrese el 1er. número: "))
    num2 = int(input("Ingrese el 2do. número: "))

    #Instanciamos la clase restar
    calculadora = Restar()

    calculadora.asignarVal1(num1)
    calculadora.asignarVal2(num2)
    calculadora.restarValores()

if opcion == '3':
    num1= int(input("Ingrese un número y se desplegará la tabla de multiplicar "))

    #instanciamos la clase Multiplicación
    calculadora = Multiplicar()

    calculadora.asignarVal1(num1)
    calculadora.tablaMultiplicar()

if opcion == '4':
    num1 = int(input("Ingrese el 1er. número: "))
    num2 = int(input("Ingrese el 2do. número: "))

    #instanciar la clase Division
    calculadora = Division()

    calculadora.asignarVal1(num1)
    calculadora.asignarVal2(num2)

    calculadora.dividirValores()

if opcion == '5':
    print("\n***** Feliz día! *****\n")

