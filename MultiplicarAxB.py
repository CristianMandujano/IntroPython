import os

os.system("cls")


A= int(input("Ingrese el primer numero: "))
B= int(input("Ingrese el segundo numero: "))
resultado=0
contador=0
suma=""

while contador< B:
    resultado+=A
    suma+= str(A)
    if contador<B-1:
        suma+= "+"
    contador+=1

print(f"{suma}={resultado}")
