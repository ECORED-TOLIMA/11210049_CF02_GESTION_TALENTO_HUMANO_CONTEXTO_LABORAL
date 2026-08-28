<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 1
      h1 Comunicación en el entorno organizacional

    //- Caja #F7E3E6 de 916x170 con r=10 (col-9) y la foto de 292x292 SIN radio pegada al
    //- borde derecho, x=1121 (col-3).
    .row
      .col-lg-9
        .bg-2.r-10.p-4(data-aos="fade-right")
          p.mb-0 Se trata del conjunto de procesos mediante los cuales fluye la información entre los integrantes de una organización y el entorno en el que se desarrolla, con el propósito de coordinar acciones, construir significados compartidos y orientar el comportamiento colectivo hacia el logro de los objetivos institucionales. Más allá de la simple transmisión de datos, este proceso implica la interpretación, la negociación de sentidos, la gestión de percepciones y la construcción de relaciones de confianza entre los diferentes actores que participan en él.

        p.mt-4(data-aos="fade-right") En la gestión de personas, la comunicación no solo transmite instrucciones o reportes, sino que se convierte en un recurso estratégico que permite alinear expectativas, clarificar roles, retroalimentar desempeños, gestionar emociones colectivas y sostener la cultura organizacional en el tiempo. Por ello, quien gestiona personas requiere comprender la comunicación como un proceso complejo, sistémico y bidireccional, en el que intervienen múltiples factores como:

      .col-lg-3.mt-4.mt-lg-0
        figure.mb-0
          img(src="@/assets/curso/temas/t1/foto-1.png" ).w-100

    //- Seis factores, de tres en tres: `SlyderF` con la banda decorativa de 1328x254 detrás,
    //- que se sale del padding de la tarjeta (por eso el margen negativo de `.banda-1`).
    .banda-1.mt-4
      SlyderF.slyder--flechas-azules(columnas="col-md-6 col-lg-4")
        .tarjeta.bg-1-p.r-20.p-4.h-100.tarjeta--adornos
          figure.mb-3
            img(src="@/assets/curso/temas/t1/factor-1.svg"  style="width: 128px").m-auto
          h4.text-center Actores
          p.text-center.mb-0 Personas, grupos o unidades organizacionales que participan en el proceso comunicativo, ya sea como emisores, receptores o en ambos roles de manera simultánea, dependiendo del flujo de información y de las relaciones establecidas en el contexto de la organización.
        .tarjeta.bg-1-p.r-20.p-4.h-100.tarjeta--adornos
          figure.mb-3
            img(src="@/assets/curso/temas/t1/factor-2.svg"  style="width: 128px").m-auto
          h4.text-center Canales
          p.text-center.mb-0 Medios o vías a través de los cuales se transmite el mensaje. Pueden ser formales (correos electrónicos, reuniones, informes) o informales (conversaciones espontáneas, mensajería instantánea); su elección incide directamente en el alcance y la efectividad del proceso comunicativo.
        .tarjeta.bg-1-p.r-20.p-4.h-100.tarjeta--adornos
          figure.mb-3
            img(src="@/assets/curso/temas/t1/factor-3.svg"  style="width: 128px").m-auto
          h4.text-center Códigos
          p.text-center.mb-0 Sistemas de signos, lenguajes y convenciones compartidas que posibilitan codificar y decodificar los mensajes. Comprenden el lenguaje verbal (oral y escrito), los gestos y los símbolos propios de la cultura organizacional que hacen posible la comprensión mutua entre los actores.
        .tarjeta.bg-1-p.r-20.p-4.h-100.tarjeta--adornos
          figure.mb-3
            img(src="@/assets/curso/temas/t1/factor-4.svg"  style="width: 128px").m-auto
          h4.text-center Contextos
          p.text-center.mb-0 Condiciones físicas, culturales, históricas y relacionales en las que se produce el intercambio comunicativo. El contexto determina el significado de los mensajes: una misma expresión puede interpretarse de manera distinta según el ambiente, la jerarquía o el momento en que se emite.
        .tarjeta.bg-1-p.r-20.p-4.h-100.tarjeta--adornos
          figure.mb-3
            img(src="@/assets/curso/temas/t1/factor-5.svg"  style="width: 128px").m-auto
          h4.text-center Intencionalidades
          p.text-center.mb-0 Propósitos explícitos o implícitos que orientan el acto comunicativo. Detrás de cada mensaje existe una finalidad (informar, persuadir, coordinar, motivar o resolver un desacuerdo) que condiciona la forma, el tono y el canal seleccionados para establecer el intercambio.
        .tarjeta.bg-1-p.r-20.p-4.h-100.tarjeta--adornos
          figure.mb-3
            img(src="@/assets/curso/temas/t1/factor-6.svg"  style="width: 128px").m-auto
          h4.text-center Retroalimentaciones
          p.text-center.mb-0 Respuestas o reacciones del receptor ante el mensaje recibido, que facilitan verificar si la comunicación fue efectiva. Pueden manifestarse de forma verbal, gestual o comportamental y convierten el proceso en un intercambio bidireccional que posibilita la comprensión y el ajuste mutuo.

    .row.align-items-start.mt-4(data-aos="fade-right")
      .col-12.col-md-auto.mb-3.mb-md-0
        figure.mb-0
          img(src="@/assets/curso/temas/intro/icono-2.svg"  style="width: 84px")
      .col
        p Estos seis factores no operan de manera independiente, se articulan y se condicionan mutuamente para generar un proceso comunicativo complejo y dinámico. Identificar cómo interactúan hace posible reconocer los puntos en los que la comunicación puede fortalecerse o deteriorarse dentro de la organización.
        p.mb-0 Con esta comprensión del proceso comunicativo en su conjunto, es posible ahondar en los fundamentos teóricos que explican cómo se origina, se transmite y se recibe un mensaje en el entorno de trabajo.

    separador 
    #t_1_1.titulo-segundo.color-acento-contenido
      h2 1.1 Fundamentos de la comunicación

    //- Foto de 396x239 (col-4) y la caja #FFF5E8 de 812x190 con r=10 (col-8).
    .row.mt-4
      .col-lg-4.mb-4.mb-lg-0
        figure.mb-0
          img(src="@/assets/curso/temas/t1/foto-2.png" ).w-100
      .col-lg-8
        .bg-1.r-10.p-4(data-aos="fade-left")
          p.mb-0 Desde una perspectiva clásica, la comunicación puede describirse como el proceso mediante el cual un emisor codifica y transmite un mensaje a un receptor, a través de un canal y en un contexto determinado, esperando una respuesta o una comprensión compartida. Sin embargo, este modelo lineal resulta insuficiente para explicar la complejidad de la comunicación en las organizaciones actuales, donde los mensajes circulan en múltiples direcciones, utilizan diversos medios y se interpretan a la luz de culturas organizacionales, experiencias previas y relaciones de poder.

        p.mt-4.mb-0(data-aos="fade-left") En el contexto organizacional, suelen distinguirse los siguientes componentes básicos del proceso comunicativo:

    //- El acordeon (707 de ancho) y la foto de 292x460 van dentro de un col-10 centrado:
    //- el bloque arranca en x=290 y acaba en 1309, no en los bordes del area de contenido.
    .row.justify-content-center.mt-4
      .col-lg-10
        .row.align-items-start
          .col-lg-8.mb-4.mb-lg-0
            LineaTiempoD.color-1(data-aos="fade-right")
              .row(numero="1" titulo="Emisor")
                .col-12
                  p.mb-0 Persona, grupo o unidad organizacional que da inicio al acto comunicativo al construir y codificar un mensaje con una intención determinada. Puede ser un directivo que emite directrices, un equipo que presenta resultados o un colaborador que reporta una situación al área responsable.
              .row(numero="2" titulo="Receptor")
                .col-12
                  p.mb-0 Persona, grupo o unidad organizacional que recibe el mensaje, lo decodifica e interpreta a partir de sus conocimientos previos, sus expectativas y el contexto en el que se encuentra. La comprensión que logre puede diferir de la intención original del emisor.
              .row(numero="3" titulo="Mensaje")
                .col-12
                  p.mb-0 Contenido que se transmite en el proceso comunicativo, que puede incluir ideas, instrucciones, emociones o decisiones. Su efectividad depende de la claridad con que se construye, la coherencia interna y la pertinencia frente a las necesidades del receptor.
              .row(numero="4" titulo="Canal")
                .col-12
                  p.mb-0 Medio a través del cual el emisor transmite el mensaje al receptor. Puede ser presencial (reunión, conversación), escrito (correo, circular, memorando) o digital (plataforma colaborativa, videollamada). La elección del canal incide directamente en la calidad del intercambio.
              .row(numero="5" titulo="Código")
                .col-12
                  p.mb-0 Sistema de signos, lenguajes y convenciones compartidas que permiten codificar y decodificar el mensaje. Comprende el lenguaje verbal oral y escrito, los gestos, las expresiones y los símbolos institucionales que emisor y receptor conocen y comparten en su entorno.
              .row(numero="6" titulo="Contexto")
                .col-12
                  p.mb-0 Condiciones físicas, culturales, temporales y emocionales en las que se desarrolla el intercambio comunicativo. Determina cómo se emite e interpreta el mensaje: un mismo enunciado puede adquirir significados distintos según el momento, el lugar o la relación entre los actores.
          .col-lg-4
            figure.mb-0
              img(src="@/assets/curso/temas/t1/foto-3.png" ).w-100

    p.mt-4(data-aos="fade-right") Reconocer estos componentes en su interacción permite comprender por qué algunos mensajes llegan con claridad mientras otros generan malentendidos. En la gestión del talento humano, identificar en cuál de estos elementos se produce la falla orienta las acciones de mejora y fortalece la calidad de la comunicación en la organización.

    //- La pestaña de 25x8 en (186,2424) marca este bloque como `.cajon`.
    .row.mt-4
      .col-lg-9
        .cajon.color-1.p-4(data-aos="fade-right")
          p.mb-0 Más allá del análisis de sus componentes, la comunicación organizacional cobra pleno sentido cuando se identifican las funciones que desempeña en la vida cotidiana de los equipos. Cada intercambio comunicativo, desde una instrucción hasta una retroalimentación, cumple uno o varios propósitos que orientan las decisiones de quienes gestionan personas en la organización.

        .row.align-items-start.mt-4(data-aos="fade-right")
          .col-12.col-md-auto.mb-3.mb-md-0
            figure.mb-0
              img(src="@/assets/curso/temas/intro/icono-2.svg"  style="width: 84px")
          .col
            p.mb-0 Analizar las interacciones a partir de estos componentes permite identificar con mayor precisión dónde se originan las fallas de comunicación: mensajes ambiguos, canales inadecuados, ausencia de retroalimentación o contextos emocionales poco favorables. Esta mirada estructurada es esencial para que el gestor de talento humano pueda proponer ajustes específicos en la forma de comunicar en la organización.
      .col-lg-3.mt-4.mt-lg-0
        figure.mb-0
          img(src="@/assets/curso/temas/t1/ilus-1.png" ).w-100

    //- Foto de 292x251 (col-3) y la caja #F7E3E6 de 916x154 con r=10 en x=497 (col-9).
    .row.mt-4
      .col-lg-3.mb-4.mb-lg-0
        figure.mb-0
          img(src="@/assets/curso/temas/t1/foto-14.png" ).w-100
      .col-lg-9
        .bg-2.r-10.p-4(data-aos="fade-left")
          p.mb-0 Las funciones de la comunicación organizacional describen los propósitos que esta cumple y los efectos que produce en el comportamiento colectivo. Comprender estas funciones permite diseñar estrategias comunicativas coherentes con el momento y el propósito de cada intercambio, y evitar mensajes que lleguen sin el impacto esperado en los equipos de trabajo.

        p.mt-4.mb-0(data-aos="fade-left") La comunicación organizacional cumple, de manera simultánea o alternada, distintas funciones que se articulan para sostener el funcionamiento de los equipos. Entre las más relevantes en el contexto de la gestión del talento humano se distinguen las siguientes:

    //- Las cinco funciones, en el slider de la banda de 1328x559. Sólo la primera está en el
    //- artboard; las otras cuatro, con sus imágenes, salen del pasteboard.
    .banda-2.mt-4
      .tarjeta.bg-3-v.r-20(data-aos="fade-up")
        SlyderA(tipo="b")
          .row.justify-content-center.align-items-center.p-4.p-lg-5
            .col-lg-6.mb-4.mb-lg-0
              p.mb-0 #[b Función informativa:] permite compartir con los integrantes de la organización datos, indicadores, decisiones, cambios en procesos y resultados de gestión. Garantiza que cada persona cuente con la información necesaria para ejecutar sus tareas, comprender el estado de los procesos y fundamentar sus decisiones.
            .col-lg-6
              figure.mb-0
                img(src="@/assets/curso/temas/t1/funcion-1.png" ).w-100
          .row.justify-content-center.align-items-center.p-4.p-lg-5
            .col-lg-6.mb-4.mb-lg-0
              p.mb-0 #[b Función reguladora:] orienta el comportamiento de los integrantes de la organización mediante el establecimiento y la difusión de normas, políticas, procedimientos y manuales. Asegura que las decisiones y acciones individuales sean coherentes con los estándares institucionales y contribuyan al logro de los objetivos colectivos.
            .col-lg-6
              figure.mb-0
                img(src="@/assets/curso/temas/t1/funcion-2.png" ).w-100
          .row.justify-content-center.align-items-center.p-4.p-lg-5
            .col-lg-6.mb-4.mb-lg-0
              p.mb-0 #[b Función motivadora:] contribuye a generar compromiso, sentido de propósito y reconocimiento en los integrantes de la organización. Cuando la comunicación explica el significado del trabajo, reconoce los logros y vincula las tareas individuales con los objetivos institucionales, fortalece la motivación y el sentido de pertenencia.
            .col-lg-6
              figure.mb-0
                img(src="@/assets/curso/temas/t1/funcion-3.png" ).w-100
          .row.justify-content-center.align-items-center.p-4.p-lg-5
            .col-lg-6.mb-4.mb-lg-0
              p.mb-0 #[b Función integradora:] refuerza la identidad organizacional, los valores compartidos y la cohesión entre los integrantes. Al promover espacios de diálogo, intercambio de experiencias y trabajo colaborativo, contribuye a que las personas se reconozcan como parte de un proyecto colectivo con propósitos comunes.
            .col-lg-6
              figure.mb-0
                img(src="@/assets/curso/temas/t1/funcion-4.png" ).w-100
          .row.justify-content-center.align-items-center.p-4.p-lg-5
            .col-lg-6.mb-4.mb-lg-0
              p.mb-0 #[b Función de control:] posibilita el seguimiento, la verificación y la evaluación del cumplimiento de metas, estándares y compromisos organizacionales. A través de informes, indicadores y mecanismos de rendición de cuentas, permite detectar desviaciones y tomar decisiones correctivas de manera oportuna y fundamentada.
            .col-lg-6
              figure.mb-0
                img(src="@/assets/curso/temas/t1/funcion-5.png" ).w-100


    //- El XD dibuja este parrafo DOS veces (y=3829 y y=5328); la segunda no introduce nada,
    //- asi que va una sola vez, delante del caso que presenta.
    //- Foto de 396x257 (col-4) y la caja #FFF5E8 de 812x160 con r=10 y su icono (col-8).
    .row.mt-4
      .col-lg-4.mb-4.mb-lg-0
        figure.mb-0
          img(src="@/assets/curso/temas/t1/foto-4.png" ).w-100
      .col-lg-8
        .bg-1.r-10.p-4(data-aos="fade-left")
          .row.align-items-center
            .col-12.col-md-auto.mb-3.mb-md-0
              figure.mb-0
                img(src="@/assets/curso/temas/t1/ic-6.svg"  style="width: 84px")
            .col
              p.mb-0 Estas cinco funciones no actúan de manera independiente: en la práctica, un mismo mensaje puede informar, regular y motivar de forma simultánea. Comprender cómo se interrelacionan facilita al gestor de talento humano diseñar estrategias comunicativas coherentes con el propósito de la organización y con las necesidades reales de los equipos.

        p.mt-4.mb-0(data-aos="fade-left") El siguiente caso ilustra cómo dos funciones de la comunicación organizacional, la informativa y la motivadora, pueden integrarse en una misma acción de gestión del talento humano, con efectos positivos en el clima y el desempeño del equipo.

    //- Caso de estudio: caja #CBD5FF de 1020x248 (col-10) con la ilustracion de 243x198 dentro.
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3-a.p-4(data-aos="fade-up")
          .row.align-items-center
            .col-12.col-md-auto.mb-3.mb-md-0
              figure.mb-0
                img(src="@/assets/curso/temas/t1/ilus-2.png" ).w-100.r-10
            .col
              h4 Comunicación informativa y motivadora en una pyme de servicios
              p.mb-0 En una empresa de servicios tecnológicos, la dirección de talento humano decide reforzar la comunicación interna sobre resultados trimestrales. Para ello, integra en una misma reunión la presentación de indicadores de desempeño (función informativa) con el reconocimiento público a los equipos que cumplieron metas (función motivadora). Al vincular datos objetivos con mensajes de valoración, se fortalece la percepción de transparencia y se incrementa la disposición de los colaboradores para asumir nuevos retos.

        p.mt-4(data-aos="fade-right") Este tipo de integración comunicativa demuestra que las funciones no son compartimentos separados, sino recursos complementarios que el gestor de talento humano puede combinar según las necesidades del equipo y el propósito de cada momento organizacional. Las siguientes situaciones ilustran cuándo y cómo aplicar cada función de manera estratégica:

    //- Caja #F7E3E6 de 916x387 (col-9) con la lista, y la foto de 292x387 pegada a la derecha.
    .row.mt-4
      .col-lg-9.mb-4.mb-lg-0
        .bg-2.p-4.h-100(data-aos="fade-right")
          ul.lista-ul.mb-0
            li
              i.fas.fa-circle-right
              | #[b Reuniones de resultados:] espacio para compartir cifras de desempeño y, al mismo tiempo, reconocer el trabajo del equipo en un solo mensaje.
            li
              i.fas.fa-circle-right
              | #[b Procesos de inducción:] momento para explicar normas, funciones y expectativas del cargo de forma ordenada a quien se integra al equipo.
            li
              i.fas.fa-circle-right
              | #[b Entrevistas de desempeño:] conversación para revisar qué salió bien y qué se puede mejorar, orientando a la persona sin limitarse a señalar errores.
            li
              i.fas.fa-circle-right
              | #[b Comunicados de cambio organizacional:] oportunidad para explicar a los equipos por qué cambia algo en la empresa y cómo ese cambio los involucra.
            li.mb-0
              i.fas.fa-circle-right
              | #[b Espacios de retroalimentación:] intercambio en el que se dice a alguien qué logró y en qué puede crecer, con ejemplos claros y un tono de apoyo.
      .col-lg-3
        figure.mb-0.h-100
          img(src="@/assets/curso/temas/t1/foto-5.png" ).w-100.h-100.object-fit-cover

    .row.align-items-start.mt-4(data-aos="fade-right")
      .col-12.col-md-auto.mb-3.mb-md-0
        figure.mb-0
          img(src="@/assets/curso/temas/intro/icono-2.svg"  style="width: 84px")
      .col
        p La elección de la función comunicativa adecuada para cada situación requiere que el gestor de talento humano lea el contexto, identifique la necesidad del equipo y construya el mensaje con el propósito específico que el momento demanda.
        p.mb-0 La efectividad de cada una de estas funciones depende, en parte, del tipo de comunicación que se emplee para ejercerlas. Conocer las diferencias entre la comunicación verbal y la no verbal amplía las posibilidades del gestor y le permite ajustar no solo qué comunica, sino también cómo lo comunica en cada contexto.

    separador
    #t_1_2.titulo-segundo.color-acento-contenido
      h2 1.2 Comunicación verbal y no verbal

    //- Foto de 395x281 (col-4) y la caja #FFF5E8 de 812x160 con r=10 y su icono (col-8).
    .row.mt-4
      .col-lg-4.mb-4.mb-lg-0
        figure.mb-0
          img(src="@/assets/curso/temas/t1/foto-6.png" ).w-100
      .col-lg-8
        .bg-1.r-10.p-4(data-aos="fade-left")
          .row.align-items-center
            .col-12.col-md-auto.mb-3.mb-md-0
              figure.mb-0
                img(src="@/assets/curso/temas/t1/ic-2.svg"  style="width: 84px")
            .col
              p.mb-0 En las organizaciones se distingue, de manera general, entre comunicación verbal y comunicación no verbal. Aunque esta separación tiene fines didácticos, en la práctica ambas dimensiones se presentan de forma simultánea y su coherencia o incoherencia influye significativamente en la interpretación de los mensajes.

        p.mt-4.mb-0(data-aos="fade-left") La comunicación verbal comprende los mensajes expresados mediante palabras, ya sea de manera oral o escrita. En el ámbito organizacional, incluye conversaciones informales, reuniones formales, entrevistas, presentaciones, comunicaciones por teléfono o videoconferencia, correos electrónicos, informes, manuales, políticas, chats corporativos y documentos institucionales.

    //- Franja #CBD5FF de 1020x154 (col-10) con el icono de 80x80 montado arriba, centrado.
    .row.justify-content-center.mt-5
      .col-lg-10
        .bg-3-a.cita-destacada.p-4.text-center(data-aos="fade-up")
          figure
            img(src="@/assets/curso/temas/t1/ic-1.svg" )
          p.mb-0
            b La comunicación no verbal (gestos, tono de voz y manejo de distancias) puede reforzar o contradecir el mensaje verbal, y es determinante en la credibilidad y la confianza que genera quien comunica.

    //- Caja #F7E3E6 de 812x290 con icono (col-8) y la foto de 396x290 a la derecha (col-4).
    .row.mt-4
      .col-lg-8.mb-4.mb-lg-0
        .bg-2.p-4.h-100(data-aos="fade-right")
          .row.align-items-center
            .col-12.col-md-auto.mb-3.mb-md-0
              figure.mb-0
                img(src="@/assets/curso/temas/t1/ic-3.svg"  style="width: 84px")
         
              p.mt-2 Sus manifestaciones abarcan un espectro amplio: expresiones faciales, posturas corporales, silencios, uso del espacio y del tiempo, vestimenta y elementos simbólicos presentes en el entorno laboral. Cada uno de estos canales transmite información sobre el estado emocional, la actitud y el nivel de apertura de quien comunica, con efectos directos en la percepción de la empatía, la autoridad y la disposición al diálogo.
      .col-lg-4
        figure.mb-0.h-100
          img(src="@/assets/curso/temas/t1/foto-7.png" ).w-100.h-100.object-fit-cover

    p.mt-4(data-aos="fade-right") La comunicación verbal y la no verbal se expresan a través de formas específicas que varían según el canal y el propósito del mensaje. Identificar estas clases permite al gestor de talento humano reconocer cuándo y cómo emplear cada una para lograr una interacción más efectiva y coherente en los distintos contextos organizacionales:

    .row.justify-content-center.mt-4
      .col-lg-10
        LineaTiempoD.color-1(data-aos="fade-right")
          .row(numero="1" titulo="Comunicación verbal oral")
            .col-12
              p.mb-0 Se produce en tiempo real a través del habla y facilita aclarar expectativas, dar instrucciones y construir acuerdos de manera inmediata. Se aplica en reuniones, retroalimentaciones y presentaciones entre colaboradores. Ejemplo: en una empresa de servicios de Cali, el coordinador de área convoca una reunión semanal para revisar avances, resolver dudas y alinear al equipo en las prioridades del período.
          .row(numero="2" titulo="Comunicación verbal escrita")
            .col-12
              p.mb-0 Circula a través de correos electrónicos, circulares, manuales e informes; deja trazabilidad documental y unifica criterios a lo largo de la organización. Ejemplo: una entidad pública de Bogotá comunica por circular interna los protocolos actualizados de atención al ciudadano, garantizando que todos los colaboradores cuenten con la misma información de forma verificable y consultable.
          .row(numero="3" titulo="Comunicación no verbal corporal")
            .col-12
              p.mb-0 Se expresa a través de gestos, expresiones faciales, posturas y movimientos del cuerpo, y refuerza o contradice el contenido del mensaje verbal. Ejemplo: en una IPS de Medellín, la coordinadora de talento humano mantiene contacto visual y una postura abierta durante las entrevistas de desempeño, lo que transmite respeto y disposición genuina al diálogo.
          .row(numero="4" titulo="Comunicación no verbal paraverbal")
            .col-12
              p.mb-0 Comprende los elementos vocales que acompañan el habla sin ser propiamente palabras: el tono, el volumen, el ritmo, las pausas y los silencios. Ejemplo: un supervisor en Barranquilla baja deliberadamente el tono de voz al informar una reestructuración del equipo, lo que transmite calma y seguridad a los colaboradores en un momento de incertidumbre laboral.
          .row(numero="5" titulo="Comunicación no verbal contextual")
            .col-12
              p.mb-0 Abarca los espacios físicos, los tiempos y los símbolos que enmarcan la interacción y condicionan su interpretación. Ejemplo: una cooperativa del Huila organiza su oficina de atención al asociado con espacios cómodos, iluminados y ordenados, lo que transmite confianza y profesionalismo desde el primer contacto con la persona.

    p.mt-4(data-aos="fade-right") La combinación de estas clases de comunicación determina la calidad del intercambio en la organización. Un mensaje verbal sólido puede verse reforzado o contradicho por la postura, el tono o el espacio en el que se emite. Para el gestor de talento humano, desarrollar consciencia sobre todos estos canales resulta tan importante como seleccionar las palabras adecuadas al comunicar.

    .row.align-items-start.mt-4(data-aos="fade-right")
      .col-12.col-md-auto.mb-3.mb-md-0
        figure.mb-0
          img(src="@/assets/curso/temas/intro/icono-2.svg"  style="width: 84px")
      .col
        p.mb-0 La atención a estas señales no es solo una habilidad individual: se convierte en una responsabilidad de gestión cuando el mensaje que se emite contradice las actitudes que se proyectan. Esta contradicción, conocida como incoherencia comunicativa, puede erosionar la credibilidad del gestor y deteriorar el ambiente laboral de manera gradual. El siguiente caso ilustra cómo esta situación se presenta en un contexto organizacional concreto:

    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3-a.p-4(data-aos="fade-up")
          .row.align-items-center
            .col-12.col-md-auto.mb-3.mb-md-0
              figure.mb-0
                img(src="@/assets/curso/temas/t1/ilus-3.png" ).w-100.r-10
            .col
              h4 Incoherencia entre mensaje verbal y no verbal
              p.mb-0 En una entidad del sector público, un directivo comunica verbalmente su disposición al diálogo con los funcionarios, pero durante las reuniones mantiene los brazos cruzados, evita el contacto visual y responde de manera evasiva a las preguntas incómodas. Aunque las palabras sugieren apertura, el lenguaje corporal transmite distancia y resistencia. Como consecuencia, los colaboradores perciben que no existe un verdadero espacio para expresar inquietudes, y se incrementa la comunicación informal cargada de rumores.

    p.mt-4(data-aos="fade-right") Reconocer las diferencias entre la comunicación verbal y la no verbal en la práctica organizacional permite al gestor de talento humano tomar decisiones más informadas sobre cómo construir, transmitir e interpretar los mensajes en cada situación. La siguiente tabla presenta, de forma comparativa, las principales dimensiones de ambas modalidades, sus canales, su intencionalidad, su efecto en la confianza y los riesgos asociados a su omisión o incoherencia:

    //- La Tabla 1 esta VACIA en el .xd: solo dibuja la cabecera y las filas en blanco. El
    //- contenido son las siete filas del `_DI.docx`.
    .row.justify-content-center.mt-4
      .col-lg-10
        .titulo-sexto.color-acento-contenido.mb-3
          h5 Tabla 1.
          span  Manifestaciones y efectos de la comunicación verbal y no verbal en el entorno organizacional
        .tabla-a.color-acento-contenido(data-aos="fade-up")
          table
            thead
              tr
                th Dimensión
                th Comunicación verbal
                th Comunicación no verbal
            tbody
              tr
                td Naturaleza
                td Emplea palabras en forma oral o escrita para transmitir información, instrucciones o acuerdos.
                td Emplea gestos, posturas, tono de voz, silencios y uso del espacio para acompañar o reemplazar el mensaje verbal.
              tr
                td Canales principales
                td Reuniones, correos, circulares, informes, chats corporativos y conversaciones directas.
                td Expresiones faciales, contacto visual, postura corporal, proxémica, vestimenta y elementos del entorno.
              tr
                td Intencionalidad
                td Generalmente consciente: el emisor elige y construye deliberadamente el mensaje.
                td Puede ser consciente o inconsciente; muchas señales se emiten sin que el emisor las perciba.
              tr
                td Función en la interacción
                td Informa, regula, motiva e integra a través de contenidos explícitos y verificables.
                td Refuerza, matiza o contradice el mensaje verbal; transmite emociones y actitudes difíciles de verbalizar.
              tr
                td Efecto en la confianza
                td Un mensaje verbal claro y oportuno genera seguridad y reduce la incertidumbre en el equipo.
                td La coherencia entre lo que se dice y lo que se proyecta es determinante en la percepción de credibilidad del gestor.
              tr
                td Riesgo de omisión
                td Mensajes ambiguos, incompletos o en canales inadecuados generan errores e incertidumbre.
                td La incoherencia entre el mensaje verbal y las señales no verbales deteriora la confianza y estimula los rumores.
              tr
                td Ejemplo organizacional
                td Una circular de Bogotá comunica el cambio de política de turnos con pasos claros y fechas precisas.
                td Un directivo declara apertura al diálogo, pero cruza los brazos y evita el contacto visual durante la reunión.

    //- Caja #FFF5E8 de 812x150 con r=10 (col-8) y la foto de 396x271 a la derecha (col-4).
    .row.mt-4
      .col-lg-8.mb-4.mb-lg-0
        .bg-1.r-10.p-4(data-aos="fade-right")
          p.mb-0 La gestión efectiva de personas requiere, además del dominio de la comunicación escrita y oral, la capacidad de leer e interpretar las señales no verbales que circulan en los equipos de trabajo. Reconocer una postura cerrada, un silencio prolongado o una mirada esquiva puede ofrecer información valiosa sobre el clima del grupo y anticipar situaciones que aún no han sido verbalizadas.
      
        p.mt-4(data-aos="fade-right") Profundizar en la coherencia entre el mensaje verbal y las señales no verbales implica conocer con mayor detalle los sistemas a través de los cuales opera la comunicación no verbal. La comunicación kinésica y la paralingüística son dos de esos sistemas, y su comprensión resulta clave para interpretar con mayor exactitud las interacciones cotidianas en el entorno organizacional.

      .col-lg-4
        figure.mb-0.h-100
          img(src="@/assets/curso/temas/t1/foto-8.png" ).w-100.h-100.object-fit-cover



    separador
    #t_1_3.titulo-segundo.color-acento-contenido
      h2 1.3 Comunicación kinésica, proxémica y paralingüística

    //- Foto de 292x261 (col-3) y, a su lado, el parrafo y la caja #CBD5FF (col-9).
    .row.mt-4
      .col-lg-3.mb-4.mb-lg-0
        figure.mb-0
          img(src="@/assets/curso/temas/t1/foto-9.png" ).w-100
      .col-lg-9
        p(data-aos="fade-left") En toda interacción laboral, la comunicación va más allá de las palabras. El cuerpo expresa actitudes a través de gestos y posturas; la voz transmite emociones mediante el tono, el volumen y las pausas; el espacio físico condiciona la disposición de quienes interactúan. Estas señales operan de manera simultánea al mensaje verbal y tienen un efecto directo en cómo se interpreta lo que se dice en cada contexto organizacional.

        .bg-3-a.p-4(data-aos="fade-left")
          p.mb-0 Para el gestor de talento humano, desarrollar sensibilidad frente a estas señales representa una ventaja concreta en la práctica diaria. Quien reconoce una postura cerrada en una reunión, detecta un tono de voz cargado de tensión o advierte que el espacio de trabajo genera distancia entre los interlocutores, cuenta con información valiosa para intervenir oportunamente, ajustar su estilo comunicativo y favorecer intercambios más abiertos, respetuosos y productivos.

    p.mt-4(data-aos="fade-right") Dentro de la comunicación no verbal, se distinguen tres dimensiones especialmente relevantes para la gestión de personas en las organizaciones. Cada una opera sobre un canal distinto y aporta información complementaria que enriquece o, en ocasiones, contradice el contenido del mensaje verbal:

    //- Tres tarjetas pegadas de 405/419/405, con el circulo de 150 dentro. El XD redondea
    //- solo las esquinas exteriores: lo resuelve `.tarjeta--container`.
    .tarjeta--container.row.mt-4(data-aos="fade-up")
      .col-md.tarjeta.bg-1-p.p-4
        figure.mb-3
          img(src="@/assets/curso/temas/t1/dim-1.svg"  style="width: 150px").m-auto
        h4.text-center Comunicación kinésica
        p.mb-0 Estudia los movimientos del cuerpo, los gestos y las expresiones faciales como portadores de significado en la interacción humana. Incluye la postura, la orientación del cuerpo, el contacto visual y los movimientos de manos. En el entorno laboral, estos elementos pueden reforzar la credibilidad del comunicador o generar distancia con el interlocutor.
      .col-md.tarjeta.bg-2-s.p-4
        figure.mb-3
          img(src="@/assets/curso/temas/t1/dim-2.svg"  style="width: 150px").m-auto
        h4.text-center Comunicación proxémica
        p.mb-0 Analiza el uso del espacio físico y las distancias interpersonales en las interacciones. La distancia que se mantiene durante una conversación comunica información sobre el tipo de relación, el nivel de confianza y las normas culturales del entorno. En las organizaciones, el diseño del espacio también influye en la dinámica comunicativa del equipo.
      .col-md.tarjeta.bg-3.p-4
        figure.mb-3
          img(src="@/assets/curso/temas/t1/dim-3.svg"  style="width: 150px").m-auto
        h4.text-center Comunicación paralingüística
        p.mb-0 Examina los elementos vocales que acompañan el habla sin pertenecer al lenguaje verbal en sí: el tono, el volumen, el ritmo, las pausas y los silencios. Estos componentes modulan el significado del mensaje y revelan estados emocionales, actitudes e intenciones que las palabras por sí solas no siempre logran expresar.

    .row.align-items-start.mt-4(data-aos="fade-right")
      .col-12.col-md-auto.mb-3.mb-md-0
        figure.mb-0
          img(src="@/assets/curso/temas/intro/icono-2.svg"  style="width: 84px")
      .col
        p.mb-0 Estas tres dimensiones actúan de manera simultánea e interdependiente durante cualquier intercambio. Conocerlas permite identificar señales de tensión o apertura en el equipo y ajustar la propia comunicación para transmitir mensajes más coherentes. En la gestión del talento humano, esta habilidad se traduce en una lectura más precisa de las situaciones interpersonales en el entorno laboral.

    //- Caja #F7E3E6 de 708x270 con icono (col-7) y la foto de 292x270 a la derecha (col-3).
    .row.justify-content-center.mt-4
      .col-lg-10
        .row
          .col-lg-8.mb-4.mb-lg-0
            .bg-2.p-4.h-100(data-aos="fade-right")
              .row.align-items-center
                .col-12.col-md-auto.mb-3.mb-md-0
                  figure.mb-0
                    img(src="@/assets/curso/temas/t1/ic-4.svg"  style="width: 84px")
                
                  p.mt-3 La aplicación efectiva de estas dimensiones no es automática: requiere observación, práctica y disposición para ajustar los propios patrones comunicativos. Quien gestiona personas no solo debe conocer estas categorías, sino también reconocerlas en tiempo real durante las interacciones cotidianas con los colaboradores.
          .col-lg-4
            figure.mb-0.h-100
              img(src="@/assets/curso/temas/t1/foto-10.png" ).w-100.h-100.object-fit-cover

    p.mt-4(data-aos="fade-right") El desconocimiento de estas dimensiones puede llevar a interpretaciones erróneas o a la reproducción involuntaria de señales que generan distancia y desconfianza. En contraste, cuando el gestor ajusta de manera consciente sus gestos, el uso del espacio y el tono de voz, fortalece la efectividad de sus mensajes y contribuye al cuidado del clima organizacional. El siguiente caso ilustra cómo este ajuste transforma el resultado de una conversación de retroalimentación:

    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3-a.p-4(data-aos="fade-up")
          .row.align-items-center
            .col-12.col-md-auto.mb-3.mb-md-0
              figure.mb-0
                img(src="@/assets/curso/temas/t1/ilus-4.png" ).w-100.r-10
            .col
              h4 Ajuste proxémico en una retroalimentación de desempeño
              p.mb-0 En una empresa del sector comercio, una coordinadora de talento humano debe brindar retroalimentación a un colaborador respecto a incumplimientos reiterados en los horarios de llegada. En lugar de abordar el tema en el pasillo o frente a otros compañeros, decide realizar la conversación en un espacio privado, adecuadamente ventilado y con sillas ubicadas a una distancia que no invade la zona íntima del colaborador. Este manejo proxémico, sumado a un tono de voz sereno, reduce la actitud defensiva del colaborador y facilita que asuma compromisos de mejora concretos.

    //- Parrafo y caja #EFF2FF (col-9) con la foto de 291x217 a la derecha (col-3).
    .row.mt-4
      .col-lg-9
        p(data-aos="fade-right") La decisión de elegir un espacio privado, adoptar una distancia adecuada y mantener un tono sereno no es casual: responde al reconocimiento de que el entorno físico y el lenguaje no verbal condicionan la disposición del interlocutor y determinan, en buena medida, si el mensaje se recibe con apertura o con resistencia.

        .bg-3.p-4(data-aos="fade-right")
          p.mb-0 El dominio de estas dimensiones no verbales alcanza su mayor potencial cuando se integra con el uso deliberado de técnicas de comunicación verbal. La comunicación efectiva en el trabajo surge precisamente de esta articulación: de saber no solo qué comunicar, sino cómo hacerlo, en qué momento y con qué actitud corporal y vocal.
      .col-lg-3.mt-4.mt-lg-0
        figure.mb-0
          img(src="@/assets/curso/temas/t1/foto-11.png" ).w-100

    separador
    #t_1_4.titulo-segundo.color-acento-contenido
      h2 1.4 Comunicación efectiva en el trabajo

    p.mt-4(data-aos="fade-right") El dominio de técnicas de comunicación efectiva es una competencia transversal para quienes gestionan equipos en entornos organizacionales. Comunicarse de forma efectiva implica formular mensajes claros, utilizar canales adecuados, promover la participación de los interlocutores, verificar la comprensión y ofrecer retroalimentación orientada al aprendizaje.

    //- Foto de 614x280 (col-6) y la franja #FEDDB4 de 919x280 con la caja blanca de 685x200
    //- montada dentro: es `.bloque-texto-g` del catalogo.
    .bloque-texto-g.color-primario.p-3.p-sm-4.p-md-5.mt-4(data-aos="fade-up")
      .bloque-texto-g__img(:style="{ backgroundImage: `url(${require_src('@/assets/curso/temas/t1/foto-12.png')})` }")
      .bloque-texto-g__texto.p-4
        p.mb-0 En el contexto de la gestión del talento humano, la comunicación efectiva no es una habilidad innata ni espontánea: se construye mediante la aplicación consciente de técnicas que permiten adaptar el mensaje a la situación, al interlocutor y al propósito de cada intercambio. Su dominio marca una diferencia significativa en la calidad de las relaciones laborales, en la resolución de conflictos y en la capacidad del equipo para alcanzar resultados colectivos.

    p.mt-4(data-aos="fade-right") En la práctica cotidiana, la comunicación efectiva se pone a prueba en momentos clave de la gestión. Los siguientes escenarios representan situaciones frecuentes en las que el uso adecuado de las técnicas comunicativas resulta determinante:

    //- Caja #F7E3E6 de 1020x215 (col-10) con la lista numerada de cuadros azules.
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-2.p-4(data-aos="fade-up")
          ol.lista-ol--cuadro.mb-0
            li
              .lista-ol--cuadro__vineta
                span 1
              | Reuniones de equipo en las que se deben alinear expectativas y resolver dudas sobre un proceso en curso.
            li
              .lista-ol--cuadro__vineta
                span 2
              | Conversaciones de retroalimentación individual en las que se abordan fortalezas y oportunidades de mejora.
            li
              .lista-ol--cuadro__vineta
                span 3
              | Comunicados de cambio organizacional que exigen claridad, empatía y elección del canal adecuado.
            li
              .lista-ol--cuadro__vineta
                span 4
              | Situaciones de conflicto en las que escuchar activamente y responder con asertividad evita la escalada del problema.
            li
              .lista-ol--cuadro__vineta
                span 5
              | Procesos de inducción en los que la precisión del mensaje reduce la incertidumbre del colaborador que se integra al equipo.

    p.mt-4(data-aos="fade-right") Cada uno de estos escenarios exige del gestor de talento humano una respuesta comunicativa distinta: no existe una fórmula única que funcione en todas las situaciones. Lo que determina la efectividad es la capacidad de leer el contexto, identificar las necesidades del momento y responder con claridad, empatía y precisión.

    p(data-aos="fade-right") El desarrollo de estas habilidades se apoya en un conjunto de técnicas que pueden incorporarse de manera progresiva a la práctica profesional. A continuación, se presentan las más relevantes en el contexto de la gestión organizacional:

    //- Acordeon de chevron: el XD dibuja el circulo del boton a la DERECHA (tipo b), con la
    //- tarjeta abierta en #F7E3E6 y las cerradas en #E5EBFC, todas con r=20.
    .row.justify-content-center.mt-4
      .col-lg-10
        AcordionA.acordion--tecnicas(tipo="b" clase-tarjeta="tarjeta bg-4 r-20")
          div(titulo="Escucha activa")
            p.mb-0 Consiste en prestar atención plena al interlocutor, identificar el contenido explícito y las emociones implícitas del mensaje, y confirmar la comprensión antes de responder. Requiere disposición genuina y suspensión de juicios previos. En la práctica: en una alcaldía de Nariño, el coordinador de talento humano parafrasea las preocupaciones del colaborador antes de responder, lo que garantiza comprensión mutua y fortalece la confianza.
          div(titulo="Claridad y precisión")
            p.mb-0 Implica construir mensajes específicos, sin ambigüedad y adaptados al nivel de comprensión del receptor. Un mensaje claro reduce los errores de interpretación y agiliza la ejecución de las tareas. Caso real: una pyme de Pereira redacta instrucciones paso a paso para el proceso de despacho de pedidos y elimina las dudas recurrentes que generaban reprocesos en el área operativa.
          div(titulo="Elección del canal")
            p.mb-0 Supone seleccionar el medio de comunicación más adecuado según el tipo de mensaje, la urgencia y el perfil del receptor. Una elección inadecuada puede distorsionar el contenido o generar desconfianza. Aplicación: una empresa de Cúcuta anuncia un cambio en las condiciones laborales en reunión presencial en lugar de comunicarlo por chat, para garantizar comprensión y atender las reacciones del equipo.
          div(titulo="Retroalimentación constructiva")
            p.mb-0 Permite señalar fortalezas y oportunidades de mejora de forma objetiva, específica y respetuosa, con el propósito de fortalecer el desempeño sin afectar la relación. Ejemplo: en una obra de Cartagena, el residente de obra reconoce el avance del equipo, describe el error específico y propone conjuntamente una mejora, sin descalificar a la persona ni afectar el clima del grupo.
          div(titulo="Comunicación empática")
            p.mb-0 Considera las emociones, las circunstancias y la perspectiva del interlocutor al construir y transmitir un mensaje. Implica adaptar el tono, el contenido y el momento de la comunicación al estado emocional del receptor. En contexto: una jefa de talento humano en Manizales ajusta el estilo comunicativo con un colaborador que atraviesa una situación personal difícil para preservar la confianza y el vínculo laboral.

    //- Ilustracion de 292x198 sobre #EBB9C1 (col-3) y la caja #FEDDB4 al lado.
    .row.justify-content-center.mt-4
      .col-lg-10
        .row.mt-4
          .col-lg-4.mb-4.mb-lg-0.order-2
            figure.mb-0.h-100
              img(src="@/assets/curso/temas/t1/ilus-5.png" ).w-100.h-100.object-fit-cover
          .col-lg-8
              p Integrar estas técnicas de manera sistemática transforma la comunicación de un proceso improvisado en un componente planificado de la gestión. Esto se traduce en una reducción de errores, una resolución más constructiva de los conflictos y el fortalecimiento de relaciones laborales más colaborativas y respetuosas.
              p.mb-0 La aplicación simultánea de varias de estas técnicas en una misma situación organizacional multiplica su impacto. El siguiente caso ilustra cómo su uso combinado puede facilitar la implementación de un cambio significativo en el equipo:

    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3-a.p-4(data-aos="fade-up")
          .row.align-items-center
            .col-12.col-md-auto.mb-3.mb-md-0
              figure.mb-0
                img(src="@/assets/curso/temas/t1/ilus-6.png" ).w-100.r-10
            .col
              h4 Uso combinado de técnicas de comunicación efectiva
              p.mb-0 En una organización del sector salud, la jefatura de talento humano debe comunicar la implementación de un nuevo sistema de registro de turnos. Para ello, realiza primero una reunión sincrónica donde explica con claridad el propósito del cambio, los pasos de implementación y los apoyos disponibles (claridad, elección adecuada del canal). Durante la reunión, abre espacios para preguntas, escucha activamente las preocupaciones de los colaboradores y las recoge para ajustar el plan de soporte (escucha activa, comunicación empática). Posteriormente, envía un instructivo escrito con los procedimientos y fechas clave, y programa sesiones de retroalimentación sobre la experiencia inicial con la nueva herramienta (refuerzo del mensaje, retroalimentación constructiva). Esta combinación de técnicas reduce la resistencia al cambio y mejora la adopción del sistema.

    p.mt-4(data-aos="fade-right") El caso anterior demuestra que la comunicación efectiva no depende de una sola técnica, sino de la capacidad de combinarlas según el momento, el interlocutor y el propósito del mensaje. Esta flexibilidad comunicativa es una de las competencias más valoradas en quienes lideran y gestionan equipos dentro de las organizaciones.

    //- Caja #F7E3E6 con icono (col-8) y la foto de 397x300 a la derecha (col-4).
    .row.mt-4
      .col-lg-8.mb-4.mb-lg-0
        .bg-2.p-4.h-100(data-aos="fade-right")
          figure.mb-3
            img(src="@/assets/curso/temas/t1/ic-5.svg"  style="width: 84px")
          p.mb-0 Las técnicas de comunicación efectiva no operan de manera aislada: su verdadero alcance se evidencia cuando se aplican en el marco del trabajo colaborativo y el trabajo en equipo. La calidad de los intercambios comunicativos entre los integrantes de un equipo determina la coordinación de las tareas, la cohesión del grupo y la capacidad colectiva para alcanzar resultados que ningún individuo podría lograr por sí solo.
      .col-lg-4
        figure.mb-0.h-100
          img(src="@/assets/curso/temas/t1/foto-13.png" ).w-100.h-100.object-fit-cover


</template>

<script>
export default {
  name: 'Tema1',
  data: () => ({}),
}
</script>

<style lang="sass"></style>
