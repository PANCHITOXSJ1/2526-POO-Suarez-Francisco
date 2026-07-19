# Programación Tradicional
# Cálculo del promedio semanal del clima (mejorado)

import argparse
import random
import statistics
from typing import List, Optional


def input_temperatures(days: int = 7) -> List[float]:
    """Solicita al usuario temperaturas por consola para un número de días.

    Valida que la entrada sea convertible a float y esté en un rango razonable.
    """
    temps: List[float] = []
    for day in range(1, days + 1):
        while True:
            raw = input(f"Ingrese la temperatura del día {day}: ").strip()
            try:
                temp = float(raw)
            except ValueError:
                print("Entrada inválida. Introduzca un número, por ejemplo: 23.5")
                continue
            # Rango plausible para temperaturas (evita errores por unidad accidental)
            if temp < -100 or temp > 100:
                confirm = input(f"La temperatura {temp} parece inusual. ¿Está seguro? (s/n): ").lower()
                if confirm not in ("s", "si", "y", "yes"):
                    print("Reingrese la temperatura.")
                    continue
            temps.append(temp)
            break
    return temps


def parse_temperatures_list(raw: str) -> List[float]:
    """Convierte una cadena separada por comas en una lista de floats.

    Ejemplo: '23, 24.5, 19' -> [23.0, 24.5, 19.0]
    Lanza ValueError si alguna entrada no es un número.
    """
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    if not parts:
        raise ValueError("No se proporcionaron temperaturas en la lista.")
    temps = [float(p) for p in parts]
    return temps


def random_temperatures(days: int = 7, low: float = 0.0, high: float = 30.0, seed: Optional[int] = None) -> List[float]:
    """Genera una lista de temperaturas aleatorias entre low y high."""
    if seed is not None:
        random.seed(seed)
    return [round(random.uniform(low, high), 1) for _ in range(days)]


def calculate_statistics(temps: List[float]) -> dict:
    """Calcula estadísticas básicas sobre la lista de temperaturas.

    Retorna un diccionario con promedio, min, max, mediana, desviación estándar y conteo.
    """
    if not temps:
        raise ValueError("La lista de temperaturas está vacía.")

    avg = statistics.mean(temps)
    minimum = min(temps)
    maximum = max(temps)
    median = statistics.median(temps)
    stdev = statistics.pstdev(temps) if len(temps) > 1 else 0.0

    return {
        "count": len(temps),
        "average": avg,
        "min": minimum,
        "max": maximum,
        "median": median,
        "stdev": stdev,
    }


def format_statistics(stats: dict, precision: int = 2) -> str:
    """Devuelve una cadena formateada con las estadísticas."""
    p = precision
    lines = [
        f"Días: {stats['count']}",
        f"Promedio: {stats['average']:.{p}f} °C",
        f"Mínima: {stats['min']:.{p}f} °C",
        f"Máxima: {stats['max']:.{p}f} °C",
        f"Mediana: {stats['median']:.{p}f} °C",
        f"Desviación (poblacional): {stats['stdev']:.{p}f} °C",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Cálculo de estadísticas semanales de temperatura (tradicional mejorado).")
    parser.add_argument("--days", "-d", type=int, default=7, help="Número de días a considerar (por defecto 7).")
    parser.add_argument("--list", "-l", type=str, help="Lista de temperaturas separadas por comas, e.g. '23,24.5,19'")
    parser.add_argument("--sample", "-s", action="store_true", help="Usar un conjunto de ejemplo predefinido (no interactivo).")
    parser.add_argument("--random", "-r", action="store_true", help="Generar temperaturas aleatorias en lugar de pedirlas.")
    parser.add_argument("--seed", type=int, default=None, help="Semilla para generación aleatoria (opcional).")
    parser.add_argument("--low", type=float, default=10.0, help="Límite inferior para generación aleatoria.")
    parser.add_argument("--high", type=float, default=30.0, help="Límite superior para generación aleatoria.")
    parser.add_argument("--precision", "-p", type=int, default=2, help="Decimales en la salida (por defecto 2).")

    args = parser.parse_args()

    # Determinar la fuente de temperaturas
    if args.list:
        try:
            temps = parse_temperatures_list(args.list)
        except ValueError as e:
            print(f"Error al parsear la lista: {e}")
            return
    elif args.sample:
        # Conjunto de ejemplo predefinido (puede cambiarse libremente)
        temps = [22.5, 24.0, 19.8, 21.0, 23.4, 20.2, 25.1][: args.days]
    elif args.random:
        temps = random_temperatures(args.days, low=args.low, high=args.high, seed=args.seed)
    else:
        # Entrada interactiva
        temps = input_temperatures(args.days)

    stats = calculate_statistics(temps)

    print("\n--- Estadísticas de temperatura semanal (Tradicional Mejorado) ---")
    print(format_statistics(stats, precision=args.precision))
    print("\nListado de temperaturas:")
    print(", ".join(f"{t:.{args.precision}f} °C" for t in temps))


if __name__ == "__main__":
    main()
