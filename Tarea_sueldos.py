Sueldo=int(input("Ingrese el sueldo:"))



if Sueldo<1000:
    Impuesto=0

else:
    if Sueldo<=2000:
        Impuesto=Sueldo*0.10

        sueldoNeto=Sueldo-Impuesto
    else:
        Impuesto=Sueldo*0.20

        sueldoNeto=Sueldo-Impuesto

print("Impuestos: ", Impuesto)

print("Sueldo neto:", sueldoNeto)

