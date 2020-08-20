###############
print("Como funcionan los if en python")

condicion = True

if condicion:
    print("Adentro")
    print("Sigo adentro")
print("Adios")

###############
print("Validación con if & else")

numero = int(input())

if numero > 0:
    print("Es positivo")
else:
    print("Es negativo")

################
print("Validación con elif:")

if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("Es 0")

################
print("Condiciones anidadas")

if numero > 0:
    if numero % 2 == 0:
        print("Es positivo y par")
    else:
        print("Es positivo e impar")
else:
    if numero % 2 == 0:
        print("Es negativo (o 0) y par")
    else:
        print("Es negativo (o 0) e impar")