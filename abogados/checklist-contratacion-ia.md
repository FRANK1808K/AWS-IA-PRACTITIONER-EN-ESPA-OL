# Checklist de Due Diligence para Contratar una Solución de IA

> Lista de verificación para revisar la contratación de una herramienta o un proveedor de IA. Está pensada para usarse junto al equipo técnico: cada pregunta indica **qué pedir** y **por qué importa**.
>
> ⚠️ Material orientativo, no sustituye el análisis del caso concreto ni la normativa aplicable.

## 1. Identificación del sistema y de los actores

- [ ] ¿Qué **finalidad** tiene el sistema y qué decisiones apoya o toma?
- [ ] ¿Quién es el **proveedor del modelo**, quién el **proveedor de nube** y quién el **integrador**? (ver [Módulo 3](03-soluciones-en-la-nube.md#1-la-cadena-de-actores-la-primera-pregunta-de-cualquier-abogado))
- [ ] ¿Qué **términos de servicio** aplican a cada uno y cuál prevalece?
- [ ] ¿La herramienta es de **consumo** o **empresarial**? Los términos suelen ser muy distintos.
- [ ] ¿Cuál es su **nivel de riesgo** según la regulación aplicable (por ejemplo, alto riesgo en el AI Act)?

## 2. Datos

- [ ] ¿Qué **datos** se introducirán (personales, sensibles, confidenciales, secreto profesional)?
- [ ] ¿Hay **base legal** para ese tratamiento y para la finalidad concreta?
- [ ] ¿El proveedor se compromete por contrato a **no usar los datos para entrenar** sus modelos?
- [ ] ¿En qué **país o región** se procesan y almacenan los datos? ¿Hay **transferencias internacionales**? ¿Se usa inferencia entre regiones?
- [ ] ¿Existe un **contrato de encargo de tratamiento** (DPA) con subencargados identificados?
- [ ] ¿Cuánto tiempo se **conservan** los prompts, las respuestas y los registros? ¿Cómo se **eliminan**?
- [ ] ¿Se aplica **minimización**: se envía a la IA solo la información necesaria?

## 3. Seguridad

- [ ] ¿El proveedor tiene **certificaciones** verificables (ISO/IEC 27001, ISO/IEC 42001, SOC 2…)? Pide los informes (en AWS: AWS Artifact).
- [ ] ¿Los datos se **cifran** en tránsito y en reposo? ¿Quién controla las claves?
- [ ] ¿Quién tiene **acceso**? ¿Se aplica el principio de **mínimo privilegio**?
- [ ] ¿Hay **registros de auditoría** de quién usó el sistema, cuándo y con qué resultado?
- [ ] ¿Cómo se protege contra **prompt injection** y filtraciones de información?
- [ ] ¿Cuál es el procedimiento y el plazo para notificar **incidentes de seguridad**?

## 4. Calidad, sesgo y explicabilidad

- [ ] ¿Existe documentación del modelo (**Model Card** o equivalente): uso previsto, limitaciones, evaluación?
- [ ] ¿Se ha medido el **sesgo** por grupos relevantes? ¿Con qué resultados?
- [ ] ¿Puede el sistema **explicar** los factores de una decisión concreta?
- [ ] ¿Cómo se gestionan las **alucinaciones**? ¿Las respuestas citan fuentes verificables?
- [ ] ¿Hay **monitoreo** continuo de la calidad y un procedimiento para corregir o retirar el sistema?

## 5. Supervisión humana y derechos de las personas

- [ ] ¿Qué decisiones requieren **revisión humana** antes de producir efectos?
- [ ] ¿Se **informa** a las personas de que interactúan con una IA o de que una IA intervino en una decisión que les afecta?
- [ ] ¿Cómo pueden ejercer sus derechos (acceso, rectificación, oposición, **revisión** de decisiones automatizadas)?
- [ ] Si el sistema es un **agente**, ¿qué acciones puede ejecutar y qué **límites** tiene que la IA no pueda saltarse?

## 6. Propiedad intelectual

- [ ] ¿Quién es **titular** de los resultados generados (textos, imágenes, código)?
- [ ] ¿Quién es titular de los **modelos ajustados** con datos propios (*fine-tuning*)?
- [ ] ¿El proveedor ofrece **indemnidad** frente a reclamaciones de terceros por infracción de derechos? ¿Con qué exclusiones?
- [ ] ¿Qué **licencia** tiene el modelo (abierta, comercial, restricciones de uso)?

## 7. Condiciones comerciales y continuidad

- [ ] ¿Cómo se **cobra** (por token, por usuario, capacidad reservada)? ¿Hay **topes de gasto** y alertas?
- [ ] ¿Qué **niveles de servicio** (SLA) se garantizan: disponibilidad, tiempo de respuesta, soporte?
- [ ] ¿Qué ocurre si el proveedor **retira o cambia** el modelo? ¿Con cuánto preaviso?
- [ ] ¿Cómo se **recuperan** los datos y se migra a otro proveedor al terminar el contrato (portabilidad)?
- [ ] ¿Qué **limitaciones de responsabilidad** contiene el contrato? ¿Son razonables frente al riesgo?

## 8. Gobernanza interna

- [ ] ¿El sistema está en el **inventario** de sistemas de IA de la organización?
- [ ] ¿Hay un **responsable** designado y un proceso de aprobación?
- [ ] ¿Existe una **política de uso aceptable** y formación para los usuarios?
- [ ] ¿Se hizo una **evaluación de impacto** (protección de datos y, si procede, derechos fundamentales)?
- [ ] ¿Cuándo se **revisará** de nuevo el sistema?

---

⬅️ [Casos prácticos](casos-practicos.md) · ➡️ [Glosario traductor](glosario-traductor.md)
