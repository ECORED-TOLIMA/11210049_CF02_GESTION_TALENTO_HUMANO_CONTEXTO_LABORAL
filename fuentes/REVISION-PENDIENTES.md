# Revisión y pendientes

Este documento recoge lo que hace falta de terceros y las decisiones que se tomaron sin una
fuente exacta, con su motivo, por si se quieren revertir.

## Lo que hace falta de terceros

Tres cosas que no dependen de la maqueta: no están ni en el `.xd` ni en los documentos, y hay
que pedirlas. Mientras tanto cada una tiene puesto un sustituto que deja el curso funcionando.

| Qué falta                             | Dónde va             | Qué hay puesto mientras tanto              |
| ------------------------------------- | -------------------- | ------------------------------------------ |
| **La URL del vídeo**                  | Introducción         | el `iframe` de ejemplo del scaffold        |
| **El audio del pódcast**              | Tema 4, apartado 4.1 | un MP3 mudo de 3 minutos, `t4/podcast.mp3` |
| **Las diez imágenes de la actividad** | Actividad didáctica  | diez composiciones propias, ver el punto 4 |

Ninguna afecta a la maquetación: se sustituye el archivo y ya está.

## 1. Falta la URL del vídeo de la Introducción

El `.xd` deja el espacio marcado con el rótulo «Espacio para vídeo» y un rect de 1228x580 en
`#265D99`, y el `_DI.docx` nombra el guion (`11210049_CF02_Guion_video_introduccion.docx`) pero
no trae el enlace. Se deja el `iframe` de ejemplo que venía en la plantilla hasta que llegue la
URL real.

## 2. Falta el audio del pódcast del 4.1

El `_DI.docx` nombra el guion (`11210049_CF02_Guion_podcast`) y el `.xd` dibuja la barra del
reproductor con su texto («Comunicación asertiva: decir lo que se piensa sin herir ni callar»),
pero no hay archivo de audio. Se genera un **MP3 mudo de 3 minutos** para que el reproductor
funcione y se reemplaza por el audio real cuando llegue.

## 3. Aplicado del `.xd` y el PDF nuevos

El `.xd` del 2026-08-26 mueve y reescribe contenido del Tema 1. Comparando texto a texto contra
la maqueta:

- «Estas cinco funciones no actúan de manera independiente…» **cambia de sitio**: estaba en la
  caja del 1.2 y ahora va en el 1.1 (`y=3662`), en la caja de 812x160 que acompaña a la foto de
  396x257. Movida.
- El párrafo que se repetía dos veces («El siguiente caso ilustra…») ya sólo aparece una vez, en
  `y=3829`. Queda dentro de esa misma columna, delante del caso que presenta.
- **Dos párrafos nuevos** en el 1.2, los dos maquetados: «En las organizaciones se distingue, de
  manera general, entre comunicación verbal y comunicación no verbal…» (dentro de la caja con
  icono) y «La comunicación verbal comprende los mensajes expresados mediante palabras…» (debajo).
- La fila de `y=2735` llevaba la foto equivocada: son 292x251 (col-3) con la caja de 916 a la
  derecha (col-9), no 396x257 con una caja de 812.

## 4. Las imágenes de la actividad didáctica

La actividad **no tiene artboard en el `.xd`**, así que sus imágenes no se pueden medir contra
ningún diseño. La plantilla traía diez archivos de otro curso (fotografías de electrónica, y
sólo cuatro distintas repetidas), que no sirven.

Se componen diez imágenes nuevas de **396 x 396**, una por cada pregunta que muestra el
componente, en el lenguaje visual de este curso: fotografía del propio `.xd` recortada dentro de
un arco sobre `#CBD5FF`, que es el tratamiento que usa la portada. **Son un sustituto**: las
definitivas las aporta el diseñador.

Dato del componente: el `_AD.docx` trae un banco de **20 preguntas** y el kit muestra **10**, por
lo que `barajarPreguntas` va en `true` y hacen falta diez imágenes distintas, no menos.

