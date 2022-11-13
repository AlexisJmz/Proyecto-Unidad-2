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
        print("Division entre 2 numeros")
        num1 = int(input("Ingrese su primer numero:"))
        num2 = int(input("Ingrese su segundo numero:"))
        print("La division entre",num1,"/",num2,"es:", num1/num2)
        pass
    case '4':
        num = int(input("Ingrese el su numero:"))
        factorial = 1
        if num < 0:
            print("No se puede activar factorial en numeros negativos")
        elif num == 0:
            print("El factorial de 0 es 1")
        else:
            for i in range(1,num+1):
                factorial = factorial*i
            print("El factorial de",num,"es:",factorial)
            pass
# CODIGO DE XIMENA
    case '5':
        tabla = int(input("Que tabla desea mostrar:"))
        if tabla >=1 and tabla <=10:
            print(tabla,"x 1 =",tabla*1)
            print(tabla,"x 2 =",tabla*2)
            print(tabla,"x 3 =",tabla*3)
            print(tabla,"x 4 =",tabla*4)
            print(tabla,"x 5 =",tabla*5)
            print(tabla,"x 6 =",tabla*6)
            print(tabla,"x 7 =",tabla*7) 
            print(tabla,"x 8 =",tabla*8)
            print(tabla,"x 9 =",tabla*9)
            print(tabla,"x 10 =",tabla*10)
        else:
            print("Escoja un numero entre 1 y 10")
            exit()
    case '6':
        num = int(input("Ingrese el numero al que desee elevar al cuadrado y al cubo:"))
        print("El cuadrado de",num,"es:",num*num)
        print("El cubo de",num,"es:",num*num*num)
# CODIGO DE ALEXIS
    case '7':
        serie = []
        print("Cuantos numeros ingresara?: ")
        o = int(input())
        i = 0 
        while i < o:
            print ("Valor:", i + 1 )
            val = float(input())
            serie.append(val)
            i+=1
        media = sum(serie) / len(serie)
        print("el promedio es: ",media) 
    case '8':
        serie = []
        print("Cuantos numeros ingresara?: ")
        o = int(input())
        i = 0 
        while i < o:
            print ("Valor:", i + 1 )
            num = int(input())
            serie.append(num)
            i+=1

            min = serie[0]
            for a in serie:
                if a < min:
                    min = a
            
            max = serie[0]
            for a in serie:
                if a > max:
                    max = a
            
        print("La minima es:",min,"y la maxima es:",max)
    case '9':
        exit()