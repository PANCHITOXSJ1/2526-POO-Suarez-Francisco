namespace Practica02Colas;

/// <summary>
/// Representa a una persona que espera ingresar a la atracción.
/// </summary>
public class Persona
{
    public int Id { get; }
    public string Nombre { get; }
    public DateTime HoraLlegada { get; }

    public Persona(int id, string nombre)
    {
        if (id <= 0)
        {
            throw new ArgumentException(
                "El identificador debe ser mayor que cero.",
                nameof(id)
            );
        }

        if (string.IsNullOrWhiteSpace(nombre))
        {
            throw new ArgumentException(
                "El nombre no puede estar vacío.",
                nameof(nombre)
            );
        }

        Id = id;
        Nombre = nombre.Trim();
        HoraLlegada = DateTime.Now;
    }

    public override string ToString()
    {
        return $"ID: {Id} | Nombre: {Nombre} | " +
               $"Llegada: {HoraLlegada:HH:mm:ss}";
    }
}