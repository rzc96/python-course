

# Crea una función que reciba un número y regrese un booleano indicando si es divisible entre 243
def isDivisible(num):
    return num % 243 == 0

print(isDivisible(490))
print(isDivisible(486))

# Crea una función llamada multiplicarString que reciba un string y un número entero positivo. 
# La función debe regresar el mismo string repetido n veces. Por ejemplo:
# “Hola” y 3 → “HolaHolaHola”
# “Adios” y 5 →	“AdiosAdiosAdiosAdiosAdios”

def multiplicarString(texto, num):
    return texto * num

print(multiplicarString("hola", 3))
print(multiplicarString("adios", 5))

# Crea una función que reciba 3 números como parámetros (no en arreglo) 
# y regrese la suma si al menos uno de esos números es mayor que 100, 
# si no regresa la multiplicación de los 3.

def checarValores(x, y, z):
    if x > 100 or y > 100 or z > 100:
        return x + y + z
    return x * y * z

print(checarValores(1, 2, 3))
print(checarValores(100, 2, 3))

# Crea una función llamada stringsExclusivos que reciba 2 strings 
# y regresa true si uno tiene puras vocales y el otro puras consonantes, 
# regresa false en cualquier otro caso.
# Ejemplo:
# “aeeaei” , “qwt” →  True
# “aaeac” , “ttsdf”  →  False

def onlyVocals(str):
    vocals = "aeiou"
    for c in str:
        if not(c in vocals):
            return False
    return True

def onlyCons(str):
    vocals = "aeiou"
    for c in str:
        if c in vocals:
            return False
    return True

def stringsExclusivos(text1, text2):
    case1 = onlyVocals(text1) and onlyCons(text2)

    case2 = onlyCons(text1) and onlyVocals(text2)

    return case1 or case2

print(stringsExclusivos("aeeaei", "qwt"))
print(stringsExclusivos("aaeac", "ttsdf"))



#  Crea una función que se llame esPalindromo que reciba un string cualquiera 
# y regrese true si es palíndromo, y false en el caso contrario.
# Ejemplo:
# “hola” →  False
# “kayak” → True

def esPalindromo(texto):
    reverso = texto[::-1]
    if texto.lower() == reverso.lower():
        return True
    return False

print(esPalindromo("Ana"))
print(esPalindromo("Raquel"))

# Challenge: Crea una función llamada aBinario que reciba un número entero positivo 
# y regrese un arreglo de ceros y unos que sea la representación en el sistema numérico binario del número recibido. 
# Si no estás familiarizado con el sistema binario, dale primero una leida a este artículo: 
# https://www.elvisualista.com/2016/10/20/que-son-los-numeros-binarios/
# Ejemplos: 
# 5 →  [ 1, 0, 1 ]
# 2 →  [ 1, 0 ]
# 1 →  [ 1 ]
# 45 →  [ 1, 0, 1, 1, 0, 1 ]

def aBinario(num):
    return f'{num:08b}'

print(aBinario(5))
print(aBinario(2))
print(aBinario(1))
print(aBinario(45))

def binario(num):
    lista = []
    while num != 0:
        bit = num % 2
        lista.append(bit)
        num = int(num/2)
    lista.reverse()
    return lista

print(binario(5))
print(binario(2))
print(binario(1))
print(binario(45))