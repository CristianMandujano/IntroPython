import math, os
suma=0
num=int(input("Ingrese un numero diferente de cero para continuar o 0 para salir"))

while num!=0:
    suma+=num
    num=int(input("Ingrese el numero 0 para terminar"))
    print("La suma total es: ", suma)