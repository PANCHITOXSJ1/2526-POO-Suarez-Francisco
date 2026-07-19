# Programación Orientada a Objetos (POO)
# Cálculo del promedio semanal del clima (mejorado)

import argparse
import random
from typing import List, Optional


class WeatherWeek:
    def __init__(self, temperatures: Optional[List[float]] = None):
        # Encapsulamiento de los datos
        self.temperatures: List[float] = temperatures[:] if temperatures else []

    # Método para ingresar las temperaturas diarias (con validación)
    def input_temperatures(self, days: int = 7) -> None:
        self.temperatures = []
        for day in range(1, days + 1):
            while True:
                raw = input(f"Ingrese la temperatura del día {day}: ").strip()
                try:
                    temp = float(raw)
                except ValueError:
                    print("Entrada inválida. Introduzca un número, por ejemplo: 23.5")
                    continue
                if temp < -100 or temp > 100:
                    confirm = input(f"La temperatura {temp} parece inusual. ¿Está seguro? (s/n): ").lower()
                    if confirm not in ("s", "si", "y", "yes"):
                        print("Reingrese la temperatura.")
                        continue
                self.temperatures.append(temp)
                break

    # Método para calcular el promedio semanal
    def calculate_weekly_average(self) -> float:
        if not self.temperatures:
            raise ValueError("No hay temperaturas para calcular el promedio.")
        total = sum(self.temperatures)
        average = total / len(self.temperatures)
        return average

    @classmethod
    def from_list(cls, temps: List[float]) -> "WeatherWeek":
        return cls(temperatures=temps)

    @classmethod
    def random_week(cls, days: int = 7, low: float = 10.0, high: float = 30.0, seed: Optional[int] = None) -> "WeatherWeek":
        if seed is not None:
            random.seed(seed)
        temps = [round(random.uniform(low, high), 1) for _ in range(days)]
        return cls(temperatures=temps)

    def __str__(self) -> str:
        if not self.temperatures:
            return "No hay datos de temperatura."
        temps_str = ", ".join(f"{t:.2f} °C" for t in self.temperatures)
        try:
            avg = self.calculate_weekly_average()
            return f"Promedio semanal de temperatura (POO): {avg:.2f} °C\nListado: {temps_str}"
        except ValueError:
            return "No hay datos para calcular el promedio."


def parse_temperatures_list(raw: str) -> List[float]:
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    if not parts:
        raise ValueError("No se proporcionaron temperaturas en la lista.")
    return [float(p) for p in parts]


def main() -> None:
    parser = argparse.ArgumentParser(description="Cálculo del promedio semanal de temperatura (POO mejorado).")
    parser.add_argument("--days", "-d", type=int, default=7, help="Número de días a considerar (por defecto 7).")
    parser.add_argument("--list", "-l", type=str, help="Lista de temperaturas separadas por comas, e.g. '23,24.5,19'")
    parser.add_argument("--sample", "-s", action="store_true", help="Usar un conjunto de ejemplo predefinido (no interactivo).")
    parser.add_argument("--random", "-r", action="store_true", help="Generar temperaturas aleatorias en lugar de pedirlas.")
    parser.add_argument("--seed", type=int, default=None, help="Semilla para generación aleatoria (opcional).")
    parser.add_argument("--low", type=float, default=10.0, help="Límite inferior para generación aleatoria.")
    parser.add_argument("--high", type=float, default=30.0, help="Límite superior para generación aleatoria.")
    parser.add_argument("--precision", "-p", type=int, default=2, help="Decimales en la salida (por defecto 2).")

    args = parser.parse_args()

    if args.list:
        try:
            temps = parse_temperatures_list(args.list)
            week = WeatherWeek.from_list(temps)
        except ValueError as e:
            print(f"Error al parsear la lista: {e}")
            return
    elif args.sample:
        temps = [22.5, 24.0, 19.8, 21.0, 23.4, 20.2, 25.1][: args.days]
        week = WeatherWeek.from_list(temps)
    elif args.random:
        week = WeatherWeek.random_week(days=args.days, low=args.low, high=args.high, seed=args.seed)
    else:
        # Entrada interactiva
        week = WeatherWeek()
        try:
            week.input_temperatures(days=args.days)
        except (KeyboardInterrupt, EOFError):
            print("\nEntrada interrumpida. Saliendo.")
            return

    # Imprimir resultados
    try:
        avg = week.calculate_weekly_average()
        print("\n--- Estadísticas semanales (POO) ---")
        print(f"Días: {len(week.temperatures)}")
        print(f"Promedio: {avg:.{args.precision}f} °C")
        print(f"Listado: {', '.join(f'{t:.{args.precision}f} °C' for t in week.temperatures)}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
