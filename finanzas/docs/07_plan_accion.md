# 7. Plan de acción

Orden propuesto. Cada paso depende del anterior.

## Fase 0 — Datos (usuario)
- [ ] Rellenar la tabla 1.1 de `01_perfil_y_objetivos.md`.
- [ ] Elegir nivel ético en `05_criterios_eticos.md` §5.3.
- [ ] Copiar plantillas de `data/` a `cartera.csv`, `letras.csv`, `movimientos.csv` con datos reales.
- [x] Fechas de amortización de las Letras: 06-11-2026 y 04-06-2027. Falta confirmar precio de compra y nominal (`08_escalera_letras.md` §8.1).
- [x] Fondo de emergencia aparte: confirmado.
- [ ] Tipo marginal de IRPF (para saber si el plan de pensiones compensa).
- [x] Letras en cuenta directa del Banco de España (compra en web del Tesoro): confirmado.
- [ ] En la próxima Renta, restar la comisión del 0,15 % del BdE al rendimiento de las Letras (no viene en el borrador).
- [x] Capital total ≈ 37.900 €: 16.000 € Letras + 16.000 € cuentas + 5.890 € PIAS; sin comisión de mantenimiento.
- [x] Los ≈ 16.000 € en cuentas son el fondo de emergencia (y candidatos a inversión segura).
- [x] PIAS identificado: CABK PIAS CMV1 (VidaCaixa), 2010, 5.267 € aportados, 5.891 € de rescate, TIR ≈ 0,8–1,3 %.
- [ ] PIAS: preguntar tipo de interés actual, si el valor de rescate es neto de penalización y gastos anuales (documento 10 §10.6). Decidir después si se rescata hacia Letras.
- [x] Gasto mensual ≈ 1.095 € (cuota de autónomos 328 € aparte). Colchón prudente 9–12 meses = 9.900–13.100 €; sobran ≈ 2.900–6.100 €.
- [x] Colchón de 12 meses (≈ 13.100 €): decidido.

## Fase 0c — Poner a rendir el colchón y el sobrante (documento 11 §11.2 ter)
- [x] Condiciones de la cuenta de MyInvestor verificadas con las bases legales: 1,00–1,25 % el primer año, 0,30 % después. No supera el listón.
- [ ] Colchón que rinde (≈ 10.400 €): Letras a 3 y 6 meses en el Banco de España, 5.000 € en cada plazo, en las próximas subastas (calendario en tesoro.es); renovar a cada vencimiento.
- [ ] Pedir 2.000 € de Letra a 12 meses en la próxima subasta (octubre o noviembre de 2026).
- [ ] Dejar ≈ 2.700 € (dos meses de salidas + reserva fiscal del trimestre) en la cuenta corriente.
- [ ] Decidir dónde va el colchón que rinde (cuenta remunerada o Letras a 3–6 meses) y cuánto pasa a la Letra a 12 meses.
- [x] Los "bonos" son las Letras: aclarado.
- [ ] Verificar en tesoro.es el tipo de la última subasta y en la app de MyInvestor las comisiones vigentes
  (resolver la discrepancia de coste de la Cartera Sostenible: 0,81 % vs 1,09–1,33 %).

## Fase 0b — Primer fondo de aprendizaje (en curso, documento 09)
- [x] Buscador de MyInvestor revisado: único indexado de renta fija con filtro ético visto es iShares ESG Screened Global Corporate Bond EUR Hedged (IE00BJN4RG66, TER 0,14 %).
- [ ] Repetir la búsqueda con el interruptor ESG activado y enviar la lista.
- [ ] Abrir la ficha del IE00BJN4RG66: indicador de riesgo, artículo SFDR, duración, patrimonio; descargar el KID y rellenar §9.4.
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
