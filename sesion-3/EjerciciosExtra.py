# Escribe un programa que le pida al usuario que 
# introduzca un mes (ej. enero, febrero, etc.). 
# El programa debe imprimir cuantos días hay en ese mes (asume un año no bisiesto).

mes = input()

if mes == "febrero":
    print("Tiene 28 días")
elif mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre":
    print("Tiene 31 días")
else:
    print("Tiene 30 días")

# Escribe un programa que le pida al usuario que 
# introduzca un día de la semana (ej. lunes, martes, etc.). 
# El programa debe imprimir la posición de ese día en la semana. 
# En este ejemplo asumimos que la semana empieza en lunes 
# por lo que lunes sería 1, martes sería 2, etc.

dia = input()

if dia == "lunes":
    print("día 1")
elif dia == "martes":
    print("día 2")
elif dia == "miercoles":
    print("día 3")
elif dia == "jueves":
    print("día 4")
elif dia == "viernes":
    print("día 5")
elif dia == "sabado":
    print("día 6")
else:
    print("día 7")

# Escribe un programa que le pida al usuario un año 
# e imprima “Bisiesto” si el año es bisiesto 
# e imprima “No bisiesto” en el caso contrario.

year = int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("bisiesto")
else:
    print("no es bisiesto")
    

# Crea un clasificador de números de la siguiente manera. 
# Pide al usuario que ingrese un número entero cualquiera. 
# Indica si es positivo o no, indica si es un número par, 
# indica si es menor o mayor que 100. Imprime tu clasificación 
# en una sola oración como en este ejemplo con el número -53:  
# “Es un número negativo, par y menor que 100”

#CONCATENACION

# numero = int(input())
# if numero > 0:
#     texto1 = "Positivo "
# else:
#     texto1 = "Negativo "
# if numero % 2 == 0:
#     texto2 = "Par "
# else:
#     texto2 = "Impar "
# if numero > 100:
#     texto3 = "Mayor que 100"
# else:
#     texto3 = "Menos que 100"

# print(texto1 + texto2 + texto3)



# Challenge
# Averigua si es un cuadrado
# Vas a recibir dos números enteros positivos que representan 
# un lado y una diagonal de un cuadrilátero. 
# Tu tarea es identificar si la figura es un cuadrado o un rectángulo.

lado = float(input())
diagonal = float(input())

eps = 0.0001

resta = diagonal - ( 2 * lado * lado ) ** (0.5)
if resta <= eps and resta >= -eps:
    print("cuadrado")
else:
    print("rectangulo")