# Simulador interactivo AIF-C01

Simulador del examen con **cronómetro**, **marcadores de revisión**, **navegador de preguntas** e **informe por dominio** con el formato «Cumple / Necesita mejora» del informe oficial de AWS.

## Cómo abrirlo

- **En el navegador, sin instalar nada:** descarga [`index.html`](index.html) (botón *Raw* → Guardar como) y ábrelo con doble clic. Funciona sin conexión salvo las fuentes tipográficas.
- **Desde el repositorio clonado:** abre `simulator/index.html` en tu navegador.

## Pruebas disponibles

| Prueba | Preguntas | Tiempo estándar |
|---|---|---|
| Simulacro 01 | 65 (pesos oficiales, incluye v1.1) | 90 min |
| Simulacro 02 | 65 de escenario, más difícil | 90 min |
| Refuerzo D1 · D3 · D4 · D5 | 40 al azar de los dominios débiles | 55 min |
| Novedades v1.1 | Todas las preguntas 🆕 de ambos simulacros | ≈ 1,4 min por pregunta |

Opciones: tiempo **estándar**, **ESL +30** (×1,33) o **sin límite**, y **corrección inmediata** (modo estudio). El progreso de un intento en curso y el historial de resultados se guardan **solo en tu navegador** (`localStorage`).

## Regenerar tras editar los simulacros

Las preguntas salen de `practice-questions/mock-exam-*.md`. Tras modificarlas:

```bash
python simulator/build.py
```

El script valida que cada pregunta tenga su entrada en la clave de respuestas y que la respuesta exista entre las opciones.
