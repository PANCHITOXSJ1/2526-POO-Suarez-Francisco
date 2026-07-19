# Clase que demuestra el uso de constructores y destructores en Python
class ArchivoTexto:
    """
    Esta clase representa un archivo de texto.
    Utiliza un constructor para abrir el archivo
    y un destructor para cerrarlo.
    """

    def __init__(self, nombre_archivo):
        """
        Constructor de la clase.
        Se ejecuta automáticamente cuando se crea un objeto.

        Inicializa el atributo nombre_archivo
        y abre el archivo en modo escritura.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, "w")
        print(f"📂 Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir(self, texto):
        """
        Método para escribir contenido en el archivo.
        """
        self.archivo.write(texto + "\n")
        print("✍️ Texto escrito en el archivo.")

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta automáticamente cuando el objeto
        está a punto de ser eliminado de la memoria.

        Se encarga de cerrar el archivo para liberar recursos.
        """
        self.archivo.close()
        print(f"🔒 Archivo '{self.nombre_archivo}' cerrado y recursos liberados.")


# Programa principal
if __name__ == "__main__":
    # Creación del objeto (se ejecuta el constructor)
    archivo = ArchivoTexto("ejemplo.txt")

    # Uso del objeto
    archivo.escribir("Este es un ejemplo del uso de constructores.")
    archivo.escribir("Y destructores en Python.")

    # Eliminación del objeto (se ejecuta el destructor)
    del archivo
