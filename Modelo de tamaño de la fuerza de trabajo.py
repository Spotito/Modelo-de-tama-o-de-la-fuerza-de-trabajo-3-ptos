def optimizar_fuerza_trabajo(demandas, costo_contratar, costo_despedir):
    """
    Optimiza la fuerza de trabajo para minimizar los costos.

    Args:
        demandas: Lista con la demanda de trabajadores para cada semana.
        costo_contratar: Costo por contratar a un trabajador.
        costo_despedir: Costo por despedir a un trabajador.

    Returns:
        Una lista con la fuerza de trabajo óptima para cada semana y el costo total.
    """

    n = len(demandas)
    fuerza_trabajo = [0] * n
    costo_total = 0

    # Inicializar la fuerza de trabajo para la primera semana
    fuerza_trabajo[0] = demandas[0]
    costo_total += demandas[0] * costo_contratar
    print(f"Semana 1: {fuerza_trabajo[0]} trabajadores, costo: ${demandas[0] * costo_contratar}")

    # Iterar sobre las demás semanas
    for i in range(1, n):
        diferencia = demandas[i] - fuerza_trabajo[i-1]

        # Ajustar la fuerza de trabajo y calcular el costo
        if diferencia > 0:
            # Contratar trabajadores
            fuerza_trabajo[i] = demandas[i]
            costo_total += diferencia * costo_contratar
            print(f"Semana {i+1}: {fuerza_trabajo[i]} trabajadores, costo: ${diferencia * costo_contratar}")
        elif diferencia < 0:
            # Despedir trabajadores
            fuerza_trabajo[i] = demandas[i]
            costo_total += abs(diferencia) * costo_despedir
            print(f"Semana {i+1}: {fuerza_trabajo[i]} trabajadores, costo: ${abs(diferencia) * costo_despedir}")

    return fuerza_trabajo, costo_total

# Datos del problema
demandas = [5, 7, 8, 4, 6]
costo_contratar = 200
costo_despedir = 300

# Calcular la solución óptima
fuerza_trabajo_optima, costo_total = optimizar_fuerza_trabajo(demandas, costo_contratar, costo_despedir)

# Imprimir los resultados
print("\nCosto total:", costo_total)