# Módulo 6 — Mapa regulatorio de la IA (actualizado a octubre de 2026)

> **No forma parte del examen AWS**, pero es el puente natural entre el derecho y la tecnología. El examen solo exige *reconocer* que existen regulaciones y marcos de gobernanza (Dominio 5).
>
> ⚠️ **Aviso:** este módulo es material de estudio, no asesoramiento jurídico. La regulación de la IA cambia mes a mes: **verifica siempre la versión vigente en las fuentes oficiales** (diarios oficiales y portales legislativos) antes de aplicarla a un caso.

---

## 1. Tres formas de regular la IA

| Enfoque | Idea | Ejemplo |
|---|---|---|
| **Basado en riesgo** | Más obligaciones cuanto mayor es el riesgo para las personas | Reglamento de IA de la UE (AI Act); proyecto brasileño PL 2338/2023; ley peruana |
| **Sectorial / normas existentes** | Aplicar las leyes ya vigentes (protección de datos, consumo, no discriminación, responsabilidad civil) | Estados Unidos a nivel federal; la mayoría de países latinoamericanos hoy |
| **Principios y *soft law*** | Recomendaciones éticas no vinculantes | Recomendación de la UNESCO sobre la ética de la IA (2021); Principios de IA de la OCDE |

> **Idea clave:** aunque un país no tenga "ley de IA", la IA **ya está regulada** por la protección de datos, el derecho del consumo, la prohibición de discriminación, la propiedad intelectual, la responsabilidad civil y las normas de cada profesión.

## 2. Unión Europea: el Reglamento de IA (AI Act)

### 2.1 La pirámide de riesgos

```text
                 ▲
                / \        RIESGO INACEPTABLE → PROHIBIDO
               /   \       (p. ej., puntuación social, manipulación dañina,
              /     \       ciertos usos de reconocimiento biométrico)
             /───────\
            /         \    ALTO RIESGO → obligaciones estrictas
           /           \   (empleo, crédito, educación, servicios esenciales,
          /             \   justicia, migración; IA en productos regulados)
         /───────────────\
        /                 \   RIESGO DE TRANSPARENCIA → informar
       /                   \  (chatbots, deepfakes, contenido generado por IA)
      /─────────────────────\
     /                       \  RIESGO MÍNIMO → sin obligaciones específicas
    /_________________________\ (filtros de spam, videojuegos)

   + Modelos de IA de uso general (GPAI): obligaciones propias de documentación,
     transparencia y respeto de los derechos de autor; más exigentes si tienen "riesgo sistémico".
```

### 2.2 Calendario tras el *Digital Omnibus* de 2026

En 2026 la UE aprobó un paquete de simplificación (*Digital Omnibus*) que **aplazó** las obligaciones de alto riesgo. Según el análisis de varios despachos internacionales, el calendario queda así:

| Fecha | Qué se aplica |
|---|---|
| 1-ago-2024 | Entrada en vigor del Reglamento |
| 2-feb-2025 | **Prácticas prohibidas** y reglas de **alfabetización en IA** (el Omnibus revisó el alcance de estas últimas: verifica el texto vigente) |
| 2-ago-2025 | Obligaciones de los **modelos de uso general** (GPAI) |
| 2-ago-2026 | **Obligaciones de transparencia** (art. 50): informar de que se interactúa con una IA, marcar contenido sintético… |
| 2-dic-2026 | Nuevas prohibiciones añadidas por el Omnibus (IA para generar imágenes íntimas no consentidas y material de abuso sexual infantil) y plazo de marcado de contenido para sistemas ya comercializados |
| **2-dic-2027** | Sistemas de **alto riesgo del Anexo III** (empleo, crédito, educación, etc.), antes previsto para agosto de 2026 |
| **2-ago-2028** | IA de alto riesgo integrada en **productos regulados** (Anexo I: dispositivos médicos, maquinaria…) |

**Multas previstas:** hasta 35 millones de euros o el 7 % de la facturación mundial anual por prácticas prohibidas, y escalas menores para otros incumplimientos.

