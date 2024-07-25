import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def derivar_y_graficar(c, n, x_range):
    x = sp.symbols('x')

    try:
        c = sp.sympify(c)  
    except sp.SympifyError:
        print(f"Error: '{c}' no es un valor válido para la constante c.")
        return None

    try:
        n = sp.sympify(n) 
    except sp.SympifyError:
        print(f"Error: '{n}' no es un valor válido para el exponente n.")
        return None

    f = c * x**n

    f_prime = sp.diff(f, x)

    print(f'La derivada de {c}x^{n} es: {sp.simplify(f_prime)}')

    f_func = sp.lambdify(x, f, 'numpy')
    f_prime_func = sp.lambdify(x, f_prime, 'numpy')

    x_vals = np.linspace(x_range[0], x_range[1], 400)

    y_vals = f_func(x_vals)
    y_prime_vals = f_prime_func(x_vals)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x_vals, y_vals, label=f'{c}x^{n}', color='blue')

    ax.plot(x_vals, y_prime_vals, label=f'Derivada: {sp.simplify(f_prime)}', color='red', linestyle='--')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Gráfica de {c}x^{n} y su derivada')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    ax.grid(True)

    return fig

def calcular():
    global canvas
    c = entry_c.get()
    n = entry_n.get()
    x_range = (-10, 10)
    fig = derivar_y_graficar(c, n, x_range)
    
    if canvas:
        canvas.get_tk_widget().pack_forget()

    if fig is not None:
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def limpiar():
    entry_c.delete(0, tk.END)
    entry_n.delete(0, tk.END)
    if canvas:
        canvas.get_tk_widget().pack_forget()

def cerrar():
    window.destroy()

window = tk.Tk()
window.title("Calculadora de Derivadas y Gráficas")
window.geometry("800x600") 

label_c = tk.Label(window, text="Ingrese el valor de c:")
label_c.pack()
entry_c = tk.Entry(window)
entry_c.pack()

label_n = tk.Label(window, text="Ingrese el valor de n:")
label_n.pack()
entry_n = tk.Entry(window)
entry_n.pack()

btn_calcular = tk.Button(window, text="Calcular", command=calcular)
btn_calcular.pack()

btn_limpiar = tk.Button(window, text="Limpiar", command=limpiar)
btn_limpiar.pack()

btn_cerrar = tk.Button(window, text="Cerrar", command=cerrar)
btn_cerrar.pack()

canvas = None

window.mainloop()
