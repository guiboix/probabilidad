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

| Bloque | Función | Instrumento candidato | Peso objetivo |
|---|---|---|---|
| Liquidez / emergencia | Cubrir [3–6] meses de gastos y necesidades < 3 años | Letras 3–12 m, cuenta remunerada, fondo monetario | [ ] % |
| Renta fija | Amortiguar caídas, tramo 3–10 años | Fondo indexado RF euro gobierno/agregado ESG, duración corta-media | [ ] % |
| Renta variable | Crecimiento real a > 10 años | Fondo indexado RV mundial con filtro ESG/SRI | [ ] % |

Regla orientativa (no norma): peso máximo de renta variable ≈ caída máxima tolerable × 2.
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
