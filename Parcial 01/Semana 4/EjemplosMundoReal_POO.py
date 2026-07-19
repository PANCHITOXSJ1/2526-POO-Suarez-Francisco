# Clase base que representa a un cliente de la tienda
class Cliente:

    def __init__(self, nombre, saldo, descuento):
        self.nombre = nombre
        self.saldo = saldo
        self.descuento = descuento
        self.activo = True

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Saldo:", self.saldo)
        print("·Descuento:", self.descuento, "%")

    def tiene_saldo(self):
        return self.saldo > 0

    def desactivar(self):
        self.activo = False
        print(self.nombre, "ha sido desactivado del sistema")

    def calcular_pago(self, producto):
        return producto.precio - (producto.precio * self.descuento / 100)

    def comprar(self, producto):
        costo = self.calcular_pago(producto)
        self.saldo = self.saldo - costo
        print(self.nombre, "ha comprado", producto.nombre, "por", costo)
        if self.tiene_saldo():
            print("Saldo restante:", self.saldo)
        else:
            self.desactivar()


# Clase que representa un cliente premium (hereda de Cliente)
class ClientePremium(Cliente):

    def __init__(self, nombre, saldo, descuento, membresia):
        super().__init__(nombre, saldo, descuento)
        self.membresia = membresia

    def atributos(self):
        super().atributos()
        print("·Membresía:", self.membresia)

    def calcular_pago(self, producto):
        # Beneficio adicional por ser cliente premium
        return producto.precio - (producto.precio * (self.descuento + 10) / 100)


# Clase que representa un cliente normal
class ClienteRegular(Cliente):

    def __init__(self, nombre, saldo, descuento):
        super().__init__(nombre, saldo, descuento)

    def calcular_pago(self, producto):
        return producto.precio - (producto.precio * self.descuento / 100)


# Clase Producto
class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_producto(self):
        print("Producto:", self.nombre, "- Precio:", self.precio)


# Función que simula una compra
def compra(cliente_1, cliente_2, producto):
    turno = 1
    while cliente_1.activo and cliente_2.activo:
        print("\n========================= Compra", turno, "=========================")
        print(">>> Acción de", cliente_1.nombre)
        cliente_1.comprar(producto)

        print(">>> Acción de", cliente_2.nombre)
        cliente_2.comprar(producto)

        turno = turno + 1

    print("\n=========================== Fin ===========================")
    if cliente_1.activo:
        print("Cliente activo:", cliente_1.nombre)
    elif cliente_2.activo:
        print("Cliente activo:", cliente_2.nombre)
    else:
        print("Ambos clientes se quedaron sin saldo")


# -------- PROGRAMA PRINCIPAL --------
producto_1 = Producto("Laptop", 500)

cliente_1 = ClientePremium("Ana", 1000, 10, "Oro")
cliente_2 = ClienteRegular("Carlos", 600, 5)

cliente_1.atributos()
cliente_2.atributos()

producto_1.mostrar_producto()

compra(cliente_1, cliente_2, producto_1)
