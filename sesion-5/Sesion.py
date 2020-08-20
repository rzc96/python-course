# Dada una lista de nombres, ingresada por usuario 
# que regresa la cantidad de nombres en la lista 
# e imprima la lista alfabeticamente

ordenador = []
nombres = int(input("Numero de nombres:"))

for i in range (nombres):
    n = (input("Ingresa un nombre:"))
    ordenador.append(n)

print("Arreglo antes de ordenarlo:")
print(ordenador)
print("Arreglo ordenado:")
ordenador.sort()
print(ordenador)

# Vas a recibir un número n del teclado, vas a imprirmir los números de 1 a n,
# pero cuando el número sea divisible entre 3 vas a imprimir "Fizz"
# cuando el número sea divisible entre 5 vas a imprimir "Buzz"
# cuando el número sea divisible entre 3 y entre 5 vas a imprimir "FizzBuzz"
# y cuando no, vas a imprimir el número n

n = int(input("Ingrese cantidad de números"))

for i in range (1, n+1):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 3 != 0 and i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)

# Calcula los primeros n términos de la sucesión de Fibonacci

n = int(input("Ingrese cantidad de números para la serie de Fibonacci"))

i = 0
fibo = []

while i < n:
    if i == 0 or i==1:
        fibo.append(1)
    else:
        fibo.append(fibo[i-1] + fibo[i-2])
    i+=1

print(fibo)

# Lea un número del teclado y calcule su factorial

n = int(input())
factorial = 1
for i in range(1, n+1):
    factorial *= i

print(factorial)

# Ordena un arreglo de menor a mayor con 15 elementos 

num = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]


for i in range(len(num)):
    minimo = i  
    for j in range(i+1, len(num)): 
        if num[minimo] > num[j]: 
            minimo = j 
    num[i], num[minimo] = num[minimo], num[i] 

print(num)

