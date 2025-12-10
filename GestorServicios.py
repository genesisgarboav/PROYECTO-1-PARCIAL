# Integrantes:
# - Crespo John
# - Danna Rodriguez
# - Genesis Garboa
# -Alvarado


from typing import List
from ServiciosUG import ServicioUniversitario


class GestorServicios:
    """
    Clase que contiene operaciones sobre listas de ServiciosUniversitarios.
    Aquí residirán los métodos polimórficos requeridos.
    """

    @staticmethod
    def sumar_costos(servicios: List[ServicioUniversitario]) -> float:
        """
        Polimórfico: recibe una lista de objetos derivados de ServicioUniversitario
        y suma su costo llamando al método calcular_costo() de cada uno.
        """
        total = 0.0
        for s in servicios:
            total += s.calcular_costo()
        return round(total, 2)

    @staticmethod
    def generar_reporte(servicios: List[ServicioUniversitario]) -> str:
        """
        Polimórfico: genera un reporte que usa mostrar_info() de cada servicio.
        No hace comprobaciones de tipo explícitas — demuestra polimorfismo.
        """
        lineas = []
        for s in servicios:
            lineas.append(s.mostrar_info())
        resumen = "\n".join(lineas)
        return resumen

    @staticmethod
    def filtrar_por_rango_costos(servicios: List[ServicioUniversitario], minimo: float, maximo: float):
        """Ejemplo adicional: devuelve servicios cuyo costo esté en [minimo, maximo]."""
        resultado = [s for s in servicios if minimo <= s.calcular_costo() <= maximo]
        return resultado