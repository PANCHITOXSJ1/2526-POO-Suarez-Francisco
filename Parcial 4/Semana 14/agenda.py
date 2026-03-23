# Importación de librerías
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Asegúrate de instalar: pip install tkcalendar

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# ============================
# FRAME DE ENTRADA DE DATOS
# ============================
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Fecha
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
fecha_entry = DateEntry(frame_entrada)
fecha_entry.grid(row=0, column=1, padx=5)

# Hora
tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5)
hora_entry = tk.Entry(frame_entrada)
hora_entry.grid(row=0, column=3, padx=5)

# Descripción
tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5)
descripcion_entry = tk.Entry(frame_entrada, width=40)
descripcion_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# ============================
# FRAME DE LISTA (TREEVIEW)
# ============================
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

# Crear tabla
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")

tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")

tree.pack()

# ============================
# FUNCIONES
# ============================

def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    # Validación
    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    # Insertar datos correctamente (SIN errores de tupla)
    tree.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar campos
    hora_entry.delete(0, tk.END)
    descripcion_entry.delete(0, tk.END)


def eliminar_evento():
    seleccion = tree.selection()

    if not seleccion:
        messagebox.showwarning("Advertencia", "Seleccione un evento")
        return

    confirmar = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento seleccionado?")

    if confirmar:
        tree.delete(seleccion)


def salir():
    ventana.destroy()

# ============================
# FRAME DE BOTONES
# ============================
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=5)

# Ejecutar aplicación
ventana.mainloop()