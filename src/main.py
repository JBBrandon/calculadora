# main.py

from src.calculadora import sumar, restar, multiplicar, dividir

def mostrar_menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elige una opción(1-5): "))
        except ValueError:
            print("Por favor, intruduce un número valido.")
            continue

        if opcion == 5:
            print("!Hasta luego¡")
            break

        if opcion not in [1, 2, 3, 4]:
            print("Opción no valida. Intenta de nuevo")
            continue

        try:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
        except ValueError:
            print("Por favor, ingresa numeros validos.")
            continue

        if opcion == 1:
            print(f"El rasultado es: {sumar(num1, num2)}")
        elif opcion == 2:
            print(f"El resultado es: {restar(num1, num2)}")
        elif opcion == 3: 
            print(f"El resultado es: {multiplicar(num1, num2)}")
        elif opcion == 4:   
            print(f"El resultado es: {dividir(num1, num2)}")    
    
if __name__ == "__main__":
    main()