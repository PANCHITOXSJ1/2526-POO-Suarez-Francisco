namespace Practica02Colas;

/// <summary>
/// Representa el boleto asignado a una persona.
/// </summary>
public class Boleto
{
    public int NumeroAsiento { get; }
    public Persona PersonaAsignada { get; }
    public DateTime HoraAsignacion { get; }

    public Boleto(int numeroAsiento, Persona personaAsignada)
    {
        if (numeroAsiento <= 0)
        {
            throw new ArgumentException(
                "El número de asiento debe ser mayor que cero.",
                nameof(numeroAsiento)
            );
        }

        PersonaAsignada = personaAsignada
            ?? throw new ArgumentNullException(nameof(personaAsignada));

        NumeroAsiento = numeroAsiento;
        HoraAsignacion = DateTime.Now;
    }

    public override string ToString()
    {
        return $"Asiento: {NumeroAsiento:D2} | " +
               $"Persona: {PersonaAsignada.Nombre} | " +
               $"Asignación: {HoraAsignacion:HH:mm:ss}";
    }
}