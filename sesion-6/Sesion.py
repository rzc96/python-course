# Hacer una función que imprima "Hola Mundo"

def holaMundo():
    return "Hola Mundo"

print(holaMundo())

# Hacer una función que reciba como parámetro el nombre de una persona e imprima un saludo.

def personalizedHello(name):
    return "Hola, "+name+"!"

print(personalizedHello("Raquel"))

# Hacer una función que reciba un char (letra, fragmento de string)
# y determine si es vocal o no regresando un valor booleano

def isVowel(character):
    vocales = ['a', 'e', 'i', 'o', 'u']
    if character in vocales:
        return True
    return False

    #return character in vocales <- funciona igual

print(isVowel("a"))
print(isVowel("b"))

# Hacer una función que reciba un número n e imprima los primeros n números de la serie de Fibonacci

def fibonacci(n):
    fib = [1,1]
    if n > 2: # más de los números 1 y 1 
        for cuenta in range(0, n-2):
            fib.append(fib[cuenta] + fib[cuenta + 1])
    elif n == 1: # solo el primer número
        fib.pop()
    return fib

print(fibonacci(7))
print(fibonacci(10))

# Hacer una función que reciba una lista y regrese el menor valor de la lista

def getMinorValue(lista):
    return min(lista)

lista = [5, 3, 7, 9, 10]

print(getMinorValue(lista))