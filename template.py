import re
from copy import deepcopy
from contextlib import contextmanager
from typing import Generator
from pathlib import Path

from pylatex import (
    Document,
    Command,
    NoEscape
)
from pylatex import utils

import cairo

import manim as mn

from manim_mobject_svg import svg as pdf


@contextmanager
def get_cairo_context(
    file_name: str | Path,
    width: int = None,
    height: int = None,
) -> Generator[cairo.Context, None, None]:
    from manim import config

    pw = config.pixel_width
    ph = config.pixel_height
    fw = config.frame_width
    fh = config.frame_height
    if width and height:
        pw = int(width * pw / fw)
        ph = int(height * ph / fh)
        fw = width
        fh = height

    fc = [0, 0]
    surface = cairo.PDFSurface(
        file_name,
        pw,
        ph,
    )
    ctx = cairo.Context(surface)
    ctx.scale(pw, ph)
    ctx.set_matrix(
        cairo.Matrix(
            (pw / fw),
            0,
            0,
            -(ph / fh),
            (pw / 2) - fc[0] * (pw / fw),
            (ph / 2) + fc[1] * (ph / fh),
        ),
    )
    yield ctx
    surface.finish()


pdf._get_cairo_context = get_cairo_context


old_dumps_list = deepcopy(utils.dumps_list)


def dumps_list(l, *, escape=True, token="\n", mapper=None, as_content=True) -> NoEscape:
    return old_dumps_list(l, escape=escape, token=token, mapper=mapper, as_content=as_content)


utils.dumps_list = dumps_list
Document.content_separator = "\n"


def dumps(doc: Document) -> str:
    return "\n".join([
        doc.documentclass.dumps(),
        dumps_list(doc.preamble),
        super(Document, doc).dumps(),
    ])


Document.dumps = dumps


def generar_desde_plantilla(
    s: str,
    archivo: str,
    n_alumno: int,
    nombre: str,
    apellido: str,
    n_tarea: int
) -> Document:
    lines = s.splitlines()
    doc_class_wo_options_regex = r"\\documentclass\{(.*)\}"
    doc_class_with_options_regex = r"\\documentclass\[(.*)\]\{(.*)\}"
    package_wo_options_regex = r"\\usepackage\{(.*)\}"
    package_with_options_regex = r"\\usepackage\[(.*)\]\{(.*)\}"
    length_regex = r"\\setlength\{(.*)\}\{(.*)\}"
    page_style_regex = r"\\pagestyle\{(.*)\}"
    new_command_regex = r"\\newcommand\{(.*)\}\{(.*)\}"
    new_command_with_options_regex = r"\\newcommand\{(.*)\}\[(.*)\]\{(.*)\}"
    renew_command_regex = r"\\renewcommand\{(.*)\}\{(.*)\}"
    renew_command_with_options_regex = r"\\renewcommand\{(.*)\}\[(.*)\]\{(.*)\}"
    rhead_regex = r"\\rhead\{(.*)\}"
    doc: Document | None = None
    is_in_document: bool = False
    for line in lines:
        result_wo_options = re.match(doc_class_wo_options_regex, line)
        result_with_options = re.match(doc_class_with_options_regex, line)
        if result_wo_options:
            doc = Document(
                default_filepath=archivo,
                documentclass=result_wo_options.group(1),
                fontenc=None,
                inputenc=None,
                textcomp=False,
                microtype=None,
                page_numbers=False,
                geometry_options=None,
                lmodern=False,
                indent=False
            )
        elif result_with_options:
            options = [option.strip() for option in result_with_options.group(1).split(",")]
            doc = Document(
                default_filepath=archivo,
                documentclass=result_with_options.group(2),
                document_options=options,
                fontenc=None,
                inputenc=None,
                textcomp=False,
                microtype=None,
                geometry_options=None,
                lmodern=False,
                indent=False
            )
        elif line == "\\newcommand{\\alumno}{Nombre Apellido - 10000001}":
            doc.preamble.append(NoEscape(f"\\newcommand{{\\alumno}}{{{nombre} {apellido} - {n_alumno}}}"))
        elif line == "{\\huge\\bf Tarea N}\\\\":
            doc.append(NoEscape(f"{{\\huge\\bf Tarea {n_tarea}}}\\\\"))
        elif line == "\\rhead{Tarea N - \\alumno}":
            doc.preamble.append(NoEscape(f"\\rhead{{Tarea {n_tarea} - \\alumno}}"))
        elif "Pregunta 1" in line or "Pregunta 2" in line:
            continue
        elif line.startswith("%"):
            continue
        elif line == "\\newpage":
            continue
        elif re.match(package_wo_options_regex, line):
            doc.preamble.append(NoEscape(line))
        elif re.match(package_with_options_regex, line):
            doc.preamble.append(NoEscape(line))
        elif re.match(length_regex, line):
            doc.preamble.append(NoEscape(line))
        elif re.match(page_style_regex, line):
            page_style = re.match(page_style_regex, line).group(1)
            doc.preamble.append(Command(command="pagestyle", arguments=page_style))
        elif re.match(new_command_regex, line):
            doc.preamble.append(NoEscape(line))
        elif re.match(renew_command_regex, line):
            doc.preamble.append(NoEscape(line))
        elif re.match(new_command_with_options_regex, line):
            doc.preamble.append(NoEscape(line))
        elif re.match(renew_command_with_options_regex, line):
            doc.preamble.append(NoEscape(line))
        elif re.match(rhead_regex, line):
            doc.preamble.append(NoEscape(line))
        elif line == "\\begin{document}":
            is_in_document = True
            continue
        elif line == "\\end{document}":
            continue
        elif doc is not None:
            if is_in_document:
                doc.append(NoEscape(line))
                continue
            doc.preamble.append(NoEscape(line))
    return doc


