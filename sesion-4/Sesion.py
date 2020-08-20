# Elabora un arreglo que contenga los números del 1 al 5

numero = [1,2,3,4,5] 

print(numero)

#Teniendo el siguiente arreglo
# nums = [1,2,3,4,5,6,7,8,9,10]
# Transformarlo para que quede como el siguiente:
# nums = [3,3,3,6,7,8,9]

nums = [1,2,3,4,5,6,7,8,9,10]

nums.pop(0)
nums.pop(0)
nums.pop(0)
nums.pop(0)
nums.pop(0)
nums.insert(0,3)
nums.insert(0,3)
nums.insert(0,3)
nums.pop(7)

print(nums)

# Teniendo un arreglo,que solo tenga numeros par

pares = [1,2,3,4,5,6,7,8,9,10]
pares.pop(0)
pares.pop(1)
pares.pop(2)
pares.pop(3)
pares.pop(4)

print(pares)


# Elabora un arreglo que contenga los primeros 7 términos de la secuencia de Fibonacci

# fib = [1,1]
# temp1 = (len-1) + (len-2)
# fib.append(temp1)

fib = [1] * 2

fib.append(fib[0] + fib[1])

fib.append(fib[1] + fib[2])

fib.append(fib[2] + fib[3])

fib.append(fib[3] + fib[4])

fib.append(fib[4] + fib[5])

fib.append(fib[5] + fib[6])

print(fib)