> **¿Por qué le importa a un abogado latinoamericano?** El Reglamento tiene **alcance extraterritorial**: se aplica a proveedores que comercialicen sistemas en la UE y a sistemas cuyos **resultados se utilicen en la UE**, aunque la empresa esté fuera. Además, ha servido de **modelo** para los proyectos de Brasil, Chile, Colombia y otros países.

### 2.3 Roles principales

| Rol | Quién es | Obligaciones en síntesis |
|---|---|---|
| **Proveedor** | Quien desarrolla el sistema y lo comercializa con su nombre | Evaluación de conformidad, documentación técnica, gestión de riesgos, calidad de los datos |
| **Responsable del despliegue** (*deployer*) | Quien usa el sistema bajo su autoridad (un banco, un despacho, una administración) | Usarlo según las instrucciones, supervisión humana, informar a los afectados y, en ciertos casos, evaluar el impacto en los derechos fundamentales |
| **Importador / distribuidor** | Quien introduce o distribuye sistemas de terceros | Verificar que el proveedor cumplió |

## 3. Protección de datos: la norma de IA que ya existe

| Jurisdicción | Norma principal | Puntos clave para IA |
|---|---|---|
| **Unión Europea** | RGPD (Reglamento (UE) 2016/679) | Art. 22 (decisiones automatizadas), evaluación de impacto (art. 35), minimización, transferencias internacionales |
| **Brasil** | LGPD (Ley 13.709/2018) | Art. 20: derecho a solicitar la **revisión** de decisiones tomadas únicamente con base en tratamiento automatizado |
| **México** | Ley Federal de Protección de Datos Personales en Posesión de los Particulares (nueva ley de 2025) | Principios de información y finalidad; derechos ARCO |
| **Colombia** | Ley 1581 de 2012 | Autorización del titular, finalidad, transferencias internacionales |
| **Argentina** | Ley 25.326 | Principios de calidad y finalidad de los datos |
| **Chile** | Ley 21.719 (2024), que entra en vigor el **1-dic-2026** | Nueva ley con autoridad de control y derechos frente a decisiones automatizadas |
| **Perú** | Ley 29733 | Consentimiento, finalidad, transferencias |

> Verifica siempre el texto vigente y la normativa de desarrollo de cada país.

## 4. Leyes y proyectos específicos de IA en América Latina

| País | Situación (octubre de 2026) |
|---|---|
| **Perú** | **Ley 31814 (2023)** que promueve el uso de la IA, con **reglamento** que clasifica los sistemas por niveles de riesgo. Es el marco más avanzado de la región. |
| **Brasil** | **PL 2338/2023** aprobado por el Senado en diciembre de 2024, en trámite en la Cámara de Diputados (comisión especial). Si la Cámara lo modifica, vuelve al Senado. |
| **Chile** | Proyecto de ley de IA en trámite en el Congreso; la nueva ley de datos (21.719) entra en vigor en diciembre de 2026. |
| **Colombia** | Proyecto de ley en trámite (PL 043/2025 Senado), además de documentos de política pública y un *sandbox* regulatorio. |
| **México** | Iniciativas de ley general en comisiones; se aplica la normativa de datos personales y la regulación sectorial. |
| **Argentina** | Principios y disposiciones administrativas, sin ley general de IA. |

**Internacional:** el **Convenio Marco del Consejo de Europa sobre IA y derechos humanos** (abierto a la firma en 2024) es el primer tratado internacional vinculante sobre IA, y está abierto también a Estados no europeos.

## 5. Propiedad intelectual: los litigios que marcan el camino

