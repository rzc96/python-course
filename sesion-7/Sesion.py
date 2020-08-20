import math, random

pi = 3.14159265359

piFloor = math.floor(pi)
piCeil = math.ceil(pi)

print(piFloor)
print(piCeil)


# Crea una función que regrese un número aleatorio

def randomNumber(n):
    return random.randint(0, n)

print(randomNumber(100))

# Crea una función que reciba dos números 
# y regrese el piso de la división de los dos números

def returnFloor(x, y):
    return math.floor((x / y))

print(returnFloor(10,2))

# Crea una función que reciba dos números y regrese el máximo común
# divisor de los dos números

def getMCD(x, y):
    return math.gcd(x, y)

print(getMCD(10, 5))
print(getMCD(100, 22))

# Crea una función que reciba el radio de un círculo y regrese el área
# del círculo

def getCircleArea(radius):
    return math.pi * math.pow(radius, 2)

print(getCircleArea(5))
print(getCircleArea(2))

# Crea una función que reciba el área de un círculo y regrese el radio

def getCircleRadius(area):
    return math.sqrt(area / math.pi)

print(getCircleRadius(15))
print(getCircleRadius(22))
