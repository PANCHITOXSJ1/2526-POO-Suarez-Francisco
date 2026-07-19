"""
Programa: Conversión de temperatura
Descripción:
Este programa solicita una temperatura en grados Celsius,
la convierte a grados Fahrenheit y muestra los resultados en pantalla.
"""

# Mensaje inicial
print("=== CONVERSIÓN DE TEMPERATURA ===")

# Entrada de datos
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Proceso de conversión
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

# Validación con variable booleana
es_temperatura_valida = temperatura_celsius >= -273.15

# Salida de resultados
print("\n--- RESULTADOS ---")
print("Temperatura en Celsius:", temperatura_celsius)
print("Temperatura en Fahrenheit:", temperatura_fahrenheit)
print("¿La temperatura ingresada es válida?", es_temperatura_valida)

# Mensaje final
print("\nPrograma finalizado correctamente.")
