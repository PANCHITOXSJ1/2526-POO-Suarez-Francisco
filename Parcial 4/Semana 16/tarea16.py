import tkinter as tk
from tkinter import messagebox

# ==============================
# CONFIGURACIÓN DE LA VENTANA
# ==============================
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("450x450")
root.resizable(False, False)

# ==============================
# LISTA DE TAREAS
# ==============================
tareas = []  # (texto, estado)

# ==============================
# FUNCIONES
# ==============================

def actualizar_lista():
    listbox.delete(0, tk.END)
    for tarea, completada in tareas:
        if completada:
            listbox.insert(tk.END, "✔ " + tarea)
        else:
            listbox.insert(tk.END, "✘ " + tarea)


def añadir_tarea(event=None):
    texto = entrada.get().strip()
    if texto:
        tareas.append((texto, False))
        entrada.delete(0, tk.END)
        actualizar_lista()
    else:
        messagebox.showwarning("Aviso", "Debe ingresar una tarea")


def completar_tarea(event=None):
    try:
        indice = listbox.curselection()[0]
        texto, estado = tareas[indice]
        tareas[indice] = (texto, True)
        actualizar_lista()
    except:
        messagebox.showwarning("Aviso", "Seleccione una tarea")


def eliminar_tarea(event=None):
    try:
        indice = listbox.curselection()[0]
        tareas.pop(indice)
        actualizar_lista()
    except:
        messagebox.showwarning("Aviso", "Seleccione una tarea")


def cerrar_aplicacion(event=None):
    root.destroy()

# ==============================
# INTERFAZ GRÁFICA
# ==============================

# Campo de entrada
entrada = tk.Entry(root, width=35, font=("Arial", 12))
entrada.pack(pady=10)

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack()

btn_agregar = tk.Button(frame_botones, text="Añadir", width=15, command=añadir_tarea)
btn_agregar.grid(row=0, column=0, padx=5, pady=5)

btn_completar = tk.Button(frame_botones, text="Completar", width=15, command=completar_tarea)
btn_completar.grid(row=0, column=1, padx=5, pady=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar", width=15, command=eliminar_tarea)
btn_eliminar.grid(row=1, column=0, padx=5, pady=5)

btn_salir = tk.Button(frame_botones, text="Salir", width=15, command=cerrar_aplicacion)
btn_salir.grid(row=1, column=1, padx=5, pady=5)

# Lista de tareas
listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 11))
listbox.pack(pady=10)

# ==============================
# ATAJOS DE TECLADO
# ==============================
root.bind("<Return>", añadir_tarea)     # Enter
root.bind("<c>", completar_tarea)      # tecla C
root.bind("<C>", completar_tarea)      # tecla C mayúscula
root.bind("<d>", eliminar_tarea)       # tecla D
root.bind("<D>", eliminar_tarea)       # tecla D mayúscula
root.bind("<Delete>", eliminar_tarea)  # tecla Supr
root.bind("<Escape>", cerrar_aplicacion)  # Escape

# ==============================
# EJECUCIÓN
# ==============================
root.mainloop()