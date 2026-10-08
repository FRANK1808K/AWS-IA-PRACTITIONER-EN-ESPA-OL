# Módulo 5 — Seguridad, cumplimiento y gobernanza: quién responde de qué

> **Equivale a:** Dominio 5 del examen AWS AIF-C01 (14 %). Versión técnica: [Dominio 5](../domains/05-security-compliance-governance/README.md).
>
> **Lo que sabrás al terminar:** entender el **modelo de responsabilidad compartida** como un reparto de obligaciones, reconocer los controles técnicos que sirven de **prueba** en una auditoría o un litigio, y saber qué pedir a un proveedor de IA.

---

## 1. Responsabilidad compartida: el reparto de obligaciones

AWS lo resume así: **AWS es responsable de la seguridad "de" la nube; el cliente, de la seguridad "en" la nube.**

> **Analogía:** es como alquilar un despacho en un edificio con seguridad. El **propietario** responde de la estructura, la cerradura de la entrada principal y la vigilancia del edificio. El **inquilino** responde de quién tiene llave de su despacho, de cerrar los archivadores y de lo que guarda dentro.

| AWS responde de… | El cliente responde de… |
|---|---|
| Centros de datos, servidores y redes | **Quién** puede usar cada servicio y modelo (permisos) |
| Funcionamiento y disponibilidad del servicio | **Qué datos** introduce y si tiene base legal para hacerlo |
| Aislamiento de los modelos | **Configuración**: cifrado, filtros, registros de actividad |
| No usar los datos del cliente para entrenar los modelos base (Bedrock) | **Uso responsable** de los resultados y **cumplimiento** normativo del caso de uso |

> **Consecuencia práctica:** una organización **no puede trasladar al proveedor de nube** la responsabilidad por los datos que introduce, por los permisos que concede o por el uso que hace de la IA. El contrato debe reflejar ese reparto con claridad.

### Cuanto más "a medida", más responsabilidad

AWS clasifica los usos de IA generativa en cinco niveles (*Generative AI Security Scoping Matrix*):

| Nivel | Situación | Ejemplo | Responsabilidad del cliente |
|---|---|---|---|
| 1 | Usar una app de consumo | Un empleado usa un chatbot público | Políticas internas de uso |
| 2 | Usar una app empresarial | Licencia corporativa de un asistente de IA | Contrato, configuración |
| 3 | Construir sobre un modelo ya entrenado | App propia con un modelo de Bedrock | Diseño de la app y de los datos |
| 4 | Ajustar un modelo con datos propios (*fine-tuning*) | Modelo entrenado con los escritos del despacho | También los datos de entrenamiento |
| 5 | Entrenar un modelo propio | Modelo creado desde cero | Prácticamente todo |

## 2. Los controles técnicos, traducidos

| Control técnico | Qué hace | Equivalente jurídico |
|---|---|---|
| **IAM** (gestión de identidades y accesos) | Define **quién puede hacer qué** | **Poderes y facultades**: cada persona o sistema solo tiene las facultades estrictamente necesarias (*mínimo privilegio*) |
| **SCP** (políticas de la organización) | Límites que se aplican a **todas** las cuentas de una empresa | **Estatutos o políticas corporativas** que ningún directivo puede saltarse |
| **VPC endpoint / PrivateLink** | La comunicación con la IA **no pasa por internet público** | Un **canal privado** entre sedes |
| **Cifrado con AWS KMS** | Los datos solo pueden leerse con una clave | **Caja fuerte**: quien controla la llave controla el acceso |
| **AWS CloudTrail** | Registra **quién** hizo cada operación, **cuándo** y **desde dónde** | **Libro de registro** o **acta** de actuaciones |
| **Model invocation logging** | Guarda el **contenido** de las preguntas y respuestas de la IA | **Transcripción literal** de la conversación |
| **Amazon CloudWatch** | Métricas y alarmas de funcionamiento | **Sistema de alertas** ante anomalías |
| **Amazon Macie** | Detecta datos personales almacenados | **Inventario de datos personales** |
| **AWS Artifact** | Permite descargar las **certificaciones e informes de auditoría** de AWS (ISO, SOC…) | **Due diligence documental** del proveedor |

