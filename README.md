# AWS Certified AI Practitioner (AIF-C01) — Guía de Preparación en Español

[![AWS Certified AI Practitioner](https://img.shields.io/badge/AWS%20Certified-AI%20Practitioner%20%28AIF--C01%29-FF9900?logo=amazonwebservices&logoColor=white)](https://aws.amazon.com/certification/certified-ai-practitioner/)
[![Versión](https://img.shields.io/badge/versi%C3%B3n-1.0.0-blue)](#roadmap)
[![Docs lint](https://github.com/FRANK1808K/AWS-IA-PRACTITIONER-EN-ESPA-OL/actions/workflows/docs-lint.yml/badge.svg)](https://github.com/FRANK1808K/AWS-IA-PRACTITIONER-EN-ESPA-OL/actions/workflows/docs-lint.yml)
[![Idioma](https://img.shields.io/badge/idioma-espa%C3%B1ol-c60b1e)](#índice)
[![Actualizado](https://img.shields.io/badge/actualizado-2026--10-informational)](#roadmap)
[![PRs bienvenidos](https://img.shields.io/badge/PRs-bienvenidos-brightgreen)](CONTRIBUTING.md)

Documentación técnica, modular y en español para preparar el examen **AWS Certified AI Practitioner (AIF-C01)**, orientada a ingenieros cloud, desarrolladores y especialistas en datos. Combina teoría alineada con los dominios oficiales, criterios de selección de servicios, laboratorios prácticos con IAM de mínimo privilegio y estimación de costos, cheatsheets de decisión rápida y preguntas de práctica originales.

> **Aviso:** proyecto comunitario no afiliado a Amazon Web Services. Los servicios de AWS evolucionan rápidamente: contrasta siempre con la [guía oficial del examen](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html) y la documentación oficial. Las preguntas de práctica son originales y no proceden de exámenes reales.

---

## Índice

- [El examen en una tabla](#el-examen-en-una-tabla)
- [Dominios](#dominios)
- [Estructura de directorios](#estructura-de-directorios)
- [Guía de estudio recomendada](#guía-de-estudio-recomendada)
- [Roadmap](#roadmap)
- [Cómo contribuir](#cómo-contribuir)
- [Recursos oficiales](#recursos-oficiales)

---

## El examen en una tabla

| Aspecto | Detalle |
|---|---|
| **Código** | AIF-C01 |
| **Nivel** | Foundational |
| **Candidato objetivo** | Hasta 6 meses de exposición a IA/ML en AWS; usa (no necesariamente construye) soluciones de IA/ML |
| **Preguntas** | 65 (50 puntúan + 15 sin puntuación) |
| **Tipos de pregunta** | Opción múltiple, respuesta múltiple, ordenación, emparejamiento, casos de estudio |
| **Duración** | 90 minutos |
| **Puntaje mínimo** | 700 / 1000 |
| **Costo** | USD 100 |
| **Vigencia** | 3 años |

---

## Dominios

| # | Dominio | Peso | Documento | Temas clave |
|---|---|---|---|---|
| 1 | Fundamentos de IA y ML | **20 %** | [`domains/01-fundamentals-ai-ml`](domains/01-fundamentals-ai-ml/README.md) | AI/ML/DL/GenAI, tipos de aprendizaje, ciclo de vida de ML, métricas |
| 2 | Fundamentos de IA Generativa | **24 %** | [`domains/02-fundamentals-generative-ai`](domains/02-fundamentals-generative-ai/README.md) | FMs y LLMs, tokens, temperatura/Top-P/Top-K, RAG vs. fine-tuning, alucinaciones |
| 3 | Aplicaciones de Modelos Fundacionales | **28 %** | [`domains/03-applications-foundation-models`](domains/03-applications-foundation-models/README.md) | Bedrock (KB, Agents, Guardrails), JumpStart, servicios de IA, Amazon Q |
| 4 | Directrices de IA Responsable | **14 %** | [`domains/04-responsible-ai`](domains/04-responsible-ai/README.md) | Equidad, explicabilidad, Clarify, Model Cards, Model Monitor, privacidad |
| 5 | Seguridad, Cumplimiento y Gobernanza | **14 %** | [`domains/05-security-compliance-governance`](domains/05-security-compliance-governance/README.md) | Responsabilidad compartida, IAM, PrivateLink, CloudTrail/CloudWatch, costos |

```mermaid
pie showData
    title Peso de los dominios en AIF-C01
    "D1 Fundamentos IA/ML" : 20
    "D2 Fundamentos GenAI" : 24
    "D3 Aplicaciones de FMs" : 28
    "D4 IA Responsable" : 14
    "D5 Seguridad y Gobernanza" : 14
```

---

## Estructura de directorios

```text
.
├── README.md                                   # Este documento: visión general, plan de estudio y roadmap
├── CONTRIBUTING.md                             # Convenciones de nombres, estilo y flujo de contribución
├── .markdownlint-cli2.jsonc                    # Reglas de estilo Markdown
├── .github/
│   ├── scripts/check_links.py                  # Validación de enlaces relativos y anclas
│   └── workflows/docs-lint.yml                 # CI: markdownlint + enlaces + JSON + sintaxis Python
├── domains/                                    # Teoría por dominio oficial del examen
│   ├── 01-fundamentals-ai-ml/README.md         # D1 (20 %)
│   ├── 02-fundamentals-generative-ai/README.md # D2 (24 %)
│   ├── 03-applications-foundation-models/README.md  # D3 (28 %)
│   ├── 04-responsible-ai/README.md             # D4 (14 %)
│   └── 05-security-compliance-governance/README.md  # D5 (14 %)
├── labs/                                       # Laboratorios prácticos en AWS
│   ├── README.md                               # Catálogo de labs y reglas de seguridad
│   ├── template.md                             # Plantilla estándar de laboratorio
│   └── lab-01-rag-bedrock-knowledge-bases/
│       ├── README.md                           # Guía paso a paso (CLI), costos y limpieza
│       ├── policies/                           # Trust/permissions IAM y políticas de OpenSearch Serverless
│       ├── scripts/                            # create_vector_index.py, query_kb.py, requirements.txt
│       └── sample-data/                        # Documentos ficticios a indexar
├── cheatsheets/                                # Repaso rápido
│   ├── README.md
│   ├── exam-decision-matrix.md                 # 40 escenarios requisito + restricción → servicio
│   └── glossary.md                             # Glosario español–inglés
└── practice-questions/                         # Banco de preguntas originales por dominio
    ├── README.md                               # Formato del examen y plantilla de preguntas
    └── domain-0{1..5}-questions.md
```

---

## Guía de estudio recomendada

Plan de **6 semanas** con una dedicación de **6–8 horas por semana**. Los pesos del examen guían la asignación de tiempo: el Dominio 3 recibe dos semanas.

| Semana | Objetivos | Entregables | Servicios clave | Horas |
|---|---|---|---|---|
| **1** — D1 | Dominar la terminología de IA/ML, los tipos de aprendizaje, el ciclo de vida de ML y las métricas. | Mapa mental AI/ML/DL/GenAI · Tabla propia "métrica → cuándo priorizarla" · [Preguntas D1](practice-questions/domain-01-questions.md) ≥ 80 % | SageMaker AI (Canvas, Autopilot, Ground Truth, Data Wrangler, Feature Store, Pipelines, Model Registry) | 6 |
| **2** — D2 | Comprender FMs/LLMs, tokens, parámetros de inferencia y técnicas de adaptación; reconocer limitaciones. | Tabla comparativa PE vs. RAG vs. FT vs. pre-entrenamiento explicada con tus palabras · Experimentar con temperatura/Top-P en el *playground* de Bedrock · [Preguntas D2](practice-questions/domain-02-questions.md) ≥ 80 % | Amazon Bedrock (playground, Converse API), Titan Embeddings | 7 |
| **3** — D3 (I) | Diseñar soluciones con Bedrock: selección de modelos, Knowledge Bases, Agents, Guardrails, personalización. | **[Lab 01 — RAG](labs/lab-01-rag-bedrock-knowledge-bases/README.md)** completado y limpiado · Diagrama propio de un agente con action groups | Bedrock Knowledge Bases, Agents, Guardrails, OpenSearch Serverless, Lambda | 8 |
| **4** — D3 (II) | Decidir entre Bedrock y JumpStart; dominar los servicios de IA aplicada y Amazon Q; evaluación de FMs. | Tabla "servicio → caso de uso → cuándo NO usarlo" memorizada · [Preguntas D3](practice-questions/domain-03-questions.md) ≥ 80 % | SageMaker JumpStart, Comprehend, Rekognition, Textract, Polly, Transcribe, Lex, Q Developer/Business, Q in QuickSight, Bedrock Model Evaluation | 8 |
| **5** — D4 + D5 | Aplicar IA responsable y seguridad: sesgo, explicabilidad, responsabilidad compartida, IAM, PrivateLink, auditoría, costos. | Políticas IAM de ejemplo comentadas · Matriz On-Demand vs. Batch vs. Provisioned Throughput · [Preguntas D4](practice-questions/domain-04-questions.md) y [D5](practice-questions/domain-05-questions.md) ≥ 80 % | SageMaker Clarify, Model Cards, Model Monitor, A2I, IAM, KMS, VPC endpoints, CloudTrail, CloudWatch, Macie, Organizations (SCP) | 8 |
| **6** — Repaso | Consolidar, detectar puntos débiles y simular condiciones reales. | Repaso de la [matriz de decisión](cheatsheets/exam-decision-matrix.md) · Examen de práctica oficial en AWS Skill Builder ≥ 80 % · Reserva del examen | Todos | 6–8 |

**Variante intensiva (3 semanas, ~15 h/semana):** semana 1 → D1 + D2 · semana 2 → D3 + Lab 01 · semana 3 → D4 + D5 + simulacros.

### Método recomendado por sesión

1. **Leer** el documento del dominio (teoría + tablas de decisión).
2. **Practicar** en la consola o con el laboratorio correspondiente.
3. **Responder** las preguntas del dominio sin mirar las soluciones.
4. **Registrar** errores y respuestas con baja confianza en un log personal.
5. **Repasar** con los [cheatsheets](cheatsheets/) a las 24 h y a los 7 días (repetición espaciada).

---

## Roadmap

| Versión | Estado | Alcance |
|---|---|---|
| **v1.0** | ✅ Publicado | 5 dominios completos · Plantilla de laboratorio · Lab 01 (RAG) · Matriz de decisión (40 escenarios) · Glosario · 30 preguntas de práctica · CI de documentación |
| **v1.1** | 🔜 Planificado | Lab 02 (Guardrails) · Lab 03 (Bedrock Agents) · +50 preguntas (incluidos casos de estudio) |
| **v1.2** | 🗓️ Planificado | Lab 04 (Clarify) · Lab 05 (PrivateLink + auditoría) · Versión IaC (CDK/Terraform) del Lab 01 |
| **v2.0** | 💡 Propuesta | Simulacro completo de 65 preguntas cronometrado · Flashcards exportables (Anki) · Licencia de contenido definida |

¿Quieres proponer algo? Abre un *issue* con la etiqueta `enhancement`.

---

## Cómo contribuir

Las contribuciones son bienvenidas. Resumen de reglas (detalle completo en [`CONTRIBUTING.md`](CONTRIBUTING.md)):

| Aspecto | Convención |
|---|---|
| **Directorios y archivos** | `kebab-case`, en inglés, con prefijo numérico de dos dígitos cuando hay orden: `domains/03-applications-foundation-models/`, `labs/lab-02-bedrock-guardrails/`. |
| **Idioma del contenido** | Español neutro. Los nombres de servicios, APIs, parámetros y términos técnicos establecidos se mantienen en inglés (`Provisioned Throughput`, `RetrieveAndGenerate`, *fine-tuning*). |
| **Encabezados** | Un único `#` por documento; secciones numeradas `## 1.`, `### 1.1`. |
| **Tablas** | Para comparaciones y criterios de decisión; columna de "cuándo NO usarlo" cuando aplique. |
| **Diagramas** | Mermaid para flujos; ASCII en bloques de código `text` para jerarquías y estructuras. |
| **Código** | Bloques con lenguaje declarado (`bash`, `json`, `python`); sin credenciales ni IDs de cuenta reales (usa `111122223333` o `__ACCOUNT_ID__`). |
| **Preguntas** | Originales (nunca de *dumps*), con justificación de **todas** las opciones y enlace a la sección del dominio. |
| **Commits** | [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/): `docs(d3): añade Bedrock Flows`, `feat(labs): lab 02 guardrails`, `fix(questions): corrige respuesta D2-Q4`. |
| **Calidad** | La CI (`markdownlint`, validación de enlaces, JSON y Python) debe pasar antes de fusionar. |

---

## Recursos oficiales

- [Página de la certificación AWS Certified AI Practitioner](https://aws.amazon.com/certification/certified-ai-practitioner/)
- [Guía oficial del examen AIF-C01](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html)
- [AWS Skill Builder](https://skillbuilder.aws/) — Exam Prep Plan, Official Practice Question Set y Official Practice Exam
- [Documentación de Amazon Bedrock](https://docs.aws.amazon.com/bedrock/)
- [Documentación de Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/)
- [AWS Responsible AI](https://aws.amazon.com/ai/responsible-ai/)
- [Generative AI Security Scoping Matrix](https://aws.amazon.com/ai/generative-ai/security/scoping-matrix/)
- [AWS Well-Architected — Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html)
