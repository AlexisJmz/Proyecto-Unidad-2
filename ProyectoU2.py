print("¿Que desea hacer?")
print("1. Suma de numeros")
print("2. Multiplicacion de numeros")
print("3. Division")
print("4. Calcular Factorial")
print("5. Tablas de multiplicar")
print("6. Cuadrado y cubo de un numero")
print("7. Promedio de una serie de numeros")
print("8. Maximo y minimo")
print("9. Salir")
o = input("Escoja su opcion:")
match o:
# CODIGO DE SARA
    case '1':
        opcion = int(input("Cuantos numeros quieres sumar? (min 2, max 5):"))
        if opcion == 2:
            print("Ingrese sus 2 numeros")
            num1 = int(input("Primer numero:"))
            num2 = int(input("Segundo numero:"))
            print("La suma de", num1,"+", num2, "es:", num1+num2)
        elif opcion == 3:
            print("Ingrese sus 3 numeros")
            num1 = int(input("Primer numero:"))
            num2 = int(input("Segundo numero:"))
            num3 = int(input("Tercer numero:"))
            print("La suma de", num1,"+", num2,"+", num3,"es:", num1+num2+num3)
        elif opcion == 4:
            print("Ingrese sus 4 numeros")
            num1 = int(input("Primer numero:"))
            num2 = int(input("Segundo numero:"))
            num3 = int(input("Tercer numero:"))
            num4 = int(input("Cuarto numero:"))
            print("La suma de", num1,"+", num2,"+", num3,"+", num4,"es:", num1+num2+num3+num4)
        elif opcion == 5:
            print("Ingrese sus 5 numeros")
            num1 = int(input("Primer numero:"))
            num2 = int(input("Segundo numero:"))
            num3 = int(input("Tercer numero:"))
            num4 = int(input("Cuarto numero:"))
            num5 = int(input("Quinto numero:"))
            print("La suma de", num1,"+", num2,"+", num3,"+", num4,"+", num5,"es:", num1+num2+num3+num4+num5)
        else:
            print("Seleccione otra opcion")
    case '2':
        opcion = int(input("Cuantos numeros quieres multiplicar? (min 2, max 5):"))
        if opcion == 2:
            print("Ingrese sus 2 numeros")
            num1 = int(input("Primer numero:"))
            num2 = int(input("Segundo numero:"))
            print("La multiplicacion de", num1,"x", num2, "es:", num1*num2)
        elif opcion == 3:
            print("Ingrese sus 3 numeros")
            num1 = int(input("Primer numero:"))
            num2 = int(input("Segundo numero:"))
            num3 = int(input("Tercer numero:"))
            print("La multiplicacion de", num1,"x", num2,"x", num3,"es:", num1*num2*num3)
        elif opcion == 4:
            print("Ingrese sus 4 numeros")
            num1 = int(input("Primer numero:"))
            num2 = int(input("Segundo numero:"))
            num3 = int(input("Tercer numero:"))
            num4 = int(input("Cuarto numero:"))
            print("La multiplicacion de", num1,"x", num2,"x", num3,"x", num4,"es:", num1*num2*num3*num4)
        elif opcion == 5:
            print("Ingrese sus 5 numeros")
            num1 = int(input("Primer numero:"))
            num2 = int(input("Segundo numero:"))
            num3 = int(input("Tercer numero:"))
            num4 = int(input("Cuarto numero:"))
            num5 = int(input("Quinto numero:"))
            print("La multiplicacion de", num1,"x", num2,"x", num3,"x", num4,"x", num5,"es:", num1*num2*num3*num4*num5)
        else:
            print("Seleccione otra opcion")
# CODIGO DE CYNTHIA
    case '3':
    case '4':
# CODIGO DE XIMENA
    case '5':
    case '6':
# CODIGO DE ALEXIS
    case '7':
    case '8':
    case '9':