# 8. Situación actual: escalera de dos Letras a 12 meses

## 8.1 Datos aportados por el usuario (10-09-2026)

| Dato | Valor | Estado |
|---|---|---|
| Número de Letras | 2, ambas a 12 meses | Hecho (declarado) |
| Importe de cada una | 8.000 € | Hecho; **falta saber si es nominal o importe pagado**. Las Letras se compran en múltiplos de 1.000 € de nominal, así que lo más probable es 8.000 € nominal (≈ 7.790–7.800 € pagados) |
| Vencimientos | Separados 6 meses entre sí | Hecho (declarado); **faltan las fechas exactas** |
| Precio de compra de cada una | Desconocido | Estimado con subastas de 2026: 12 meses entre 2,50 % (julio) y 2,66 % (agosto); abril ≈ 2,64 % |

Hasta tener el resguardo de cada compra, los cálculos siguientes usan fechas y precios **supuestos**:
vencimientos el 12-02-2027 (precio 974,50) y el 06-08-2027 (precio 973,78, subasta real del 04-08-2026).
Sustituir en `data/letras.csv` y volver a ejecutar `python -m cartera escalera`.

## 8.2 Qué es esta estructura y qué hace bien

Es una **escalera de dos peldaños**: cada 6 meses vence una Letra, así que la mitad del capital vuelve a
estar disponible dos veces al año. Ventajas objetivas:

- Liquidez semestral sin vender en el mercado secundario.
- Cada vencimiento es un punto de decisión natural: renovar, mover a fondos o mezclar, **sin ningún
  coste ni penalización fiscal** por no renovar.
- Si los tipos suben, la mitad de la cartera se reinvierte al nuevo tipo en menos de 6 meses.
- Diversificación temporal del riesgo de tipos (pequeña, con dos peldaños).

Es una estructura razonable para un fondo de emergencia o para dinero con destino a < 3 años.

## 8.3 Qué rinde hoy (supuestos de 8.1)

`python -m cartera escalera --data data --hoy 2026-09-10 --inflacion 0.033`

| Vence | Nominal | Pagado | Tipo bruto | TAE neta | Rendimiento neto |
|---|---|---|---|---|---|
| 2027-02-12 | 8.000 € | 7.796,00 € | 2,59 % | 2,13 % | 165,24 € |
| 2027-08-06 | 8.000 € | 7.790,24 € | 2,66 % | 2,19 % | 169,91 € |

| Concepto | Valor anual aproximado |
|---|---|
| Rendimiento neto total de la escalera (16.000 € nominal) | **≈ 335 €** |
| Pérdida de poder adquisitivo con inflación del 3,3 % | **≈ 193 €** (16.000 × 3,3 % − 335) |
| TAE real neta | ≈ −1,1 % a −1,2 % |

Sensibilidad: si la primera Letra se compró al 2,50 % en lugar de al 2,59 %, su rendimiento neto baja
a ≈ 160 €. El orden de magnitud no cambia: la escalera gana ≈ 320–340 € netos al año y pierde ≈ 190–210 €
de poder adquisitivo. Estos números son hechos condicionados a los supuestos de fecha y precio.

## 8.4 Opciones a cada vencimiento

El comando `escalera --peso-letras X --reserva Y` calcula cuánto renovar y cuánto mover en cada
vencimiento para acabar con la fracción X del nominal actual (o al menos Y euros) en Letras.

| Escenario | Vence 02-2027 | Vence 08-2027 | Resultado |
|---|---|---|---|
| Mantener todo (`--peso-letras 1`) | Renovar 8.000 | Renovar 8.000 | 16.000 € en Letras; sigue la pérdida real |
| Mitad (`--peso-letras 0.5`) | Mover 8.000 a fondos | Renovar 8.000 | 8.000 € en Letras como reserva; 8.000 € en fondos |
| Reserva fija (`--peso-letras 0 --reserva 5000`) | Mover 8.000 | Renovar 5.000, mover 3.000 | 5.000 € en Letras; 11.000 € en fondos |
| Todo a fondos (`--peso-letras 0`) | Mover 8.000 | Mover 8.000 | 0 € en Letras |

Cuál elegir depende de los datos del documento 01, sobre todo de si estos 16.000 € **son** el fondo de
emergencia o hay otro aparte. Sin ese dato no procede recomendar un escenario.

## 8.5 Ventaja de mover por vencimientos y no de golpe

Mover 8.000 € en febrero y 8.000 € en agosto de 2027 reparte la entrada en renta variable en dos momentos
separados 6 meses. Reduce (no elimina) el riesgo de entrar todo el capital justo antes de una caída.
No vender las Letras antes de vencimiento evita además el diferencial de precio del mercado secundario.

## 8.6 Qué hacer ahora con esta información

1. Localizar en la cuenta directa del Banco de España (o en el banco intermediario) la fecha de compra,
   fecha de vencimiento y precio de cada Letra, y pasarlos a `data/letras.csv`.
2. Confirmar si existe fondo de emergencia aparte de estas dos Letras.
3. Con eso, fijar `--peso-letras` y `--reserva` y dejar el plan escrito en el documento 02.
