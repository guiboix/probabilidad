# 8. Situación actual: escalera de dos Letras a 12 meses

## 8.1 Datos confirmados por el usuario (10-09-2026)

| Dato | Valor | Estado |
|---|---|---|
| Fondo de emergencia | Existe, **aparte** de estas Letras | Hecho (declarado) |
| Decisión actual sobre las Letras | Se mantienen renovándose de momento | Hecho (declarado) |
| Letra A | 8.000 €, amortiza el **06-11-2026** | Hecho (declarado) |
| Letra B | 8.000 €, amortiza el **04-06-2027** | Hecho (declarado) |
| Precio de compra de A | 980,28 por 1.000 € (tipo medio 1,990 %) | **Inferido**: coincide con la subasta a 12 meses del 04-11-2025, vencimiento 06-11-2026 (fuente: extracto de Finect/Tesoro vía búsqueda) |
| Precio de compra de B | ≈ 974,93 por 1.000 € (tipo medio 2,543 %) | **Inferido**: coincide con la subasta del 02-06-2026; el precio se deriva del tipo medio porque la fuente daba un precio incoherente (97,535 corresponde al 2,50 % de julio) |
| Nominal | 8.000 € cada una | **Supuesto** (las Letras se compran en múltiplos de 1.000 € de nominal) |
| Custodio | Cuenta directa del Banco de España (compra en la web del Tesoro) | Hecho (declarado). Comisión: 0,15 % al vencer (12 € por Letra), deducible en la Renta |

Si el usuario pujó a precio distinto del medio (petición competitiva) o el nominal no es 8.000 €, corregir
`data/letras.csv` y volver a ejecutar `python -m cartera escalera`.

Consecuencia de que el fondo de emergencia esté aparte: estos 16.000 € **no tienen función de liquidez de
urgencia**. Son capital invertible cuyo horizonte lo decide el usuario. Eso cambia el análisis: mantenerlos
en Letras es una elección de riesgo, no una necesidad.

## 8.2 Qué es esta estructura y qué hace bien

Escalera de dos peldaños separados unos 7 meses (noviembre / junio). Ventajas objetivas:

- Liquidez dos veces al año sin acudir al mercado secundario.
- Cada vencimiento es un punto de decisión sin coste ni efecto fiscal adicional por no renovar.
- Si los tipos suben (el BCE subía en septiembre de 2026), la mitad se reinvierte al nuevo tipo en menos de 7 meses.
- Diversificación temporal del riesgo de tipos, pequeña con dos peldaños.

## 8.3 Qué rinde hoy

`python -m cartera escalera --data data --hoy 2026-09-10 --inflacion 0.033 --peso-letras 1 --custodio bde`

| Vence | Días | Nominal | Pagado | Tipo bruto | TAE neta | Rendimiento neto (tras IRPF y 12 € de comisión BdE) |
|---|---|---|---|---|---|---|
| 06-11-2026 | 57 | 8.000 € | 7.842,24 € | 1,99 % | 1,48 % | 115,79 € |
| 04-06-2027 | 267 | 8.000 € | 7.799,44 € | 2,54 % | 1,94 % | 150,45 € |

| Concepto | Valor |
|---|---|
| Rendimiento neto total de las dos Letras al vencer | **266,24 €** |
| Pérdida de poder adquisitivo con inflación del 3,3 % | **≈ 262 €** (16.000 × 3,3 % − 266) |
| TAE real neta de A / de B | ≈ −1,8 % / ≈ −1,3 % |

La Letra A se compró en el momento de tipos más bajos del ciclo (1,99 %). Al renovarla en noviembre de 2026
al tipo de referencia de agosto (2,66 %), su rendimiento neto subiría de 128 € a ≈ 170 €, con TAE real
neta ≈ −1,1 %: mejora, pero sigue por debajo de la inflación.

## 8.4 Calendario de decisión

| Fecha | Evento | Decisión |
|---|---|---|
| Finales de octubre de 2026 | Plazo para cursar la petición en la subasta a 12 meses de noviembre (fecha estimada: 03-11-2026, liquidación 06-11-2026; confirmar en el calendario de tesoro.es) | Renovar A total, parcial o no renovar |
| 06-11-2026 | Amortiza A: 8.000 € en cuenta | Si no se renueva todo, el resto va a fondos ese mismo día |
| Finales de mayo de 2027 | Plazo para la subasta a 12 meses de junio (fecha estimada: 01-06-2027) | Renovar B total, parcial o no renovar |
| 04-06-2027 | Amortiza B: 8.000 € en cuenta | Idem |

