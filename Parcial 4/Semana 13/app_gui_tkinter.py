# Importamos la librería Tkinter
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI - Lista de Datos")
ventana.geometry("400x350")

# -----------------------------
# Función para agregar datos
# -----------------------------
def agregar_dato():
    texto = entrada_texto.get()  # Obtener texto del campo
    if texto != "":  # Verificar que no esté vacío
        lista_datos.insert(tk.END, texto)  # Agregar a la lista
        entrada_texto.delete(0, tk.END)  # Limpiar el campo de texto

# -----------------------------
# Función para limpiar lista
# -----------------------------
def limpiar_lista():
    lista_datos.delete(0, tk.END)  # Elimina todos los elementos

# -----------------------------
# Etiqueta de título
# -----------------------------
titulo = tk.Label(ventana, text="Gestión de Datos", font=("Arial", 16))
titulo.pack(pady=10)

# -----------------------------
# Etiqueta de instrucción
# -----------------------------
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack()

# -----------------------------
# Campo de texto
# -----------------------------
entrada_texto = tk.Entry(ventana, width=30)
entrada_texto.pack(pady=5)

# -----------------------------
# Botón agregar
# -----------------------------
boton_agregar = tk.Button(
    ventana,
    text="Agregar",
    command=agregar_dato
)
boton_agregar.pack(pady=5)

# -----------------------------
# Lista para mostrar datos
# -----------------------------
lista_datos = tk.Listbox(ventana, width=40, height=10)
lista_datos.pack(pady=10)

# -----------------------------
# Botón limpiar
# -----------------------------
boton_limpiar = tk.Button(
    ventana,
    text="Limpiar Lista",
    command=limpiar_lista
)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()