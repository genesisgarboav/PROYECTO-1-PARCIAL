# Integrantes:
# - Crespo John
# - Danna Rodriguez
# - Genesis Garboa
# -Alvarado

class Estudiante:
    """
    Representa un estudiante que puede inscribirse a cursos.
    """

    def __init__(self, identificacion: str, nombre_completo: str, correo: str):
        self._identificacion = None
        self._nombre_completo = None
        self._correo = None

        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.correo = correo

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @identificacion.setter
    def identificacion(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("identificacion debe ser un string no vacío.")
        self._identificacion = value.strip()

    @property
    def nombre_completo(self) -> str:
        return self._nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("nombre_completo debe ser un string no vacío.")
        self._nombre_completo = value.strip()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, value: str):
        if not isinstance(value, str) or "@" not in value:
            raise ValueError("correo debe ser un email válido.")
        self._correo = value.strip()

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre_completo} <{self.correo}>"