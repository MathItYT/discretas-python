# Tareas de Matemáticas Discretas en Python
¡Ahora puedes editar la plantilla de tu tarea del ramo IIC1253 con Python, sin usar ni un solo código de LaTeX! Cualquier duda que tengas, abre una *issue*.

## Instalación en Windows
- [Git](https://git-scm.com/download/win)
- [Visual Studio Code](https://code.visualstudio.com/)
- [MiKTeX](https://miktex.org/)
- [Python](https://www.python.org/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
- [Manim](https://docs.manim.community/en/stable/installation/windows.html)
- Manim Mobject SVG. Para instalar esto, debes abrir tu terminal y pegar el comando `pip install manim-mobject-svg` y luego dar `Enter` para correr el comando.
- PyLaTeX. Para instalar esto, debes abrir tu terminal y pegar el comando `pip install PyLaTeX` y luego dar `Enter` para correr el comando.

## Instalación en MacOS
- [Git](https://git-scm.com/download/mac)
- [Visual Studio Code](https://code.visualstudio.com/)
- [MacTeX](https://www.tug.org/mactex/mainpage2024.html)
- [Python](https://www.python.org/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
- [Manim](https://docs.manim.community/en/stable/installation/macos.html)
- Manim Mobject SVG. Para instalar esto, deberás abrir tu terminal y pegar el comando `pip3 install manim-mobject-svg` y luego dar `Enter` para correr el comando.
- PyLaTeX. Para instalar esto, deberás abrir tu terminal y pegar el comando `pip3 install PyLaTeX` y luego dar `Enter` para correr el comando.

## Instalación en Linux o Unix
- [Git](https://git-scm.com/download/linux)
- [Visual Studio Code](https://code.visualstudio.com/)
- TeX Live. La guía oficial de instalación no es muy clara y son demasiadas distros. La guía está en [esta *issue*](https://github.com/MathItYT/discretas-python/issues/1), y si falta tu distro, **comenta la *issue*** .
- [Python](https://www.python.org/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
- [Manim](https://docs.manim.community/en/stable/installation/linux.html)
- Manim Mobject SVG. Para instalar esto, deberás abrir tu terminal y pegar el comando `pip3 install manim-mobject-svg` y luego dar `Enter` para correr el comando.
- PyLaTeX. Para instalar esto, deberás abrir tu terminal y pegar el comando `pip3 install PyLaTeX` y luego dar `Enter` para correr el comando.

## Uso

Clona este repositorio abriendo tu terminal y pega el siguiente comando, luego dale `Enter` para correrlo:

```bash
git clone https://github.com/MathItYT/discretas-python.git
```

Luego, inicializa tu entorno virtual con el siguiente comando, luego dale `Enter` para correrlo:

```bash
virtualenv .venv
```

Después, activa tu entorno virtual con el siguiente comando, luego dale `Enter` para correrlo:

```bash
# Windows
.\.venv\Scripts\Activate.ps1
# MacOS o Linux
source .venv/bin/activate
```

Luego, en Visual Studio Code, abre la carpeta `discretas-python` y edita el archivo `main.py` con tus tareas. **No edites otra cosa aparte de la función `modificar_plantilla` y los parámetros indicados ahí mismo según tus datos.**.

Para compilar tu tarea, abre tu terminal y pega el siguiente comando, luego dale `Enter` para correrlo:

```bash
# Windows
python main.py
# MacOS o Linux
python3 main.py
```

Si todo sale bien, se generará un archivo PDF llamado `<N_ALUMNO>.tex` carpeta y el PDF `<N_ALUMNO>.pdf` en la misma carpeta que abriste en Visual Studio Code.

## Funciones incluidas en `template.py` para usar
- `encabezado_pregunta`: Genera el encabezado de la pregunta. Recibe un `str` con el número de la pregunta.

- `encabezado_subpregunta`: Genera el encabezado de la subpregunta. Recibe dos `str`, el número de la pregunta y el número (o letra) de la subpregunta.

- `texto`: Genera un texto normal. Recibe un `str` con el texto.

- `texto_en_negrita`: Genera un texto en negrita. Recibe un `str` con el texto.

- `texto_en_cursiva`: Genera un texto en cursiva. Recibe un `str` con el texto.

- `texto_en_negrita_y_cursiva`: Genera un texto en negrita y cursiva. Recibe un `str` con el texto.

- `imagen`: Genera una imagen. Recibe un `str` con la ruta de la imagen y un `float` con la altura de la imagen en pixeles.

- `ecuacion`: Genera una ecuación. Recibe un `str` con la ecuación en LaTeX.

- `ecuacion_en_linea`: Genera una ecuación para ponerla junto con el texto. Recibe un `str` con la ecuación en LaTeX.

- `ecuacion_numerada`: Genera una ecuación numerada, para poder mencionarla con su número. Recibe un `str` con la ecuación en LaTeX y un `int` con el número de la ecuación.

- `centrar`: Centra el contenido. Recibe una cantidad indefinida de argumentos `str`, los cuales serán centrados.

- `texto_plano`: Genera un texto plano, que se coloca en medio de una ecuación. Recibe un `str` con el texto.

- `tabla`: Genera una tabla. Recibe un `list` de `list` con los datos de la tabla y un `list` de `str` con los encabezados de la tabla. Los encabezados si son `None`, no se mostrarán.

- `nueva_linea`: Genera una nueva línea.

- `salto_de_pagina`: Genera un salto de página. Recuerda siempre incluir esto cada vez que quieras responder una nueva pregunta.

- `fraccion`: Genera una fracción. Recibe dos `str`, el numerador y el denominador.

- `sumatoria`: Genera una sumatoria. Recibe un `str` con el inicio, un `str` con el fin y un `str` con la función a sumar.

- `producto`: Genera un producto iterado. Recibe un `str` con el inicio, un `str` con el fin y un `str` con la función a multiplicar.

- `conjuncion_iterada`: Genera una conjunción iterada, como una sumatoria, pero con el símbolo de conjunción. Recibe un `str` con el inicio, un `str` con el fin y un `str` con la función a conjugar.

- `disyuncion_iterada`: Genera una disyunción iterada, como una sumatoria, pero con el símbolo de disyunción. Recibe un `str` con el inicio, un `str` con el fin y un `str` con la función a disyuntar.

- `union_iterada`: Genera una unión iterada, como una sumatoria, pero con el símbolo de unión. Recibe un `str` con el inicio, un `str` con el fin y un `str` con la función a unir.

- `interseccion_iterada`: Genera una intersección iterada, como una sumatoria, pero con el símbolo de intersección. Recibe un `str` con el inicio, un `str` con el fin y un `str` con la función a intersecar.

- `conjuncion`: Genera una conjunción. Recibe varios `str` con las proposiciones para hacer la conjunción.

- `disyuncion`: Genera una disyunción. Recibe varios `str` con las proposiciones para hacer la disyunción.

- `implicancia`: Genera una implicancia. Recibe dos `str`, la proposición antecedente y la proposición consecuente.

- `negacion`: Genera una negación. Recibe un `str` con la proposición a negar.

- `cuantificador_universal`: Genera un cuantificador universal. Recibe un `str` con la variable cuantificada, otro `str` con el conjunto donde se cuantifica y un `str` con la proposición cuantificada.

- `cuantificador_existencial`: Genera un cuantificador existencial. Recibe un `str` con la variable cuantificada, otro `str` con el conjunto donde se cuantifica y un `str` con la proposición cuantificada.

- `cuantificador_existencial_unico`: Genera un cuantificador existencial único. Recibe un `str` con la variable cuantificada, otro `str` con el conjunto donde se cuantifica y un `str` con la proposición cuantificada.

- `union`: Genera una unión. Recibe varios `str` con los conjuntos a unir.

- `interseccion`: Genera una intersección. Recibe varios `str` con los conjuntos a intersectar.

- `raiz`: Genera una raíz. Recibe un `str` con el índice y otro `str` con el radicando.

- `factorial`: Genera un factorial. Recibe un `str` con el número a sacar el factorial.

- `raiz_cuadrada`: Genera una raíz cuadrada. Recibe un `str` con el radicando.

- `potencia`: Genera una potencia. Recibe un `str` con la base y otro `str` con el exponente.

- `parentesis`: Genera un paréntesis. Recibe un `str` con el contenido de los paréntesis.

- `corchetes`: Genera corchetes. Recibe un `str` con el contenido de los corchetes.

- `llaves`: Genera llaves. Recibe un `str` con el contenido de las llaves.

- `valor_absoluto`: Genera un valor absoluto. Recibe un `str` con el contenido del valor absoluto.

- `congruencia_modulo`: Genera una equivalencia módulo. Recibe tres `str`, el primer número, el segundo número y el módulo.

- `subindice`: Genera un subíndice. Recibe dos `str`, el texto base y el texto subíndice.

- `log`: Genera un logaritmo. Recibe dos `str`, la base y el argumento.

- `ln`: Genera un logaritmo natural. Recibe un `str` con el argumento.

- `log2`: Genera un logaritmo en base 2. Recibe un `str` con el argumento.

- `log_sin_base`: Genera un logaritmo sin base. Recibe un `str` con la base.

- `grafo`: Genera la imagen de un grafo. Recibe un `list` de `str` con los nodos y un `list` de `tuple` de dos `str` con las aristas, un `float` con la altura de la imagen en pixeles y un `str` con el nombre de la imagen, sin la extensión. Opcionalmente, puedes pasarle un `float` con el padding de la imagen, que por defecto es `2.0`.
