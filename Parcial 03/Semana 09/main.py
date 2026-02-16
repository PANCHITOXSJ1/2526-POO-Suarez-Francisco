# main.py
# Menú interactivo en consola para gestionar el inventario.

from producto import Producto
from inventario import Inventario


def leer_entero(mensaje: str, minimo: int | None = None) -> int:
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"⚠️ Debe ser un número >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("⚠️ Ingrese un número entero válido.")


def leer_flotante(mensaje: str, minimo: float | None = None) -> float:
    while True:
        try:
            valor = float(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"⚠️ Debe ser un número >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("⚠️ Ingrese un número válido (ej: 2.50).")


def menu():
    print("\n" + "=" * 45)
    print("     🧾 SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("=" * 45)
    print("1) ➕ Añadir producto")
    print("2) 🗑️ Eliminar producto por ID")
    print("3) ✏️ Actualizar cantidad o precio por ID")
    print("4) 🔎 Buscar producto por nombre")
    print("5) 📋 Mostrar todos los productos")
    print("0) 🚪 Salir")


def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()

        # 1) Añadir producto
        if opcion == "1":
            print("\n➕ AÑADIR PRODUCTO")
            id_producto = input("ID (único): ").strip()
            nombre = input("Nombre: ").strip()
            cantidad = leer_entero("Cantidad (>=0): ", minimo=0)
            precio = leer_flotante("Precio (>=0): ", minimo=0)

            producto = Producto(id_producto, nombre, cantidad, precio)
            if inventario.anadir_producto(producto):
                print("✅ Producto añadido correctamente.")
            else:
                print("❌ No se pudo añadir: el ID ya existe.")

        # 2) Eliminar por ID
        elif opcion == "2":
            print("\n🗑️ ELIMINAR PRODUCTO")
            id_producto = input("Ingrese el ID a eliminar: ").strip()
            if inventario.eliminar_producto(id_producto):
                print("✅ Producto eliminado.")
            else:
                print("❌ No se encontró el producto con ese ID.")

        # 3) Actualizar cantidad o precio por ID
        elif opcion == "3":
            print("\n✏️ ACTUALIZAR PRODUCTO")
            id_producto = input("Ingrese el ID a actualizar: ").strip()

            print("¿Qué desea actualizar?")
            print("1) Cantidad")
            print("2) Precio")
            print("3) Cantidad y precio")
            eleccion = input("Opción: ").strip()

            if eleccion == "1":
                nueva_cantidad = leer_entero("Nueva cantidad (>=0): ", minimo=0)
                ok = inventario.actualizar_producto(id_producto, nueva_cantidad=nueva_cantidad)

            elif eleccion == "2":
                nuevo_precio = leer_flotante("Nuevo precio (>=0): ", minimo=0)
                ok = inventario.actualizar_producto(id_producto, nuevo_precio=nuevo_precio)

            elif eleccion == "3":
                nueva_cantidad = leer_entero("Nueva cantidad (>=0): ", minimo=0)
                nuevo_precio = leer_flotante("Nuevo precio (>=0): ", minimo=0)
                ok = inventario.actualizar_producto(id_producto, nueva_cantidad=nueva_cantidad, nuevo_precio=nuevo_precio)

            else:
                ok = False

            print("✅ Actualizado correctamente." if ok else "❌ No se pudo actualizar (ID no encontrado u opción inválida).")

        # 4) Buscar por nombre
        elif opcion == "4":
            print("\n🔎 BUSCAR PRODUCTO")
            texto = input("Ingrese nombre o parte del nombre: ").strip()
            resultados = inventario.buscar_por_nombre(texto)

            if resultados:
                print(f"\n✅ Se encontraron {len(resultados)} producto(s):")
                for p in resultados:
                    print(" -", p)
            else:
                print("❌ No se encontraron productos con ese criterio.")

        # 5) Mostrar todos
        elif opcion == "5":
            print("\n📋 INVENTARIO")
            productos = inventario.mostrar_todos()

            if productos:
                for p in productos:
                    print(" -", p)
            else:
                print("ℹ️ El inventario está vacío.")

        # 0) Salir
        elif opcion == "0":
            print("\n👋 ¡Hasta luego!")
            break

        else:
            print("⚠️ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
