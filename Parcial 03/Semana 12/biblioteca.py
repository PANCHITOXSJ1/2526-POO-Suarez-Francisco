# ============================================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
# Archivo: biblioteca.py
# Lenguaje: Python
# ============================================================

# ============================================================
# CLASE LIBRO
# Representa un libro dentro de la biblioteca
# ============================================================

class Libro:

    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para datos que no cambiarán
        self.info = (titulo, autor)

        self.categoria = categoria
        self.isbn = isbn

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def __str__(self):
        return f"Título: {self.info[0]} | Autor: {self.info[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"


# ============================================================
# CLASE USUARIO
# Representa un usuario de la biblioteca
# ============================================================

class Usuario:

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

        # Lista para guardar los libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        if len(self.libros_prestados) == 0:
            print("No tiene libros prestados.")
        else:
            print("Libros prestados:")
            for libro in self.libros_prestados:
                print(libro)

    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario}"


# ============================================================
# CLASE BIBLIOTECA
# Gestiona libros, usuarios y préstamos
# ============================================================

class Biblioteca:

    def __init__(self):

        # Diccionario de libros disponibles
        # clave = ISBN
        # valor = objeto Libro
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Conjunto para IDs únicos
        self.ids_usuarios = set()

    # --------------------------------------------------------
    # Añadir libro
    # --------------------------------------------------------
    def añadir_libro(self, libro):

        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro añadido correctamente.")
        else:
            print("El libro ya existe en la biblioteca.")

    # --------------------------------------------------------
    # Quitar libro
    # --------------------------------------------------------
    def quitar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # --------------------------------------------------------
    # Registrar usuario
    # --------------------------------------------------------
    def registrar_usuario(self, usuario):

        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente.")
        else:
            print("El ID de usuario ya existe.")

    # --------------------------------------------------------
    # Dar de baja usuario
    # --------------------------------------------------------
    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # --------------------------------------------------------
    # Prestar libro
    # --------------------------------------------------------
    def prestar_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return

        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]

        usuario.prestar_libro(libro)

        del self.libros[isbn]

        print("Libro prestado correctamente.")

    # --------------------------------------------------------
    # Devolver libro
    # --------------------------------------------------------
    def devolver_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.devolver_libro(libro)
                self.libros[isbn] = libro
                print("Libro devuelto correctamente.")
                return

        print("El usuario no tiene ese libro.")

    # --------------------------------------------------------
    # Buscar libro por título
    # --------------------------------------------------------
    def buscar_por_titulo(self, titulo):

        encontrado = False

        for libro in self.libros.values():
            if libro.obtener_titulo().lower() == titulo.lower():
                print(libro)
                encontrado = True

        if not encontrado:
            print("No se encontró el libro.")

    # --------------------------------------------------------
    # Buscar libro por autor
    # --------------------------------------------------------
    def buscar_por_autor(self, autor):

        encontrado = False

        for libro in self.libros.values():
            if libro.obtener_autor().lower() == autor.lower():
                print(libro)
                encontrado = True

        if not encontrado:
            print("No se encontraron libros de ese autor.")

    # --------------------------------------------------------
    # Buscar por categoría
    # --------------------------------------------------------
    def buscar_por_categoria(self, categoria):

        encontrado = False

        for libro in self.libros.values():
            if libro.categoria.lower() == categoria.lower():
                print(libro)
                encontrado = True

        if not encontrado:
            print("No se encontraron libros en esa categoría.")


# ============================================================
# PROGRAMA PRINCIPAL (PRUEBA DEL SISTEMA)
# ============================================================

if __name__ == "__main__":

    biblioteca = Biblioteca()

    # Crear algunos libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "111")
    libro2 = Libro("Don Quijote", "Miguel de Cervantes", "Clásico", "222")
    libro3 = Libro("Python para principiantes", "Juan Pérez", "Tecnología", "333")

    # Añadir libros
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Crear usuarios
    usuario1 = Usuario("Ana", 1)
    usuario2 = Usuario("Luis", 2)

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libro
    biblioteca.prestar_libro(1, "111")

    # Mostrar libros prestados
    print("\nLibros prestados a Ana:")
    usuario1.listar_libros()

    # Devolver libro
    biblioteca.devolver_libro(1, "111")

    # Buscar libros
    print("\nBuscar por autor:")
    biblioteca.buscar_por_autor("Miguel de Cervantes")

    print("\nBuscar por categoría:")
    biblioteca.buscar_por_categoria("Tecnología")