> **Para litigios y auditorías:** CloudTrail y los registros de invocación pueden servir como **evidencia** de quién usó la IA, con qué instrucciones y qué respondió. Conviene definir con antelación **cuánto tiempo se conservan, quién accede y cómo se garantiza su integridad** (cadena de custodia). Los registros con datos personales también deben cumplir las reglas de protección de datos.

## 3. 🆕 Los agentes de IA: delimitar el "mandato"

Cuando la IA **actúa** (consulta sistemas, ejecuta pagos, envía correos), aparece el riesgo de **agencia excesiva**: que el agente haga más de lo debido, por error o porque alguien lo manipula con instrucciones maliciosas (*prompt injection*).

| Medida | Equivalente jurídico |
|---|---|
| **AgentCore Identity**: el agente se identifica y usa credenciales propias y limitadas, sin contraseñas escritas en el código | Un **poder especial** con facultades concretas, no un poder general |
| **Policy in AgentCore**: reglas fijas, fuera de la IA, que impiden ciertas acciones ("nunca reembolsar más de 500") | **Límites del mandato** inscritos y oponibles: el mandatario no puede excederlos aunque lo intenten engañar |
| **Registros de cada acción** | **Rendición de cuentas** del mandatario |
| **Revisión humana** en acciones de alto impacto | **Autorización previa** del mandante |

## 4. Cómo se cobra la IA (útil para contratos)

| Modalidad | Cómo funciona | Analogía contractual |
|---|---|---|
| **Bajo demanda** | Se paga por uso (tokens procesados) | Tarifa **por servicio prestado** |
| **Por lotes** (*batch*) | Procesamiento masivo sin urgencia, más barato | Tarifa reducida por **encargos no urgentes** |
| **Capacidad reservada** (*Provisioned Throughput*) | Se paga por hora una capacidad garantizada, con o sin compromiso de permanencia | **Iguala** o tarifa plana con disponibilidad garantizada |

> **Al revisar un contrato de IA:** comprueba cómo se calculan los costos variables (tokens), si hay **topes de gasto**, alertas y quién asume el sobrecosto si la herramienta se usa más de lo previsto.

## 5. Gobernanza: marcos de referencia

| Marco | Qué es | Utilidad |
|---|---|---|
| **ISO/IEC 42001** | Norma internacional de **sistemas de gestión de IA** (certificable) | Referencia para exigir a proveedores o para certificar a la propia organización |
| **NIST AI Risk Management Framework** | Marco estadounidense de **gestión de riesgos de IA** (voluntario) | Metodología para identificar, medir y mitigar riesgos |
| **AWS Well-Architected — Generative AI Lens** | Buenas prácticas técnicas de AWS para IA generativa | Lista de verificación técnica |
| **OWASP Top 10 para aplicaciones con LLM** | Los 10 riesgos de seguridad más comunes en aplicaciones con modelos de lenguaje | Base para auditorías de seguridad |

**Una política de gobernanza de IA mínima incluye:** inventario de sistemas de IA en uso → clasificación por riesgo → responsables designados → reglas de uso aceptable → controles técnicos → registros y auditoría → formación → revisión periódica.

## 6. Para reflexionar

1. Una filtración de datos se produjo porque un empleado tenía permisos excesivos en la nube. ¿Responde el proveedor de nube? ¿Por qué?
2. ¿Qué registros pedirías en un procedimiento para probar qué respondió una IA a un cliente concreto en una fecha concreta?
3. Redacta en una frase el "límite del mandato" de un agente de IA que gestiona devoluciones en una tienda online.

⬅️ [Módulo 4](04-ia-responsable.md) · ➡️ [Módulo 6 — Mapa regulatorio](06-mapa-regulatorio.md)
