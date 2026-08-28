<template lang="pug">
.curso-main-container.introduccion.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5

    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span
          i.fas.fa-info
      h1 Introducción

    //- Fila 1: el parrafo mide 915px de los 1228 del area de contenido (col-9) y la foto
    //- 292x261 con r=10 va pegada al borde derecho, x=1121 (col-3).
    .row
      .col-lg-9
        p(data-aos="fade-right") El presente componente formativo orienta la comprensión de la comunicación como base de la gestión organizacional y su relación con el trabajo colaborativo. Desde el contexto colombiano, se abordan los procesos y las clases de comunicación, el trabajo en equipo, la resolución de problemas y la asertividad, con el fin de reconocer cómo las organizaciones fortalecen la convivencia, la coordinación y el logro de sus objetivos.

        //- Caja #FEDDB4 de 916x140 SIN radio, con el icono de 84x84 (r=10, #CBD5FF) dentro.
        .bg-1-p.r-0.p-4.mt-4(data-aos="fade-right")
          .row.align-items-center
            .col-12.col-md-auto.mb-3.mb-md-0
              figure.mb-0
                img(src="@/assets/curso/temas/intro/icono-1.svg"  style="width: 84px")
            .col
              p.mb-0 A partir de este recorrido, se analizan los fundamentos de la comunicación en el contexto organizacional, con sus procesos, componentes y sus manifestaciones verbales y no verbales. También se reconoce el papel del trabajo colaborativo y del trabajo en equipo para potenciar la inteligencia colectiva y la construcción conjunta de soluciones.

      .col-lg-3.mt-4.mt-lg-0
        figure.mb-0
          img(src="@/assets/curso/temas/intro/foto.png" ).w-100.r-10

    .row.align-items-start.mt-4(data-aos="fade-right")
      .col-12.col-md-auto.mb-3.mb-md-0
        figure.mb-0
          img(src="@/assets/curso/temas/intro/icono-2.svg"  style="width: 84px")
      .col
        p.mb-0 De manera complementaria, el componente integra la resolución de problemas organizacionales para la dirección de personas, con énfasis en la argumentación, las alternativas creativas y la construcción de consensos. Estos elementos favorecen el aprendizaje activo, la reflexión sobre casos cercanos al contexto colombiano y la toma de decisiones informadas, para conectar los contenidos con situaciones reales del entorno organizacional.

    p.mt-4(data-aos="fade-right") Para ampliar la comprensión de los conceptos abordados y contextualizar su aplicación en la comunicación y el trabajo colaborativo, se recomienda acceder al recurso audiovisual que acompaña esta sección.

    //- El XD deja este espacio como marcador («Espacio para video») y ni el .xd ni el DI traen la
    //- URL: se queda el iframe del scaffold hasta que llegue el enlace real.
    .row.justify-content-center.align-items-center.mt-5
      .col-lg-12
        figure
          .video
            iframe(width="560" height="315" src="https://www.youtube.com/embed/vdPrCjWJSHo?si=X4NxENRo3LLXAua_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)

</template>

<script>
export default {
  name: 'Introduccion',
}
</script>

<style lang="sass"></style>
