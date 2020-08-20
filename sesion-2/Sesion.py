num = 3
print(num)

########################

# recibe puros valores int
a = int(input())
b = int(input())

print(a + b)

########################

# recibe puros valores flotantes

a = float(input())
b = float(input())

print(a + b)


#########################

# para variables booleanas 
# True y False con la primera letra mayúscula
# true y false lo toma como variable

print(True and True)
print(not False and False)
print(not False and not False)

#########################

# Ejercicio 1
# Haz un programa que lea 2 y 3 e imprima su suma (5)

a = int(input())
b = int(input())

print(a + b)

#########################

# Ejercicio 2
# Haz un programa que lea 3 números e imprima la multiplicación 
# del primer por el segundo y a eso le sume el tercero

a = int(input())
b = int(input())
c = int(input())

print((a * b) + c)

# Ejercicio 3
# Haz un programa que lea un número e imprima la mitad
# de ese número

a = int(input())

print(a / 2)

# Ejercicio 4
# Haz un programa que lea 3 números e imprima True 
# si el primero y segundo son iguales 
# o si el primero es al menos 3 unidades más grande que el segundo.
# Si no imprime False
# 2 2 3 da true
# 3 7 7 da false

a = int(input())
b = int(input())
c = int(input())

print ( (a == b) or (a - 3 >= b) )