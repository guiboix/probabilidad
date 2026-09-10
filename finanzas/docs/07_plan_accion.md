# 7. Plan de acción

Orden propuesto. Cada paso depende del anterior.

## Fase 0 — Datos (usuario)
- [ ] Rellenar la tabla 1.1 de `01_perfil_y_objetivos.md`.
- [ ] Elegir nivel ético en `05_criterios_eticos.md` §5.3.
- [ ] Copiar plantillas de `data/` a `cartera.csv`, `letras.csv`, `movimientos.csv` con datos reales.
- [x] Fechas de amortización de las Letras: 06-11-2026 y 04-06-2027. Falta confirmar precio de compra y nominal (`08_escalera_letras.md` §8.1).
- [x] Fondo de emergencia aparte: confirmado.
- [ ] Datos de los bonos que ya posee (documento 10 §10.4) → `data/bonos.csv`.
- [ ] Tipo marginal de IRPF (para saber si el plan de pensiones compensa).
- [ ] Verificar en tesoro.es el tipo de la última subasta y en la app de MyInvestor las comisiones vigentes
  (resolver la discrepancia de coste de la Cartera Sostenible: 0,81 % vs 1,09–1,33 %).

## Fase 0b — Primer fondo de aprendizaje (en curso, documento 09)
- [ ] Buscar en la app los candidatos de §9.2 y rellenar la lista §9.4 con el KID.
- [ ] Elegir uno, suscribir **300 €** con ahorro nuevo y anotarlo en `movimientos.csv` y `cartera.csv`.
- [ ] Importar `data/calendario_vencimientos.ics` en el calendario personal.
- [ ] Registrar el VL semanal en `vl.csv` y ejecutar `python -m cartera seguimiento`.
- [ ] Antes de finales de octubre de 2026: decidir si la Letra del 06-11-2026 se renueva entera.

## Fase 1 — Diseño (usuario + herramientas)
- [ ] Fijar pesos objetivo en `02_politica_inversion.md` §2.2 y en `cartera.csv`.
- [ ] Ejecutar `python -m cartera simular` con el importe y la aportación reales; comprobar que el P5 a
  10 años es una cifra con la que se puede vivir.
- [ ] Decidir vía A (fondos sueltos) o B (cartera automatizada) según `04_myinvestor_opciones.md`.
- [ ] Seleccionar los fondos concretos y pasar la lista de comprobación §4.4 con el KID de cada uno.

## Fase 2 — Ejecución
- [ ] Mantener en Letras el fondo de emergencia y las necesidades a < 3 años.
- [ ] En cada vencimiento de Letra, aplicar `python -m cartera informe --aportacion <importe que vence>`
  y suscribir los fondos por los importes que indique.
- [ ] Programar la aportación mensual periódica en MyInvestor.
- [ ] Registrar cada movimiento en `movimientos.csv`.

## Fase 3 — Seguimiento
- [ ] Mensual: `make informe`. Actuar solo si hay "SÍ" en la columna *fuera de banda*.
- [ ] Anual: revisar TER de los fondos, tramos IRPF (`fiscalidad.py`), `supuestos.json`, y este plan.
- [ ] Ante una caída fuerte: releer `02_politica_inversion.md` §2.3 antes de hacer nada.

## Lo que este proyecto NO hace (todavía)
- No descarga precios ni valores liquidativos automáticamente (MyInvestor no ofrece API pública).
- No modela la compensación de pérdidas entre ejercicios.
- No incluye planes de pensiones (deducción en la base general; puede interesar según tipo marginal del
  usuario, dato que falta).
- No es asesoramiento financiero regulado.
