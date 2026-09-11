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

## 11.2 bis Mapa del capital (≈ 37.900 €, corregido 10-09-2026)

| Dónde | Importe | Estado |
|---|---|---|
| Letras A y B (Banco de España) | 16.000 € | Confirmado |
| Cuentas (CaixaBank) al 0 % = fondo de emergencia | ≈ 16.000 € | Confirmado. Doble función: colchón e "invertible si es seguro" |
| PIAS (seguro de ahorro) | 5.890 € | Confirmado el importe. Aseguradora, costes, rentabilidad y penalizaciones: pendientes (documento 10 §10.6) |
| Fondo de aprendizaje (previsto) | 300 € | Por contratar, con ahorro nuevo |
| **Total** | **≈ 37.900 €** | |

Dos consecuencias inmediatas:

- **Garantía de depósitos:** con ≈ 38.000 € en total estás muy por debajo de los 100.000 € cubiertos por entidad.
  Sin problema de concentración.
- **Mantenimiento:** el usuario confirma que CaixaBank no le cobra. Nada que corregir.

## 11.2 ter Qué hacer con un fondo de emergencia de 16.000 € (explicado desde cero)

Un fondo de emergencia tiene una sola obligación: **estar disponible en días y no haber bajado de valor**
cuando haga falta. No tiene obligación de rendir 0 %. Hoy los 16.000 € pierden ≈ 530 € al año de poder de
compra (3,3 % de inflación) por estar en una cuenta al 0 %.

Los productos que cumplen esa obligación y además rinden algo son solo estos:

| Producto | Disponible en | ¿Puede bajar de valor? | Rendimiento 09-2026 | Garantía |
|---|---|---|---|---|
| Cuenta remunerada (MyInvestor) | Inmediato | No | 1,00–1,25 % TAE el primer año; 0,30 % después (bases legales aportadas) | FGD hasta 100.000 € |
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

(Ejemplo genérico sustituido por el cálculo con datos reales, más abajo.)

### Cálculo con los datos del usuario (10-09-2026, cuota de autónomos confirmada)

Datos declarados: autónomo; cuota de autónomos 328 €/mes; asesoría e impuestos ≈ 500 € por trimestre como
mínimo; gastos personales ≈ 600 €/mes.

| Concepto | Al mes |
|---|---|
| Gastos personales | 600 € |
| Cuota de autónomos | 328 € |
| Asesoría e impuestos (500 €/trimestre) | 167 € |
| **Salida mensual mínima** | **≈ 1.095 €** |

| Colchón | Importe |
|---|---|
| 6 meses | 6.570 € |
| 9 meses | 9.855 € |
| 12 meses | 13.140 € |

Para un autónomo con ingresos variables la referencia prudente son **9–12 meses**, no 3–6: un mal
trimestre de facturación no puede obligar a tocar las Letras. Además, como autónomo hay dinero en la
cuenta que **no es tuyo**: el IVA cobrado y el pago fraccionado de IRPF se liquidan cada trimestre. Ese
importe debe estar apartado mentalmente (o en una subcuenta) y no cuenta ni como colchón ni como inversión.

Reparto propuesto de los ≈ 16.000 € en cuentas (interpretación, no norma):

| Tramo | Con colchón de 9 meses | Con colchón de 12 meses | Dónde | Función |
|---|---|---|---|---|
| Operativa: 2 meses de salidas + reserva fiscal del trimestre | ≈ 2.700 € | ≈ 2.700 € | Cuenta corriente CaixaBank | Pagar el mes y el próximo modelo trimestral sin mirar |
| Resto del colchón | ≈ 7.200 € | ≈ 10.400 € | Cuenta remunerada (si el tipo es bueno) o Letras a 3 y 6 meses escalonadas en el Banco de España | Emergencias; no baja de valor; disponible en ≤ 3 meses |
| Sobrante | ≈ 6.100 € | ≈ 2.900 € | Cartera conservadora: Letra a 12 meses (tercer peldaño de la escalera) o, tras el aprendizaje, renta fija corta ética | Deja de ser colchón; sigue siendo seguro |

**Decisión del usuario (10-09-2026): colchón de 12 meses**, porque su facturación es variable.
**Esquema del usuario (11-09-2026):** dos bloques de Letras a 12 meses de 10.000 € cada uno, renovados
en noviembre y junio; el resto en cuenta (documento 08 §8.4 bis):

| Tramo | Importe | Dónde | Cuándo |
|---|---|---|---|
| Liquidez inmediata (colchón + reserva fiscal) | ≈ 12.000 € | Cuenta corriente CaixaBank | Ya está |
| Se suma al bloque A | 2.000 € | Letra a 12 meses, subasta 03-11-2026 | Petición antes del 27-10-2026 |
| Se suma al bloque B | 2.000 € | Letra a 12 meses, subasta ≈ 01-06-2027 | Petición ≈ 25-05-2027 |

Con esto, el capital queda así: 20.000 € en Letras a 12 meses + ≈ 12.000 € en cuenta + el PIAS (5.891 €),
pendiente de la respuesta de la asesora.

Coste de mantener 12.000 € en cuenta al 0 %: ≈ 400 € al año de poder de compra (≈ 265 € netos que darían
las Letras). Es el precio de la liquidez total; decisión del usuario, revisable en junio de 2027.

Sobre la confianza que pide el usuario: los cuatro productos de la tabla comparten la característica de que
**el capital no baja**. La forma de ganar confianza sin arriesgar el colchón es empezar por uno de ellos
(cuenta remunerada o una Letra a 3 meses) y comprobar durante un trimestre que el dinero está ahí, rinde
lo prometido y se puede recuperar. Solo después tiene sentido probar productos de riesgo 2 con dinero que
no sea el colchón.