def generar_desde_plantilla_archivo(
    input_file_name: str,
    output_file_name: str,
    n_alumno: int,
    nombre: str,
    apellido: str,
    n_tarea: int
) -> Document:
    with open(input_file_name, "r", encoding="utf-8") as f:
        return generar_desde_plantilla(
            f.read(),
            output_file_name,
            n_alumno,
            nombre,
            apellido,
            n_tarea
        )


# Funciones para agregar contenido a un documento LaTeX


def encabezado_pregunta(
    pregunta: str
) -> NoEscape:
    return NoEscape(f"\\subsection*{{Pregunta {pregunta}}}")


def encabezado_subpregunta(
    pregunta: str,
    subpregunta: str
) -> NoEscape:
    return NoEscape(f"\\subsubsection*{{Pregunta {pregunta}.{subpregunta}}}")


def texto(
    texto: str
) -> NoEscape:
    return NoEscape(texto)


def texto_en_negrita(
    texto: str
) -> str:
    return f"\\textbf{{{texto}}}"


def texto_en_cursiva(
    texto: str
) -> str:
    return f"\\textit{{{texto}}}"


def texto_en_negrita_y_cursiva(
    texto: str
) -> str:
    return f"\\textbf{{\\textit{{{texto}}}}}"


def imagen(
    ruta: str,
    alto_en_px: int,
) -> NoEscape:
    return NoEscape(f"\\includegraphics[height={alto_en_px}px]{{{ruta}}}")


def ecuacion(
    texto: str
) -> NoEscape:
    return NoEscape(f"\\[\n{texto}\n\\]")


def ecuacion_en_linea(
    texto: str
) -> str:
    return f"\\(\\displaystyle {texto}\\)"


def ecuacion_numerada(
    texto: str,
    numero: int
) -> NoEscape:
    return NoEscape(f"\\[\n{texto}\n\\tag{{{numero}}}\\]")


def centrar(
    *contenido: str
) -> NoEscape:
    contenido = "\n".join(contenido)
    return NoEscape(f"\\begin{{center}}\n{contenido}\n\\end{{center}}")


def texto_plano(
    texto: str
) -> str:
    return f"\\text{{{texto}}}"


def tabla(
    filas: list[list[str]],
    encabezados: list[str] | None = None
) -> NoEscape:
    if encabezados is not None:
        return NoEscape(f"\\begin{{tabular}}{{{'|'.join(['c'] * len(encabezados))}}}\n" +
                        " & ".join(encabezados) + "\\\\\n" +
                        "\\hline\n" +
                        "\n".join([" & ".join(fila) + "\\\\" for fila in filas]) +
                        "\n\\end{tabular}")
    return NoEscape(f"\\begin{{tabular}}{{{'|'.join(['c'] * len(filas[0]))}}}\n" +
                    "\n".join([" & ".join(fila) + "\\\\" for fila in filas]) +
                    "\n\\end{tabular}")


def nueva_linea() -> NoEscape:
    return NoEscape("\\\\")


def nueva_pagina() -> NoEscape:
    return NoEscape("\\newpage")


def fraccion(
    numerador: str,
    denominador: str
) -> str:
    return f"\\frac{{{numerador}}}{{{denominador}}}"


def sumatoria(
    inicio: str,
    fin: str,
    funcion: str
) -> str:
    return f"\\sum_{{{inicio}}}^{{{fin}}}{funcion}"


