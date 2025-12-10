# Integrantes:
# - Crespo John
# - Danna Rodriguez
# - Genesis Garboa
# -Alvarado

print("\n")
print("=" *120)
from CursoPresencial import CursoPresencial # Clase para cursos presenciales (hereda de Servicio)
from CursoVirtual import CursoVirtual  # Clase para cursos virtuales (hereda de Servicio)
from Estudiante  import Estudiante  # Clase para manejar información de estudiantes
from GestorServicios import GestorServicios
from datetime import datetime

#Aquí la función para que se pueda ejecutar

def main():
    # Crear estudiantes (ejemplo)
    est1 = Estudiante("0945352819", "Jhon Crespo", "ana.perez@example.com")
    est2 = Estudiante("0954692904", "Génesis Garboa", "c.ruiz@example.com")

    # Crear servicios (cursos),#Creamos 2 cursos prenciales eje.
    curso1 = CursoPresencial(
        codigo="P001",
        nombre="Matemáticas I",
        duracion_horas=40,
        costo_base=120.0,
        costo_materiales=15.0,
        cuota_infraestructura=10.0
    )

    curso2 = CursoPresencial(
        codigo="P002",
        nombre="Laboratorio de Física",
        duracion_horas=30,
        costo_base=100.0,
        costo_materiales=25.0,
        cuota_infraestructura=20.0
    )

#Creación de 2 cursos virtuales eje.
    curso3 = CursoVirtual(
        codigo="V101",
        nombre="Introducción a Python",
        duracion_horas=25,
        costo_base=80.0,
        tarifa_plataforma=5.0,
        descuento_percent=10.0
    )

    curso4 = CursoVirtual(
        codigo="V102",
        nombre="Historia del Arte (Online)",
        duracion_horas=20,
        costo_base=60.0,
        tarifa_plataforma=3.0,
        descuento_percent=0.0
    )
    # Guardar en lista de la superclase
    servicios = [curso1, curso2, curso3, curso4]

    # Mostrar __str__ de cada objeto
    print("------------ LISTA DE SERVICIOS (STR) ------------")
    for s in servicios:
        print(s)

    # Usar GestorServicios (polimorfismo)
    gestor = GestorServicios()
    print("=" * 120)
    print("\n------------ REPORTE GENERADO (polimórfico) ------------")
    print(gestor.generar_reporte(servicios))

    total = gestor.sumar_costos(servicios)
    print(f"\nCosto total de todos los cursos: ${total:.2f}")
    print("=" * 120)

    # Filtrar ejemplo
    filtrados = gestor.filtrar_por_rango_costos(servicios, minimo=50, maximo=130)
    print("\n=== CURSOS CON COSTO ENTRE $50 Y $130 ===")
    for f in filtrados:
        print(f.mostrar_info())

    # Evidencia de cuando y a que hora ejecutamos el programa
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nEVIDENCIA: Ejecución Realizada el {ahora}")
    print("=" * 120)

if __name__ == "__main__":
    main()