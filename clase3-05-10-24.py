#Enteros (int)
#entradas:

#numero1 = 1
#print(type(numero1))

#suma de enteros
#numero2= 2

#proceso
#suma= numero1 + numero2

#salida
#print(suma)

# el input sirve para darle un mensaje al usuario, pero lo que toma lo va a guardar
#en la variable temperaturaDelagua, pero lo toma como str, y yo lo necesito como int,
# entonces englobo todo el input en el metodo int ()

"""


temperaturaDelagua = int(input("Ingrese la temperatura del agua:"))

if temperaturaDelagua>=100:
    print("El agua está hirviendo")
else:
    print("El agua aún no está hirviendo")
#print(type(temperaturaDelagua))
"""
#Trabajamos con una Base de datos de medicos que emiten recetas. 
# Necesitamos avisarle al profesional
# en caso de que emitio más de 1000 recetas, que tenga cuidado.

#recetasmedicas = int(input("Bienvenido doctor/ra ingrese cuantas recetas emitio:"))

#if recetasmedicas > 1000:
 #   print("Doctor/ra tenga cuidado, ud. supero las 1000 recetas emitidas")
#else:
 #   print("No se preocupe, aún no ha alcanzado las 1000 recetas emitidas")

# Decimales: llamados float (por que tienen una parte flotante, es decir la parte decimal).
 # Se usa el sistema metrico de usa, es decir que los decimales van despues del . (y no despues de la coma)


#total = 10.5



#print(type(total))

# ingrese tres facturar y realice el calculo total a pagar (suma de las tres)
#entradas
#factura1 =float(input("ingrese el monto de la factura 1: "))
#factura2 =float(input("ingrese el monto de la factura 2: "))
#factura3 =float(input("ingrese el monto de la factura 3: "))
#proceso
#total=factura1+factura2+factura3

#salida
#print(total)
#print(type(factura1))

# un = es de asignacion para declarar variables
# que la variable suma esta tomando el valor de la derecha
suma = float(input("ingrese el monto de la suma:"))

# cuando uso dos == estoy consultando si ambos son iguales
#variante con ==
#if suma == 1000.0:
 #   print("la suma da mil! correcto")
#else:
 #   print("LA SUMA NO DA MIL! TENES UN ERROR EN LA SUMA")

#variante con !=

if suma != 1000.0:
    print("LA SUMA NO DA MIL! TENES UN ERROR EN LA SUMA")
else:
    print("la suma da mil! correcto")


#
#
#
