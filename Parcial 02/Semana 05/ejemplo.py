import math
import datetime
import os

# --- CONFIGURACIÓN GLOBAL (Arreglos y Constantes) ---
# Definimos la capacidad según la teoría de arreglos [cite: 152]
FILAS = 8
COLUMNAS = 8
LETRAS_FILAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Matriz para controlar qué puesto está ocupado (Lógica de Arreglos Bidimensionales [cite: 151])
# Inicializamos con None para indicar vacío.
matriz_parqueadero = [[None for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Diccionario para guardar tiempos de entrada (Simula base de datos en memoria)
registro_vehiculos = {}


# --- FUNCIONES DEL SISTEMA (Modularidad [cite: 917]) ---

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def autenticar_usuario():
    """
    Maneja el inicio de sesión con máximo 3 intentos.
    Uso de bucle while para repetición condicional.
    """
    intentos = 0
    max_intentos = 3

    print("=== BIENVENIDO A PARKCONTROL S.A. ===")

    while intentos < max_intentos:
        usuario = input("Usuario: ")
        password = input("Contraseña: ")

        # Validación simple (If-Else )
        if usuario == "admin" and password == "1234":
            print("Acceso concedido.")
            return True
        else:
            intentos += 1
            print(f"Credenciales incorrectas. Intentos restantes: {max_intentos - intentos}")

    print("Ha excedido el número de intentos. Cerrando sistema...")
    return False


def visualizar_mapa():
    """
    Muestra el estado del parqueadero (O = Libre, X = Ocupado).
    Uso de bucles for anidados para recorrer la matriz.
    """
    libres = 0
    ocupados = 0

    print("\n--- MAPA DEL PARQUEADERO ---")
    print("   " + " ".join([str(i + 1) for i in range(COLUMNAS)]))  # Cabecera de columnas

    for i in range(FILAS):
        fila_visual = f"{LETRAS_FILAS[i]} |"
        for j in range(COLUMNAS):
            if matriz_parqueadero[i][j] is None:
                fila_visual += " O"
                libres += 1
            else:
                fila_visual += " X"
                ocupados += 1
        print(fila_visual)

    print(f"\nResumen: {ocupados} Ocupados | {libres} Disponibles")


def ingresar_vehiculo():
    """
    Asigna automáticamente el primer puesto disponible.
    """
    placa = input("\nIngrese la placa del vehículo: ").upper()
    if not placa:
        print("Error: La placa no puede estar vacía.")
        return

    # Verificar si ya existe
    if placa in registro_vehiculos:
        print("Error: Este vehículo ya se encuentra en el parqueadero.")
        return

    # Búsqueda secuencial del primer espacio libre (Nested Loops )
    puesto_asignado = ""
    encontrado = False

    for i in range(FILAS):
        for j in range(COLUMNAS):
            if matriz_parqueadero[i][j] is None:
                # Asignar puesto
                matriz_parqueadero[i][j] = placa
                hora_entrada = datetime.datetime.now()
                registro_vehiculos[placa] = {
                    "fila": i,
                    "columna": j,
                    "entrada": hora_entrada
                }
                puesto_asignado = f"{LETRAS_FILAS[i]}{j + 1}"
                encontrado = True
                break  # Romper ciclo interno [cite: 353]
        if encontrado:
            break  # Romper ciclo externo [cite: 353]

    if encontrado:
        print(f"✅ Vehículo registrado exitosamente.")
        print(f"🅿️ Puesto asignado: {puesto_asignado}")
        print(f"🕒 Hora de entrada: {hora_entrada.strftime('%H:%M:%S')}")
    else:
        print("❌ Lo sentimos, el parqueadero está lleno.")


def consultar_vehiculo():
    placa = input("\nIngrese placa a consultar: ").upper()
    datos = registro_vehiculos.get(placa)

    if datos:
        fila = datos['fila']
        col = datos['columna']
        codigo = f"{LETRAS_FILAS[fila]}{col + 1}"
        hora = datos['entrada'].strftime('%H:%M:%S')
        print(f"-> El vehículo {placa} está en el puesto {codigo}.")
        print(f"-> Hora de ingreso: {hora}")
        print("-> Estado: Estacionado")
    else:
        print("Vehículo no encontrado o ya se retiró.")


def calcular_tarifa(horas):
    """
    Lógica de cálculo de tarifa (Sentencias Condicionales [cite: 645]).
    """
    if horas <= 2:
        return horas * 0.50
    else:
        return horas * 1.00


def salida_vehiculo():
    placa = input("\nIngrese placa para salida: ").upper()
    datos = registro_vehiculos.get(placa)

    if not datos:
        print("Vehículo no encontrado.")
        return

    # Cálculos
    hora_salida = datetime.datetime.now()
    hora_entrada = datos['entrada']

    # Calcular diferencia en segundos y convertir a horas (fracción cuenta como hora)
    diferencia = hora_salida - hora_entrada
    segundos_totales = diferencia.total_seconds()
    horas_cobrar = math.ceil(segundos_totales / 3600)

    # Evitar cobrar 0 si entró y salió al instante
    if horas_cobrar == 0:
        horas_cobrar = 1

    monto = calcular_tarifa(horas_cobrar)

    # Liberar puesto en la matriz
    f, c = datos['fila'], datos['columna']
    matriz_parqueadero[f][c] = None  # Arreglo vuelve a estar vacío
    del registro_vehiculos[placa]  # Eliminar del registro

    print("\n--- TICKET DE SALIDA ---")
    print(f"Placa: {placa}")
    print(f"Entrada: {hora_entrada.strftime('%H:%M:%S')}")
    print(f"Salida:  {hora_salida.strftime('%H:%M:%S')}")
    print(f"Tiempo:  {diferencia}")
    print(f"Horas a cobrar: {horas_cobrar}")
    print(f"TOTAL A PAGAR: ${monto:.2f}")
    print("------------------------")


def menu_principal():
    """
    Bucle principal del programa (Do-While simulado o While ).
    """
    if not autenticar_usuario():
        return

    while True:
        print("\n=== MENÚ PRINCIPAL PARKCONTROL ===")
        print("1. Ingresar Vehículo")
        print("2. Visualizar Mapa (O/X)")
        print("3. Consultar Vehículo")
        print("4. Salida de Vehículo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        # Estructura de selección múltiple simulada (if-elif-else) [cite: 660]
        if opcion == '1':
            ingresar_vehiculo()
        elif opcion == '2':
            visualizar_mapa()
        elif opcion == '3':
            consultar_vehiculo()
        elif opcion == '4':
            salida_vehiculo()
        elif opcion == '5':
            print("Gracias por usar ParkControl.")
            break  # [cite: 353]
        else:
            print("Opción inválida, intente de nuevo.")


# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    menu_principal()