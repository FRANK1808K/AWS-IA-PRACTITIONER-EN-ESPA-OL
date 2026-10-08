# Módulo 4 — IA responsable: donde la técnica se encuentra con los derechos

> **Equivale a:** Dominio 4 del examen AWS AIF-C01 (14 %). Versión técnica: [Dominio 4](../domains/04-responsible-ai/README.md).
>
> **Lo que sabrás al terminar:** traducir los principios de "IA responsable" a conceptos jurídicos que ya conoces (igualdad, motivación, transparencia, diligencia debida) y saber qué herramienta técnica aporta **evidencia** de cumplimiento para cada uno.

---

## 1. Los pilares de la IA responsable, en clave jurídica

| Pilar técnico | Qué significa | Concepto jurídico equivalente | Herramienta de AWS que aporta evidencia |
|---|---|---|---|
| **Equidad** (*fairness*) | El sistema no perjudica sistemáticamente a ciertos grupos | **Igualdad y no discriminación** | SageMaker Clarify (mide el sesgo) |
| **Explicabilidad** | Poder explicar **por qué** el sistema decidió algo en un caso concreto | **Deber de motivación**; derecho a obtener una explicación en decisiones automatizadas | SageMaker Clarify (factores que influyeron en cada decisión) |
| **Transparencia** | Informar de que se usa IA, cómo se construyó y cuáles son sus límites | **Deber de información** al afectado | Model Cards (fichas del modelo), AI Service Cards |
| **Privacidad y seguridad** | Proteger los datos personales y el sistema | **Protección de datos**, secreto profesional | Cifrado, control de accesos, filtros de datos personales |
| **Robustez y veracidad** | Resultados correctos incluso ante situaciones imprevistas | **Diligencia debida**, calidad del servicio | Evaluaciones de modelos, detección de alucinaciones |
| **Seguridad del contenido** (*safety*) | Evitar contenido dañino | Protección de menores, honor, orden público | Bedrock Guardrails |
| **Controlabilidad / supervisión humana** | Que una persona pueda intervenir y corregir | **Derecho a intervención humana** | Amazon A2I (revisión humana) |
| **Gobernanza** | Procesos, responsables y registros a lo largo de todo el ciclo de vida | **Compliance**, rendición de cuentas (*accountability*) | Registros de auditoría, aprobaciones, documentación |

## 2. El sesgo: cómo discrimina una máquina sin "querer"

Un modelo aprende de datos del pasado. Si el pasado era injusto, **el modelo automatiza la injusticia**, a gran escala y con apariencia de objetividad.

| Tipo de sesgo | Qué ocurre | Ejemplo |
|---|---|---|
| **Sesgo histórico** | Los datos reflejan discriminaciones pasadas | Un modelo de selección entrenado con contrataciones de una época en la que casi no se contrataban mujeres |
| **Sesgo de muestreo** | Un grupo está poco representado en los datos | Reconocimiento facial que falla más con ciertos tonos de piel |
| **Sesgo por variables "proxy"** | Una variable aparentemente neutra sustituye a una protegida | El código postal funcionando como indicador indirecto del origen étnico |
| **Sesgo de automatización** | Las personas confían ciegamente en la máquina | Un funcionario que aprueba lo que sugiere el sistema sin revisarlo |

> **Idea clave para litigar o asesorar:** eliminar la variable "género" o "raza" **no elimina el sesgo** si hay variables que la sustituyen. Lo que demuestra diligencia es **medir el impacto por grupos** y documentarlo.

**¿Cómo se mide?** Herramientas como **SageMaker Clarify** comparan los resultados del modelo entre grupos (por ejemplo, la tasa de aprobación de créditos por edad o por sexo), antes y después de entrenarlo. **SageMaker Model Monitor** vigila que el sesgo no aparezca con el tiempo, cuando cambia la población de usuarios.

## 3. Explicabilidad: el deber de motivar aplicado a las máquinas

| Concepto | En lenguaje llano | Ejemplo |
|---|---|---|
| **Interpretabilidad** | El modelo es comprensible "por dentro" | Un árbol de decisión: "si los ingresos son menores de X y hay deudas, se rechaza" |
| **Explicabilidad** | Aunque el modelo sea una "caja negra", se puede explicar **qué factores pesaron** en una decisión concreta | "Su solicitud se rechazó principalmente por su nivel de endeudamiento (60 %) y su antigüedad laboral (25 %)" |

> **El dilema:** los modelos más precisos suelen ser los **menos interpretables**. En decisiones con efectos jurídicos sobre personas (crédito, empleo, prestaciones públicas), puede ser preferible un modelo algo menos preciso pero **explicable**, o complementar el modelo complejo con herramientas de explicabilidad y **revisión humana**.

**Conexión normativa:** el Reglamento General de Protección de Datos europeo (RGPD, art. 22) reconoce el derecho a no ser objeto de decisiones **basadas únicamente** en el tratamiento automatizado con efectos jurídicos significativos, con garantías como la **intervención humana**. Varias leyes latinoamericanas de protección de datos incluyen derechos similares. Ver [Módulo 6](06-mapa-regulatorio.md).

## 4. Transparencia y documentación: el "prospecto" del modelo

Una **Model Card** (ficha del modelo) es un documento estandarizado que describe:

- **Para qué** sirve el modelo y para qué **no** debe usarse.
- **Con qué datos** se entrenó.
- **Cómo se evaluó** y con qué resultados, incluido el análisis de sesgo.
- **Nivel de riesgo** y limitaciones conocidas.

> **Analogía:** es el **prospecto de un medicamento**: indicaciones, contraindicaciones y efectos secundarios. Para un abogado es **prueba documental** de que la organización actuó con diligencia.

## 5. Garantías de privacidad en los servicios gestionados

| Garantía | Qué significa | Qué revisar en el contrato |
|---|---|---|
| **No uso para entrenamiento** | Amazon Bedrock no usa tus prompts ni respuestas para entrenar los modelos base | Que el compromiso figure en los términos del servicio concreto contratado |
| **Exclusión centralizada** | AWS Organizations permite una política para que los servicios de IA no usen el contenido para mejorar sus servicios | Que la política esté activada en todas las cuentas |
| **Residencia de datos** | Los datos se procesan en la región elegida | Cuidado con la inferencia entre regiones: puede procesar en otros países de la misma zona geográfica |
| **Cifrado con claves propias** | La organización controla las claves (AWS KMS) | Quién custodia las claves y cómo se revocan |

## 6. Riesgos legales propios de la IA generativa

- **Propiedad intelectual:** contenido generado que reproduce obras protegidas, o modelos entrenados con obras sin licencia.
- **Responsabilidad por información falsa:** asesoramiento legal, médico o financiero erróneo.
- **Daño reputacional y pérdida de confianza.**
- **Impacto ambiental:** entrenar y usar modelos grandes consume mucha energía. Elegir el modelo **más pequeño que cumpla la tarea** también es una decisión de responsabilidad.

## 7. Para reflexionar

1. Un municipio usa un modelo para priorizar inspecciones. Un vecino alega discriminación por barrio. ¿Qué documentos pedirías en un procedimiento?
2. ¿Una Model Card bien hecha podría servir como prueba de diligencia? ¿Y si la organización no la actualizó?
3. ¿Cómo explicarías a un juez la diferencia entre "interpretabilidad" y "explicabilidad"?

⬅️ [Módulo 3](03-soluciones-en-la-nube.md) · ➡️ [Módulo 5 — Seguridad y gobernanza](05-seguridad-y-gobernanza.md)
