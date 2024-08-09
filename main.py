# Hecho con ❤ por Benjamín Ubilla

import random
from pathlib import Path

from template import (
    generar_desde_plantilla_archivo,
    encabezado_pregunta,
    encabezado_subpregunta
)
from pylatex import Document

import template


# Modificar parámetros de acuerdo a tus datos
NOMBRE: str = "Nombre"
APELLIDO: str = "Apellido"
N_ALUMNO: int = 123456789
N_TAREA: int = 1


def modificar_plantilla(doc: Document) -> None:
    # Modificar para responder las preguntas
    doc.append(encabezado_pregunta("1"))
    doc.append(encabezado_subpregunta("1", "a"))
    potencia_x = template.potencia("x", "2")
    potencia_y = template.potencia("y", "2")
    doc.append(template.ecuacion(f"{potencia_x} + {potencia_y} = 1"))
    doc.append(template.nueva_pagina())
    doc.append(encabezado_subpregunta("1", "b"))
    doc.append(template.texto(f"La ecuación de la circunferencia es: {template.ecuacion_en_linea('x^2 + y^2 = 1')}"))
    doc.append(template.nueva_pagina())
    doc.append(encabezado_pregunta("2"))
    doc.append(encabezado_subpregunta("2", "a"))
    doc.append(template.texto("Usaremos la siguiente ecuación:"))
    doc.append(template.ecuacion_numerada("x + y = 1", 1))
    doc.append(template.nueva_pagina())
    doc.append(encabezado_subpregunta("2", "b"))
    for i in range(3):
        eq = template.ecuacion_en_linea(f"{i} + 1")
        doc.append(template.texto(f"El valor de {eq} es {i + 1}."))
        doc.append(template.nueva_linea())
    doc.append(template.nueva_pagina())
    doc.append(encabezado_pregunta("3"))
    doc.append(encabezado_subpregunta("3", "a"))
    doc.append(template.texto("Miren la siguiente tabla:"))
    doc.append(template.nueva_linea())
    fraccion = template.fraccion("1", "2")
    encabezado_tabla = [template.ecuacion_en_linea("x"), template.ecuacion_en_linea(f"y={fraccion}")]
    filas = []
    for i in range(3):
        filas.append([str(random.randint(1, 10)), str(random.randint(1, 10))])
    doc.append(template.centrar(template.tabla(filas, encabezado_tabla)))
    doc.append(template.nueva_pagina())
    doc.append(encabezado_subpregunta("3", "b"))
    doc.append(template.texto("Tenemos el siguiente grafo:"))
    doc.append(template.nueva_linea())
    doc.append(template.centrar(template.grafo(
        ["A", "B", "C"], [("A", "B"), ("B", "C"), ("C", "A")],
        200,
        "grafo"
    )))


def main():
    if not Path.cwd() / "numalumno.tex":
        raise FileNotFoundError("No se encontró el archivo numalumno.tex. Asegúrate de que esté en la misma carpeta que tu archivo main.py.")
    media_folder = Path.cwd() / "media"
    media_folder.mkdir(exist_ok=True)
    tex_folder = media_folder / "Tex"
    tex_folder.mkdir(exist_ok=True)
    # NO MODIFICAR
    doc = generar_desde_plantilla_archivo(
        "numalumno.tex",
        str(N_ALUMNO),
        N_ALUMNO,
        NOMBRE,
        APELLIDO,
        N_TAREA
    )
    modificar_plantilla(doc)
    doc.generate_pdf(clean_tex=False)


if __name__ == "__main__":
    main()