Plan de transición según fracción que se quiera mantener en Letras:

| Escenario | 06-11-2026 | 04-06-2027 | Queda en Letras |
|---|---|---|---|
| Mantener todo (decisión actual, `--peso-letras 1`) | Renovar 8.000 | Renovar 8.000 | 16.000 € |
| Mitad (`--peso-letras 0.5`) | Mover 8.000 a fondos | Renovar 8.000 | 8.000 € |
| Todo a fondos (`--peso-letras 0`) | Mover 8.000 | Mover 8.000 | 0 € |

La decisión declarada es mantener. Es compatible con empezar a aprender con fondos usando ahorro nuevo
(documento 09) y revisar en octubre de 2026, con dos meses de experiencia, si se renueva A entera.

## 8.4 bis Decisión operativa (11-09-2026): dos bloques de 10.000 € en vez de una tercera Letra

Pregunta del usuario: al renovar la Letra A, ¿comprar aparte una tercera Letra o hacer dos bloques de
10.000 €? **Respuesta: dos bloques de 10.000 €.** Mismo resultado económico (todo son Letras a 12 meses
al tipo de la subasta), menos posiciones que vigilar y menos comisiones del Banco de España (una
transferencia de amortización por bloque). La escalera se mantiene en dos peldaños separados 7 meses.

Cómo se hace en la cuenta directa: en la petición de la subasta del 03-11-2026 se pide un nominal de
10.000 € y se marca que el pago se haga con **reinversión** del importe que amortiza ese mismo día
(8.000 €); los 2.000 € restantes se cargan en la cuenta bancaria. Petición no competitiva (se acepta el
precio medio).

**Plazos reales (calendario del Tesoro aportado por el usuario el 11-09-2026, fila de Letras a 12 meses):**

| Subasta | Amortización | Límite petición **en línea** | Límite petición en oficina del Banco de España | Límite de pago | Emisión |
|---|---|---|---|---|---|
| 06-10-2026 | 08-10-2027 | **29-09-2026** | 02-10-2026 | 08-10-2026 | 09-10-2026 |

Es decir, la petición por internet cierra **el martes de la semana anterior a la subasta**. Aplicado al resto
de fechas (regla del calendario; confirmar cada una en la misma tabla del Tesoro):

| Subasta | Plazos | Límite en línea (estimado por la misma regla) |
|---|---|---|
| 06-10-2026 | 6 y 12 meses | 29-09-2026 (confirmado) |
| 13-10-2026 | 3 y 9 meses | 06-10-2026 |
| **03-11-2026** | 6 y 12 meses | **27-10-2026** |

Fuente del dinero nuevo: los ≈ 2.900 € sobrantes del colchón (documento 11). Para el segundo bloque, en
junio de 2027, harían falta otros 2.000 €: si el ahorro acumulado hasta entonces no los cubre, se renueva
B por 9.000 € y se mantiene el colchón en 12 meses exactos. Se decide en mayo de 2027 con los datos de entonces.

### Simplificación decidida el 11-09-2026: solo dos bloques a 12 meses, renovados cada seis meses

Objeción del usuario: con Letras a 3 y 6 meses para el colchón habría ≈ 8 renovaciones al año. Es cierto y
el beneficio no lo compensa (una Letra a 3 meses renta ≈ 0,4 puntos menos que una a 12 y exige cuatro
peticiones al año). Nuevo esquema:

| Dónde | Importe | Función |
|---|---|---|
| Cuenta corriente CaixaBank | **≈ 5.000 €** (≈ 4,5 meses de salidas) | Liquidez inmediata: gastos, reserva fiscal y primer tramo del colchón |
| Bloque A: Letra a 12 meses, subasta 03-11-2026 | **13.000 €** (8.000 por reinversión + 5.000 nuevos) | Vence 11-2027 |
| Bloque B: Letra a 12 meses, subasta ≈ 01-06-2027 | **14.000 €** (8.000 por reinversión + 6.000 nuevos) | Vence 06-2027 y luego 06-2028 |

