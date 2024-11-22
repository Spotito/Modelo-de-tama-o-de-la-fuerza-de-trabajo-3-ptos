class FuerzaTrabajo:
    def __init__(self, requerimientos):
        self.requerimientos = requerimientos
        self.costo_excedente = 300
        self.costo_contratar = 400
        self.costo_por_trabajador = 200
        self.n = len(requerimientos)
        self.dp = [0] * (self.n + 1)

    def calcular_costo_minimo(self):
        self.dp[1] = self.requerimientos[0] * self.costo_por_trabajador
        print(f"Semana 1: Costo = {self.dp[1]}")
        print("")
        for i in range(2, self.n + 1):
            # Opción 1: Mantener a todos los trabajadores de la semana anterior
            opcion1 = self.dp[i - 1] + self.costo_excedente * max(0, self.dp[i - 1] - self.requerimientos[i - 1])

            # Opción 2: Contratar solo los necesarios para la semana actual
            opcion2 = self.costo_contratar + self.requerimientos[i - 1] * self.costo_por_trabajador

            self.dp[i] = min(opcion1, opcion2)

            print(f"Semana {i}:")
            print(f"  Opción 1 (Mantener): {opcion1}")
            print(f"  Opción 2 (Contratar): {opcion2}")
            print(f"  Costo mínimo: {self.dp[i]}")
            print("")

        return self.dp[self.n]

if __name__ == "__main__":
    requerimientos = [5, 7, 8, 4, 6]
    fuerza_trabajo = FuerzaTrabajo(requerimientos)
    costo_minimo = fuerza_trabajo.calcular_costo_minimo()
    print("El costo mínimo total es:", costo_minimo)
