import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Entry, Button, messagebox

# Función para actualizar el gráfico con nuevos datos
def actualizar_grafico():
    # Obtener los datos ingresados
    try:
        nuevos_x = list(map(int, entry_x.get().split(',')))
        nuevos_y = list(map(int, entry_y.get().split(',')))

        # Verificar si las longitudes son iguales
        if len(nuevos_x) != len(nuevos_y):
            messagebox.showerror("Error", "Las longitudes de X y Y deben ser iguales.")
            return  # Salir de la función si hay un error

        # Limpiar el gráfico anterior
        ax.clear()

        # Crear el nuevo gráfico con los datos actualizados
        ax.plot(nuevos_x, nuevos_y)

        # Redibujar el gráfico en el canvas
        canvas.draw()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese solo números enteros separados por comas.")

# Crear la ventana principal de tkinter
root = tk.Tk()
root.title("Editar Datos del Gráfico")

# Crear la figura de Matplotlib
fig, ax = plt.subplots()

# Datos iniciales
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
ax.plot(x, y)

# Crear un canvas de Matplotlib dentro de la ventana tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Crear campos de entrada para los nuevos datos
label_x = tk.Label(root, text="Nuevos valores de X (separados por comas):")
label_x.pack()

entry_x = Entry(root)
entry_x.pack()
entry_x.insert(0, ','.join(map(str, x)))  # Insertar los valores iniciales de X

label_y = tk.Label(root, text="Nuevos valores de Y (separados por comas):")
label_y.pack()

entry_y = Entry(root)
entry_y.pack()
entry_y.insert(0, ','.join(map(str, y)))  # Insertar los valores iniciales de Y

# Botón para actualizar el gráfico
boton_actualizar = Button(root, text="Actualizar Gráfico", command=actualizar_grafico)
boton_actualizar.pack()

# Iniciar el bucle de la ventana tkinter
root.mainloop()
