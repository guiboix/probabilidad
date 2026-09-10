# 11. Dónde está el dinero: CaixaBank, Banco de España y MyInvestor

> Datos del usuario (10-09-2026): su capital está en CaixaBank, pero **las Letras las compra directamente en
> la web del Tesoro Público**, es decir, en la cuenta directa del Banco de España. Este documento explica por
> qué importa el custodio, cuantifica lo que se ahorra con esa elección y propone qué comprobar sobre el
> resto del capital. Cifras de comisiones obtenidas de prensa financiera
> (El Independiente, Kelisto, Finect) y de la web del Tesoro vía búsqueda; **confirmar en el extracto y en
> el documento de comisiones de CaixaBank**, porque pueden haber cambiado.

## 11.1 Por qué importa el custodio (explicado desde cero)

Una Letra del Tesoro es la misma la compres donde la compres: el Estado te devuelve 1.000 € por cada
Letra. Lo que cambia es **quién la guarda por ti** (el custodio) y **cuánto cobra por hacerlo**. Hay dos
caminos:

| | Banco de España (cuenta directa) | Banco intermediario (CaixaBank) |
|---|---|---|
| Comisión de compra | 0 € | ≈ 0,6 % del nominal, mínimo 30,05 € |
| Comisión de custodia | 0 € | ≈ 0,05 % anual del nominal |
| Comisión al vencer | 0,15 % del importe transferido (mín. 0,90 €, máx. 200 €) | Normalmente 0 |
| Cómo se opera | Web del Tesoro con certificado digital o Cl@ve, o en una sucursal del Banco de España | Oficina o app del banco |
| Fiscalidad | La comisión del 0,15 % es deducible del rendimiento (criterio de la Dirección General de Tributos); hay que meterla a mano en la declaración | Las comisiones bancarias no son deducibles |

## 11.2 Cuánto cuesta en tus Letras (ya estás en el camino barato)

`python -m cartera letras --precio 980.28 --dias 364 --nominal 8000 --custodio caixabank` frente a `--custodio bde`:

| Letra A (8.000 €, 1,99 %) | Sin comisiones | En CaixaBank | En Banco de España |
|---|---|---|---|
| Rendimiento bruto | 157,76 € | 157,76 € | 157,76 € |
| IRPF | 29,97 € | 29,97 € | 29,97 € |
| Comisiones | 0 € | **51,99 €** | 12,00 € |
| **Rendimiento neto** | 127,79 € | **75,80 €** | 115,79 € |
| TAE neta | 1,63 % | **0,97 %** | 1,48 % |

**Confirmado por el usuario: compra en la web del Tesoro (cuenta directa).** Es la columna de la derecha:
pagas 12 € por Letra al vencer y nada más. Si las tuvieras en CaixaBank pagarías ≈ 52 € por Letra; la
elección ya hecha te ahorra ≈ 80 € al año en las dos Letras. Este análisis se conserva como referencia
para no cambiar nunca al canal bancario.

Detalle fiscal útil: la comisión del 0,15 % del Banco de España **es deducible** del rendimiento de la
Letra (criterio de la Dirección General de Tributos), pero el borrador de la Renta no la incluye: hay que
restarla a mano en la casilla del rendimiento. En tus dos Letras son 24 € de base menos, ≈ 4,6 € de impuesto.

## 11.2 bis Mapa del capital (≈ 30.000 €, declarado 10-09-2026)

| Dónde | Importe | Estado |
|---|---|---|
| Letras A y B (Banco de España) | 16.000 € | Confirmado |
| Cuenta corriente CaixaBank al 0 % = fondo de emergencia | ≈ 14.000 € | Confirmado. Doble función: colchón e "invertible si es seguro" |
| Fondo de aprendizaje (previsto) | 300 € | Por contratar, con ahorro nuevo |
| **Total** | **≈ 30.000 €** | |

Dos consecuencias inmediatas:

- **Garantía de depósitos:** con 30.000 € en total estás muy por debajo de los 100.000 € cubiertos por entidad.
  Sin problema de concentración.
- **Mantenimiento:** el usuario confirma que CaixaBank no le cobra. Nada que corregir.

## 11.2 ter Qué hacer con un fondo de emergencia de 14.000 € (explicado desde cero)

Un fondo de emergencia tiene una sola obligación: **estar disponible en días y no haber bajado de valor**
cuando haga falta. No tiene obligación de rendir 0 %. Hoy los 14.000 € pierden ≈ 460 € al año de poder de
compra (3,3 % de inflación) por estar en una cuenta al 0 %.

Los productos que cumplen esa obligación y además rinden algo son solo estos:

