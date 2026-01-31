import os 

os.system("cls")


Num=int(input("Ingrese un numero: "))

print("La tabla de multiplicar del numero", Num, "es: ")

for i in range (1,11):
    print(str(Num) + "x" + str(i) + "=" + str(Num*i  ))
