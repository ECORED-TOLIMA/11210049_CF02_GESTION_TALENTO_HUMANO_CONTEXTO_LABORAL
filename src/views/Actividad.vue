<template lang="pug">
.curso-main-container.pb-3
  BannerInterno(icono="far fa-question-circle" titulo="Actividad didáctica")
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5
    #Actividad
    ActividadController(:cuestionario="cuestionario")

</template>

<script>
//- GENERADO por `scripts/gen_actividad.py` desde `11210049_CF02_AD.docx`.
//- No editar a mano: volver a correr el script si cambia el docx.
import ActividadController from '@ecored-sena/boulder-kit/plugin/components/actividad/ActividadController.vue'

export default {
  name: 'ActividadDidactica',
  components: {
    ActividadController,
  },
  data: () => ({
    cuestionario: {
      tema: 'Comunicación, trabajo colaborativo y asertividad',
      titulo: 'Cuestionario',
      introduccion:
        '<b>Objetivo:</b> evaluar la comprensión de los conceptos de comunicación organizacional, trabajo colaborativo, asertividad y resolución de problemas aplicados a la gestión del talento humano.',
      // el kit sólo muestra 10 de las 20: barajar es OBLIGATORIO
      barajarPreguntas: true,
      titulo_aprobado: '¡BUEN TRABAJO!',
      titulo_reprobado: 'VUELVA A INTENTARLO',
      // `mensaje_final_*`, NO `mensaje_*`: es el nombre que lee
      // `actividadCuestionario/Actividad.vue` del kit (1.0.9). Con el nombre corto los dos
      // mensajes finales del docx no se pintan nunca y no salta ningún error.
      mensaje_final_aprobado: 'Ha superado la actividad. Sus respuestas demuestran conocimientos sólidos sobre la comunicación organizacional, el trabajo colaborativo en equipo, la resolución de problemas y la asertividad para la dirección de personas.',
      mensaje_final_reprobado: 'No ha superado la actividad. Le recomendamos volver a revisar el componente formativo e intentar nuevamente la actividad didáctica.',
      preguntas: [
        {
          id: 1,
          texto: '¿Cuál es una función de la comunicación organizacional relacionada con compartir datos y resultados?',
          imagen: '@/assets/actividad/imagen1.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Función motivadora.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Función informativa.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Función integradora.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Función de control.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La función informativa permite transmitir datos, decisiones, indicadores y resultados necesarios para el funcionamiento de la organización.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 2,
          texto: '¿Qué componente del proceso comunicativo corresponde al medio por donde circula el mensaje?',
          imagen: '@/assets/actividad/imagen2.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Código.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Receptor.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Canal.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Contexto.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'El canal es el medio utilizado para transmitir el mensaje, como correos electrónicos, reuniones o plataformas digitales.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 3,
          texto: 'La comunicación no verbal incluye:',
          imagen: '@/assets/actividad/imagen3.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Únicamente documentos escritos.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Exclusivamente conversaciones orales.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Gestos, posturas y tono de voz.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Manuales y políticas institucionales.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La comunicación no verbal comprende elementos corporales y vocales que complementan o contradicen el mensaje verbal.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 4,
          texto: '¿Qué estudia la comunicación proxémica?',
          imagen: '@/assets/actividad/imagen4.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'El significado de las palabras.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'El uso del espacio y las distancias.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Los movimientos corporales.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'La redacción de mensajes escritos.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La comunicación proxémica analiza cómo las personas utilizan el espacio físico durante las interacciones.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 5,
          texto: '¿Cuál técnica de comunicación implica prestar atención plena al interlocutor?',
          imagen: '@/assets/actividad/imagen5.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Comunicación empática.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Escucha activa.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Argumentación.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Retroalimentación escrita.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La escucha activa requiere atención, interés y preguntas de clarificación para comprender correctamente al interlocutor.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 6,
          texto: '¿Qué riesgo puede presentarse cuando no existe claridad y precisión en el mensaje?',
          imagen: '@/assets/actividad/imagen6.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Motivación organizacional.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Sentido de pertenencia.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Confusión y errores operativos.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Innovación organizacional.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Los mensajes ambiguos generan malentendidos, conflictos y errores en los procesos laborales.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 7,
          texto: 'El trabajo colaborativo se caracteriza principalmente por:',
          imagen: '@/assets/actividad/imagen7.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'La competencia entre integrantes.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'La supervisión estricta.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'La construcción conjunta de soluciones.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'El trabajo individual aislado.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'En el trabajo colaborativo existe diálogo, negociación y co-creación para alcanzar objetivos comunes.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 8,
          texto: '¿Cuál es un principio fundamental del trabajo colaborativo?',
          imagen: '@/assets/actividad/imagen8.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Autoridad centralizada.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Interdependencia positiva.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Competencia individual.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Comunicación limitada.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La interdependencia positiva implica reconocer que el éxito individual depende también del éxito del grupo.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 9,
          texto: 'La técnica conocida como brainstorming tiene como objetivo:',
          imagen: '@/assets/actividad/imagen9.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Controlar el desempeño.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Sancionar errores.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Generar ideas creativas.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Elaborar manuales.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: '',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 10,
          texto: '¿Cuál es la función principal de la retroalimentación asertiva en el entorno laboral?',
          imagen: '@/assets/actividad/imagen10.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Señalar los errores del equipo de forma directa.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Comunicar observaciones con claridad y respeto.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Evitar el conflicto entre los integrantes del equipo.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Reforzar la autoridad del líder frente al grupo.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La retroalimentación asertiva permite expresar observaciones de manera clara y respetuosa, con el fin de fortalecer el desempeño individual y colectivo.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 11,
          texto: 'Un conflicto funcional en la organización:',
          imagen: '@/assets/actividad/imagen1.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Deteriora permanentemente el desempeño.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Impide la innovación.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Genera tensión productiva y cambio.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Elimina la comunicación.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Los conflictos funcionales pueden estimular mejoras, innovación y aprendizaje organizacional.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 12,
          texto: '¿Cuál es el primer paso en una metodología estructurada de resolución de problemas?',
          imagen: '@/assets/actividad/imagen2.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Implementar la solución.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Evaluar resultados.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Definir el problema con precisión.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Asignar sanciones.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Definir correctamente el problema evita confundir síntomas con causas reales.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 13,
          texto: 'La argumentación organizacional debe basarse en:',
          imagen: '@/assets/actividad/imagen3.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Opiniones personales sin evidencia.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Hechos y datos verificables.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Rumores organizacionales.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Emociones únicamente.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Una argumentación sólida utiliza información objetiva y verificable para sustentar posiciones.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 14,
          texto: 'El consenso organizacional implica:',
          imagen: '@/assets/actividad/imagen4.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Que todos piensen exactamente igual.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'La imposición de una sola opinión.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'La aceptación colectiva de una decisión.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Evitar cualquier desacuerdo.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'El consenso no significa unanimidad absoluta, sino aceptación y compromiso con la decisión tomada.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 15,
          texto: 'La asertividad se ubica entre:',
          imagen: '@/assets/actividad/imagen5.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Liderazgo y control.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Pasividad y agresividad.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Creatividad y disciplina.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Motivación y productividad.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La comunicación asertiva permite expresar ideas y necesidades con respeto y claridad.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 16,
          texto: '¿Cuál es una característica de la persona agresiva?',
          imagen: '@/assets/actividad/imagen6.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Expresa sus ideas respetando a los demás.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Evita cualquier conflicto.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Impone sus ideas sin considerar a otros.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Escucha activamente todas las opiniones.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La persona con estilo de comunicación agresivo tiende a imponer sus ideas sin considerar las necesidades ni las opiniones de los demás, lo que genera tensión y dificulta la colaboración en los equipos de trabajo.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 17,
          texto: '¿Qué estrategia fortalece la motivación y retención del talento humano?',
          imagen: '@/assets/actividad/imagen7.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Comunicación ambigua.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Reconocimiento y valoración.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Aislamiento laboral.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Falta de retroalimentación.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Reconocer los logros y esfuerzos incrementa el compromiso y el sentido de pertenencia.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 18,
          texto: '¿Cuál es una característica de la retroalimentación constructiva?',
          imagen: '@/assets/actividad/imagen8.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Se basa en descalificaciones personales.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Evita señalar oportunidades de mejora.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Se orienta al aprendizaje y mejora futura.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Busca generar temor.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La retroalimentación constructiva ayuda a mejorar el desempeño sin afectar la dignidad de la persona.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 19,
          texto: 'La comunicación kinésica se relaciona con:',
          imagen: '@/assets/actividad/imagen9.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Las normas organizacionales.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'El manejo del espacio físico.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Los movimientos corporales y gestos.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Los documentos institucionales.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La kinésica estudia expresiones faciales, posturas y movimientos corporales como formas de comunicación.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 20,
          texto: '¿Qué busca la comunicación empática?',
          imagen: '@/assets/actividad/imagen10.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Ignorar emociones del interlocutor.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Imponer decisiones rápidamente.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Considerar emociones y perspectivas del otro.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Limitar la participación grupal.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La comunicación empática tiene en cuenta las emociones, necesidades y expectativas del interlocutor para fortalecer las relaciones laborales.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
      ],
    },
  }),
}
</script>

<style lang="sass"></style>
