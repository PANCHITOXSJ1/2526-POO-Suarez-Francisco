# inventario_app.py
# Sistema de Gestión de Inventarios Mejorado (POO + Archivos + Excepciones)
# Guarda/recupera productos desde inventario.txt y maneja errores comunes de archivo.

import os
from dataclasses import dataclass
from typing import List, Optional, Tuple


ARCHIVO_INVENTARIO = "inventario.txt"
SEPARADOR = "|"  # formato de línea: id|nombre|cantidad|precio


@dataclass
class Producto:
    """Representa un producto del inventario."""
    id: str
    nombre: str
    cantidad: int
    precio: float

    def to_line(self) -> str:
        """Convierte el producto a una línea de texto para el archivo."""
        # Reemplazamos el separador dentro del nombre para evitar corrupción del formato.
        nombre_seguro = self.nombre.replace(SEPARADOR, "/")
        return f"{self.id}{SEPARADOR}{nombre_seguro}{SEPARADOR}{self.cantidad}{SEPARADOR}{self.precio:.2f}"

    @staticmethod
    def from_line(linea: str) -> "Producto":
        """Crea un Producto a partir de una línea del archivo.
        Lanza ValueError si el formato no es válido.
        """
        partes = [p.strip() for p in linea.strip().split(SEPARADOR)]
        if len(partes) != 4:
            raise ValueError("Formato incorrecto (se esperaban 4 campos).")

        pid, nombre, cant_str, precio_str = partes

        if pid == "" or nombre == "":
            raise ValueError("ID o nombre vacío.")

        cantidad = int(cant_str)          # puede lanzar ValueError
        precio = float(precio_str)        # puede lanzar ValueError

        if cantidad < 0 or precio < 0:
            raise ValueError("Cantidad o precio no pueden ser negativos.")

        return Producto(pid, nombre, cantidad, precio)


class Inventario:
    """Gestiona productos en memoria y en archivo."""
    def __init__(self, ruta_archivo: str = ARCHIVO_INVENTARIO):
        self.ruta_archivo = ruta_archivo
        self.productos: List[Producto] = []
        self._cargar_desde_archivo()

    # ----------------------------
    # Carga y guardado en archivo
    # ----------------------------
    def _asegurar_archivo(self) -> None:
        """Asegura que el archivo exista. Si no existe, lo crea vacío."""
        if not os.path.exists(self.ruta_archivo):
            try:
                # Modo 'w' crea el archivo si no existe (según PDF: escritura) y lo deja vacío.
                with open(self.ruta_archivo, "w", encoding="utf-8") as _:
                    pass
            except PermissionError as e:
                raise PermissionError(
                    f"No tengo permisos para crear el archivo: {self.ruta_archivo}"
                ) from e

    def _cargar_desde_archivo(self) -> None:
        """Carga productos desde el archivo al iniciar el programa.
        Maneja archivo inexistente, permisos y líneas corruptas.
        """
        try:
            self._asegurar_archivo()

            productos_cargados: List[Producto] = []
            lineas_corruptas = 0

            # Modo 'r' lectura; se recomienda with para cierre automático.
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                for nro, linea in enumerate(f, start=1):
                    if not linea.strip():
                        continue
                    try:
                        prod = Producto.from_line(linea)
                        productos_cargados.append(prod)
                    except Exception:
                        # Si una línea está corrupta, no caemos: la saltamos y seguimos.
                        lineas_corruptas += 1

            # Si hay IDs repetidos en el archivo, nos quedamos con el último (simple y práctico).
            self.productos = self._normalizar_por_id(productos_cargados)

            if lineas_corruptas > 0:
                print(f"⚠️ Aviso: Se ignoraron {lineas_corruptas} línea(s) corrupta(s) del archivo.")
            print(f"✅ Inventario cargado: {len(self.productos)} producto(s).")

        except FileNotFoundError:
            # Por seguridad, si algo pasó, intentamos crear nuevamente.
            try:
                self._asegurar_archivo()
                self.productos = []
                print("✅ Archivo de inventario creado (no existía). Inventario vacío.")
            except Exception as e:
                print(f"❌ No se pudo crear el archivo: {e}")
                self.productos = []

        except PermissionError as e:
            print(f"❌ Error de permisos al leer/crear el archivo: {e}")
            self.productos = []

        except Exception as e:
            print(f"❌ Error inesperado cargando inventario: {e}")
            self.productos = []

    def _normalizar_por_id(self, lista: List[Producto]) -> List[Producto]:
        """Elimina duplicados por ID conservando el último."""
        dic = {}
        for p in lista:
            dic[p.id] = p
        return list(dic.values())

    def _guardar_todo(self) -> Tuple[bool, str]:
        """Sobrescribe el archivo con el inventario actual (lectura->memoria->reescritura).
        Esto es lo recomendado para 'modificar' un archivo de texto (no se edita una línea in situ).
        Retorna (ok, mensaje).
        """
        try:
            self._asegurar_archivo()

            # Escritura atómica: escribir a un temporal y reemplazar.
            temp = self.ruta_archivo + ".tmp"

            with open(temp, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(p.to_line() + "\n")

            os.replace(temp, self.ruta_archivo)
            return True, "✅ Archivo actualizado correctamente."

        except PermissionError:
            return False, "❌ No hay permisos para escribir en el archivo (PermissionError)."

        except Exception as e:
            return False, f"❌ Error al guardar archivo: {e}"

    # ----------------------------
    # Operaciones del inventario
    # ----------------------------
    def _buscar_por_id(self, pid: str) -> Optional[Producto]:
        for p in self.productos:
            if p.id == pid:
                return p
        return None

    def agregar_producto(self, producto: Producto) -> Tuple[bool, str]:
        """Añade un producto (ID único). Guarda en archivo."""
        if self._buscar_por_id(producto.id) is not None:
            return False, "❌ Ya existe un producto con ese ID."

        self.productos.append(producto)
        ok, msg_archivo = self._guardar_todo()
        if ok:
            return True, "✅ Producto añadido y guardado en el archivo."
        else:
            # Si falló guardar, revertimos para no mentir al usuario
            self.productos = [p for p in self.productos if p.id != producto.id]
            return False, f"❌ Se añadió en memoria, pero falló el guardado. {msg_archivo}"

    def eliminar_producto(self, pid: str) -> Tuple[bool, str]:
        """Elimina un producto por ID. Guarda en archivo."""
        p = self._buscar_por_id(pid)
        if p is None:
            return False, "❌ No existe un producto con ese ID."

        self.productos = [x for x in self.productos if x.id != pid]
        ok, msg_archivo = self._guardar_todo()
        if ok:
            return True, "✅ Producto eliminado y archivo actualizado."
        else:
            # revertir
            self.productos.append(p)
            return False, f"❌ Se eliminó en memoria, pero falló el guardado. {msg_archivo}"

    def actualizar_producto(self, pid: str, nueva_cantidad: Optional[int] = None,
                            nuevo_precio: Optional[float] = None) -> Tuple[bool, str]:
        """Actualiza cantidad y/o precio. Guarda en archivo."""
        p = self._buscar_por_id(pid)
        if p is None:
            return False, "❌ No existe un producto con ese ID."

        # Guardamos valores anteriores por si hay que revertir
        cant_ant, prec_ant = p.cantidad, p.precio

        if nueva_cantidad is not None:
            if nueva_cantidad < 0:
                return False, "❌ La cantidad no puede ser negativa."
            p.cantidad = nueva_cantidad

        if nuevo_precio is not None:
            if nuevo_precio < 0:
                return False, "❌ El precio no puede ser negativo."
            p.precio = nuevo_precio

        ok, msg_archivo = self._guardar_todo()
        if ok:
            return True, "✅ Producto actualizado y guardado en el archivo."
        else:
            # revertir
            p.cantidad, p.precio = cant_ant, prec_ant
            return False, f"❌ Se actualizó en memoria, pero falló el guardado. {msg_archivo}"

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        """Busca productos por nombre (coincidencia parcial, sin distinguir mayúsculas)."""
        texto = texto.strip().lower()
        return [p for p in self.productos if texto in p.nombre.lower()]

    def mostrar_todos(self) -> None:
        """Muestra el inventario completo."""
        if not self.productos:
            print("📦 Inventario vacío.")
            return

        print("\n📋 LISTA DE PRODUCTOS")
        print("-" * 60)
        print(f"{'ID':<10} {'NOMBRE':<25} {'CANT':>6} {'PRECIO':>10}")
        print("-" * 60)
        for p in sorted(self.productos, key=lambda x: x.id):
            print(f"{p.id:<10} {p.nombre:<25} {p.cantidad:>6} {p.precio:>10.2f}")
        print("-" * 60)


# ----------------------------
# Interfaz de consola (Menú)
# ----------------------------
def pedir_int(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("❌ Ingresa un número entero válido.")


def pedir_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje).strip())
        except ValueError:
            print("❌ Ingresa un número válido (ej: 10.50).")


