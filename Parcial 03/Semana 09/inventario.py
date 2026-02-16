# inventario.py
# Clase Inventario:
# - Atributo: lista de productos
# - Métodos: añadir (ID único), eliminar por ID, actualizar por ID, buscar por nombre, mostrar todos

from producto import Producto


class Inventario:
    def __init__(self):
        self.__productos: list[Producto] = []

    def anadir_producto(self, producto: Producto) -> bool:
        # Asegura ID único
        if self.buscar_por_id(producto.get_id()) is not None:
            return False
        self.__productos.append(producto)
        return True

    def eliminar_producto(self, id_producto: str) -> bool:
        for i, p in enumerate(self.__productos):
            if p.get_id() == id_producto:
                del self.__productos[i]
                return True
        return False

    def actualizar_producto(self, id_producto: str, nueva_cantidad: int | None = None, nuevo_precio: float | None = None) -> bool:
        producto = self.buscar_por_id(id_producto)
        if producto is None:
            return False

        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad)

        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)

        return True

    def buscar_por_nombre(self, texto: str) -> list[Producto]:
        # Permite coincidencias parciales y nombres similares
        texto = texto.strip().lower()
        resultados = []
        for p in self.__productos:
            if texto in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_todos(self) -> list[Producto]:
        return self.__productos.copy()

    def buscar_por_id(self, id_producto: str) -> Producto | None:
        for p in self.__productos:
            if p.get_id() == id_producto:
                return p
        return None
