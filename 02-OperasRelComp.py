import math, os


os.system("cls")


print(" -----Grupos ICO201-9, ICO201-14----- ")


num1=input("ingrese el primer numero: ")
num2=input("ingrese el segundo numero: ")

suma=int(num1)+int(num2)
print("la suma de {} con {} es:{}".format(numero1,numero2,suma)) 
num1=input("ingrese el primer numero: ")
num2=input("ingrese el segundo numero: ")

resta=int(num1)-int(num2)
print("la resta de {} con {} es:{}".format(numero1,numero2,resta)) 

num1=input("ingrese el primer numero: ")
num2=input("ingrese el segundo numero: ")

multiplicacion=int(num1)*int(num2)
print("la multiplicacion de {} con {} es:{}".format(numero1,numero2,multiplicacion)) 

num1=input("ingrese el primer numero: ")
num2=input("ingrese el segundo numero: ")

division=int(num1)/int(num2)
print("la division de {} con {} es:{}".format(numero1,numero2,division)) 

num1=input("ingrese el primer numero: ")
num2=input("ingrese el segundo numero: ")

potencia=int(num1)**int(num2)
print("la potencia de {} con{} es:{}".format(numero1, numero2, potencia))


val1=3
val2=5

temp=val1>val2 #False
temp=val1==val2 #False
temp=val1<val2 #True
temp=val1>=val2 #False
temp=val1<=val2 #False
temp=val1!=val2 #False


print("El valor de la comparacion es:", temp)
tem2=not (val1>val2) and (val1<val2)#true

print("El valor de la comparacion not es:", tem2)

