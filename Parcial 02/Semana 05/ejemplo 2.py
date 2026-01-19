# Importamos la biblioteca para funciones matemáticas (PDF Funciones: Biblioteca cmath/math)
import math
# Importamos la biblioteca para manejar el tiempo (PDF Funciones: Biblioteca ctime/datetime)
import datetime
# Importamos biblioteca para limpiar pantalla (PDF Funciones: Biblioteca cstdlib/os)
import os

# --- DEFINICIÓN DE ARREGLOS Y CONSTANTES (PDF Arreglos) ---

# Variable constante para definir el número de filas (PDF Arreglos: Tamaño/Capacidad)
FILAS = 8
# Variable constante para definir el número de columnas (PDF Arreglos: Tamaño/Capacidad)
COLUMNAS = 8
# Arreglo unidimensional para etiquetar las filas visualmente (PDF Arreglos: Declaración)
LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Declaración de un arreglo bidimensional (Matriz) de 8x8.
# Inicializamos con 'None' que representa un espacio vacío.
# Concepto teórico: Un array a cuyos valores se accede a través de dos índices (PDF Arreglos: Pág 8)
matriz_parqueadero = [[None for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Diccionario auxiliar para guardar la hora de entrada.
# (Se usa para apoyar la lógica, simulando una base de datos simple)
tiempos_ingreso = {}


# --- DEFINICIÓN DE FUNCIONES (PDF Funciones: Definición y Prototipos) ---

# Función que no recibe parámetros y no retorna valor (void), solo limpia la consola
def limpiar_pantalla():
    # Sentencia condicional para detectar el sistema operativo
    if os.name == 'nt':
        os.system('cls')  # Comando para Windows
    else:
        os.system('clear')  # Comando para Linux/Mac


# Función para autenticar usuario. Retorna un valor Booleano (Verdadero/Falso)
# PDF Funciones: Tipo de retorno (Pág 5)
def autenticar():
    # Variable local para contar intentos
    intentos = 0
    # Variable constante local para límite de intentos
    MAX_INTENTOS = 3
    # Inicialización de credenciales correctas
    USUARIO_CORRECTO = "admin"
    CLAVE_CORRECTA = "1234"

    # Sentencia de repetición 'while'. Se ejecuta mientras intentos sea menor a 3.
    # PDF Sentencias de Repetición: Pág 7, "Mientras la condición sea verdadera"
    while intentos < MAX_INTENTOS:
        # Imprimir mensaje en pantalla
        print("\n--- LOGIN ---")
        # Captura de datos ingresados por el usuario
        usuario = input("Ingrese usuario: ")
        clave = input("Ingrese contraseña: ")

        # Sentencia condicional compuesta (AND lógicos).
        # PDF Expresiones: Operadores lógicos && (and) (Pág 9)
        if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRECTA:
            # Retorno exitoso, sale de la función inmediatamente
            return True
        else:
            # Operador de incremento (contador)
            # PDF Expresiones: Operadores unitarios/asignación (Pág 6)
            intentos += 1
            # Mostrar mensaje de error con formateo básico
            print(f"Incorrecto. Intentos restantes: {MAX_INTENTOS - intentos}")

    # Si el bucle termina (se acabaron los intentos), retorna Falso
    return False


# Función para mostrar el mapa del parqueadero (Recorrido de Matriz)
def mostrar_mapa():
    print("\n--- ESTADO DEL PARQUEADERO (X=Ocupado, O=Libre) ---")
    # Imprimimos encabezado de columnas (1 al 8)
    print("   1 2 3 4 5 6 7 8")

    # Sentencia de repetición 'for' anidada para recorrer filas.
    # PDF Arreglos: Acceso a través de índices (Pág 8)
    for i in range(FILAS):
        # Variable acumuladora para construir la línea visual de la fila actual
        fila_str = LETRAS[i] + " |"

        # Sentencia de repetición 'for' interna para recorrer columnas (Matriz)
        # PDF Arreglos: Índice de la derecha denota columnas (Pág 8)
        for j in range(COLUMNAS):
            # Sentencia condicional para verificar si la celda es None (Vacía)
            if matriz_parqueadero[i][j] == None:
                # Concatenamos "O" si está libre
                fila_str += " O"
            else:
                # Sentencia 'else': Concatenamos "X" si está ocupada
                fila_str += " X"

        # Imprimimos la fila completa
        print(fila_str)


# Función para ingresar un vehículo al primer espacio libre
def ingresar_vehiculo():
    # Solicitar placa y convertir a mayúsculas
    placa = input("Ingrese placa del vehículo: ").upper()

    # Bandera (flag) para saber si encontramos puesto
    encontrado = False

    # Recorrido de la matriz para buscar el primer espacio vacío
    # PDF Sentencias de Repetición: for anidado
    for i in range(FILAS):
        for j in range(COLUMNAS):
            # Condicional: Si la posición [i][j] es None (Vacío)
            if matriz_parqueadero[i][j] == None:
                # Asignación: Guardamos la placa en la matriz
                # PDF Arreglos: Modificación de datos (Pág 6)
                matriz_parqueadero[i][j] = placa

                # Guardamos la hora actual usando función de biblioteca datetime
                tiempos_ingreso[placa] = datetime.datetime.now()

                # Mostramos confirmación al usuario
                print(f"Asignado al puesto: {LETRAS[i]}{j + 1}")

                # Cambiamos la bandera a Verdadero
                encontrado = True

                # Sentencia 'break' para romper el bucle interno (columnas)
                # PDF Sentencias de Repetición: Sentencia break (Pág 10)
                break

                # Condicional: Si ya encontramos puesto, rompemos el bucle externo (filas)
        if encontrado == True:
            break

    # Si terminaron los ciclos y no se encontró puesto (Else del if de bandera)
    if encontrado == False:
        print("Error: Parqueadero lleno.")


# Función para calcular tarifa basada en reglas de negocio
# Recibe parámetro 'horas' (int o float) y retorna 'total' (float)
def calcular_pago(horas):
    # Sentencia condicional simple
    # Si las horas son menores o iguales a 2
    if horas <= 2:
        # Operación aritmética: multiplicación
        total = horas * 0.50
    else:
        # Sentencia 'else': Si las horas son mayores a 2
        total = horas * 1.00

    # Retorna el valor calculado
    return total


# Función para procesar la salida del vehículo
def salida_vehiculo():
    # Solicitar placa
    placa = input("Ingrese placa para salida: ").upper()

    # Bandera para búsqueda
    ubicado = False

    # Recorrido de búsqueda en la matriz
    for i in range(FILAS):
        for j in range(COLUMNAS):
            # Operador de comparación: Igualdad (==)
            # PDF Expresiones: Operadores de comparación (Pág 8)
            if matriz_parqueadero[i][j] == placa:
                # Recuperar hora de entrada guardada
                hora_entrada = tiempos_ingreso[placa]
                # Obtener hora de salida actual
                hora_salida = datetime.datetime.now()

                # Calcular diferencia de tiempo (resta)
                duracion = hora_salida - hora_entrada
                # Convertir diferencia a segundos totales
                segundos = duracion.total_seconds()
                # Convertir a horas (división)
                # Usamos math.ceil para redondear hacia arriba (fracción cuenta como hora)
                # PDF Funciones: Biblioteca cmath (Pág 11)
                horas_cobrar = math.ceil(segundos / 3600)

                # Llamada a función definida por el usuario para obtener precio
                monto = calcular_pago(horas_cobrar)

                # Liberar el espacio en el arreglo (Asignar None)
                # PDF Arreglos: Modificación de datos (Pág 6)
                matriz_parqueadero[i][j] = None

                # Eliminar registro de tiempo del diccionario
                del tiempos_ingreso[placa]

                # Mostrar factura
                print(f"\n--- TICKET DE SALIDA ---")
                print(f"Placa: {placa}")
                print(f"Tiempo total: {horas_cobrar} horas")
                print(f"Total a pagar: ${monto}")

                # Marcar como ubicado y salir del bucle
                ubicado = True
                break

        if ubicado:
            break

    # Si no se encontró la placa tras recorrer toda la matriz
    if not ubicado:
        print("Vehículo no encontrado en el sistema.")


# Función para consultar estado de un vehículo específico
def consultar_vehiculo():
    placa = input("Ingrese placa a buscar: ").upper()
    encontrado = False

    # Recorrido secuencial de la matriz
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if matriz_parqueadero[i][j] == placa:
                # Obtener hora formateada
                hora_str = tiempos_ingreso[placa].strftime("%H:%M:%S")
                print(f"El vehículo {placa} está en {LETRAS[i]}{j + 1}.")
                print(f"Hora de ingreso: {hora_str}")
                encontrado = True
                break
        if encontrado:
            break

    if not encontrado:
        print("El vehículo no se encuentra estacionado.")


# --- BLOQUE PRINCIPAL (MAIN) ---

# Invocamos la autenticación primero. Si retorna False, no entra al menú.
if autenticar() == True:

    # Sentencia de repetición infinita para el menú (hasta que se decida salir)
    # PDF Sentencias de Repetición: while (Pág 7)
    while True:
        # Pausa visual antes de mostrar menú (input vacío)
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

        # Mostrar opciones
        print("\n--- MENÚ PARKCONTROL S.A. ---")
        print("1. Ingresar Vehículo")
        print("2. Visualizar Mapa")
        print("3. Consultar Vehículo")
        print("4. Salida de Vehículo")
        print("5. Salir")

        # Captura de opción
        opcion = input("Seleccione una opción: ")

        # Sentencias condicionales múltiples (if-elif-else)
        # PDF Sentencias Condicionales: if..else..if (Pág 10)
        if opcion == "1":
            ingresar_vehiculo()
        elif opcion == "2":
            mostrar_mapa()
        elif opcion == "3":
            consultar_vehiculo()
        elif opcion == "4":
            salida_vehiculo()
        elif opcion == "5":
            print("Cerrando sistema...")
            # Sentencia break para terminar el ciclo while infinito
            break
        else:
            # Caso por defecto (Default)
            print("Opción inválida.")
else:
    # Si la autenticación falla 3 veces
    print("Acceso denegado. Sistema bloqueado.")