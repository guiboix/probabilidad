# 11. Dónde está el dinero: CaixaBank, Banco de España y MyInvestor

> Dato del usuario (10-09-2026): su capital está en CaixaBank. Este documento explica por qué eso importa,
> cuantifica el coste y propone qué comprobar. Cifras de comisiones obtenidas de prensa financiera
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

## 11.2 Cuánto cuesta en tus Letras

`python -m cartera letras --precio 980.28 --dias 364 --nominal 8000 --custodio caixabank` frente a `--custodio bde`:

| Letra A (8.000 €, 1,99 %) | Sin comisiones | En CaixaBank | En Banco de España |
|---|---|---|---|
| Rendimiento bruto | 157,76 € | 157,76 € | 157,76 € |
| IRPF | 29,97 € | 29,97 € | 29,97 € |
| Comisiones | 0 € | **51,99 €** | 12,00 € |
| **Rendimiento neto** | 127,79 € | **75,80 €** | 115,79 € |
| TAE neta | 1,63 % | **0,97 %** | 1,48 % |

Si tus Letras están en CaixaBank con esas tarifas, las comisiones se llevan **un tercio** de lo que
ganas con la Letra A y algo más de una cuarta parte de la B. En las dos Letras, pasar de CaixaBank al Banco
de España supone ≈ 80 € más al año, sin cambiar de producto ni de riesgo.

Es un hecho condicionado a dos cosas que debes comprobar: que las Letras estén efectivamente en CaixaBank
y que la tarifa aplicada sea esa. Se ve en el extracto: busca un cargo de ≈ 48 € al comprar y cargos
semestrales de ≈ 2 € por custodia.

## 11.3 El dinero que está parado

CaixaBank no remunera la cuenta corriente (0 % TAE) salvo promociones para clientes nuevos. Todo euro que
esté en la cuenta sin función (por encima del fondo de emergencia y de los gastos del mes) pierde el 3,3 %
anual de inflación entero. Como referencia:

| Dónde | Rendimiento 09-2026 | Garantía | Coste de tener 5.000 € parados un año |
|---|---|---|---|
| Cuenta corriente CaixaBank | 0 % | FGD España 100.000 € | 0 € ganados; ≈ 165 € de poder adquisitivo perdido |
| Cuenta remunerada MyInvestor | 2,5 % TAE (promoción, condiciones) | FGD España 100.000 € | ≈ 101 € netos ganados |
| Letra 12 meses en BdE | 2,66 % | Estado | ≈ 106 € netos ganados |

Además, CaixaBank cobra 60 € al trimestre de mantenimiento si no se cumplen condiciones (nómina, 20.000 €
en productos, etc.). Comprobar si las cumples.

## 11.4 Lo que NO conviene hacer en CaixaBank

- **Comprar fondos de CaixaBank AM**: comisiones habituales del 1–2 % anual, sin acceso a indexados baratos.
- **Contratar fondos "sostenibles" de la propia entidad** sin comparar TER: el filtro ético no justifica
  pagar 1,5 % cuando un indexado ESG cuesta 0,15–0,30 %.
- **Depósitos estructurados o "garantizados"** que la oficina ofrezca al vencer las Letras.

## 11.5 Qué comprobar y qué decidir

1. **Dónde están las Letras.** Si en CaixaBank: al vencer la A (06-11-2026), abrir cuenta directa en el
   Banco de España (gratis, con certificado digital o Cl@ve) y hacer la renovación allí. No hay que vender:
   cobras en CaixaBank y compras en la subasta desde la cuenta directa.
2. **Cuánto dinero está parado** en la cuenta corriente y cuánto necesitas de verdad como colchón. Lo que
   sobre, a cuenta remunerada o a Letras.
3. **Si pagas mantenimiento** (60 €/trimestre) y por qué condición estás exento.
4. **Dónde están los bonos** y qué te cobran por ellos (documento 10 §10.4).
5. **Concentración**: si el capital total en CaixaBank supera 100.000 €, el exceso queda fuera de la garantía
   de depósitos. Dato pendiente.

## 11.6 Cómo queda el mapa de custodios propuesto

| Custodio | Qué guarda | Por qué |
|---|---|---|
| CaixaBank | Cuenta operativa (nómina, recibos) y fondo de emergencia | Ya está montado; condiciones de exención de comisiones |
| Banco de España (cuenta directa) | Letras y, si se decide, Bonos del Estado | Coste mínimo, cero intermediarios |
| MyInvestor | Fondos indexados éticos y, si cumple condiciones, liquidez remunerada | Sin custodia ni mínimos; traspasos gratuitos |
