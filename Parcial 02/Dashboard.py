import os
import subprocess


# ================================
# FUNCIÓN PARA EJECUTAR ARCHIVOS
# ================================
def ejecutar_script(ruta_script):
    try:
        if os.name == "nt":  # WINDOWS
            subprocess.Popen(["cmd", "/k", "python", ruta_script])
        else:  # LINUX / MAC
            subprocess.Popen(["xterm", "-hold", "-e", "python3", ruta_script])
    except Exception as e:
        print("Error al ejecutar:", e)


# ================================
# MENÚ PRINCIPAL DASHBOARD
# ================================
def menu_dashboard():

    # Ruta base del proyecto
    ruta_base = os.path.dirname(__file__)

    # Lista de trabajos organizados
    opciones = {
        "1": {
            "titulo": "Semana 05 - Tipos de Datos",
            "archivo": "Semana 05/S5 Tipo de Datos snake_case.py"
        },
        "2": {
            "titulo": "Semana 06 - Herencia",
            "archivo": "Semana 06/Herencia.py"
        },
        "3": {
            "titulo": "Semana 07 - Constructores y Destructores",
            "archivo": "Semana 07/S7 Contrcutores y Destructores.py"
        },
        "4": {
            "titulo": "Ejecutar main.py",
            "archivo": "main.py"
        }
    }

    while True:
        print("\n==============================")
        print("   DASHBOARD - POO PARCIAL 02")
        print("==============================")

        # Mostrar opciones disponibles
        for key, valor in opciones.items():
            print(f"{key}. {valor['titulo']}")

        print("0. Salir")

        # Entrada del usuario
        eleccion = input("\nElige una opción: ")

        if eleccion == "0":
            print("\n✅ Saliendo del programa... Hasta pronto.")
            break

        elif eleccion in opciones:

            # Obtener ruta completa del archivo
            ruta_script = os.path.join(ruta_base, opciones[eleccion]["archivo"])

            if os.path.exists(ruta_script):

                print("\n📌 Ejecutando:", opciones[eleccion]["titulo"])
                ejecutar_script(ruta_script)

            else:
                print("\n❌ Error: No se encontró el archivo:")
                print("Ruta:", ruta_script)

        else:
            print("\n⚠️ Opción inválida. Intenta nuevamente.")


# ================================
# EJECUCIÓN DEL DASHBOARD
# ================================
if __name__ == "__main__":
    menu_dashboard()
