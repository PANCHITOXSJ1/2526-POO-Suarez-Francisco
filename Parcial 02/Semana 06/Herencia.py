# ============================================================
# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# Ejemplo práctico basado en los conceptos de:
# Clases, Objetos, Herencia, Encapsulación y Polimorfismo
# ============================================================

# ------------------------------------------------------------
# CLASE BASE
# ------------------------------------------------------------
class DispositivoElectronico:
    """
    En la Programación Orientada a Objetos, una clase es una plantilla
    o modelo que define las características (atributos) y comportamientos
    (métodos) que tendrán los objetos creados a partir de ella.
    """

    def __init__(self, marca):
        # Atributo protegido que representa una característica común
        # de los dispositivos electrónicos
        self.marca = marca

    def encender(self):
        """
        Método que define un comportamiento general del objeto.
        Este método será sobrescrito en las clases hijas,
        permitiendo aplicar el principio de polimorfismo.
        """
        print("El dispositivo electrónico se está encendiendo.")


# ------------------------------------------------------------
# CLASE DERIVADA (HERENCIA)
# ------------------------------------------------------------
class Telefono(DispositivoElectronico):
    """
    La herencia permite que una clase hija herede atributos y métodos
    de una clase padre, facilitando la reutilización de código.
    """

    def __init__(self, marca, numero):
        # Se llama al constructor de la clase base
        super().__init__(marca)

        # --------------------------------------------------------
        # ENCAPSULACIÓN
        # --------------------------------------------------------
        # El atributo __numero es privado y no puede ser accedido
        # directamente desde fuera de la clase.
        self.__numero = numero

    # Método getter
    def obtener_numero(self):
        """
        Los métodos getter permiten acceder de forma controlada
        a los atributos privados, protegiendo la información interna.
        """
        return self.__numero

    # Método setter
    def cambiar_numero(self, nuevo_numero):
        """
        Los métodos setter permiten modificar los atributos privados
        de forma segura, aplicando el principio de encapsulación.
        """
        self.__numero = nuevo_numero

    # --------------------------------------------------------
    # POLIMORFISMO (SOBREESCRITURA)
    # --------------------------------------------------------
    def encender(self):
        """
        Este método sobrescribe el método encender() de la clase padre.
        Aunque tiene el mismo nombre, su comportamiento es diferente,
        demostrando el principio de polimorfismo.
        """
        print(f"El teléfono de la marca {self.marca} se está encendiendo.")


# ------------------------------------------------------------
# OTRA CLASE DERIVADA
# ------------------------------------------------------------
class Computadora(DispositivoElectronico):
    """
    Esta clase también hereda de DispositivoElectronico y sobrescribe
    el método encender(), demostrando que distintos objetos pueden
    responder de manera diferente al mismo método.
    """

    def encender(self):
        print(f"La computadora de la marca {self.marca} está iniciando el sistema.")


# ------------------------------------------------------------
# CREACIÓN DE OBJETOS (INSTANCIACIÓN)
# ------------------------------------------------------------
"""
Un objeto es una instancia concreta de una clase.
Durante la instanciación se ejecuta automáticamente el constructor __init__.
"""

telefono1 = Telefono("Samsung", "0991234567")
computadora1 = Computadora("Dell")

# ------------------------------------------------------------
# USO DE MÉTODOS Y DEMOSTRACIÓN DE FUNCIONALIDAD
# ------------------------------------------------------------

# Encapsulación: acceso controlado al atributo privado
print("Número original del teléfono:", telefono1.obtener_numero())
telefono1.cambiar_numero("0987654321")
print("Número actualizado del teléfono:", telefono1.obtener_numero())

# Polimorfismo: mismo método, distinto comportamiento
telefono1.encender()
computadora1.encender()
