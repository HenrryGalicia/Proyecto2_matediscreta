import tkinter as tk
from tkinter import ttk

def calcular_mcd():
    numero1 = int(entry_numero1.get())
    numero2 = int(entry_numero2.get())
    mcd = euclides_mcd(numero1, numero2)
    label_resultado_mcd.config(text=f"El MCD de {numero1} y {numero2} es: {mcd}")

def euclides_mcd(x, b):
    if b == 0:
        return x
    else:
        return euclides_mcd(b, x % b)

def calcular_combinaciones_placas():
    num_combinaciones_digitos = 10 ** 3
    num_combinaciones_letras = 27 ** 3
    total_combinaciones = num_combinaciones_digitos * num_combinaciones_letras
    label_resultado_combinaciones.config(text=f"Número total de placas posibles en Guatemala: {total_combinaciones}")

def calcular_diferencia_conjuntos():
    conjunto_a = {"a", 2, "c", 3, "e", 4, "g", 5, "i", 6, "k", 7, "m"}
    conjunto_b = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}
    diferencia_a_b = conjunto_a - conjunto_b
    resultado_conjuntos.config(text=f"Conjunto A: {conjunto_a}\nConjunto B: {conjunto_b}\nResultado de la diferencia A-B: {diferencia_a_b}")

ventana = tk.Tk()
ventana.title("Calculadora y Placas de Guatemala")

pestanas = ttk.Notebook(ventana)

pestaña1 = ttk.Frame(pestanas)
pestanas.add(pestaña1, text="Calcular MCD")

label_instrucciones1 = tk.Label(pestaña1, text="Ingresa dos números para calcular el MCD:")
label_instrucciones1.config(fg="Blue")  
label_instrucciones1.config(font=("new roman", 12))  
label_numero1 = tk.Label(pestaña1, text="Número 1:")
label_numero1.config(fg="purple")
label_numero2 = tk.Label(pestaña1, text="Número 2:")
label_numero2.config(fg="red")  
entry_numero1 = tk.Entry(pestaña1)
entry_numero2 = tk.Entry(pestaña1)
boton_calcular_mcd = tk.Button(pestaña1, text="Calcular MCD", command=calcular_mcd)
boton_calcular_mcd.config(fg="Orange")  
label_resultado_mcd = tk.Label(pestaña1, text="", fg="Green")

label_instrucciones1.pack()
label_numero1.pack()
entry_numero1.pack()
label_numero2.pack()
entry_numero2.pack()
boton_calcular_mcd.pack()
label_resultado_mcd.pack()

pestaña2 = ttk.Frame(pestanas)
pestanas.add(pestaña2, text="Placas de Guatemala")

label_instrucciones2 = tk.Label(pestaña2, text="Calcular el número de placas posibles en Guatemala:")
label_instrucciones2.config(fg="Blue") 
label_instrucciones2.config(font=("Helvetica", 12)) 
boton_calcular_combinaciones = tk.Button(pestaña2, text="Calcular Combinaciones", command=calcular_combinaciones_placas)
boton_calcular_combinaciones.config(fg="purple")  
label_resultado_combinaciones = tk.Label(pestaña2, text="", fg="Green") 

label_instrucciones2.pack()
boton_calcular_combinaciones.pack()
label_resultado_combinaciones.pack()

pestaña3 = ttk.Frame(pestanas)
pestanas.add(pestaña3, text="Diferencia de Conjuntos")

label_instrucciones3 = tk.Label(pestaña3, text="Calcular la diferencia A-B de conjuntos:")
label_instrucciones3.config(fg="Blue") 
label_instrucciones3.config(font=("Helvetica", 12)) 
boton_calcular_diferencia = tk.Button(pestaña3, text="Calcular Diferencia", command=calcular_diferencia_conjuntos)
boton_calcular_diferencia.config(fg="purple") 
resultado_conjuntos = tk.Label(pestaña3, text="", fg="Green") 

label_instrucciones3.pack()
boton_calcular_diferencia.pack()
resultado_conjuntos.pack()

pestanas.pack(fill="both", expand="yes")

ventana.mainloop()
