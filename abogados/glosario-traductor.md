# Glosario Traductor — Tecnología ↔ Derecho

> Cada término técnico con su explicación en lenguaje llano y el **concepto jurídico** con el que mejor se relaciona. Las analogías ayudan a entender; no implican que los conceptos sean jurídicamente equivalentes.

## 1. Conceptos de IA

| Término técnico | En lenguaje llano | Concepto jurídico relacionado |
|---|---|---|
| **Algoritmo** | Procedimiento paso a paso para resolver un problema | Procedimiento reglado |
| **Modelo** | El resultado del entrenamiento: la "fórmula" aprendida que produce respuestas | Objeto de derechos (secreto empresarial, propiedad intelectual) |
| **Entrenamiento** | Proceso en que el modelo aprende a partir de datos | Tratamiento de datos; posible uso de obras protegidas |
| **Inferencia** | Uso del modelo ya entrenado para obtener una respuesta | Tratamiento de los datos introducidos |
| **Dataset** | Conjunto de datos usados para entrenar o evaluar | Base de datos (derecho *sui generis* en algunos países); origen y licencias |
| **Etiqueta** | La respuesta correcta asociada a un ejemplo | Calificación hecha por personas: puede arrastrar sus sesgos |
| **Sesgo** | Error sistemático que perjudica a ciertos grupos | Discriminación directa o indirecta |
| **Variable proxy** | Dato aparentemente neutro que sustituye a uno protegido | Discriminación indirecta |
| **Sobreajuste** (*overfitting*) | El modelo memoriza los ejemplos y falla con casos nuevos | Riesgo de memorizar y revelar datos personales del entrenamiento |
| **Falso positivo / negativo** | Acusar a un inocente / dejar pasar a un culpable | Error de tipo I y II; presunción de inocencia |
| **Explicabilidad** | Poder explicar por qué se tomó una decisión concreta | Deber de motivación; derecho a explicación |
| **Interpretabilidad** | El modelo es comprensible por dentro | Transparencia del procedimiento |
| **Drift** (deriva) | El modelo empeora porque la realidad cambia | Deber de vigilancia y diligencia continuada |

## 2. IA generativa

| Término técnico | En lenguaje llano | Concepto jurídico relacionado |
|---|---|---|
| **Modelo fundacional / LLM** | Modelo enorme y general que genera texto, imágenes o código | Producto o servicio del proveedor; licencia de uso |
| **Prompt** | La instrucción que se da a la IA | Puede contener información confidencial: comunicación con un tercero |
| **Token** | Trozo de texto; unidad de cobro | Base del precio del servicio |
| **Ventana de contexto** | Cuánto texto "ve" la IA a la vez | Límite técnico del análisis documental |
| **Temperatura** | Grado de creatividad o aleatoriedad | Previsibilidad del resultado |
| **Alucinación** | Respuesta falsa presentada como cierta | Error; posible negligencia profesional si no se verifica |
| **RAG** | La IA consulta documentos verificados antes de responder y los cita | Fundamentación con fuentes; trazabilidad |
| **Fine-tuning** | Reentrenar el modelo con datos propios | Incorporación de datos al modelo: titularidad y licencias |
| **Embedding** | Huella numérica del significado de un texto | Representación derivada de datos (posible dato personal) |
| **Prompt injection** | Instrucciones maliciosas que "secuestran" a la IA | Ataque informático; fraude; deber de seguridad |
| **Jailbreak** | Técnicas para que la IA se salte sus restricciones | Uso indebido; vulneración de términos de servicio |
| **IA agéntica / agente** | IA que planifica y ejecuta acciones | Mandato, representación, responsabilidad por actos de auxiliares |
| **MCP** | Estándar abierto para conectar agentes con herramientas y datos | Acceso a sistemas de terceros: autorizaciones y responsabilidad |
| **Context engineering** | Decidir qué información recibe la IA en cada consulta | Minimización de datos |
| **Contenido sintético / deepfake** | Imagen, audio o video generado por IA | Derecho a la propia imagen, honor; deber de marcar el contenido |

## 3. Nube y AWS

| Término técnico | En lenguaje llano | Concepto jurídico relacionado |
|---|---|---|
| **Nube** (*cloud*) | Usar servidores de un proveedor en lugar de propios | Contratación de servicios; encargo de tratamiento |
| **Región** | Ubicación geográfica de los centros de datos | Localización de datos; transferencias internacionales |
| **Cross-region inference** | El proveedor puede procesar en otra región de la misma zona | Transferencias internacionales no evidentes |
| **Responsabilidad compartida** | Reparto de tareas de seguridad entre AWS y el cliente | Reparto contractual de obligaciones |
| **Amazon Bedrock** | Plataforma para usar modelos de varios proveedores | Proveedor de servicios de IA |
| **Knowledge Base** | Repositorio de documentos que la IA consulta | Archivo documental con control de acceso |
| **Guardrails** | Filtros automáticos de contenido y datos personales | Medidas técnicas de cumplimiento |
| **IAM** | Gestión de quién puede hacer qué | Poderes y facultades; mínimo privilegio |
| **SCP** | Límites para todas las cuentas de una organización | Políticas corporativas obligatorias |
| **PrivateLink / VPC endpoint** | Conexión privada sin pasar por internet | Canal seguro de comunicación |
| **KMS / cifrado** | Protección de datos con claves | Medidas de seguridad; control de acceso |
| **CloudTrail** | Registro de quién hizo qué y cuándo | Libro de registro; evidencia |
| **Invocation logging** | Registro del contenido de las consultas a la IA | Transcripción; evidencia; datos personales a proteger |
| **Model Card** | Ficha del modelo con su uso previsto y sus límites | Documentación técnica; prueba de diligencia |
| **SageMaker Clarify** | Herramienta que mide sesgo y explica decisiones | Prueba de no discriminación y de motivación |
| **Amazon A2I** | Envía casos a revisión humana | Intervención humana en decisiones automatizadas |
| **AWS Artifact** | Informes de certificación del proveedor | Due diligence documental |
| **AI services opt-out policy** | Impide que AWS use el contenido para mejorar sus servicios de IA | Limitación de finalidad del encargado |

## 4. Siglas frecuentes

| Sigla | Significado |
|---|---|
| **AI Act** | Reglamento de Inteligencia Artificial de la Unión Europea |
| **RGPD / GDPR** | Reglamento General de Protección de Datos de la UE |
| **LGPD** | Lei Geral de Proteção de Dados (Brasil) |
| **DPA** | *Data Processing Agreement*: contrato de encargo de tratamiento |
| **DPIA / EIPD** | Evaluación de impacto relativa a la protección de datos |
| **GPAI** | *General-Purpose AI*: modelos de IA de uso general |
| **SLA** | *Service Level Agreement*: acuerdo de nivel de servicio |
| **FM / LLM** | *Foundation Model* / *Large Language Model* |
| **RAG** | *Retrieval-Augmented Generation*: generación aumentada por recuperación |
| **AIF-C01** | Código del examen AWS Certified AI Practitioner |

⬅️ [Checklist](checklist-contratacion-ia.md) · 🏠 [Inicio de la guía para abogados](README.md)
