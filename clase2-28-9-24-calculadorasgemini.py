#Para convertirlo en un archivo ejecutable:
#  pip install pyinstaller
 # Luego, navega a la carpeta donde guardaste el archivo Python en tu terminal y ejecuta el siguiente comando:Bash
#pyinstaller --onefile --windowed tu_archivo.py
#  pip install tkinter
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