## 5. Encabezado de la actividad

El `_AD.docx` da como «Nombre de la Actividad» un título largo («Diálogo y colaboración:
comunicación efectiva en la gestión del talento humano») y unas «Instrucciones para el aprendiz»
de tres párrafos. El encabezado del componente **no los lleva**: el título es `Cuestionario` y la
introducción, sólo el objetivo. El resto del documento sí se transcribe entero (las 20 preguntas,
sus 80 opciones, las retroalimentaciones y los dos mensajes finales).

## 6. Contenido que el PDF muestra y no pertenece al diseño

En la página del Tema 3, el PDF pinta una miniatura de la Figura 1 encima del texto, hacia la
mitad del 3.1. Ese elemento **no está en el artboard**: es contenido del pasteboard que se coló
al exportar el PDF, así que no se ha maquetado. La versión buena es la Figura 1, que sí está en
su sitio con su título y su versión móvil.

## 7. Decisiones de color que no salen de la ficha automática

Tres casos en los que la ficha y el dibujo no coinciden, resueltos **muestreando el píxel del
PDF**, que es lo que se ve:

- **La cuarta tarjeta de las estrategias del 2.4 no es una tarjeta más: es el estado _hover_.**
  La ficha daba círculos alternos `#003CE1`/`#FAFBFF`; el PDF da tres tarjetas `#E5EBFC` con el
  círculo en `#003CE1` y una cuarta en `#F7E3E6` con el círculo en `#5E4A4D`. Se maquetan cuatro
  tarjetas iguales y el cuarto icono se genera intercambiando el color del círculo, que es lo
  único que cambia entre los dos estados.
- **La viñeta cuadrada de las listas numeradas** lleva el número en `#12263F` y en negrilla, no
  en blanco como lo pinta el componente. El fondo, `#CBD5FF`, ya era el correcto.
- **La viñeta de las listas con icono** es el `circle-right` de Font Awesome —el pasteboard deja
  escrita la URL del icono— relleno en `#474A59`.

## 8. Ajustes sobre lo que traía la plantilla

- El scaffold venía con `Tema1`, `Tema2` y `Tema3` y **sin `Tema4.vue`**. Al referenciarlo el
  menú, la portada entera fallaba con «No match for». Creada la vista y su ruta.
- El texto del banner de portada venía en blanco; con esta paleta va en `#12263F`.
- El componente de pestañas marca la activa con un borde **superior** y el diseño pone la línea
  de 340x5 en el **borde inferior** (pestaña en `y=3296..3361`, línea en `y=3361`).
- Los botones adelante/atrás del slider: el componente los deja blancos, con borde y al 70 % de
  opacidad; el diseño los quiere como círculos rellenos de 50 px en `#003CE1`, opacos, a 23 px
  de los lados y 24 px por encima del borde inferior de la tarjeta.
- Las pestañas inactivas del 4.1: el componente usa `#F6F6F6` y el diseño `#E5EBFC`.

## 9. Revisión final

Las cinco comprobaciones que se ejecutan al cerrar, con lo que dieron:

1. **Colores de los fondos.** Cada caja con fondo del render contra los `fill` del `.xd`:
   **ningún color inventado** en las cinco pantallas medibles.
2. **Distribución de los elementos y los textos.** Todos los textos del artboard están en la
   página: 83 de 84 en el tema 1, 79 de 80 en el 2, 94 de 104 en el 3 y 56 de 60 en el 4. Lo que
   no aparece es, en todos los casos, el rótulo de plantilla «Manual de Componentes para
   Diseñadores Instruccionales», los textos que van **dentro** de la Figura 1 (son parte de la
   imagen) y los de las pestañas cerradas del 4.1 (se leen al abrirlas). De los anchos quedan
   avisos de 13 a 41 px, todos por debajo de una columna (102 px), en bloques cuyo `col-lg-N` es
   el que da la regla `round(ancho / 1228 × 12)`.