## 11.2 quater La cuenta remunerada de MyInvestor: condiciones reales (bases legales aportadas por el usuario)

El usuario ha aportado el 10-09-2026 las **bases legales de la promoción vigente desde el 01-05-2026**, el
contrato marco (versión 19-01-2026), el certificado de titularidad y el extracto de la cuenta. Datos que
importan (los personales no se copian aquí):

| Situación | TAE | Detalle |
|---|---|---|
| Primeros 12 meses desde la apertura, sin condiciones | **Tipo de la facilidad de depósito del BCE − 1,25 puntos**, como mínimo | El BCE subió la facilidad de depósito al **2,50 %** el 10-09-2026 (efectos desde el 16-09-2026) → **1,25 %** para tu cuenta. Saldo máximo 70.000 €. La TAE exacta se publica en la web de MyInvestor |
| A partir del mes 13, sin condiciones | **0,30 %** | Máximo 210 € brutos al año |
| Invirtiendo 300 € netos/mes en productos MyInvestor | Igual que el primer año | Desde el 01-09-2026 |
| Invirtiendo 600 € netos/mes | 1,75 % | Idem |
| Invirtiendo 900 € netos/mes | 2,50 % | Idem |
| Con una póliza AXA contratada a través de MyInvestor | Igual que el primer año | Solo cuentas de más de 12 meses |

Otros puntos de las bases: los intereses se abonan cada mes en el aniversario de apertura; hay retención
del 19 %; los traspasos no cuentan como inversión, solo las suscripciones nuevas; MyInvestor puede
modificar o cancelar la promoción avisando; cancelar y reabrir la cuenta no reinicia el primer año.

**Estado de la cuenta según el extracto del 10-09-2026:** cuenta de efectivo y cuenta de valores activadas,
saldo 0 €, sin movimientos. Es una cuenta recién abierta: el primer año de remuneración corre desde ahora.

**Lectura con la regla del listón** (documento 02 §2.2 bis): la Letra a 12 meses da 2,66 % bruto y la de
3 meses ≈ 2,2–2,4 %. La cuenta da 1,00–1,25 % el primer año y 0,30 % después. Los tramos del 1,75 % y
2,50 % exigen suscribir 600 o 900 € nuevos **cada mes** en productos de la lista (carteras automatizadas,
fondos de la casa, planes de pensiones), sin traspasos; para un fondo de aprendizaje de 300 € no tiene
sentido y el 2,50 % ni siquiera supera claramente a la Letra. **Conclusión: el colchón no va a la cuenta
de MyInvestor; va a Letras a 3 y 6 meses en el Banco de España.** La cuenta de MyInvestor se usa solo
como cuenta operativa para comprar el fondo de aprendizaje.

Nota: en una búsqueda previa apareció una promoción del 2,5 % para cuentas abiertas entre julio y agosto de
2026. No figura en las bases aportadas (versión de mayo de 2026), así que **no se cuenta con ella**. Si la
app mostrara una TAE distinta de la calculada aquí, manda la app.

**Contrato marco:** MyInvestor Banco es entidad de crédito supervisada por el Banco de España y la CNMV,
adherida al Fondo de Garantía de Depósitos español (hasta 100.000 € por titular). Sin comisión de custodia
ni de mantenimiento en cuentas y fondos según sus tarifas; comprobar el apartado "Tarifas especiales"
(página 48 del contrato) antes de operar con cualquier producto que no sea un fondo indexado.

**Aviso sobre los documentos aportados:** el certificado de titularidad y el extracto contienen nombre,
NIF, IBAN y domicilio. No se han copiado a este repositorio ni hacen falta para el análisis. Conviene no
compartirlos salvo con quien los necesite.

**Cómo verlo en la app o la web de MyInvestor** (los menús cambian; esto es lo que hay que buscar, no un
recorrido exacto):

1. Entrar y abrir la **cuenta corriente**. En su ficha o en "Detalles" / "Condiciones" aparece la
   remuneración que se aplica **a ti** (TAE) y el saldo máximo remunerado. Ese número es el que importa;
   los de la web comercial son los máximos posibles.
2. Comprobar la **fecha de apertura** de la cuenta (en los datos de la cuenta o en el contrato que llegó
   por correo electrónico al abrirla). Decide si estás dentro de la promoción del 2,5 %.
3. Mirar el **último abono de intereses**: si la cuenta lleva más de un mes con saldo, hay un apunte
   mensual "Intereses" o "Remuneración". Dividir ese importe entre el saldo medio y multiplicar por 12
   da la TAE real que estás cobrando, sin depender de lo que diga ninguna página.
4. Si no aparece, la sección **Ayuda → Preguntas frecuentes → Cuentas** de la web explica los tramos, y
   el chat de atención al cliente responde con la TAE aplicada a tu cuenta.

**Cómo ver los fondos** (para el documento 09): en la sección de inversión, buscador de fondos. Filtrar por
categoría **renta fija** y, si existe el filtro, por **gestión indexada** o **sostenible/ESG**. En la caja
de búsqueda probar "ESG", "SRI", "Screened", "Sustainable", "Green", "corto plazo", "short term". En la ficha
de cada fondo, buscar: ISIN, "gastos corrientes" o TER, "indicador de riesgo" (1–7), "artículo SFDR" y el
enlace al **documento de datos fundamentales** (KID). Anotar nombre exacto e ISIN de los que aparezcan.

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
| MyInvestor | Fondos indexados éticos (cuenta operativa para el fondo de aprendizaje) | Sin custodia ni mínimos; traspasos gratuitos. Su cuenta remunerada no supera el listón |
