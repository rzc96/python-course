# Dado el siguiente arreglo = [‘Do’, ‘Re’, ‘Mi’, ‘Fa’, ‘Sol’, ‘La’, ‘Si’] y accediendo a él. 
# Imprime lo siguiente: Si Si Do Re Re Do Si La Sol Sol La Si Si La La 
# (accediendo al arreglo, no es válido directamente imprimir tales palabras).

arreglo = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']

notas = []
notas.append(arreglo[6])
notas.append(arreglo[6])
notas.append(arreglo[0])
notas.append(arreglo[1])
notas.append(arreglo[1])
notas.append(arreglo[0])
notas.append(arreglo[6])
notas.append(arreglo[5])
notas.append(arreglo[4])
notas.append(arreglo[4])
notas.append(arreglo[5])
notas.append(arreglo[6])
notas.append(arreglo[6])
notas.append(arreglo[5])
notas.append(arreglo[5])

print(notas)


# Dado el siguiente arreglo = [ “Paco”, “Pablo”, “Carlos”, “Isa” ], 
# reciba un string del usuario e indique si ese string aparece dentro del arreglo o no, 
# puedes regresar “True” si el elemento está dentro del arreglo 
# o “False” si el elemento no está dentro del arreglo.
# Ejemplo: 
# Erick
# False

nombres = [ 'Paco', 'Pablo', 'Carlos', 'Isa' ]
nombre = input("Ingrese un nombre: ")
print( nombre in nombres )

# Dado el siguiente arreglo = [12,456,2,123], 
# ordenalo e imprimelo siendo [2,12,123,456].

numeros = [ 12, 456, 2, 123]
numeros.sort()
print(numeros)

# Crea un programa que lea 6 números del teclado y los guarde en un arreglo. 
# Luego imprime la resta de la suma de los índices pares con la suma de los índices impares.

operacion = []

operacion.append(int(input())) # mas eficiente con un for
operacion.append(int(input()))
operacion.append(int(input()))
operacion.append(int(input()))
operacion.append(int(input()))
operacion.append(int(input()))

resultado = (operacion[0] + operacion[2] + operacion[4]) - (operacion[1] + operacion[3] + operacion[5]) 

print(resultado)

# Challenge: dado un arreglo con cinco elementos ingresados por el usuario, 
# imprimir “Es palíndromo” si el arreglo es palíndromo o “No palíndromo” si el arreglo no es palíndromo:
# Nota: Un palíndromo es una palabra que se lee igual del inicio al final o del final al inicio.
# Ejemplo: 
# 1 2 3 2 1
# Es palíndromo
# 1 2 3 4 5
# No palíndrono

palindromo = []

palindromo.append(int(input()))
palindromo.append(int(input()))
palindromo.append(int(input()))
palindromo.append(int(input()))
palindromo.append(int(input()))

copia_palindromo = palindromo.copy()
copia_palindromo.reverse()

if palindromo == copia_palindromo:
    print("Es palindromo")
else:
    print("No es palindromo")