| Caso | Jurisdicción | Qué se discute | Estado |
|---|---|---|---|
| ***Thomson Reuters v. Ross Intelligence*** | EE. UU. | ¿Es "uso legítimo" (*fair use*) copiar los resúmenes de Westlaw para entrenar una IA jurídica competidora? | El tribunal de distrito dijo que **no** (2025) y el Tercer Circuito **confirmó** en septiembre de 2026, primera decisión de apelación sobre IA y *fair use*. Muy relevante para la **legaltech**. |
| ***Bartz v. Anthropic*** | EE. UU. | Uso de libros para entrenar modelos | En 2025 el juez consideró *fair use* el entrenamiento con copias adquiridas legalmente, pero no el uso de copias pirateadas. Acuerdo de **USD 1 500 millones** aprobado en julio de 2026, que **no crea precedente**. |
| ***Kadrey v. Meta*** | EE. UU. | Entrenamiento con libros | En 2025, el juez falló a favor de Meta por falta de prueba del daño al mercado, advirtiendo que con mejor prueba el resultado podría cambiar. |
| ***Getty Images v. Stability AI*** | Reino Unido | Entrenamiento con imágenes y reproducción de marcas de agua | En noviembre de 2025, Stability ganó en lo principal (el entrenamiento se hizo fuera del Reino Unido); Getty obtuvo permiso para apelar. |
| ***Thaler v. Perlmutter*** | EE. UU. | ¿Puede una IA ser autora de una obra? | No: la protección por derechos de autor exige **autoría humana**. |

> **Dos preguntas distintas que un abogado debe separar:** (1) ¿es lícito **entrenar** con obras ajenas? (2) ¿quién es titular de lo que **genera** la IA, y puede infringir derechos de terceros?

## 6. Responsabilidad profesional del abogado que usa IA

- **Deber de competencia:** conocer las capacidades y los límites de la herramienta que se usa. La **Opinión Formal 512 de la ABA** (Estados Unidos, julio de 2024) es una referencia sobre IA generativa en la abogacía: competencia, confidencialidad, comunicación con el cliente y honorarios razonables.
- **Confidencialidad y secreto profesional:** no introducir información del cliente en herramientas sin garantías contractuales adecuadas.
- **Deber de verificación:** toda cita, dato o precedente debe comprobarse en la fuente original (ver *Mata v. Avianca* en el [Módulo 2](02-ia-generativa.md#3-alucinaciones-el-riesgo-número-uno-para-un-abogado)).
- **Transparencia con el cliente y el tribunal:** varios tribunales exigen declarar el uso de IA en los escritos. Revisa las normas locales.

## 7. ¿Qué normas reviso según el caso?

| Si el caso trata de… | Revisa |
|---|---|
| Selección de personal con IA | Protección de datos (decisiones automatizadas), no discriminación laboral, AI Act (alto riesgo) si hay conexión con la UE |
| Crédito o seguros | Protección de datos, normativa financiera y de consumo, explicabilidad, AI Act (alto riesgo) |
| Chatbot de atención al cliente | Consumo, deber de informar que es una IA (AI Act, art. 50), protección de datos |
| Contenido generado (imágenes, textos) | Propiedad intelectual, derechos de imagen y honor, marcado de contenido sintético |
| Contratación de un proveedor de IA | Contrato de encargo de tratamiento, transferencias internacionales, confidencialidad, propiedad intelectual, SLA ([checklist](checklist-contratacion-ia.md)) |
| Uso de IA dentro del despacho | Deontología profesional, secreto profesional, política interna de uso |

⬅️ [Módulo 5](05-seguridad-y-gobernanza.md) · ➡️ [Casos prácticos](casos-practicos.md)

---

**Fuentes consultadas (octubre de 2026):** análisis del *Digital Omnibus* de [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) y [Orrick](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes); tramitación del [PL 2338/2023 en el Senado de Brasil](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233); panorama latinoamericano de [ParlAmericas (enero de 2026)](https://parlamericas.org/uploads/documents/Presentation-ArtificialIntelligence-DL-sp.pdf); [Mata v. Avianca](https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.); [Thomson Reuters v. Ross en apelación](https://ipwatchdog.com/2026/09/30/third-circuit-affirms-revised-fair-use-ruling-against-ross-ai-legal-research-platform-in-sealed-opinion/); [acuerdo Bartz v. Anthropic](https://authorsalliance.org/bartz-v-anthropic-settlement-faq/); [Getty v. Stability AI](https://cm.twobirds.com/en/insights/2025/uk/stability-ai-defeats-getty-images-copyright-claims-in-first-of-its-kind-dispute-before-the-high-cour).
