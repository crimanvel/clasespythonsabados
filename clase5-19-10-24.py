#Estrecturas de Repetición:
#Ayuda a realizar tareas hasta que suceda algún corte.

#Ejercicio 1: Ingresar 3 notas de los alumnos 
# y realizar un promedio de las notas
'''

Sin usar estructura de repetición
nota1=float(input("Ingrese la nota 1: "))
nota2=float(input("Ingrese la nota 2: "))
nota3=float(input("Ingrese la nota 3: "))




















promedio=(nota1+nota2+nota3)/3

print("El promedio es: ", promedio)
'''

#Usando el ciclo for
'''
acumulativonota = 0
contadordenotas= 0
cantidaddenotasanalizar=int(input("Ingrese la cantidad de notas que desea promediar: "))
for i in range(cantidaddenotasanalizar):
  print("Nota número: ", i+1)
  nota = float(input("Ingrese la nota #:"))
  acumulativonota=nota+acumulativonota
  contadordenotas=i+1
print("El Promedio de las notas es:", acumulativonota/contadordenotas)'''


'''
Multiplicación de los primeros N números: 
Escribe un programa que solicite al usuario un número entero positivo.
Utiliza un ciclo for para calcular el producto de los primeros 𝑁 números enteros (desde 1 hasta N).

Ejemplo:

Entrada: 4
Salida: 24 (porque 
1
×
2
×
3
×
4
=
24
1×2×3×4=24)
'''

# Solicitar al usuario un número entero positivo
#N = int(input("Introduce un número entero positivo: "))

# Inicializar el producto en 1 (ya que es el elemento neutro de la multiplicación)
#producto = 1

# Usar un ciclo for para multiplicar los números del 1 al N
#for i in range(1, N + 1):
 #   producto *= i

# Mostrar el resultado
#print("El producto de los primeros", N, "números es:", producto)




# Escribe un programa que solicite al usuario un número entero positivo 
# Utiliza un ciclo for para imprimir los números del 1 al 𝑁

# Solicitar al usuario un número entero positivo
N = int(input("Introduce un número entero positivo: "))

# Usar un ciclo for para imprimir los números del 1 al N
for i in range(1, N + 1):
    print(i)





