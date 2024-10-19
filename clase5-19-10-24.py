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

acumulativonota = 0
contadordenotas= 0
cantidaddenotasanalizar=int(input("Ingrese la cantidad de notas que desea promediar: "))
for i in range(cantidaddenotasanalizar):
  print("Nota número: ", i+1)
  nota = float(input("Ingrese la nota #:"))
  acumulativonota=nota+acumulativonota
  contadordenotas=i+1
print("El Promedio de las notas es:", acumulativonota/contadordenotas)