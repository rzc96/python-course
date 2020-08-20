# Haz un programa que lea 2 números e imprima True si el primero es 20 veces el valor del segundo. Si no, imprime False.

print("Ejercicio #1")
a = int(input())
b = int(input())

print( a == (b * 20))

# Haz un programa que lea 3 números e imprima el producto de los 3 dividido entre la suma de los 3.

print("Ejercicio #2")
a = int(input())
b = int(input())
c = int(input())

print( (a * b * c) / (a + b + c))

# Haz un programa que lea 3 números e imprima True si están en orden ascendiente. Si no, imprime False.

print("Ejercicio #3")
a = int(input())
b = int(input())
c = int(input())

print(a < b < c)

# Haz un programa lea 4 números e imprima True si todos son negativos. Si alguno es positivo, imprime False.

print("Ejercicio #4")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(( a < 0) and (b < 0) and (c < 0) and (d < 0))

# Haz un programa que lea un número e imprima True si es un número par e imprima False si es un número impar.

print("Ejercicio #5")
a = int(print())
print( a % 2 == 0)

# Sandía (Challenge) (Redacción editada por James Scoon para mayor claridad) 
# Un caluroso día de verano, Paco y su amigo Roberto, decidieron comprar una sandía. 
# Eligieron la más grande y más madura para su opinión. 
# Pesaron la sandía y corrieron a su casa sedientos para poder comer la rica sandía. 
# Pero se encontraron con un problema. 
# Paco y Roberto son muy fanáticos de los números pares, 
# es por esto que quieren partir la sandía en en dos partes tal que cada parte pese una cantidad par de kilos, 
# no es obligatorio que pesen lo mismo. 
# 
# Crea un programa que reciba de entrada un número entero, que equivale al peso de la sandía, 
# y que imprime True si se puede separar este valor en dos partes pares o False en caso contrario. 
# Prueba el programa con enteros positivos.

print("Ejercicio #6")
a = int(input())
print( (a % 2 == 0) and (a >= 4) )