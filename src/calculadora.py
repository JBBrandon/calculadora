#calculadora.py
import math
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b    

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def potencia(a, b):
    return a ** b   

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede obtener la raiz cuadrada de un numero negativo"
    return math.sqrt(a)

def factorial(a):
    if a < 0: 
        return "Error: No se puede obtener el factorial de un numero negativo"
    return math.factorial(int(a))
