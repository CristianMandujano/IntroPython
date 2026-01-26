import os 
op=0

while op!=5:
    os.system("cls")
    print("1.- suma\n2.- resta\n3.- multiplicacion\n4.- Division\n5.- salir")
    op=int(input("Seleccione una opcion (1-5): "))
    if op==1:
        num1=int(input("Ingrese el primer numero: "))
        num2=int(input("Ingrese el segundo numero: "))
        print("La suma de {} + {} es: {}". format(num1,num2,num1+num2))
        input("Presiona Enter para continuar...")
    if op==2:
        num1=int(input("Ingrese el primer numero: "))
        num2=int(input("Ingrese el segundo numero: "))
        print("La resta de {} - {} es: {}". format(num1,num2,num1-num2))
        input("Presiona Enter para continuar...")
    if op==3:
        num1=int(input("Ingrese el primer numero: "))
        num2=int(input("Ingrese el segundo numero: "))
        print("La multiplicacion de {} * {} es: {}". format(num1,num2,num1*num2))
        input("Presiona Enter para continuar...")
    if op==4:
        num1=int(input("Ingrese el primer numero: "))
        num2=int(input("Ingrese el segundo numero: "))
        if num2!=0:
            print("La division de {} / {} es: {}". format(num1,num2,num1/num2))
        else:
            print("Error no se puede dividir entre cero.")
        input("Presiona enter para continuar...")
        