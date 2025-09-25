def calculator():#Definir el proyecto
    while True:#Iniciar el while para el menu
        print("\nBienvenido a la calculadora")
        print("1. Suma")#Agregado de opciones
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        opcion = input("Elige una opcion: ")#Aqui la variable guarda la seleccion

        if opcion == "1":#Acciones de la opcion 1
            num1 = float(input("Ingresa el primer número: "))#Delcaramos num1 y num2 de tipo float
            num2 = float(input("Ingresa el segundo número: "))
            print("Resultado:", num1 + num2)#Hace las operaciones logicas y las muestra

        elif opcion == "2":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print("Resultado:", num1 - num2)

        elif opcion == "3":
            num1 = float(input("Ingresar el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
            print("Resutado", num1 * num2)

        elif opcion == "4":
            num1 = float(input("Ingresar el primer numero: "))
            num2 = float(input("Ingresar el segundo numero: "))
            print("Resultado",num1 / num2)

        elif opcion == "5":
            print("Saliendo de la calculadora...")#Da cierre al programa
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Llamar la función para que el programa se ejecute
calculator()
