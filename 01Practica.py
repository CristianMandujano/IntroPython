import math,os

Contador=1
Suma=0

while Contador<=5:
    Calificacion=int(input("infrese la calificacion:"))
    Suma+=Calificacion
    Contador+=1

Promedio=Suma/5
print("El promedio es:", Promedio)