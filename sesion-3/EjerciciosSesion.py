# Elabora un programa que pide la edad del usuario y
# y valide con mensaje si el usuario es mayor de 21 años

edad = int(input())

if edad >= 21:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Dados 3 números, encontrar el máximo de los 3 e imprimirlo

a = int(input())
b = int(input())
c = int(input())

if a > b > c:
    print("El número más grande es: " + str(a))
elif a < b > c:
    print("El número más grande es:", b)
else: # default c es mayor
    print("El número más grande es:" + str(c))

print("Otro método de comparativa:")

print(max(a, b, c))

# Recibe de la terminal un número y valida si este número puede
# ser telefónico, consideremos que un número de teléfono debe
# tener 10 dígitos

tel = input()

if len(tel) == 10: # len() solo se le puede aplicar a string
    print("Es télefono")
else:
    print("No es un teléfono")

# Consideremos que tenemos 4 rangos de edad
# niñez (0-12 años)
# juventud (13 a 23 años)
# adultez (24 a 62 años)
# vejez (63 años en adelante)
# Recibamos un valor de entrada que representa la edad de alguien
# Clasifiquemos en qué rango de edad se encuentra la persona con un mensaje

edad = int(input())

if edad <= 12:
    print("Niñez")
elif edad <= 23:
    print("Juventud")
elif edad <= 62:
    print("Adultez")
else:
    print("Vejez")

# Para calcular el índice de masa corporal es necesario para obtener el peso
# y la estatura de una persona. Y se calcula con la formula de la izquierda
# mc = peso / altura^2
# tu tarea es recibir el peso y la altura de una persona para definir en
# que categoría de composición corporal se encuentra según la tabla de la derecha
# Peso inferior a normal = Menos de 18.5
# Normal = 18.5 - 24.9
# Peso superial al normal = 25.0 - 29.9
# Obesidad = Más de 30.0

peso = float(input())
altura = float(input())

imc = peso / (altura * altura)

print("IMC: " + imc)

if imc < 18.5:
    print("Peso inferior al normal")
if imc < 24.9:
    print("Normal")
if imc < 29.9:
    print("Peso superior al normal")
else:
    print("Obesidad")