3. **Iconos de las tarjetas.** Los 40 iconos de tarjeta correlacionados contra el recorte del PDF
   en la posición de la que se exportaron: **34 por encima de 0,95** y los seis restantes
   (0,84-0,95) revisados a mano, son el mismo icono y la misma orientación; la correlación baja
   por el color de la tarjeta que queda detrás del círculo.
4. **Botones adelante y atrás del slider.** Círculos de 50 px en `#003CE1`, opacos, a 23 px del
   borde derecho y 24 px del inferior, en los dos sliders del curso. Las flechas de los
   carruseles de tarjetas van en el mismo azul.
5. **Animaciones de los iconos de la portada.** Los dos distintivos ejecutan `float1`, infinito y
   alterno, a **2,8 s y 2,5 s** — tiempos distintos, como pide la nota del pasteboard.

Además: **0 desbordes horizontales a 360 px** en las once rutas, ninguna vista rota, ningún
elemento que se quede sin animar y ningún icono repetido dentro de un mismo tema.

**Revisiones pendientes**

- valida el pdf y el xd que tienen algunos cambios.
- Revisa el background de las tarjetas que inician con este texto "Condiciones físicas, culturales, históricas y relacionales en las que se produce el intercambio comunicativo. El contexto determina el significado de los mensajes: una misma expresión puede interpretarse de manera distinta según el ambiente, la jerarquía o el momento en que se emite." ya que es una imagen png con diseño.
- recuerda que siempre antes de un titulo segundo sin excepcion va un separador asi:
  separador
  #t_1_1.titulo-segundo.color-acento-contenido
  h2 1.1 Fundamentos de la comunicación
- Recuerda siempre revisar los colores de los bullets de los sliders.
- Revisar el componente que inicia en: "Reuniones de resultados: espacio para compartir cifras de desempeño y, al mismo tiempo, reconocer el trabajo del equipo en un solo mensaje." ya que recuerda que todas las viñetas que tengan salto de linea deben iniciar sin excepcion debajo de la primer letra de la primera fila.
- En ese mismo componente revisa la imagen que la exportaste sin el fondo.
- Revisa todos los temas que al parecer te falta texto. Revisa nuevamente el XD, el pdf y el di.

## 10. Correcciones aplicadas de la revisión

- **Separador antes de cada título segundo, sin excepción.** Añadido en los 15 del curso.
- **Las tarjetas de los carruseles no son un color plano.** El diseño les pone dos adornos
  recortados por la propia tarjeta: un rayado de 125x45 arriba a la derecha, que se sale 30 px, y
  una espiral de 68x69 abajo a la izquierda, que se sale 25 px. Se aplican con la clase
  `.tarjeta--adornos` en las 22 tarjetas de carrusel, en porcentajes medidos sobre la tarjeta de
  327x435 del Tema 1, para que acompañen a cualquier tamaño.
- **Viñetas de los sliders.** El componente deja la activa en gris y las demás en blanco con
  borde. El píxel del PDF las da al revés de lo esperable: la **activa en `#FEDDB4`** y las
  inactivas **rellenas en `#003CE1`**.
- **Sangría francesa en las viñetas.** Cuando el texto de un `li` salta de línea, la segunda
  empieza ahora debajo de la primera letra de la primera, no debajo de la viñeta. Además, el
  texto de las listas numeradas iba en un `p` (bloque), que echaba el número a su propia línea:
  ahora va en línea, como en el diseño.
- **La foto del 1.1 estaba exportada sin fondo.** El recorte salía sólo con la persona; el diseño
  la pone sobre un arco de `#EBB9C1` de 273x387. Reexportada con él.

**Revision Final ten en cuenta que ya corregimos los errores la idea es que valides y aprendas.**
-Siempre sin excepcion debes validar si las imagenes son con las esquinas en punta o redondas.
-Siempre sin excepcion validar la distribucion de los textos segun el xd.
-Siempre sin excepcion, validar si cada imagen si viene con su fondo como esta en el xd
-Validar la construccion de los podcast, estas usando colores que no son.
