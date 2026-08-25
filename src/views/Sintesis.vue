<template lang="pug">
.curso-main-container.pb-3
  BannerInterno(icono="fas fa-sitemap" titulo="Síntesis")
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5

    p(data-aos="fade-down") El componente formativo aborda la comunicación, el trabajo colaborativo y la asertividad como capacidades que se potencian de manera conjunta para mejorar las interacciones y los resultados en los entornos laborales. Explora la comunicación organizacional desde sus fundamentos hasta su uso efectivo en los equipos, reconociendo sus formas verbales y no verbales, así como las barreras que la dificultan; el trabajo colaborativo y las bases que permiten construir grupos integrados y orientados a un propósito común; la resolución de conflictos como proceso que transforma las diferencias en oportunidades de acuerdo; y la asertividad como habilidad para orientar las personas, retroalimentar con criterio constructivo y sostener vínculos de trabajo respetuosos y productivos.

    p.mt-4.mb-0(data-aos="fade-down") A continuación, se presenta el mapa conceptual que organiza de manera visual los ejes temáticos del componente y las relaciones que los articulan:

    //- El mapa del XD mide 1245 px y el ancho útil de la tarjeta es 1228: se ajusta a él.
    //- El texto alternativo lo deja escrito el pasteboard del XD.
    figure.mt-4(data-aos="fade-down")
      img(src="@/assets/curso/sintesis.svg" alt="Se presenta un mapa conceptual conformado por cuatro ejes: comunicación organizacional, trabajo colaborativo, resolución de conflictos y asertividad, como base para mejorar el desempeño y la convivencia laboral." style="width: 1228px").m-auto

    .row.justify-content-center.mt-5
      .col-auto
        a.anexo(:href="obtenerLink('/downloads/Sintesis.pdf')" target="_blank")
          .anexo__icono
            img(src="@/assets/bullets/icono-pdf.svg")
          .anexo__texto
            p Anexo. Síntesis
</template>

<script>
export default {
  name: 'Sintesis',
  mounted() {
    this.$nextTick(() => {
      this.$aosRefresh()
    })
  },
  updated() {
    this.$aosRefresh()
  },
}
</script>

<style lang="sass"></style>
