import json
import os


# ==============================
# CLASE PRODUCTO
# ==============================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Convertir objeto a diccionario (para JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


# ==============================
# CLASE INVENTARIO
# ==============================
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario {id: Producto}
        self.archivo = "inventario.json"
        self.cargar_archivo()

    # Agregar producto
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("⚠️ Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto agregado correctamente.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑 Producto eliminado correctamente.")
        else:
            print("❌ Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("🔄 Producto actualizado correctamente.")
        else:
            print("❌ Producto no encontrado.")

    # Buscar producto por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = [
            producto for producto in self.productos.values()
            if nombre.lower() in producto.get_nombre().lower()
        ]

        if encontrados:
            print("\n🔎 Resultados encontrados:")
            for p in encontrados:
                print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | "
                      f"Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")
        else:
            print("❌ No se encontraron productos con ese nombre.")

    # Mostrar todos los productos
    def mostrar_todos(self):
        if not self.productos:
            print("📭 El inventario está vacío.")
        else:
            print("\n📦 LISTA DE PRODUCTOS:")
            for p in self.productos.values():
                print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | "
                      f"Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")

    # Guardar en archivo JSON
    def guardar_archivo(self):
        datos = {id_p: producto.to_dict() for id_p, producto in self.productos.items()}
        with open(self.archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)
        print("💾 Inventario guardado correctamente.")

    # Cargar desde archivo JSON
    def cargar_archivo(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as archivo:
                    datos = json.load(archivo)
                    for id_p, info in datos.items():
                        producto = Producto(
                            info["id"],
                            info["nombre"],
                            info["cantidad"],
                            info["precio"]
                        )
                        self.productos[id_p] = producto
            except:
                print("⚠️ Error al cargar el archivo.")


# ==============================
# MENÚ INTERACTIVO
# ==============================
def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA AVANZADO DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                producto = Producto(id_p, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("❌ Cantidad o precio inválidos.")

        elif opcion == "2":
            id_p = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("Ingrese ID del producto a actualizar: ")

            cantidad_input = input("Nueva cantidad (Enter para omitir): ")
            precio_input = input("Nuevo precio (Enter para omitir): ")

            cantidad = int(cantidad_input) if cantidad_input else None
            precio = float(precio_input) if precio_input else None

            inventario.actualizar_producto(id_p, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_archivo()

        elif opcion == "7":
            inventario.guardar_archivo()
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")


# Ejecutar programa
if __name__ == "__main__":
    menu()