| Producto | Disponible en | ¿Puede bajar de valor? | Rendimiento 09-2026 | Garantía |
|---|---|---|---|---|
| Cuenta remunerada (MyInvestor u otra) | Inmediato | No | 2,5 % TAE en promoción; el tipo base sin promoción hay que consultarlo | FGD hasta 100.000 € |
| Letras a 3 meses (Banco de España) | Cada 3 meses (o venta en secundario) | No, a vencimiento | ≈ 2,1–2,4 % | Estado |
| Letras a 6 meses (Banco de España) | Cada 6 meses | No, a vencimiento | ≈ 2,3–2,6 % | Estado |
| Fondo monetario | 1–3 días hábiles | Muy poco (riesgo 1/7) | ≈ tipos BCE − coste | Sin FGD; diversificado |

Lo que **no** cumple la obligación y por tanto no es sitio para el colchón, por seguro que parezca: fondos
de renta fija con duración (riesgo 2 o más), Bonos a 3–5 años, depósitos a plazo sin cancelación anticipada,
y por supuesto cualquier cosa con acciones.

Esquema razonable, pendiente de saber cuántos meses de gastos hay que cubrir:

1. **Gastos de 2–3 meses** en la cuenta corriente de CaixaBank (operativa) o en cuenta remunerada: acceso inmediato.
2. **El resto del colchón hasta 6 meses de gastos** en cuenta remunerada o en Letras a 3 meses escalonadas
   (una cada mes, así siempre vence una en menos de 30 días).
3. **Lo que sobre por encima de 6 meses de gastos** deja de ser fondo de emergencia y pasa al bloque
   conservador de la cartera (documento 02): Letras a 12 meses o, tras el aprendizaje, renta fija corta ética.

Ejemplo ilustrativo, **no un dato**: con gastos de 1.500 €/mes, 6 meses son 9.000 €; los otros 5.000 €
serían invertibles bajo las reglas conservadoras. Con gastos de 2.300 €/mes, los 14.000 € son el colchón
entero y no sobra nada. El número que falta es el gasto mensual.

Sobre la confianza que pide el usuario: los cuatro productos de la tabla comparten la característica de que
**el capital no baja**. La forma de ganar confianza sin arriesgar el colchón es empezar por uno de ellos
(cuenta remunerada o una Letra a 3 meses) y comprobar durante un trimestre que el dinero está ahí, rinde
lo prometido y se puede recuperar. Solo después tiene sentido probar productos de riesgo 2 con dinero que
no sea el colchón.

## 11.3 El dinero que está parado

CaixaBank no remunera la cuenta corriente (0 % TAE) salvo promociones para clientes nuevos. Todo euro que
esté en la cuenta sin función (por encima del fondo de emergencia y de los gastos del mes) pierde el 3,3 %
anual de inflación entero. Como referencia:

| Dónde | Rendimiento 09-2026 | Garantía | Coste de tener 5.000 € parados un año |
|---|---|---|---|
| Cuenta corriente CaixaBank | 0 % | FGD España 100.000 € | 0 € ganados; ≈ 165 € de poder adquisitivo perdido |
| Cuenta remunerada MyInvestor | 2,5 % TAE (promoción, condiciones) | FGD España 100.000 € | ≈ 101 € netos ganados |
| Letra 12 meses en BdE | 2,66 % | Estado | ≈ 106 € netos ganados |

CaixaBank cobra 60 € al trimestre de mantenimiento si no se cumplen condiciones; el usuario confirma
que está exento.

## 11.4 Lo que NO conviene hacer en CaixaBank

- **Comprar fondos de CaixaBank AM**: comisiones habituales del 1–2 % anual, sin acceso a indexados baratos.
- **Contratar fondos "sostenibles" de la propia entidad** sin comparar TER: el filtro ético no justifica
  pagar 1,5 % cuando un indexado ESG cuesta 0,15–0,30 %.
- **Depósitos estructurados o "garantizados"** que la oficina ofrezca al vencer las Letras.

## 11.5 Qué comprobar y qué decidir

1. ~~Dónde están las Letras~~ Confirmado: cuenta directa del Banco de España. Mantener así.
2. **Cuánto dinero está parado** en la cuenta corriente y cuánto necesitas de verdad como colchón. Lo que
   sobre, a cuenta remunerada o a Letras.
3. ~~Si pagas mantenimiento~~ Confirmado: exento.
4. ~~Dónde están los bonos~~ Aclarado: los "bonos" son las Letras.
5. ~~Concentración~~ Confirmado: ≈ 30.000 € en total, dentro de la garantía de 100.000 €.

## 11.6 Cómo queda el mapa de custodios propuesto

| Custodio | Qué guarda | Por qué |
|---|---|---|
| CaixaBank | Cuenta operativa (nómina, recibos) y fondo de emergencia | Ya está montado; condiciones de exención de comisiones |
| Banco de España (cuenta directa) | Letras (ya) y, si se decide, Bonos del Estado | Coste mínimo, cero intermediarios |
| MyInvestor | Fondos indexados éticos y, si cumple condiciones, liquidez remunerada | Sin custodia ni mínimos; traspasos gratuitos |
