import math
import platform
import matplotlib.pyplot as plt
# Utiliza la fórmula general (imagen adjunta) de la forma 
# a* x^2 + bx + c y crea una función que reciba 3 números 
# representan los coeficientes a, b y c y 
# obtenga las soluciones a x.

#def generalFormula(a, b, c):
    #print((-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a))
    #print((-b - math.sqrt((b * b) - (4 * a * c))) / (2 * a))

#generalFormula(1, 2, 3)

# Calcular la altura de un triangulo equilatero

# numero = int(input())

# while numero > 0:
    # numero = numero - 1
    # lado = int(input())
    # print(format(lado / 0.866, '.2f')) # sen(60) = 0.866


# Crea una función llamada queTengo(), 
# que no tenga parámetros y regresa un string con 
# el sistema operativo que estás utilizando. 
# (Tip: ¿Habrá una librería que nos de esto?)

def queTengo():
    return platform.system()

print(queTengo())

# Juanito es muy curioso y en su preparación para el TMR de Jalisco
# está estudiando las matemáticas porque se le había olvidado
# por completo. Justo en medio de su estudio se topó con un problema
# un tanto complicado

# Entrada - un solo entero N que representa el limite superior 
# de la serie
# Salida - un solo entero K, la respuesta de la serie

def sumaDeCuadrados(n):
    return int((n * (n + 1) * (2 * n + 1)) / n)

print(sumaDeCuadrados(5))
    
# CHALLENGE: (Ojo: Se necesita utilizar pip para instalar 
# la librería matplotlib)
# Investiga cómo se usa matplotlib y realiza un histograma de un 
# arreglo de números que representen la temperatura de la semana 
# en Monterrey.

def plottingWeather():
    y = [26, 28, 31, 30, 30, 31, 30, 30]
    x = ['Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo', 'Lunes', 'Martes', 'Miercoles']

    plt.bar(x, y, align= 'center')
    plt.xlabel = "Días"
    plt.ylabel= "Temperatura"
    plt.hlines(y, 0, x)
    plt.show()

print(plottingWeather())

