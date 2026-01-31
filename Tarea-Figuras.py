import math, os

os.system("cls")
          
print("Figuras:\n1.- triangulo\n2.- cuadrado\n3.- circulo\n4.- pentagono\n5.- Sali\n")
opcion = int(input("Elige una opcion: "))
                   
if opcion == 1:
 Num1 = int(input("Ingrese el primer numero o medida: " ))
 Num2 = int(input("Ingrese el segundo numero o medida: "))
 Area = Num1 * Num2/2
 print ("El area es: ", Area)

if opcion == 2:
 Num1 = int(input("Ingrese el primer numero o medida: " ))
 Num2 = int(input("Ingrese el segundo numero o medida: "))
 Area = Num1 * Num2
 print ("El area es: ", Area)

if opcion == 3:
 Num1 = int(input("Ingrese el primer numero o medida: " ))
 Area = 3.1416 * num1*num1 
 print ("El area es: ", Area)

 if opcion == 4:
 Num1 = int(input("Ingrese el primer numero o medida: " ))
 Num2 = int(input("Ingrese el segundo numero o medida: "))
 Area= Num1 * Num2/2
 print ("El area es: ", Area)

if opcion == 5:
 int(input("salir: "))
