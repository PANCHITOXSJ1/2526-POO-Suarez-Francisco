using System.Diagnostics;
using Practica02Colas;

Console.OutputEncoding = System.Text.Encoding.UTF8;

SistemaAtraccion sistema = new SistemaAtraccion();
bool continuar = true;

while (continuar)
{
    MostrarMenu();

    Console.Write("Seleccione una opción: ");
    string? opcion = Console.ReadLine();

    switch (opcion)
    {
        case "1":
            RegistrarPersona(sistema);
            break;

        case "2":
            MedirAsignacionDeAsiento(sistema);
            break;

        case "3":
            sistema.MostrarCola();
            Pausar();
            break;

        case "4":
            sistema.MostrarAsientosAsignados();
            Pausar();
            break;

        case "5":
            ConsultarAsiento(sistema);
            break;

        case "6":
            sistema.MostrarResumen();
            Pausar();
            break;

        case "7":
            continuar = false;
            Console.WriteLine(
                "\nGracias por utilizar el sistema de asignación."
            );
            break;

        default:
            Console.WriteLine(
                "\nOpción inválida. Seleccione una opción del 1 al 7."
            );
            Pausar();
            break;
    }
}

static void MostrarMenu()
{
    Console.Clear();

    Console.WriteLine("==========================================");
    Console.WriteLine(" SISTEMA DE ASIGNACIÓN DE ASIENTOS");
    Console.WriteLine(" ATRACCIÓN DEL PARQUE DE DIVERSIONES");
    Console.WriteLine("==========================================");
    Console.WriteLine("1. Registrar persona en la cola");
    Console.WriteLine("2. Asignar asiento a la siguiente persona");
    Console.WriteLine("3. Visualizar cola de espera");
    Console.WriteLine("4. Visualizar asientos asignados");
    Console.WriteLine("5. Consultar un asiento");
    Console.WriteLine("6. Mostrar resumen general");
    Console.WriteLine("7. Salir");
    Console.WriteLine("==========================================");
}

static void RegistrarPersona(SistemaAtraccion sistema)
{
    Console.Write("\nIngrese el nombre de la persona: ");
    string? nombre = Console.ReadLine();

    sistema.RegistrarPersona(nombre ?? string.Empty);
    Pausar();
}

static void MedirAsignacionDeAsiento(
    SistemaAtraccion sistema
)
{
    Stopwatch cronometro = Stopwatch.StartNew();

    sistema.AsignarSiguienteAsiento();

    cronometro.Stop();

    Console.WriteLine(
        $"Tiempo de ejecución: " +
        $"{cronometro.Elapsed.TotalMilliseconds:F6} milisegundos."
    );

    Pausar();
}

static void ConsultarAsiento(SistemaAtraccion sistema)
{
    Console.Write("\nIngrese el número del asiento: ");
    string? entrada = Console.ReadLine();

    if (!int.TryParse(entrada, out int numeroAsiento))
    {
        Console.WriteLine(
            "Debe ingresar un número entero válido."
        );

        Pausar();
        return;
    }

    sistema.ConsultarAsiento(numeroAsiento);
    Pausar();
}

static void Pausar()
{
    Console.WriteLine(
        "\nPresione cualquier tecla para continuar..."
    );

    Console.ReadKey();
}