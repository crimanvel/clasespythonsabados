#Comentarios: son líneas de código que, al ejecutarse 
# el programa, no son intepretadas. Sirven para dejar
# notas en el código. 
# Debo escribir el símbolo # antes de cada línea.

#Ejercicio #1:
#Calcular la suma de 20 más 20, 
# y mostrar por pantalla el resultado.

#Tipos de datos simples:
#Númericos:
#           -Enteros: en Python se conocen como int.
#           -Decimales: en Python se conocen como float.  
# Texto: 
#           -Cadena de carácteres: en Python se conocen como str
# Booleano: -Son datos que tienen uno de los dos siguientes valores de verdad 
#                   -True (Verdadero)
#                   -False (Falso)     

#Entradas
#numero1=20
#numero2=20

#Procesos
#suma=numero1+numero2

#Salidas
#print(suma)


#Ejercicio 2
# Calcular la suma de dos números enteros (que el usuario ingrese)
# y mostrar el resultado por pantalla.

#Entradas
#numero1=int(input("Ingrese el primer número a sumar: "))
#numero2=int(input("Ingrese el segundo número a sumar: "))

#Para conocer el tipo de dato de una variable
#utilizo el comando print(type(nombredelavariable))

#print(type(numero1))
#print(type(numero2))

#Procesos
#suma=numero1+numero2

#Cuando sumamos dos variables de tipo int
#obtenemos la suma de números enteros
#ejemplo: 30 + 50 , el resultado sera 80

#Salidas
#print("La suma de los números ingresados es: ",suma)

#Ejercicio #3:
# Ingrese dos patentes de auto y muestre por pantalla las patentes ingresadas

#Entradas
#patente1=input("Ingrese la patente #1:")
#Cuando trabajo con datos que son alfanúmericos, debo trabajar con datos
#de tipo str (cadena de caracteres).
#Los tipos númericos NO incluyen caracteres especiales ni letras
#En cambio el tipo str, SI incluye números y caracteres especiales.
#patente2=input("Ingrese la patente #2:")
#Procesos

#Salidas
#Dentro de un print puedo agrupar texto y variables
#Pero tengo que tener en cuenta lo siguiente:
#   Si trabajo con texto, tiene que estar entre comillas dobles ""
#   Si tabajo con nombres de variables tiene que ir exactamente el nombre de la variable sin nada más
#Todo esto separado entre comas ,

#print("La primera patente ingresada fue: "
      #,patente1, "La segunda patente ingresada fue: "
      #, patente2)

#Ejercicio 4
# Pedir la condición de un alumno para saber si esta aprobado (True) o desaprobado (False)
#nombreAlumno=input("Ingrese el nombre del alumno: ")
#condicionAlumno =bool(input("Ingrese la condición del alumno :"))

#print("El alumno ", nombreAlumno, "tiene la condición:", condicionAlumno)

#Fases de decisión (consulta):

#If: utilizada para evaluar una condición y hacer algo
# en caso de que la se cumpla la condición
# y para hacer otra cosa en caso de que no se cumpla.

#Ejercicio 5

#Ingrese la edad de una persona, si la edad es mayor o igual que 18 años
#Monstrar por pantalla un mensaje que diga : "Usted es mayor de edad"
#Caso contrario: "Usted es menor de edad"
#edad=int(input("Ingrese su edad:"))
#if
    #if condicion:
        #operaciones por si se cumple la condicion
    #else:
        #operaciones por si no se cumple la condicion

#operadores lógicos de comparación:
    #<= menor igual que
    #>= mayor igual que
    #< menor que
    #> mayor que
    # == igual que
#if edad>=18:
 #   print("Usted es mayor de edad")
#else:
  #  print("Usted es menor de edad")


#Ejercicio 6
#Ingrese la nota de un alumno, si la nota es mayor o igual a 6, que diga un 
#   mensaje que: "El alumno está aprobado", caso contrario: "El alumno esta desaprobado"

#Entradas
#nombre=input("Ingrese el nombre del alumno: ")
#nota=float(input("Ingrese la nota del alumno: "))
#Procesos
#if nota >= 6:
 #   print("El alumno ",nombre," está aprobado") #Salidas
#else:
 #  print("El alumno ",nombre, "esta desaprobado")#Salidas

 
#Ejercicio 7 - variante del ejercicio 6 utilizando <
#Entradas
#nombre=input("Ingrese el nombre del alumno: ")
#nota=float(input("Ingrese la nota del alumno: "))
#Procesos
#if nota < 6:
 #   print("El alumno ",nombre," está desaprobado") #Salidas
#else:
    #print("El alumno ",nombre," está aprobado") #Salidas

#Ejercicio 8- variante del ejercico 6 utilizando > && =
#nombre=input("Ingrese el nombre del alumno: ")
#nota=float(input("Ingrese la nota del alumno: "))
#if nota>6 or nota == 6:
    #print("El alumno ",nombre," está aprobado") #Salidas
#else:
    #print("El alumno ",nombre," está desaprobado") #Salidas

#Ejercicio 9 variante de ejercicio #6
#if anidados: en donde en el else del primer if, ingreso otro if

nombre=input("Ingrese el nombre del alumno: ")
nota=float(input("Ingrese la nota del alumno: "))
if nota>0 and nota<6:
    print("El alumno ",nombre," está desaprobado") #Salidas
else:
    if nota>=6 and nota<=10:
        print("El alumno ",nombre," está aprobado") #Salidas
    else:
        print("usted ingreso una nota invalida")    

