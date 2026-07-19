namespace Practica02Colas;

/// <summary>
/// Gestiona la cola de espera y la asignación de 30 asientos.
/// </summary>
public class SistemaAtraccion
{
    private const int CapacidadMaxima = 30;

    private readonly Queue<Persona> colaEspera;
    private readonly List<Boleto> boletosAsignados;

    private int siguienteId;

    public SistemaAtraccion()
    {
        colaEspera = new Queue<Persona>();
        boletosAsignados = new List<Boleto>();
        siguienteId = 1;
    }

    public int PersonasEnEspera => colaEspera.Count;

    public int AsientosVendidos => boletosAsignados.Count;

    public int AsientosDisponibles =>
        CapacidadMaxima - boletosAsignados.Count;

    public bool AtraccionCompleta =>
        boletosAsignados.Count >= CapacidadMaxima;

    /// <summary>
    /// Agrega una persona al final de la cola.
    /// </summary>
    public bool RegistrarPersona(string nombre)
    {
        if (AtraccionCompleta)
        {
            Console.WriteLine(
                "No se pueden registrar más personas: " +
                "los 30 asientos ya fueron vendidos."
            );

            return false;
        }

        if (string.IsNullOrWhiteSpace(nombre))
        {
            Console.WriteLine("El nombre no puede estar vacío.");
            return false;
        }

        Persona persona = new Persona(siguienteId, nombre);
        colaEspera.Enqueue(persona);
        siguienteId++;

        Console.WriteLine(
            $"\n{persona.Nombre} fue agregado/a correctamente a la cola."
        );

        Console.WriteLine(
            $"Posición actual en la cola: {colaEspera.Count}"
        );

        return true;
    }

    /// <summary>
    /// Retira a la primera persona de la cola y le asigna un asiento.
    /// </summary>
    public Boleto? AsignarSiguienteAsiento()
    {
        if (AtraccionCompleta)
        {
            Console.WriteLine(
                "\nNo existen asientos disponibles."
            );

            return null;
        }

        if (colaEspera.Count == 0)
        {
            Console.WriteLine(
                "\nNo existen personas esperando en la cola."
            );

            return null;
        }

        Persona persona = colaEspera.Dequeue();
        int numeroAsiento = boletosAsignados.Count + 1;

        Boleto boleto = new Boleto(numeroAsiento, persona);
        boletosAsignados.Add(boleto);

        Console.WriteLine("\nAsiento asignado correctamente:");
        Console.WriteLine(boleto);

        return boleto;
    }

    /// <summary>
    /// Muestra las personas que todavía esperan.
    /// </summary>
    public void MostrarCola()
    {
        Console.WriteLine("\n===== PERSONAS EN LA COLA =====");

        if (colaEspera.Count == 0)
        {
            Console.WriteLine("La cola se encuentra vacía.");
            return;
        }

        int posicion = 1;

        foreach (Persona persona in colaEspera)
        {
            Console.WriteLine(
                $"Posición {posicion:D2} | {persona}"
            );

            posicion++;
        }
    }

    /// <summary>
    /// Muestra todos los asientos asignados.
    /// </summary>
    public void MostrarAsientosAsignados()
    {
        Console.WriteLine("\n===== ASIENTOS ASIGNADOS =====");

        if (boletosAsignados.Count == 0)
        {
            Console.WriteLine(
                "Todavía no se han asignado asientos."
            );

            return;
        }

        foreach (Boleto boleto in boletosAsignados)
        {
            Console.WriteLine(boleto);
        }
    }

    /// <summary>
    /// Busca un boleto por número de asiento.
    /// </summary>
    public void ConsultarAsiento(int numeroAsiento)
    {
        Boleto? boleto = boletosAsignados.FirstOrDefault(
            elemento => elemento.NumeroAsiento == numeroAsiento
        );

        Console.WriteLine("\n===== CONSULTA DE ASIENTO =====");

        if (boleto is null)
        {
            Console.WriteLine(
                $"El asiento {numeroAsiento} todavía no ha sido asignado."
            );

            return;
        }

        Console.WriteLine(boleto);
    }

    /// <summary>
    /// Presenta un resumen general del sistema.
    /// </summary>
    public void MostrarResumen()
    {
        Console.WriteLine("\n===== RESUMEN GENERAL =====");
        Console.WriteLine($"Capacidad máxima: {CapacidadMaxima}");
        Console.WriteLine($"Personas en espera: {PersonasEnEspera}");
        Console.WriteLine($"Asientos vendidos: {AsientosVendidos}");
        Console.WriteLine($"Asientos disponibles: {AsientosDisponibles}");

        Console.WriteLine(
            AtraccionCompleta
                ? "Estado: Todos los asientos fueron vendidos."
                : "Estado: Existen asientos disponibles."
        );
    }
}