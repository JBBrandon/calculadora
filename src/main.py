# main.py
#importarmos los funciones de las operaciones
from calculadora import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada, factorial

#Se define las opsiones del menu
def mostrar_menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Factorial")
    print("8. Ver histrorial")
    print("9. Salir")

historial = []

def agregar_a_historial( operacion, resultado):
    historial.append(f"{operacion} = {resultado}")

def  mostrar_historial():
    if historial:
        print("\n Histroail de operaciones")
        for operacion in historial:
            print(operacion)
def main():
    while True:
        mostrar_menu()
        #El uso de ltry except  me sirve para que el usuario ingrese algo que no sea un numero
        try:
            opcion = int(input("Elige una opción(1-9): "))
        except ValueError:
            print("Por favor, intruduce un número valido.")
            continue

        if opcion == 9:
            print("!Hasta luego¡")
            break

        if opcion == 8:
            mostrar_historial()
            continue

        #Se valida que opsion es valido , si no  muestra un mensaje de error
        if opcion not in [1, 2, 3, 4, 5, 6, 7]:
            print("Opción no valida. Intenta de nuevo")
            continue
        
        try: 
            if opcion == 6:
                num1 = float(input("Ingresa un numero:"))
                resultado = raiz_cuadrada(num1)
                agregar_a_historial(f"sqrt({num1})", resultado)
            
            elif opcion == 7:
                num1 = float(input("Ingresa un numero:"))
                resultado = factorial(num1)
                agregar_a_historial(f"{num1}!", resultado)
            else:
                num1 = float(input("Ingresa el primer numero: "))
                num2 = float(input("Ingrese el segundo numero: "))
                #El f-string me ayuda a concatenar los valores para que sea facil de leer el codigo 
                if opcion == 1:
                    resultado = sumar(num1, num2)
                    agregar_a_historial(f"{num1} + {num2}", resultado)

                elif opcion == 2:
                    resultado = restar(num1, num2)
                    agregar_a_historial(f"{num1} - {num2}", resultado)
                elif opcion == 3: 
                    resultado = multiplicar(num1, num2)
                    agregar_a_historial(f"{num1} * {num2}", resultado)
                elif opcion == 4:   
                    resultado = dividir(num1, num2)
                    agregar_a_historial(f"{num1} / {num2}", resultado)
                elif opcion == 5:
                    resultado = potencia(num1, num2)
                    agregar_a_historial(f"{num1} ** {num2}", resultado)
            print(f"El resultado es: {resultado}")
        except ValueError:
            print("Por favor, introduce un número valido.")
        except Exception as e:
            print(f"ERROR INESPEDARO: {e}")    
if __name__ == "__main__":
    main()