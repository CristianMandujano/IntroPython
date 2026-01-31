'''
pedir 5 suleos agregar a 
lista e imprimir
'''

sueldos=[]

cont=0

while cont<=4:
    tem=float(input("Dame el sueldo "+str(([cont+1]))))
    sueldos.append(tem)
    cont+=1
    
print("Los sueldos son: ", (sueldos))

print("El promedio de los sueldos es: ")

promedio = (sueldos/5)
print("El promedio es: ", promedio)
