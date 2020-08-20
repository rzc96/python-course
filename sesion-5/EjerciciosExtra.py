# Crea un programa que lea un número del teclado e imprima la suma de 0 a ese numero.

numero = int(input())
suma = 0
for i in range(0, numero+1):
    suma += i

print(suma)

# mas rapido
suma2 = 0
suma2 = numero * (numero + 1) / 2

print(suma2)

# Crea un programa que lea números del teclado indefinidamente hasta que el usuario introduzca el número 0. 
# Una vez introducido el 0. Imprime el promedio de todos los números introducidos (incluyendo el 0).

promedio_array = []
condicion_cero = True

while(condicion_cero):
    num = int(input())
    promedio_array.append(num)
    if num == 0:
        condicion_cero = False

print(len(promedio_array))
promedio = sum(promedio_array) / len(promedio_array)
print(promedio)

# Crea un programa que cree una lista de compras. 
# Primero le pide al usuario que ingrese la cantidad n de artículos. 
# Luego lee n artículos de la terminal. Una vez leídos todos. 
# Imprime la lista en orden alfabético.

cantidad_articulos = int(input("Ingrese cantidad de artículos: "))
lista_articulos = []

for i in range(0, cantidad_articulos):
    lista_articulos.append(input("Ingrese producto: "))

lista_articulos.sort()
print(lista_articulos)

# Crea un programa filtrador de números pares. 
# Primero pide al usuario que ingrese un número n, la cantidad de números en la lista. 
# Luego filtra la lista de números para que solo tenga números pares e imprime la lista.

cantidad_numeros = int(input("Ingrese cantidad de numeros: "))
numeros = []

for i in range(cantidad_numeros):
    numeros.append(int(input("Ingrese número: ")))

numeros_filtrados = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_filtrados.append(numero)

print(numeros)
print(numeros_filtrados)

# Recibe un String de entrada e imprime sólo las vocales: 
# Por ejemplo “Carlos, quien trabaja en Google, es un muy buen programador”
# Daría como resultado: “aouieaaaeooeeuuueoaao”

vocales = ['a', 'e', 'i', 'o', 'u']

entrada = input("Ingrese texto: ")
entrada_vocales = ""

for i in entrada:
    if i in vocales:
        entrada_vocales += i

print(entrada_vocales)


# (Challenge)
# Imprime una pirámide como la siguiente:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Vas a recibir de entrada un número n que indica la cantidad de filas que debes imprimir, 
# y cada fila incrementa su longitud en 1 como se ve en el ejemplo.

filas = int(input())

for i in range(filas + 1): # cada fila
    for j in range(1, i + 1): # de 1 hasta la (fila + 1) en que estas 
        print(j, end = " ")
    print("")