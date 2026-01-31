import os

os.system("cls")

Num=int(input("Ingrese un numero: "))

print("Piramide del  numero", Num, ":")

for i in range(1, Num+1):
    print('*' * i )