# 2. Política de inversión (borrador para completar)

Una política de inversión escrita sirve para no improvisar cuando el mercado cae. Este documento es una
plantilla: los valores entre corchetes se fijan una vez rellenado `01_perfil_y_objetivos.md`.

## 2.1 Principios

1. **Coste bajo.** Cada 1 % anual de comisiones a 20 años se lleva aproximadamente el 18 % del capital final
   (1 − 0,99^20). Prioridad a fondos indexados con TER < 0,30 % y sin custodia.
2. **Diversificación global.** Ningún país, sector o empresa concentrado. Un índice mundial es el punto de partida.
3. **Fiscalidad eficiente.** Fondos de acumulación y traspasos entre fondos (no tributan) frente a
   vender y comprar. Las Letras tributan cada vencimiento; los fondos, solo al reembolsar.
4. **Sin apalancamiento, sin productos complejos** (derivados, estructurados, cripto, notas, CFD).
5. **Automatizar**: aportación periódica fija, rebalanceo por reglas, no por titulares.
6. **Criterio ético definido por escrito** (documento 05) y aplicado como filtro previo, no como tema de moda.

## 2.2 Asignación objetivo

Decisión del usuario (10-09-2026): perfil **muy conservador**, sin experiencia previa, al menos para la
mayor parte del capital. Traducción a reglas:

- **Renta variable: 0 %** hasta completar el ciclo de aprendizaje del documento 09 y decidirlo por escrito aquí.
- **Bloque conservador ≥ 85 %** del capital en todo momento: Letras del Tesoro y/o fondos de renta fija a
  corto plazo (indicador de riesgo 1–2, duración < 3, grado de inversión, euros).
- **Bloque de aprendizaje ≤ 15 %**: fondos de renta fija con filtro ético de riesgo 2, donde se aprende a
  leer un VL, una duración y un KID. Empieza con 300 €.

| Bloque | Función | Instrumento | Fase 0 (hoy) | Fase 1 (tras el aprendizaje) |
|---|---|---|---|---|
| Conservador: Letras | Capital principal, sin riesgo de precio a vencimiento | Escalera de Letras 12 m (A y B) | 98 % | 70–85 % |
| Conservador: RF corto plazo ético | Igual función, más cómodo (sin subastas), con filtro ético y traspasable | Fondo indexado RF euro corto plazo ESG o monetario responsable | 0 % | 0–15 % |
| Aprendizaje: RF ético riesgo 2 | Aprender con dinero real y riesgo contenido | Fondo indexado bonos corporativos globales ESG cubierto a euros | 2 % (300 €) | 10–15 % |
| Renta variable ética | Crecimiento real a > 10 años | Fondo indexado RV mundial ESG/SRI | 0 % | 0 % hasta nueva decisión escrita |

Lo que cabe esperar de una cartera así (hecho, no promesa): rentabilidad parecida a la de las Letras
(≈ 2–2,7 % bruto con los tipos de 2026), oscilaciones pequeñas (volatilidad total ≈ 0,5–1 %) y, mientras la
inflación siga por encima del 3 %, pérdida de poder adquisitivo de ≈ 1 % anual. La cartera conservadora
protege el capital nominal, no el real. Es un intercambio consciente: tranquilidad y aprendizaje a cambio de
renunciar, de momento, a la rentabilidad real. Se revisa en la fase 1.

Regla orientativa para la fase 1 (no norma): peso máximo de renta variable ≈ caída máxima tolerable × 2.
Si una caída del 20 % del total es lo máximo que se soportaría sin vender, RV ≤ 40 %.
Se justifica porque la renta variable global ha caído en torno al 50 % en las peores crisis del último
siglo (hecho histórico; no garantiza el futuro en ninguna dirección).

## 2.3 Reglas operativas

- **Aportación periódica:** [ ] € el día [ ] de cada mes, repartida con `python -m cartera informe --aportacion X`.
- **Rebalanceo:** revisar cada [6/12] meses. Actuar solo si un bloque se desvía más de 5 puntos
  absolutos o del 25 % de su peso objetivo (parámetros `banda_abs` y `banda_rel` en `data/supuestos.json`).
  Orden de preferencia: 1) aportaciones nuevas, 2) traspaso entre fondos, 3) no renovar una Letra al vencer, 4) vender.
- **Transición desde Letras:** no vender Letras antes de vencimiento. A cada vencimiento, decidir qué parte
  se renueva y qué parte va a fondos según la asignación objetivo. Esto reparte la entrada en el mercado
  en el tiempo (reduce el riesgo de entrar justo antes de una caída).
- **Prohibido:** cambiar la asignación objetivo por una noticia; comprar un producto que no se entiende;
  vender por una caída.
- **Cambio de política:** solo por cambio en horizonte, situación personal o criterios éticos, y por escrito
  en este documento con fecha.

## 2.4 Métricas de seguimiento

| Métrica | Herramienta | Frecuencia |
|---|---|---|
| Desviación por bloque | `informe` | mensual |
| TIR del inversor (XIRR) | `informe` (necesita `movimientos.csv`) | trimestral |
| TWR de cada fondo | `metricas.twr` con valores liquidativos | anual |
| Coste total anual (TER + custodia + gestión) | manual, ficha del producto | anual |
| Rentabilidad real neta de las Letras | `letras` | a cada renovación |

## 2.5 Historial de cambios

| Fecha | Cambio | Motivo |
|---|---|---|
| 2026-09-10 | Borrador inicial | Creación del proyecto |
| 2026-09-10 | Perfil muy conservador: RV 0 %, bloque conservador ≥ 85 %, aprendizaje ≤ 15 % | Decisión del usuario (sin experiencia previa) |
