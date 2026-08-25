export default {
  global: {
    Name: 'Comunicación, trabajo colaborativo y asertividad',
    Description:
      'El componente formativo desarrolla la capacidad de comunicarse, colaborar y dirigir personas de forma efectiva en entornos laborales. Examina la comunicación verbal, no verbal y paralingüística; el trabajo en equipo; la resolución de conflictos organizacionales; y la asertividad en la dirección de personas, con el propósito de fortalecer la convivencia y los resultados colectivos.',
    imagenBannerPrincipal: '@/assets/curso/portada/ilustracion.png',
    fondoBannerPrincipal: '@/assets/curso/portada/fondo-banner.png',
    imagenesDecorativasBanner: [
      {
        clases: ['banner-principal-decorativo-1', 'd-none', 'd-lg-block'],
        imagen: '@/assets/curso/portada/decorativo-1.png',
      },
      {
        clases: ['banner-principal-decorativo-2', 'd-none', 'd-lg-block'],
        imagen: '@/assets/curso/portada/decorativo-2.png',
      },
    ],
  },
  menuPrincipal: {
    menu: [
      {
        nombreRuta: 'inicio',
        icono: 'fas fa-home',
        titulo: 'Volver al inicio',
      },
      {
        nombreRuta: 'introduccion',
        icono: 'fas fa-info-circle',
        titulo: 'Introducción',
        desarrolloContenidos: true,
      },
      {
        nombreRuta: 'tema1',
        numero: '1',
        titulo: 'Comunicación en el entorno organizacional',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '1.1',
            titulo: 'Fundamentos de la comunicación',
            hash: 't_1_1',
          },
          {
            numero: '1.2',
            titulo: 'Comunicación verbal y no verbal',
            hash: 't_1_2',
          },
          {
            numero: '1.3',
            titulo: 'Comunicación kinésica, proxémica y paralingüística',
            hash: 't_1_3',
          },
          {
            numero: '1.4',
            titulo: 'Comunicación efectiva en el trabajo',
            hash: 't_1_4',
          },
        ],
      },
      {
        nombreRuta: 'tema2',
        numero: '2',
        titulo: 'Trabajo colaborativo y en equipo',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '2.1',
            titulo: 'Tipos de trabajo grupal',
            hash: 't_2_1',
          },
          {
            numero: '2.2',
            titulo: 'Principios del trabajo colaborativo',
            hash: 't_2_2',
          },
          {
            numero: '2.3',
            titulo: 'Técnicas para el trabajo en equipo',
            hash: 't_2_3',
          },
          {
            numero: '2.4',
            titulo: 'Barreras y estrategias comunicativas',
            hash: 't_2_4',
          },
        ],
      },
      {
        nombreRuta: 'tema3',
        numero: '3',
        titulo: 'Resolución de problemas organizacionales',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '3.1',
            titulo: 'Tipos de conflicto organizacional',
            hash: 't_3_1',
          },
          {
            numero: '3.2',
            titulo: 'Argumentación y criterios de solución',
            hash: 't_3_2',
          },
          {
            numero: '3.3',
            titulo: 'Estrategias creativas de solución',
            hash: 't_3_3',
          },
          {
            numero: '3.4',
            titulo: 'Consensos y acuerdos',
            hash: 't_3_4',
          },
        ],
      },
      {
        nombreRuta: 'tema4',
        numero: '4',
        titulo: 'Asertividad en la dirección de personas',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '4.1',
            titulo: 'Concepto de asertividad',
            hash: 't_4_1',
          },
          {
            numero: '4.2',
            titulo: 'Comunicación asertiva en el trabajo',
            hash: 't_4_2',
          },
          {
            numero: '4.3',
            titulo: 'Estrategias para dirigir personas',
            hash: 't_4_3',
          },
        ],
      },
    ],
    subMenu: [
      {
        icono: 'fas fa-sitemap',
        titulo: 'Síntesis',
        nombreRuta: 'sintesis',
        desarrolloContenidos: true,
      },
      {
        nombreRuta: 'actividad',
        icono: 'far fa-question-circle',
        titulo: 'Actividad didáctica',
        desarrolloContenidos: true,
      },
      {
        nombreRuta: 'glosario',
        icono: 'fas fa-sort-alpha-down',
        titulo: 'Glosario',
      },
      {
        icono: 'fas fa-book',
        titulo: 'Referencias bibliográficas',
        nombreRuta: 'referencias',
      },
      {
        icono: 'fas fa-file-pdf',
        titulo: 'Descargar PDF',
        download: 'downloads/dist.pdf',
      },
      {
        icono: 'fas fa-download',
        titulo: 'Descargar material',
        download: 'downloads/material.zip',
      },
      {
        icono: 'far fa-registered',
        titulo: 'Créditos',
        nombreRuta: 'creditos',
      },
    ],
  },
  glosario: [
    {
      termino: 'Asertividad',
      significado:
        'capacidad de expresar ideas, sentimientos y necesidades de forma clara, directa y respetuosa, sin agredir a otros ni renunciar a los propios derechos.',
    },
    {
      termino: 'Comunicación asertiva',
      significado:
        'modo de interacción verbal en el que se expresan expectativas, críticas y acuerdos de forma honesta y empática, orientado a preservar relaciones y alcanzar acuerdos.',
    },
    {
      termino: 'Comunicación kinésica',
      significado:
        'uso del movimiento corporal: gestos, posturas, expresiones faciales y contacto visual como canal para transmitir mensajes en una interacción.',
    },
    {
      termino: 'Comunicación no verbal',
      significado:
        'conjunto de señales no lingüísticas: gestos, postura, silencios y uso del espacio que complementan o modifican el significado del mensaje verbal.',
    },
    {
      termino: 'Conflicto organizacional',
      significado:
        'situación en la que dos o más personas o grupos perciben que sus intereses o metas son incompatibles, generando tensión que exige una respuesta colectiva.',
    },
    {
      termino: 'Consenso',
      significado:
        'acuerdo colectivo alcanzado mediante el diálogo, en el que todas las partes aceptan la decisión sin objeciones fundamentales, aunque no coincida con la preferencia inicial de cada uno.',
    },
    {
      termino: 'Escucha activa',
      significado:
        'proceso de atención plena al interlocutor que implica comprender el mensaje verbal y no verbal, sin interrumpir ni emitir juicios prematuros.',
    },
    {
      termino: 'Proxémica',
      significado:
        'estudio del uso del espacio físico en la comunicación; incluye la distancia interpersonal adoptada según el tipo de relación y el contexto cultural.',
    },
    {
      termino: 'Trabajo colaborativo',
      significado:
        'modalidad de trabajo grupal en la que los integrantes construyen conjuntamente conocimiento y soluciones mediante el diálogo y la reflexión compartida.',
    },
  ],
  referencias: [
    {
      referencia:
        'Comunicación asertiva como factor relevante en el recurso humano. (2024). <em>Experior. Revista de ciencias aplicadas</em>.',
    },
    {
      referencia:
        'Comunicación asertiva: la clave en el liderazgo organizacional. (2024). <em>Repositorio RedCol – MinCiencias</em>.',
    },
    {
      referencia:
        'Estilos de comunicación y recursos humanos: la asertividad en la organización. (2019). <em>Universidad de Buenos Aires</em>.',
    },
    {
      referencia:
        'Fernández Romero, A. (2010). <em>Creatividad e innovación en empresas y organizaciones: técnicas para la resolución de problemas</em>. Díaz de Santos.',
    },
    {
      referencia:
        'Gonçalves, S. (2024). <em>La gestión de la comunicación organizacional: un enfoque estratégico</em>. Tecnos.',
    },
    {
      referencia:
        'IESE Business School. (2026). <em>Tres modelos de gestión del conflicto organizativo</em>. IESE Insight.',
    },
    {
      referencia:
        'Ruiz Hernández, Y. E., y Sánchez Jaramillo, A. F. (2021). Caracterización de las actividades de trabajo en equipo en una empresa. <em>Revista Perspectiva Empresarial, 8</em>(2), 122-138.',
    },
    {
      referencia:
        'Trujillo Vargas, J. J. (2023). <em>Fórmulas para una comunicación organizacional efectiva</em>. Tecnos.',
    },
    {
      referencia:
        'Universidad Autónoma del Estado de Hidalgo. (s. f.). Técnica: solución creativa de problemas. <em>Revista ICEA</em>.',
    },
  ],
  creditos: [
    {
      titulo: 'ECOSISTEMA DE RECURSOS EDUCATIVOS DIGITALES',
      autores: [
        {
          nombre: 'Claudia Johanna Gómez Pérez ',
          cargo:
            'Profesional G06. Responsable Ecosistema Virtual de Recursos Educativos Digitales',
          centro: 'Centro Agroturístico - Regional Santander',
        },
        {
          nombre: 'Diana Rocío Possos Beltrán',
          cargo: 'Responsable de línea de producción ',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
    {
      titulo: 'CONTENIDO INSTRUCCIONAL',
      autores: [
        {
          nombre: 'Norma Constanza Morales Cruz',
          cargo: 'Experta temática',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Gloria Lida Alzate Suárez',
          cargo: 'Evaluadora instruccional',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
    {
      titulo: 'DISEÑO Y DESARROLLO DE RECURSOS EDUCATIVOS DIGITALES',
      autores: [
        {
          nombre: 'Juan Daniel Polanco Muñoz',
          cargo: 'Diseñador de contenidos digitales',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Manuel Felipe Echavarria Orozco',
          cargo: 'Desarrollador <em>full stack</em>',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Gilberto Junior Rodríguez Rodríguez',
          cargo: 'Animador y productor audiovisual',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
    {
      titulo: 'VALIDACIÓN RECURSO EDUCATIVO DIGITAL',
      autores: [
        {
          nombre: 'María Fernanda Pineda Mora',
          cargo: 'Evaluadora de contenidos inclusivos y accesibles',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Javier Mauricio Oviedo',
          cargo: 'Validador y vinculador de recursos educativos digitales',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
  ],
  creditosAdicionales: {
    imagenes:
      'Fotografías y vectores tomados de <a href="https://www.freepik.es/" target="_blank">www.freepik.es</a>, <a href="https://www.shutterstock.com/" target="_blank">www.shutterstock.com</a>, <a href="https://unsplash.com/" target="_blank">unsplash.com </a>y <a href="https://www.flaticon.com/" target="_blank">www.flaticon.com</a>',
    creativeCommons:
      'Licencia creative commons CC BY-NC-SA<br><a href="https://creativecommons.org/licenses/by-nc-sa/2.0/" target="_blank">ver licencia</a>',
  },
}
