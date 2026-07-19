# producto.py
# Clase Producto con atributos: ID (único), nombre, cantidad y precio.
# Incluye constructor, getters y setters para cada atributo.

class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self) -> str:
        return self.__id

    def get_nombre(self) -> str:
        return self.__nombre

    def get_cantidad(self) -> int:
        return self.__cantidad

    def get_precio(self) -> float:
        return self.__precio

    # Setters
    def set_id(self, nuevo_id: str) -> None:
        self.__id = nuevo_id

    def set_nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad: int) -> None:
        self.__cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio: float) -> None:
        self.__precio = nuevo_precio

    def __str__(self) -> str:
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"
