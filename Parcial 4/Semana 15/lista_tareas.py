import tkinter as tk
from tkinter import messagebox

# Lista donde se guardan las tareas (texto + estado)
tareas = []


# Función para añadir una tarea
def añadir_tarea(event=None):  # event=None permite usar Enter
    tarea = entrada.get().strip()

    if tarea == "":
        messagebox.showwarning("Advertencia", "Ingrese una tarea")
        return

    # Guardamos como diccionario (texto + estado)
    tareas.append({"texto": tarea, "completada": False})

    actualizar_lista()
    entrada.delete(0, tk.END)


# Función para actualizar el Listbox
def actualizar_lista():
    lista_tareas.delete(0, tk.END)

    for tarea in tareas:
        if tarea["completada"]:
            lista_tareas.insert(tk.END, "✔ " + tarea["texto"])
        else:
            lista_tareas.insert(tk.END, tarea["texto"])


# Función para marcar como completada
def marcar_completada():
    try:
        indice = lista_tareas.curselection()[0]
        tareas[indice]["completada"] = True
        actualizar_lista()
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea")


# Función para eliminar tarea
def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        tareas.pop(indice)
        actualizar_lista()
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea")


# Evento de doble clic
def doble_click(event):
    marcar_completada()


# ---------------- INTERFAZ ---------------- #

ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# Campo de entrada
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Evento Enter
entrada.bind("<Return>", añadir_tarea)

# Botones
btn_añadir = tk.Button(ventana, text="Añadir Tarea", command=añadir_tarea)
btn_añadir.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=40, height=10)
lista_tareas.pack(pady=10)

# Evento doble clic
lista_tareas.bind("<Double-Button-1>", doble_click)

# Ejecutar app
ventana.mainloop()