Los 16.000 € en cuentas se reparten así: 5.000 € nuevos en noviembre, 6.000 € nuevos en junio, 5.000 € se
quedan en la cuenta. Hasta junio de 2027 la cuenta tendrá 11.000 €; a partir de junio, 5.000 €. Se
renueva **dos veces al año**, en noviembre y junio, con reinversión.

Qué se gana y qué se pierde respecto al esquema anterior:

- Se gana: dos peticiones al año en vez de ocho; algo más de tipo (12 meses paga más que 3 o 6).
- Se pierde: liquidez. El colchón deja de estar disponible en menos de 3 meses. En cualquier momento hay
  5.000 € inmediatos y el siguiente bloque vence como máximo en 7 meses. Para una emergencia mayor de
  5.000 € antes del siguiente vencimiento habría que vender una Letra antes de tiempo (el Banco de España
  permite solicitar la venta a precio de mercado con trámite; confirmar condiciones en tesoro.es) o tirar
  del PIAS mientras exista.
- Coste de tener 5.000 € en cuenta al 0 % en vez de en Letras cortas: ≈ 110 € al año. Es el precio de la
  liquidez inmediata y de la sencillez.

Si el PIAS se rescata (≈ 5.772 €), se suma al bloque más cercano en el tiempo: al de noviembre si el dinero
llega antes del 27-10-2026 (A pasaría a 18.000 €), o al de junio de 2027 en caso contrario.

### Calendario de compras

| Subasta | Plazos | Pedir en línea antes del | Liquidación | Qué hacer | Importe |
|---|---|---|---|---|---|
| **03-11-2026** | 6 y 12 meses | **27-10-2026** (estimado por la regla del calendario; confirmar) | **06-11-2026** (= amortización de A) | Renovar A a 12 meses con reinversión + 5.000 € nuevos | **13.000 €** |
| ≈ 01-06-2027 | 6 y 12 meses | ≈ 25-05-2027 | ≈ 04-06-2027 (= amortización de B) | Renovar B a 12 meses con reinversión + 6.000 € nuevos | **14.000 €** |

Las subastas del 6 y 13 de octubre ya no se usan. Tras noviembre: 21.000 € en Letras (13.000 + 8.000),
11.000 € en cuenta; tras junio de 2027: 27.000 € en Letras (13.000 + 14.000), 5.000 € en cuenta. Todo deuda
pública en el Banco de España; ninguna gestora.

## 8.5 Sistema de avisos (petición del usuario: tener en cuenta la caducidad para reinvertir o renovar)

Dos capas operativas y una no disponible:

1. **Calendario importable:** `data/calendario_vencimientos.ics` contiene cinco eventos (decisión de
   renovación de A y B con alarma un día antes, amortización de A y B, revisión a 3 meses del primer
   fondo). Importar en Google Calendar, Outlook o el calendario del móvil.
2. **Comando `escalera`:** marca con "DECIDIR YA" cualquier Letra a menos de 30 días del vencimiento
   (`--aviso-dias` para cambiar el umbral). Ejecutarlo en la revisión mensual (`make informe` + `escalera`).
3. **Recordatorios automáticos en la sesión de Claude Code:** se intentaron programar para el 19-10-2026,
   10-12-2026 y 17-05-2027, pero la creación de tareas programadas **fue denegada por permisos** en esta
   sesión. Si el usuario los quiere, debe autorizarlos o crearlos desde su cuenta. Hasta entonces, el
   `.ics` y el comando `escalera` son las únicas capas activas.

Fechas de las subastas: las de noviembre de 2026 y junio de 2027 son estimadas por el patrón habitual
(primer martes de mes, liquidación el viernes). El calendario oficial 2027 lo publica el Tesoro en enero de
2027; actualizar el `.ics` entonces.

## 8.6 Ventaja de mover por vencimientos y no de golpe

Mover en noviembre de 2026 y en junio de 2027 reparte la entrada en dos momentos separados 7 meses.
Reduce (no elimina) el riesgo de entrar todo justo antes de una caída. No vender antes de vencimiento
evita el diferencial de precio del secundario.