def menu():
    inv = Inventario(ARCHIVO_INVENTARIO)

    while True:
        print("\n" + "=" * 45)
        print("   SISTEMA DE INVENTARIOS (ARCHIVOS + POO)")
        print("=" * 45)
        print("1) Añadir producto")
        print("2) Eliminar producto por ID")
        print("3) Actualizar cantidad o precio por ID")
        print("4) Buscar producto por nombre")
        print("5) Mostrar todos los productos")
        print("0) Salir")

        op = input("Elige una opción: ").strip()

        if op == "1":
            pid = input("ID: ").strip()
            nombre = input("Nombre: ").strip()
            cantidad = pedir_int("Cantidad: ")
            precio = pedir_float("Precio: ")

            producto = Producto(pid, nombre, cantidad, precio)
            ok, msg = inv.agregar_producto(producto)
            print(msg)

        elif op == "2":
            pid = input("ID a eliminar: ").strip()
            ok, msg = inv.eliminar_producto(pid)
            print(msg)

        elif op == "3":
            pid = input("ID a actualizar: ").strip()
            print("¿Qué deseas actualizar?")
            print("1) Cantidad")
            print("2) Precio")
            print("3) Ambos")
            sub = input("Opción: ").strip()

            if sub == "1":
                cant = pedir_int("Nueva cantidad: ")
                ok, msg = inv.actualizar_producto(pid, nueva_cantidad=cant)
                print(msg)
            elif sub == "2":
                prec = pedir_float("Nuevo precio: ")
                ok, msg = inv.actualizar_producto(pid, nuevo_precio=prec)
                print(msg)
            elif sub == "3":
                cant = pedir_int("Nueva cantidad: ")
                prec = pedir_float("Nuevo precio: ")
                ok, msg = inv.actualizar_producto(pid, nueva_cantidad=cant, nuevo_precio=prec)
                print(msg)
            else:
                print("❌ Opción inválida.")

        elif op == "4":
            texto = input("Texto a buscar (nombre): ").strip()
            encontrados = inv.buscar_por_nombre(texto)
            if not encontrados:
                print("🔎 No se encontraron productos.")
            else:
                print(f"🔎 Encontrados {len(encontrados)} producto(s):")
                for p in encontrados:
                    print(f" - {p.id} | {p.nombre} | Cant: {p.cantidad} | $ {p.precio:.2f}")

        elif op == "5":
            inv.mostrar_todos()

        elif op == "0":
            print("👋 Saliendo... Inventario guardado.")
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()