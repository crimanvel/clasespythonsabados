#Ejercicio 4 Utilizando IA (GEMINI)
# En gemini/chatgpt/copilot escribir: necesito una calculadora en python puedes darme el código?  pero lo mas sencillo posible sin utilizar librerias
""" Para hacer comentarios en bloque (muchas lineas)
    Tengo que abrir y cerrar tres veces las comillas dobles
"""
"""

def sumar(x, y):
  """#Esta función suma dos números"""
 # return x + y

#def restar(x, y):
  """ #Esta función resta dos números"""
  #return x - y

#def multiplicar(x, y):
  """Esta función multiplica dos números"""
 # return x * y

#def dividir(x, y):
  """Esta función divide dos números"""
  #if y == 0:
   # return "No se puede dividir entre cero"
  #else:
   # return x / y
#while True:
  #print("Selecciona la operación:")
  #print("1. Sumar")
  #print("2. Restar")
  #print("3. Multiplicar")
  #print("4. Dividir")
  #print("5. Salir")

  #opcion = input("Ingresa una opción (1/2/3/4/5): ")

  #if opcion in ('1', '2', '3', '4'):
    #try:
     # num1 = float(input("Ingresa el primer número: "))
      #num2 = float(input("Ingresa el segundo número: "))
    #except ValueError:
      #print("Entrada inválida. Por favor, ingresa un número.")
      #continue

    #if opcion == '1':
     # print(num1, "+", num2, "=", sumar(num1, num2))

   # elif opcion == '2':
    #  print(num1, "-", num2, "=", restar(num1, num2))

    #elif opcion == '3':
     # print(num1, "*", num2, "=", multiplicar(num1, num2))

   # elif opcion == '4':
    #  print(num1, "/", num2, "=", dividir(num1, num2))

  #elif opcion == '5':
  #  break
  #else:
   # print("Opción inválida. Por favor, ingresa una opción válida.")
   import tkinter as tk
from tkinter import ttk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculadora")

# Estilo visual
style = ttk.Style()
style.theme_use('clam')  # Puedes experimentar con otros temas como 'alt', 'default', etc.
style.configure("TButton", padding=10, font=('Arial', 14))
style.configure("TEntry", padding=10, font=('Arial', 24))

# Entrada
entry = ttk.Entry(root, width=20, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones
button_list = [
    'C', '', '', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '='
]

row_val = 1
col_val = 0
for button_text in button_list:
    if button_text == '=':
        ttk.Button(root, text=button_text, command=button_equal, width=20).grid(row=row_val, column=col_val, columnspan=2, padx=5, pady=5)
        col_val += 2
    elif button_text == 'C':
        ttk.Button(root, text=button_text, command=button_clear).grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
    elif button_text == '':
        col_val += 1
    else:
        ttk.Button(root, text=button_text, command=lambda text=button_text: button_click(text)).grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()