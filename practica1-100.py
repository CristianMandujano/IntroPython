import math,os

num=int(input("Ingrese un numero que este entre el 1 y el 100: "))

while num <1 or num >100:
    print("Numero Invalido")
    num=int(input("Ingresa solo numeros entre el 1 y el 100: "))
print("El numero es:", num)
print("El numero en binario es:", bin(num))