def producto(
    inicio: str,
    fin: str,
    funcion: str
) -> str:
    return f"\\prod_{{{inicio}}}^{{{fin}}}{funcion}"


def conjuncion_iterada(
    inicio: str,
    fin: str,
    funcion: str
) -> str:
    return f"\\bigwedge_{{{inicio}}}^{{{fin}}}{funcion}"


def disyuncion_iterada(
    inicio: str,
    fin: str,
    funcion: str
) -> str:
    return f"\\bigvee_{{{inicio}}}^{{{fin}}}{funcion}"


def union_iterada(
    inicio: str,
    fin: str,
    funcion: str
) -> str:
    return f"\\bigcup_{{{inicio}}}^{{{fin}}}{funcion}"


def interseccion_iterada(
    inicio: str,
    fin: str,
    funcion: str
) -> str:
    return f"\\bigcap_{{{inicio}}}^{{{fin}}}{funcion}"


def conjuncion(
    *proposiciones: str
) -> str:
    return " \\land ".join(proposiciones)


def disyuncion(
    *proposiciones: str
) -> str:
    return " \\lor ".join(proposiciones)


def implicancia(
    antecedente: str,
    consecuente: str
) -> str:
    return f"{antecedente} \\Rightarrow {consecuente}"


def bicondicional(
    antecedente: str,
    consecuente: str
) -> str:
    return f"{antecedente} \\Leftrightarrow {consecuente}"


def negacion(
    proposicion: str
) -> str:
    return f"\\neg {proposicion}"


def cuantificador_universal(
    variable: str,
    conjunto: str,
    proposicion: str
) -> str:
    return f"\\forall {variable} \\in {conjunto}, {proposicion}"


def cuantificador_existencial(
    variable: str,
    conjunto: str,
    proposicion: str
) -> str:
    return f"\\exists {variable} \\in {conjunto}, {proposicion}"


def cuantificador_existencial_unico(
    variable: str,
    conjunto: str,
    proposicion: str
) -> str:
    return f"\\exists! {variable} \\in {conjunto}, {proposicion}"


def union(
    *conjuntos: str
) -> str:
    return " \\cup ".join(conjuntos)


def interseccion(
    *conjuntos: str
) -> str:
    return " \\cap ".join(conjuntos)


def raiz(
    indice: str,
    radicando: str
) -> str:
    return f"\\sqrt[{indice}]{{{radicando}}}"


def factorial(
    n: str
) -> str:
    return f"{n}!"


def raiz_cuadrada(
    radicando: str
) -> str:
    return f"\\sqrt{{{radicando}}}"


def potencia(
    base: str,
    exponente: str
) -> str:
    return f"{base}^{{{exponente}}}"


def parentesis(
    contenido: str
) -> str:
    return f"\\left({contenido}\\right)"


def corchetes(
    contenido: str
) -> str:
    return f"\\left[{contenido}\\right]"


def llaves(
    contenido: str
) -> str:
    return f"\\left\\{{{contenido}\\right\\}}"


def valor_absoluto(
    contenido: str
) -> str:
    return f"\\left|{contenido}\\right|"


def congruencia_modulo(
    a: str,
    b: str,
    n: str
) -> str:
    return f"{a} \\equiv_{{{n}}} {b}"


def subindice(
    base: str,
    subindice: str
) -> str:
    return f"{base}_{{{subindice}}}"


def log(
    base: str,
    argumento: str
) -> str:
    return f"\\log_{{{base}}}({argumento})"


def ln(
    argumento: str
) -> str:
    return f"\\ln({argumento})"


def log2(
    argumento: str
) -> str:
    return f"\\log_2({argumento})"


def log_sin_base(
    argumento: str
) -> str:
    return f"\\log({argumento})"


def grafo(
    vertices: list[str],
    aristas: list[tuple[str, str]],
    altura_imagen_en_pixeles: int,
    nombre_archivo_sin_extension: str,
    padding: float = 2.0
) -> NoEscape:
    g = mn.Graph(
        vertices=vertices,
        edges=aristas,
        labels=True,
        vertex_config={
            "stroke_color": mn.BLACK,
            "stroke_width": 2.0
        },
        edge_config={
            "stroke_color": mn.BLACK,
            "stroke_width": 2.0
        }
    )
    pdf.create_svg_from_vmobject(
        g,
        f"{nombre_archivo_sin_extension}.pdf",
        crop=True,
        padding=padding
    )
    return NoEscape(f"\\includegraphics[height={altura_imagen_en_pixeles}px]{{{nombre_archivo_sin_extension}.pdf}}")

