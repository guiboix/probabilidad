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

Con esto, el capital queda así: 20.000 € en Letras a 12 meses + ≈ 12.000 € en cuenta + el dinero del PIAS ya rescatado
(5.772,75 € en cuenta desde el 18-09-2026), pendiente de destino.

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
sentido y el 2,50 % ni siquiera supera claramente a la Letra. ~~Conclusión: el colchón no va a la cuenta de MyInvestor.~~

**CORRECCIÓN (28-09-2026): el marco de comparación estaba mal.** Se comparó la cuenta remunerada contra la
Letra, cuando la regla del listón (documento 02 §2.2 bis) se aplica a productos **con riesgo**. Una cuenta
remunerada y una cuenta corriente tienen el mismo riesgo: ninguno, ambas con garantía del FGD hasta
100.000 €. El dinero que se queda líquido como colchón **no va a ir a Letras por definición**, así que su
alternativa real no es el 2,66 % de la Letra sino el **0 % de CaixaBank**.

| Destino del colchón líquido (≈ 13.073 €) | Rendimiento neto anual |
|---|---|
| Cuenta corriente CaixaBank (0 %) | 0 € |
| Cuenta MyInvestor, primer año (BCE 2,50 % − 1,25 = **1,25 %**) | **132 €** |
| Cuenta MyInvestor, desde el mes 13 (0,30 %) | 32 € |

Con la misma liquidez, la misma garantía y ningún riesgo añadido. La cuenta se abrió en septiembre de 2026,
así que el tramo del primer año corre hasta ≈ septiembre de 2027.

**Decisión sobre darse de baja (28-09-2026): NO cerrar la cuenta.** Motivos: (1) no tiene coste de
mantenimiento ni saldo mínimo; (2) las bases legales establecen que quien cancela y reabre pasa
automáticamente al 0,30 %, de modo que cerrarla **quema el derecho al primer año**; (3) sirve como destino
del colchón líquido con rendimiento; (4) deja abierta la opción de fondos sin volver a darse de alta.

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

## 11.2 quinquies ¿Hay un banco mejor que MyInvestor para el colchón? (15-10-2026)

**Pregunta del usuario:** *"¿conoces algún banco que sea mejor que este para lo que yo busco?"*

**Conclusión corta: sí, varios.** MyInvestor paga **1,25 %** a tu colchón. Hay cuentas remuneradas con la
**misma garantía española** y **sin riesgo añadido** que pagan entre el 2,75 % y el 3,25 %. La mejor
encaje con tu perfil es **Openbank (3,25 % TAE, grupo Santander)**, y el plazo para darse de alta
**acaba el 29-10-2026**.

### Comparativa (datos de prensa especializada, octubre 2026)

Saldo de referencia: **12.000 €** (colchón actual, después de la transferencia de 11.000 € a Letras) y
**20.000 €** (a partir del 6 de noviembre, cuando llega la amortización de 8.000 €). IRPF del ahorro 19 %.

| Cuenta | TAE | Neto/año con 12.000 € | Neto/año con 20.000 € | Garantía de depósitos | Condiciones |
|---|---|---|---|---|---|
| **Openbank** | **3,25 %** | **316 €** | **526 €** | **España** (Santander) | Nuevo cliente, activar Bizum, código promocional, 12 meses, sin límite de saldo |
| Trade Republic | 3,04 % | 295 € | 492 € | **Alemania** | Hasta 50.000 € |
| Bankinter Cuenta Digital | 3,00 % | 292 € | 486 € | España | 12 meses, alta antes del 28-10-2026 |
| Sabadell Cuenta Online | 2,75 % | 267 € | 446 € | España | Sin condiciones |
| Revolut | 3,51 % | 341 €* | 569 €* | **Lituania** | *Solo 4 meses y hasta 25.000 €: el importe real es ≈ 1/3 del indicado |
| MyInvestor (ya abierta) | 1,25 % | 122 € | 202 € | España | Ninguna, pero solo el primer año; luego 0,30 % |
| CaixaBank cuenta corriente | 0 % | 0 € | 0 € | España | — |

**Diferencia concreta:** con 20.000 € de colchón, Openbank deja **324 € netos más al año que MyInvestor** y
**526 € más que dejarlo en CaixaBank**. Sin riesgo de pérdida y con el dinero disponible en el día.

### Por qué Openbank y no los que pagan más

1. **Garantía española.** Revolut (Lituania) y Trade Republic (Alemania) también tienen garantía de 100.000 €,
   pero la cobertura la paga el fondo de su país y reclamarla sería un trámite transfronterizo. Openbank es
   Banco Santander: FGD español y la entidad más grande del país. Para un perfil "muy conservador" esto pesa.
2. **El 3,51 % de Revolut es publicidad.** Dura 4 meses y solo cubre 25.000 €. Al quinto mes cae.
3. **Condiciones que de verdad puedes cumplir.** Openbank pide activar Bizum y meter al menos 1 €. No exige
   nómina, ni recibos, ni invertir cada mes. No tiene comisiones de mantenimiento ni saldo mínimo.
4. **Sin límite de saldo remunerado.** MyInvestor te remunera hasta 70.000 € (irrelevante para ti) pero al
   1,25 %. Openbank no limita el saldo.

### Lo que hay que saber antes de decidir

- **Es un tipo promocional de 12 meses.** Pasado el año, la cuenta pasa al tipo vigente de la Cuenta de Ahorro
  Openbank, que probablemente será mucho más bajo. Dentro de un año habrá que repetir este ejercicio. Esto
  no es un problema: es la naturaleza de este producto. La alternativa (0 % en CaixaBank) no mejora con el tiempo.
- **Plazo de alta: 29-10-2026.** Después, el tipo que se ofrezca será otro.
- **No cierres la cuenta de MyInvestor** (ver §11.2 quater): no cuesta nada tenerla y cerrarla quema el
  derecho al tramo del primer año.
- **No pongas el colchón entero.** Deja en CaixaBank el dinero de los próximos 2–3 meses de gastos y los
  impuestos del trimestre (≈ 3.000–4.000 €), porque es la cuenta por la que pasan los cargos de autónomo.
  El resto puede ir a la remunerada.
- **Los datos de esta tabla vienen de prensa financiera, no de las webs de los bancos.** Las fuentes no
  coinciden del todo entre sí. **Antes de abrir nada, verifica la TAE, el plazo y las condiciones en la web
  oficial de Openbank.** Si lo que dice la web no coincide con esta tabla, manda la web.

### Lo que NO cambia

Esto afecta **solo al colchón líquido**. No toca:

- las Letras del Tesoro (siguen en la cuenta directa del Banco de España, que es el canal más barato);
- la decisión sobre fondos (documento 09);
- el seguro de vida ni el testamento, que siguen siendo los dos asuntos pendientes más importantes y que
  valen más que estos 300 € al año.

### Decisión pendiente

| Opción | Ventaja | Inconveniente |
|---|---|---|
| **A. Abrir Openbank antes del 29-10-2026** | +324 €/año netos con 20.000 €; FGD español; sin condiciones reales | Un banco más que gestionar; hay que repetir la búsqueda en 12 meses |
| B. Dejar el colchón en MyInvestor | Cuenta ya abierta, cero trámite | 122–202 €/año; cae al 0,30 % en septiembre de 2027 |
| C. No mover nada (CaixaBank) | Cero trámite | 0 €/año; la inflación se come el 3,3 % |

Recomendación: **opción A**, con la verificación previa en la web de Openbank.

## 11.2 sexies REVISIÓN IMPORTANTE (06-11-2026): la inflación está al 4,9 %, no al 3,3 %

**Todo el análisis anterior de este repositorio usaba una inflación del 3,3 %. Ese dato está obsoleto.**
El indicador adelantado del INE publicado el 30-10-2026 sitúa el **IPC interanual en el 4,9 %**, igual que
en septiembre y en máximos desde febrero de 2023
([INE vía FashionUnited](https://fashionunited.es/noticias/empresas/la-inflacion-se-mantiene-disparada-al-4-9-por-ciento-en-octubre/2026103051080)).
Es una estimación; el dato definitivo sale a mediados de noviembre.

Esto cambia la conclusión de fondo, así que se deja escrito sin maquillarlo:

| Producto | Bruto | Neto (IRPF 19 %) | **Real (neto − 4,9 %)** |
|---|---|---|---|
| Letra 12m adjudicada el 03-11-2026 | 3,08 % | 2,49 % | **−2,29 %** |
| Openbank (si sigue al 3,25 %) | 3,25 % | 2,63 % | **−2,16 %** |
| Bankinter Cuenta Digital | 3,00 % | 2,43 % | **−2,35 %** |
| B100 Cuenta Save | 2,75 % | 2,23 % | **−2,55 %** |
| MyInvestor | 1,25 % | 1,01 % | **−3,71 %** |
| CaixaBank cuenta corriente | 0 % | 0 % | **−4,67 %** |

**Hecho, no opinión: con la inflación al 4,9 %, ningún producto sin riesgo conserva el poder adquisitivo.**
Ni las Letras, ni la mejor cuenta remunerada del mercado. La pérdida en euros, a un año:

| Saldo | En Letra (−2,3 % real) | Al 0 % (−4,7 % real) |
|---|---|---|
| 8.000 € | −183 € | −374 € |
| 10.671 € (la Letra nueva) | −245 € | −498 € |
| 19.090 € (el saldo en cuenta) | −438 € | −891 € |

**Lo que esto NO significa:** no es un argumento para salir corriendo a buscar rentabilidad. La seguridad
nominal de la Letra sigue siendo real y sigue valiendo. Significa dos cosas concretas y limitadas:

1. **Lo que está al 0 % cuesta el doble que antes.** La diferencia entre dejar 19.090 € en CaixaBank y
   ponerlos en una cuenta remunerada al 3 % ya no son 300 € de rentabilidad: son **≈ 450 € netos al año de
   pérdida evitada**. Esto es dinero sin riesgo añadido y sin pérdida de liquidez.
2. **La decisión sobre fondos (documento 09) sigue siendo del usuario y sigue sin urgencia.** No se cambia
   la recomendación: el seguro de vida y el testamento siguen pesando más que cualquier punto de
   rentabilidad.

**Confianza en el dato:** media-alta para el 4,9 % (indicador adelantado oficial del INE, pero provisional).
Alta para los cálculos derivados. **Pendiente:** confirmar el IPC definitivo a mediados de noviembre y, si
cambia, recalcular esta tabla.

## 11.2 septies El plazo de Openbank venció el 29-10-2026 (estado a 06-11-2026)

La recomendación de §11.2 quinquies tenía fecha límite de alta el **29-10-2026** y **no se ejecutó**. A
06-11-2026 los comparadores siguen citando el 3,25 % de Openbank, lo que sugiere que la promoción se
prorrogó o se renovó, pero **no está confirmado en la web del banco**. Lo que dicen las fuentes de
noviembre de 2026:

| Cuenta | TAE citada | Nota |
|---|---|---|
| Openbank | 3,25 % (un blog dice 3,35 %) | 12 meses, sin límite de saldo, FGD español |
| Revolut | 3,51 % | FGD **lituano**; las fuentes discrepan sobre si hay condiciones |
| Raisin Cuenta Bienvenida | 3,30 % | **Solo 3 meses** |
| Bankinter Cuenta Digital | 3,00 % | Hasta 100.000 €; una fuente da alta hasta **11-11-2026** |
| bunq | 3,11 % / 2,01 % | Las fuentes se contradicen abiertamente |
| B100 Cuenta Save | 2,75 % | Sin condiciones, garantizado hasta 31-12-2026 |

Fuentes: [Finect](https://www.finect.com/usuario/AsunInfante/articulos/mejores-cuentas-remuneradas),
[Rankia](https://www.rankia.com/blog/cuentas-corrientes/5424567-mejores-cuentas-remuneradas),
[HelpMyCash](https://www.helpmycash.com/cuentas/cuentas-remuneradas/),
[Bankkers](https://bankkers.com/cuentas/mejores-cuentas-remuneradas/),
[ComparadorBancario](https://comparadorbancario.com/cuentas-remuneradas/).

**Advertencia metodológica:** son comparadores y blogs, no bancos. Las cifras se contradicen entre sí
(bunq al 3,11 % y al 2,01 % en la misma semana). **Ninguna de estas cifras sirve para decidir sin abrir la
web oficial del banco.** La recomendación de fondo no cambia: Openbank por garantía española y condiciones
cumplibles; Bankinter como alternativa; Revolut y Raisin descartados (garantía extranjera y plazo de 3 meses).

**Dinero disponible ahora:** ≈ 19.090 € en cuentas de CaixaBank, menos el cargo de los modelos
trimestrales. Dejando 4.000 € de operativa y impuestos, hay **≈ 15.000 € que podrían ir a una cuenta
remunerada**, lo que al 3,25 % serían ≈ 395 € netos al año frente a los 0 € actuales.

## 11.2 octies CONFIRMADO en la web oficial de Openbank (06-11-2026)

El usuario aporta la **página de ofertas de Openbank en PDF**. Esto ya no es un comparador: es la fuente
primaria. Lo que dice literalmente:

| Dato | Lo que pone la web |
|---|---|
| Tipo | **3,25 % TAE** "durante un año y para todo tu dinero **por traer Bizum**" |
| TIN implícito | **3,20 %** (deducido de su propia calculadora, ver verificación abajo) |
| Límite de saldo | **Ninguno** ("Calcula cuánto ganarías en un año, **sin límite**") |
| Bono adicional | **+200 €** por traer 2 recibos (20 €/mes durante 10 meses) |
| **Fecha límite** | **"¡Ampliamos promoción! Hasta el 16/11/2026"** ← se prorrogó desde el 29-10 |
| Código | **OPEN325** |
| Garantía | "Entidad adherida al **Fondo de Garantía de Depósitos de Entidades de Crédito Español**", 100.000 € por depositante |
| Indicador de riesgo | **1/6** (el más bajo de la escala) |
| Comisiones | 0 € cuenta, 0 € tarjeta (primer titular), 0 € en más de 5.000 cajeros Santander |
| Al año 13 | Pasa a Cuenta de Ahorro Openbank "con el tipo de interés nominal que tenga en ese momento" |
| Respaldo | Grupo Santander |

### Verificación del TIN contra su propia calculadora

La web muestra para 10.000 € con el bono activado: **46,67 €/mes** y **520 € en total**. Reconstrucción:

    10.000 € × 3,20 % TIN = 320,00 €/año → 26,67 €/mes
    26,67 € + 20 € (bono recibos)        = 46,67 €/mes   ✓ coincide
    320 € + 200 €                        = 520 €         ✓ coincide

Confirmado: **TIN 3,20 %, TAE 3,25 %** (la diferencia es la capitalización mensual), y las cifras de la web
son **brutas**, antes de la retención del 19 %.

### Lo que ganaría el usuario

Retención/IRPF 19 %. El bono de 200 € se trata aquí como importe bruto, en el escenario conservador.

| Saldo | Interés bruto | Interés neto | + bono | **Total neto/año** | Real (−4,9 % IPC) |
|---|---|---|---|---|---|
| 10.000 € | 320 € | 259 € | 200 € | **459 €** | −0,29 % |
| 12.000 € | 384 € | 311 € | 200 € | **511 €** | −0,61 % |
| **15.000 €** | **480 €** | **389 €** | **200 €** | **589 €** | **−0,93 %** |
| 19.000 € | 608 € | 492 € | 200 € | **692 €** | −1,20 % |

Comparación sobre 15.000 €, neto al año:

| Destino | Neto/año | % neto |
|---|---|---|
| **Openbank con bono de recibos** | **589 €** | **3,93 %** |
| Openbank sin bono | 389 € | 2,59 % |
| MyInvestor (1,25 %) | 152 € | 1,01 % |
| CaixaBank (0 %) | 0 € | 0,00 % |

Dato notable: **con el bono de recibos, la rentabilidad neta (3,93 %) supera a la Letra a 12 meses recién
adjudicada (2,49 % neto)**, con liquidez total y la misma garantía estatal de fondo. Es la primera vez en
este proyecto que un producto sin riesgo bate al Tesoro. El matiz: el bono es un pago único de captación,
no un tipo de interés; no se repite el segundo año.

### ⚠ El punto que hay que comprobar ANTES de contratar: Bizum

La condición del 3,25 % es **"traer Bizum"**. Bizum va asociado al número de teléfono y **solo puede estar
activo en un banco a la vez**. Traerlo a Openbank significa **darlo de baja en CaixaBank**.

El usuario es **autónomo**. Si recibe cobros de clientes por Bizum en CaixaBank, esos cobros pasarían a
entrar en Openbank. No es necesariamente malo, pero **es un cambio operativo real**, no un trámite menor, y
debe decidirlo con ese dato delante. Es el único punto de esta promoción que puede tener consecuencias
prácticas no evidentes.

### Lo que NO se ha podido verificar

El PDF aportado es la página comercial. Las llamadas a pie de página (1, 2, 3, 5) remiten a condiciones que
**no están en el documento**. Antes de firmar hay que leer las **bases legales** y confirmar:

1. Qué cuenta exactamente como "traer Bizum" y desde cuándo corre el 3,25 %.
2. Si el bono de 200 € es neto o bruto, y qué cuenta como "recibo domiciliado".
3. Si hay saldo mínimo o permanencia.
4. Qué pasa si se da de baja antes del año.

### Recomendación

**Contratar, si el asunto de Bizum no interfiere con los cobros de la actividad.** Quedan **10 días**
(límite 16-11-2026). El importe sugerido es **≈ 15.000 €**, dejando en CaixaBank ≈ 4.000 € para la
operativa y los modelos trimestrales. Mantener abierta la cuenta de MyInvestor (§11.2 quater).

## 11.2 nonies Análisis coste-beneficio del cambio (06-11-2026)

El usuario plantea dos objeciones correctas: **(a) usa Bizum para cobros de la actividad** y **(b) hay que
valorar qué le cobraría CaixaBank por perder la vinculación.** Se analiza.

### Corrección previa: no hay que mover ningún ingreso

El usuario habla de "eliminar mi nómina mensual de ese banco para pasarla a Openbank". Dos precisiones:

1. **Es autónomo: no tiene nómina.** Lo que tiene son cobros de clientes y la cuota de autónomos.
2. **La promoción de Openbank NO exige domiciliar ingresos.** Sus condiciones son: código OPEN325, al menos
   1 €, y **traer Bizum**. El bono de 200 € añade 2 recibos domiciliados. Nada más.

Es decir: **el coste que al usuario le preocupa no hace falta asumirlo.** Sus cobros pueden seguir entrando
en CaixaBank exactamente igual que hoy. Lo único que se mueve es Bizum, y opcionalmente dos recibos.

### El problema real de Bizum

Bizum va atado al número de teléfono y **solo puede estar activo en una entidad a la vez**. Si el usuario
cobra de clientes por Bizum, traerlo a Openbank significa que esos cobros **entran en Openbank en lugar de
CaixaBank**. El dinero no se pierde ni se retrasa, pero:

- Los cobros de la actividad quedarían repartidos en dos bancos.
- La asesoría tendría que trabajar con extractos de dos entidades. **Puede suponer un coste adicional:
  preguntárselo a Loli, es el dato que falta.**
- Fuentes secundarias discrepan sobre si basta con **activar** Bizum o hay que **mantenerlo como entidad
  principal**. No está confirmado.

### Qué puede cobrar CaixaBank

Sin cumplir el Programa Día a Día: **60 € por trimestre = 240 € al año**
([CaixaBank](https://www.caixabank.es/particular/cuentas-programa-dia-a-dia.html)). El usuario está exento
hoy, pero **no consta por qué motivo**. Las condiciones combinan ingresos recurrentes con domiciliaciones o
uso de tarjeta; los umbrales exactos no se han podido verificar en fuente oficial.

Dos matices importantes:

- **Mover Bizum, por sí solo, no suele ser una condición del Día a Día.** Las condiciones se refieren a
  ingresos y recibos. El riesgo real aparece si **los cobros por Bizum son los "ingresos recurrentes"** que
  sostienen la exención, o si se mueven los 2 recibos para el bono.
- **Existe una salida:** la **Cuenta Online de CaixaBank no tiene comisión de mantenimiento ni
  administración y no exige la vinculación del Día a Día**
  ([Finantres](https://finantres.com/dia-dia-caixabank/)). Si se perdiera la exención, cambiar a esa cuenta
  podría dejar el coste en 0 €. **No verificado para cuentas de autónomo**, que tienen tarifas propias.

### Los números: seis escenarios sobre 15.000 €

Interés neto 389 € · bono 200 € · comisión máxima de CaixaBank −240 €.

| Escenario | Ingreso | Bono | Coste | **Neto/año** |
|---|---|---|---|---|
| 1. No hacer nada | 0 € | 0 € | 0 € | **0 €** |
| 2. Openbank sin Bizum ni recibos | ? | 0 € | 0 € | **desconocido** |
| 3. Bizum sí / recibos no / exención intacta | 389 € | — | — | **+389 €** |
| 4. Bizum sí / recibos no / pierde exención | 389 € | — | −240 € | **+149 €** |
| 5. Bizum sí / recibos sí / exención intacta | 389 € | 200 € | — | **+589 €** |
| 6. Bizum sí / recibos sí / pierde exención | 389 € | 200 € | −240 € | **+349 €** |

**Conclusión cuantitativa: la operación sale positiva en todos los escenarios evaluables.** Incluso
perdiendo la exención por completo y sin cobrar el bono (escenario 4, el peor), quedan **+149 € al año**.
La comisión máxima de CaixaBank (240 €) no llega a anular el beneficio (389–589 €) en ningún caso.

**Punto de equilibrio** (saldo por debajo del cual no compensa, asumiendo que se pierde la exención):

| | Saldo mínimo |
|---|---|
| Sin el bono de recibos | **9.259 €** |
| Con el bono de recibos | **1.543 €** |

El usuario tiene ≈ 19.090 €, muy por encima de ambos umbrales.

### Dónde está la verdadera incógnita

**No es financiera, es operativa.** El coste que no se puede cuantificar aquí es **la complicación de tener
los cobros de la actividad repartidos en dos bancos**, y lo que eso pueda suponer con la asesoría. Si eso
cuesta más de 389 € al año (o más tranquilidad de la que vale el dinero), la respuesta cambia.

**Nivel de confianza:** alto en los cálculos; medio-bajo en dos supuestos de partida (el motivo exacto de la
exención en CaixaBank y la exigencia precisa sobre Bizum), que son **datos que solo pueden confirmar las
entidades**.

### Qué hay que preguntar, y a quién

**A CaixaBank** (app, chat o oficina):
1. ¿Por qué motivo exacto estoy exento de la comisión de mantenimiento ahora mismo?
2. ¿Qué tendría que dejar de cumplir para que me la empezaran a cobrar?
3. Si recibo menos Bizum o muevo 2 recibos, ¿pierdo la exención?
4. ¿Mi cuenta es de particular o de autónomo/negocio, y qué tarifa se le aplica?
5. ¿Puedo pasarme a la Cuenta Online sin comisiones si perdiera la exención?

**A Openbank** (chat 24/7, antes del 16-11-2026):
6. ¿Basta con activar Bizum o hay que mantenerlo como entidad principal durante los 12 meses?
7. Si **no** traigo Bizum, ¿qué TAE me queda? (es el escenario 2, el gran desconocido)
8. ¿Los 200 € del bono son netos o brutos?

**A la asesoría (Loli):**
9. ¿Supone algún coste o complicación que parte de los cobros entren en un segundo banco?

### Recomendación provisional

**Dependiente de la respuesta 7.** Si Openbank mantiene un tipo razonable sin Bizum, esa es la opción
limpia: todo el beneficio, ningún cambio operativo. Si el tipo sin Bizum es malo, hay que elegir entre
+389/589 € al año y la simplicidad de cobrar todo en un sitio — y esa elección es del usuario, no del
análisis. **El plazo (16-11-2026) obliga a preguntar esta semana.**

## 11.2 decies CAMBIO DE RECOMENDACIÓN (06-11-2026): la objeción del usuario es correcta

El usuario señala: *"a partir del segundo año debes ingresar dinero para mantener el interés."* **Tiene
razón, y al cruzarlo con lo de Bizum la recomendación anterior deja de sostenerse.**

### Qué pasa en el año 2

La propia web de Openbank dice: *"Tras el primer año, tu Cuenta Remunerada pasará a ser una Cuenta de
Ahorro Openbank, con el tipo de interés nominal que tenga en ese momento."* Y el tipo de esa cuenta de
ahorro depende de la vinculación. Fuentes secundarias **antiguas** citan **0,20 % TAE con nómina
domiciliada y 0,05 % sin ella**
([Kelisto](https://www.kelisto.es/cuentas-remuneradas/bancos/openbank/cuenta-de-ahorro-bienvenida-sin-condiciones)).
Son datos viejos y no verificados, pero la dirección es inequívoca: **el año 2 no renta nada.**

Sobre 15.000 €: al 0,20 % serían **24 € netos al año**; al 0,05 %, **6 €**.

### Por qué esto cambia la conclusión

El producto es **de 12 meses y se acabó**. Eso no lo invalida —se cobra la promoción y se sale—, pero sí
cambia el cálculo: **el trastorno operativo de mover Bizum también duraría solo ese año, y para ganar muy
poco frente a la alternativa sencilla.**

Comparación sobre 15.000 €, neto al año:

| Opción | TAE | Neto/año | Qué te exige |
|---|---|---|---|
| Openbank + Bizum + 2 recibos | 3,25 % | **589 €** | Bizum (tus cobros) + 2 recibos |
| Openbank + Bizum, sin recibos | 3,25 % | 389 € | Bizum (tus cobros) |
| Openbank + Bizum + recibos, perdiendo exención | 3,25 % | 349 € | Bizum + recibos + 240 € a CaixaBank |
| **B100 Cuenta Save / Sabadell Online** | **2,75 %** | **334 €** | **Nada** |
| Openbank **sin** Bizum | ? | ? | Nada (TAE desconocida) |
| MyInvestor (ya abierta) | 1,25 % | 152 € | Nada |
| CaixaBank (hoy) | 0 % | 0 € | Nada |

**Lo que realmente se paga por mover Bizum y dos recibos:**

| | Diferencia frente a una cuenta sin condiciones |
|---|---|
| Mejor caso (exención intacta + bono) | **+255 €** |
| Peor caso (pierde exención) | **+15 €** |

**Conclusión: la ventaja de Openbank sobre una cuenta sin condiciones es de 255 € en el mejor escenario y
prácticamente nula en el peor.** Para un autónomo que cobra de clientes por Bizum, repartir los cobros
entre dos bancos durante un año —con el trabajo de asesoría que eso añada— **no se justifica por 255 €.**

### Recomendación revisada

| Prioridad | Opción | Por qué |
|---|---|---|
| **1ª** | Preguntar a Openbank **qué TAE queda sin traer Bizum**. Si es ≥ 2,75 %, contratar sin Bizum | Todo el beneficio, cero trastorno |
| **2ª** | Cuenta **sin condiciones** (B100 Cuenta Save o Sabadell Online, ≈ 2,75 %, FGD español) | 334 €/año y no se toca nada de la operativa |
| **3ª** | Openbank con Bizum | Solo si el usuario confirma que apenas cobra por Bizum |
| — | No hacer nada | Cuesta 334–589 € al año de coste de oportunidad |

**Lo que NO cambia:** sacar el dinero del 0 % sigue siendo correcto y sigue siendo lo importante. La
discusión es solo sobre **a qué banco**, y la respuesta es **al que no te obligue a cambiar cómo cobras**.

### Aviso permanente: estos productos caducan

Regla general que vale para cualquier cuenta remunerada, no solo esta: **son promociones de captación.** El
banco paga un tipo alto 12 meses para traerte y confía en que te quedes al 0,05 %. El uso correcto es
cobrar la promoción y revisar antes de que termine.

**Acción obligatoria:** apuntar en la agenda una **revisión en el mes 11** desde la apertura, sea cual sea
el banco elegido. Si no se hace, el dinero se queda al 0,05 % y se pierde todo lo ganado.

**Confianza:** alta en la comparación relativa; media en el tipo exacto del año 2 (fuentes antiguas); baja
en la TAE de Openbank sin Bizum (**dato no encontrado, hay que preguntarlo**).

## 11.2 undecies ¿Cerrar CaixaBank y llevarlo todo a Openbank? (06-11-2026)

**Respuesta corta: no.** Y la pregunta sobre las oficinas del Santander tiene una respuesta parcialmente
buena que conviene entender bien, porque es donde más se equivoca la gente.

### Lo que SÍ puedes hacer en el Santander siendo cliente de Openbank

| Operación | ¿Se puede? | Detalle |
|---|---|---|
| **Sacar efectivo en cajero** | **Sí, gratis** | Más de 5.000 cajeros de Banco Santander y Euro Automatic Cash en España (confirmado en la web de Openbank) |
| **Ingresar efectivo en cajero** | **Sí, con matices** | Solo en los **cajeros nuevos** del Santander, unos **1.800** (no los 5.000). Con la tarjeta Open Debit. Máximo **40 billetes** por operación ([ayuda de Openbank](https://www.openbank.es/ayuda/como-ingresar-dinero-cajero)) |
| Ingresar/sacar en ventanilla de una oficina Santander | **Quizá** | Varias fuentes secundarias dicen que sí, dando el número completo de cuenta Openbank. **No confirmado en fuente oficial.** Verificar en la oficina concreta |

**Fíjate en el salto: 5.000 cajeros para sacar, pero solo ~1.800 para ingresar.** Hay que comprobar
físicamente si el cajero de L'Alcúdia (o el más cercano) admite ingresos.

### Lo que NO puedes hacer

- **Gestionar tu cuenta de Openbank en una oficina del Santander.** Son **entidades distintas** con
  licencias bancarias distintas. Una oficina del Santander puede aceptarte un ingreso hacia un IBAN, pero
  **no es tu oficina**: no resuelve incidencias, no te atiende un gestor, no tramita nada de Openbank.
- **Ir a una oficina de Openbank.** Tiene **dos en toda España, las dos en Madrid**, y en la principal
  (Openbank Corner) **no se puede operar con efectivo**; solo gestiones comerciales con cita previa.

Es decir: **Openbank es un banco 100 % digital con acceso prestado a los cajeros del Santander.** Eso no es
lo mismo que tener banco en el pueblo.

### Los tres riesgos específicos para un autónomo

**1. Hacienda.** Openbank tiene autorización histórica como entidad colaboradora
([BOE de 1997, autorización 413](https://www.boe.es/diario_boe/txt.php?id=BOE-A-1997-10257)), pero una
guía reciente describe su cobertura para pagos a la AEAT como **"limitada"**, con problemas para obtener
el **NRC** en algunos casos. El usuario domicilia modelos trimestrales (130 y 303) y la cuota de
autónomos. **Esto hay que confirmarlo con la asesoría y con el listado oficial de la AEAT antes de mover
nada.** Es el riesgo más serio de todos, porque un impago de un modelo por un problema técnico tiene
recargo.

**2. Las Letras del Tesoro.** La cuenta directa del Banco de España tiene **un IBAN registrado** al que
envía las amortizaciones y del que espera los depósitos previos. Hoy es el de CaixaBank. **Cerrar CaixaBank
obliga a cambiar ese IBAN en la cuenta directa**, y hay una Letra de 8.000 € venciendo el 04-06-2027. Si el
cambio no está hecho y confirmado antes, la amortización puede quedar en el limbo. Es un trámite
resoluble, pero **no puede quedar pendiente**.

**3. Un solo banco = un solo punto de fallo.** Si la app falla, si bloquean la cuenta por una operación
sospechosa, o si hay una incidencia de identificación, un autónomo con un único banco digital **se queda
sin acceso a su dinero y sin ventanilla donde reclamar**. Con dos bancos, eso es un contratiempo; con uno,
es un problema grave. Para alguien que cobra de clientes y paga impuestos a fecha fija, esto pesa más que
cualquier punto de rentabilidad.

### El argumento de fondo

**Se estaría reorganizando toda la vida bancaria por un tipo promocional de 12 meses.** El beneficio
cuantificado (§11.2 decies) es de **255 € al año en el mejor caso** frente a una cuenta sin condiciones, y
desaparece en el mes 13. Cerrar el banco principal es una decisión **permanente y costosa de revertir**
para capturar una ventaja **temporal y pequeña**. La asimetría es evidente.

### Lo que sí tiene sentido

| Banco | Papel | Qué guarda |
|---|---|---|
| **CaixaBank** | Banco operativo. **No se toca** | Cobros de clientes, Bizum, domiciliaciones (Hacienda, Seguridad Social, asesoría), tarjetas, IBAN de la cuenta directa del Tesoro. Saldo: operativa + impuestos del trimestre (≈ 4.000 €) |
| **Banco de España** | Letras | 19.000 € nominales en dos bloques |
| **Cuenta remunerada** (Openbank sin Bizum, B100 o Sabadell) | **Solo aparcar el colchón** | ≈ 15.000 €. Ni domiciliaciones, ni Bizum, ni cobros. Una transferencia al abrirla y otra al cerrarla |
| MyInvestor | Abierta sin uso | No cerrar (§11.2 quater) |

**Regla:** la cuenta remunerada es **un almacén, no un banco**. Entra dinero, sale dinero, nada más. Así se
captura el 2,75–3,25 % sin exponer nada de la operativa, y en el mes 11 se revisa y se mueve si hace falta,
sin que eso afecte a cobros, impuestos ni Letras.

### Si aun así quisiera cerrar CaixaBank en el futuro

Orden obligatorio, y **nunca con un vencimiento de Letra cerca**:

1. Confirmar con la asesoría que el nuevo banco admite domiciliación de AEAT y Seguridad Social sin
   incidencias de NRC.
2. Cambiar el IBAN en la cuenta directa del Banco de España y **esperar confirmación escrita**.
3. Trasladar domiciliaciones una a una y verificar durante **un trimestre completo** que todas pasan.
4. Comprobar que el cajero habitual admite **ingresos**, no solo reintegros.
5. Solo entonces, cerrar.

**Confianza:** alta en el diagnóstico (Openbank no tiene oficinas y es entidad distinta del Santander);
media en los detalles de cajeros (cifras de fuentes secundarias); **baja en la cobertura actual de AEAT,
que es justo el punto crítico y hay que verificar.**

## 11.2 duodecies DECISIÓN: qué cuenta remunerada elegir (07-11-2026)

Premisas fijadas por el usuario: **se queda con CaixaBank, mantiene Bizum allí**, y la cuenta nueva será
**solo un almacén** (§11.2 undecies). Eso elimina de golpe todas las ofertas que exigen vinculación —
Openbank con Bizum incluido— y deja un filtro limpio: **sin condiciones + FGD español**.

### Las opciones reales

| Opción | TIN | Neto/año (15.000 €) | FGD | Condiciones | Tipo garantizado hasta |
|---|---|---|---|---|---|
| **Bankinter Cuenta Digital** | **2,96 %** (3,00 % TAE) | **360 €** | **España** | **Ninguna** (solo ser cliente nuevo) | ≈ 30-04-2027 (~6 meses) |
| **Sabadell Cuenta Online** | 2,75 % | 334 € | **España** | **Ninguna** | No consta |
| B100 Cuenta Save | 2,75 % | 334 € | España | Ninguna | 31-12-2026 (~2 meses) |
| Trade Republic | 3,04 % | 369 € | **Alemania** | Ninguna | Variable |
| MyInvestor (ya abierta) | 1,25 % | 152 € | España | Ninguna | sep-2027 |
| CaixaBank (hoy) | 0 % | **0 €** | España | — | — |

Descartados: **Openbank** (exige Bizum para el 3,25 %), **Revolut** (FGD lituano, 4 meses),
**Raisin** (3 meses), **Trade Republic** (FGD alemán; el usuario prefiere garantía española y la ventaja
sobre Bankinter es de 9 €/año, que no paga el trámite transfronterizo en caso de problema).

### El dato que ordena la decisión

| Comparación | Diferencia |
|---|---|
| Bankinter vs. Sabadell | **+26 € al año** (2,1 €/mes) |
| Cualquiera de las dos vs. **no hacer nada** | **+334 a +360 € al año** |

**La elección de banco vale 26 €. Salir del 0 % vale 334 €.** Es trece veces más importante **hacerlo** que
**acertar con cuál**. Conviene no seguir optimizando: cualquiera de las dos primeras es una buena decisión y
la peor opción con diferencia es seguir esperando.

### Recomendación

**1ª opción: Bankinter Cuenta Digital.** 3,00 % TAE desde el primer euro y hasta 100.000 €, **sin nómina,
sin recibos, sin permanencia**, banco español con FGD español. Es exactamente el perfil de "almacén".

> **Pega: el plazo de alta acaba el 11-11-2026 — quedan 4 días** — y hay un cupo de 50.000 contrataciones
> desde el 29-10-2026, que puede estar agotado. Además **el tipo solo está garantizado hasta ≈ 30-04-2027**
> (las fuentes discrepan entre abril y mayo), es decir ~6 meses, no 12. Eso asegura ≈ 171 € netos en ese
> tramo; después hay que revisar.

**2ª opción: Sabadell Cuenta Online.** 2,75 %, sin condiciones, FGD español y **sin prisa**. Si el plazo de
Bankinter se pasa, si el cupo está agotado, o si el usuario prefiere no decidir con 4 días de margen, esta
es la opción tranquila. Cuesta 26 € al año frente a Bankinter: es un precio razonable por no correr.

**Lo que NO hay que hacer:** dejar los ≈ 19.090 € en CaixaBank al 0 % mientras se busca la opción perfecta.
Con el IPC al 4,9 % (§11.2 sexies) eso cuesta ≈ 891 € de poder adquisitivo al año.

### Condición común a todas: la revisión

Ninguna de estas cuentas mantiene el tipo para siempre; **todas son promociones de captación**. La
condición para que esto funcione es **revisar antes de que caduque el tipo garantizado** y mover el dinero
si hace falta. Mover cuesta 0 € (una transferencia) y 10 minutos.

Se añade al calendario el evento **"Revisar la cuenta remunerada"** con fecha **01-04-2027**, un mes antes
del límite de Bankinter, válido también si se elige Sabadell.

### Qué verificar antes de contratar

Las cifras provienen de comparadores, no de los bancos, y **se contradicen entre sí** (la fecha límite de
Bankinter aparece como 28-10, 11-11; la garantía del tipo como abril o mayo de 2027). Abrir la web del
banco elegido y confirmar:

1. TAE vigente y **hasta cuándo está garantizada**.
2. Saldo máximo remunerado.
3. Que **no** exige nómina, recibos, tarjeta ni permanencia.
4. Comisiones de mantenimiento y de cierre (deben ser 0 €).
5. Que admite ser cliente nuevo (Bankinter exige no haberlo sido en 6 meses).

**Confianza:** alta en la comparación relativa y en el orden de magnitud; **media en los tipos y fechas
exactos**, que dependen de verificación en fuente oficial.

## 11.2 terdecies Guía de alta en Bankinter Cuenta Digital (07-11-2026)

Decisión del usuario: **abrir la Cuenta Digital de Bankinter**. Plazo: **11-11-2026**.

### Antes de empezar: tener a mano

| Qué | Comprobación |
|---|---|
| **DNI en vigor** | Mirar la fecha de caducidad. Si está caducado, el alta se cae |
| **Móvil español (+34)** | Para los códigos SMS |
| **Correo electrónico** | El que se use habitualmente |
| **Dispositivo con cámara** | Móvil u ordenador: hay videoidentificación |
| **IBAN de CaixaBank** | Para la transferencia posterior |
| **Datos personales** | Dirección, estado civil (**soltero**), nacionalidad, profesión (**trabajador autónomo**) |

Requisito de la promoción: **no haber sido cliente de Bankinter en los últimos 6 meses.**

### Los cinco pasos

1. Entrar en **bankinter.com**, buscar **"Cuenta Digital"** y pulsar *Abrir cuenta online*. También se puede
   desde la app, en *"Quiero hacerme cliente"*.
2. **Rellenar los datos personales.** Deben coincidir **exactamente** con el DNI.
3. **Verificar la identidad:** foto del DNI por las dos caras y un vídeo breve.
4. **Firmar el contrato** electrónicamente.
5. La cuenta suele quedar operativa en minutos.

Duración estimada: ~10 minutos.

### ⚠ Los cuatro errores que hay que evitar

Mismo tipo de trampa que el desplegable de "6 meses" en la renovación de Letras del 13-10-2026: el producto
por defecto no siempre es el que se quiere.

1. **Confirmar que es "Cuenta Digital" y no "Cuenta Nómina" ni "Cuenta Pensión".** Bankinter tiene varias
   cuentas. Las otras **exigen domiciliar una nómina**, que el usuario no tiene por ser autónomo. Si el
   formulario pide una nómina o un justificante de ingresos, **se ha entrado en el producto equivocado**.
2. **No contratar nada más.** Durante el alta ofrecerán tarjeta de crédito, seguros, planes de pensiones o
   fondos. **A todo que no.** La cuenta es un almacén (§11.2 undecies).
3. **No domiciliar nada:** ni recibos, ni la cuota de autónomos, ni impuestos. Todo eso sigue en CaixaBank.
4. **Verificar que el 3,00 % TAE aparece en el contrato antes de firmar**, junto con el saldo máximo y la
   fecha hasta la que está garantizado. Si en pantalla aparece otra cifra, **manda la pantalla, no esta
   guía**: parar y consultar.

### Después del alta: mover el dinero

1. **No transferir los 15.000 € de golpe el primer día.** Hacer primero una transferencia de prueba de
   **10 €** desde CaixaBank y confirmar que llega. Cuesta 0 € y elimina el riesgo de un IBAN mal copiado.
2. Confirmada la prueba, transferir el resto. **Comprobar el límite diario de transferencias de CaixaBank**:
   si no admite 15.000 € en una sola operación, repartir en dos días.
3. **Antes de transferir, verificar que ya está cargado el pago de los modelos trimestrales.**
4. Dejar en CaixaBank ≈ 4.000 € para operativa e impuestos.

### Qué se verá luego, para no asustarse

| | |
|---|---|
| Interés sobre 15.000 € | **444 € brutos al año** |
| Abono mensual | ≈ **37 € brutos → ≈ 30 € netos** |

**Diferencia importante frente a las Letras:** los intereses de una cuenta bancaria **sí llevan retención
del 19 % en origen**. Las Letras no. Por eso el abono mensual se verá ya descontado (≈ 30 €, no 37 €). No
es un error del banco; el importe retenido se recupera o se ajusta en la declaración de la renta.

### Después de abrirla

- Anotar la **fecha exacta de apertura** y actualizar el evento del 01-04-2027 del calendario.
- Comentar a la asesoría que hay una cuenta nueva con rendimientos (aparecerá en los datos fiscales).
- **No cerrar CaixaBank ni MyInvestor.**

## 11.2 quaterdecies Documento de comisiones de Bankinter: verificado (07-11-2026)

El usuario aporta el **Documento Informativo de Comisiones** que hay que aceptar en el alta (contrato
01288700101355722, versión 15-09-2026, firmado en Madrid a 07-11-2026). Revisado punto por punto.

### Lo esencial: es el producto correcto y es gratuito

| Concepto | Lo que dice el documento |
|---|---|
| **Nombre de la cuenta** | **"CUENTA DIGITAL"** ✔ el producto correcto, no la Cuenta Nómina |
| **Mantenimiento** | **0,00 € mensual — comisión anual total 0,00 €** ✔ |
| **Tarjeta de débito** | **Emisión 0,00 € + mantenimiento anual 0,00 € = 0,00 €** ✔ |
| Nota 1 al pie | *"La Cuenta Digital incluye una tarjeta de débito sin comisiones de emisión ni de mantenimiento para el primer titular"* ✔ sin condiciones |
| **Transferencias SEPA por web** | **0,00 %, 0,00 €** — tanto estándar como **inmediata** ✔ |
| Órdenes permanentes por web | 0,00 € |

**Conclusión: el documento es correcto y puede aceptarse.** No hay comisión de mantenimiento, la tarjeta de
débito es gratuita sin condiciones y las transferencias por web (entrada y salida del dinero) son gratis,
que es justo lo que necesita una cuenta-almacén.

### Lo que cuesta dinero (y no afecta a este uso)

| Servicio | Coste | ¿Le afecta? |
|---|---|---|
| Tarjeta de **crédito** (Clásica / Dúo / Oro / Platinum) | **50 / 60 / 90 / 120 € al año** | **No: no contratar ninguna** |
| Transferencias por **banca telefónica** | 0,05 %, mín. 2 € | No: operar siempre por web/app |
| Transferencias por **oficina** | 0,25 %, mín. 4 € | No |
| Transferencias **NO SEPA** | 0,60 %, mín. 20 € | No |
| Devolución de cheques | 2 %, mín. 3,01 € | No |
| **Alertas por SMS** | **0,10 € por mensaje** | **Sí: configurar avisos por correo (0,00 €), no por SMS** |

### Retirada de efectivo con la tarjeta de débito

| Dónde | Coste |
|---|---|
| Cajeros de Bankinter | **Exento** |
| Red **EURO6000**, Grupo Cajas Rurales, Deutsche Bank | **Exento** |
| Cajeros de otras entidades (incluido CaixaBank) | **100 % de lo que fije ese cajero** |
| Internacional | 4 %, mín. 3 € |

Irrelevante para el uso previsto (la cuenta no es operativa), pero conviene saber que **el cajero de
CaixaBank no entra en la red exenta**.

### ⚠ Descubiertos: el único punto con coste real

| Concepto | Importe |
|---|---|
| Descubierto expreso | Servicio no disponible |
| Descubierto tácito (números rojos) | **7,88 % de interés** |
| Comisión por mayor saldo descubierto | **4,50 %, mínimo 15 €** |
| Reclamación de posiciones deudoras | 0 € (hasta 15 €) / 15 € / 40 € / **45 €** según el importe |

**Riesgo real: prácticamente nulo**, porque la cuenta no tendrá domiciliaciones ni recibos (§11.2
undecies) y el saldo será de cinco cifras. Pero queda escrita la regla: **nunca dejar el saldo en
negativo**, ni siquiera por unos céntimos, porque el mínimo de 15 € convierte un descubierto trivial en una
comisión desproporcionada.

### ⚠ Lo que este documento NO acredita

**No menciona el 3,00 % TAE en ninguna parte.** Es el documento de **comisiones**, no el de remuneración.
Aceptarlo es correcto, pero **sigue pendiente verificar el tipo de interés** en el contrato de la cuenta o
en la información precontractual, junto con el saldo máximo remunerado y la fecha hasta la que el tipo
está garantizado (§11.2 duodecies).

### Acciones derivadas

1. **Aceptar** el documento de comisiones.
2. **No contratar ninguna tarjeta de crédito** (50–120 €/año).
3. Al configurar la cuenta, **poner las alertas por correo electrónico, no por SMS** (0,10 €/mensaje).
4. **Operar siempre por web o app**, nunca por teléfono ni oficina.
5. **Nunca dejar el saldo en negativo.**
6. **Pendiente:** ver y guardar el documento donde conste el 3,00 % TAE.

## 11.2 quindecies Información contractual de Bankinter: revisada (07-11-2026)

El usuario aporta capturas de la **información contractual** (Prod. 2515, ref. SUC1104-01104), páginas 19 a
26. Corresponden al **contrato de la Tarjeta y al marco de servicios de pago**, no a la remuneración.

### Lo que confirma, y es bueno

| Cláusula | Lo que dice | Valoración |
|---|---|---|
| **Cancelación por el titular** | *"El Titular puede finalizar el Contrato en cualquier momento, **sin pagar ninguna penalización ni avisar con antelación**"*. Plazo máximo de 24 h desde la petición | ✔ **Sin permanencia.** Era uno de los puntos a verificar (§11.2 duodecies) |
| **Derecho de desistimiento** | **"Sí"** | ✔ 14 días naturales para echarse atrás (Ley 22/2007, venta a distancia) |
| **Ley y jurisdicción** | Legislación española; los tribunales competentes son **los del domicilio del Titular** | ✔ Favorable: litigaría en Valencia, no en Madrid |
| **Reclamaciones** | Servicio de Atención al Cliente (respuesta en 15 días hábiles) → **Servicio de Reclamaciones del Banco de España** | ✔ Vía estándar y gratuita |
| **Operaciones no autorizadas** | La Entidad devuelve el importe como máximo al final del día hábil siguiente; el titular no responde de lo ocurrido tras notificar pérdida o robo | ✔ Protección legal estándar |
| **Cancelación por la Entidad** | Necesita preavisar **2 meses**, y antes de cancelar por incumplimiento da **1 mes** para subsanarlo | ✔ Razonable |

### Tres detalles prácticos

**1. La tarjeta se cancela sola si no se usa.** Cláusula D: la Entidad puede cancelarla *"si no se ha
utilizado durante 12 meses seguidos, a fin de evitar más gastos al Titular"*. Dado que el plan es **no
usarla** (§11.2 terdecies), lo previsible es que la cancelen al año. **No pasa nada: eso cancela la
tarjeta, no la cuenta ni la remuneración.** Conviene saberlo para no asustarse con el aviso.

**2. Refuerza la regla del saldo en negativo.** Entre las causas de cancelación sin preaviso figura *"no
tener saldo suficiente en la Cuenta Asociada para cubrir los gastos de la Tarjeta"*. Suma a lo ya visto en
el documento de comisiones (descubierto al 7,88 % + 4,50 % con mínimo de 15 €): **nunca dejar el saldo en
negativo.**

**3. Plazo de 13 meses para reclamar.** Una operación no autorizada o mal ejecutada debe notificarse
**como máximo en 13 meses**; pasado ese plazo la Entidad puede rechazar la reclamación. Implicación
práctica: **revisar los movimientos al menos una vez al año**, cosa que ya cubre el aviso del 01-04-2027.

### ⚠ Lo que sigue sin aparecer

**Estas páginas tampoco contienen el 3,00 % TAE.** Son el contrato de la tarjeta y el marco de pagos. El
tipo de interés debe estar en el documento de **"Depósitos a la vista y de ahorro"**, que es el que falta
por revisar. Siguen pendientes de verificar:

1. TAE 3,00 % / TIN ≈ 2,96 %.
2. Saldo máximo remunerado (se espera 100.000 €).
3. Fecha hasta la que el tipo está garantizado.
4. Que no haya condiciones (nómina, recibos, uso de tarjeta, saldo mínimo).

### Aviso sobre datos personales

Las capturas aportadas incluyen **nombre completo y NIF** en cada página. No se han copiado a este
repositorio. Conviene no difundirlas más allá de lo necesario.

## 11.2 sexdecies Resto de la documentación de Bankinter: revisada (07-11-2026)

El usuario aporta dos documentos completos: la **Información Precontractual sobre Tarjeta Débito**
(Prod. 2515, ref. SUC1104-01104, ref. tarjeta 8700-60-2035969) y la **ficha precontractual de la cuenta
con el Impreso de Información a los Depositantes** (ref. SUC0716-00716). Ambos fechados en Madrid a
07-11-2026.

### Lo que queda confirmado y es bueno

| Punto | Lo que dice |
|---|---|
| **Fondo de Garantía de Depósitos** | *"El producto se encuentra cubierto por el Fondo de Garantía de Depósitos de Entidades de Crédito creado por el Real Decreto Ley 16/2011... La cantidad máxima garantizada es de **100.000 € por la totalidad de depósitos constituidos en Bankinter por persona**"* ✔ **FGD español, confirmado en documento firmado** |
| **Derecho de desistimiento** | **14 días naturales** desde la firma, **sin indicar motivos y sin costes**. Se notifica en oficina, por teléfono (91 657 88 00), por carta o por cualquier medio admitido en derecho ✔ |
| **Entidad y supervisión** | Bankinter S.A., entidad de crédito inscrita en el Banco de España con el **nº 128**, NIF A-28157360, supervisada por el Banco de España ✔ |
| **Tarjeta de débito** | Emisión **0,00 €** y mantenimiento **0,00 €** (principal y adicionales) ✔ |
| **Cajeros en España** | **0,00 %, mínimo 0,00 €** ✔ |
| **Reembolso del FGD** | 7 días hábiles |
| **Traslado de cuentas** | Derecho legal de traslado (RDL 19/2017 y Orden ECE/228/2019) ✔ útil si algún día se cambia de banco |
| **Operaciones no autorizadas** | Responsabilidad máxima del titular: **50 €**, con varias exenciones. Plazo para comunicar: 13 meses |

### Siete avisos prácticos nuevos

**1. COINC y Bankinter Roboadvisor son la misma entidad a efectos del FGD.** El impreso lo dice
expresamente. Los 100.000 € se cuentan sumando todo lo que se tenga bajo esas tres marcas. Irrelevante hoy
(15.000 €), pero conviene recordarlo si algún día se amplía.

**2. La cuenta debe usarse solo para operativa doméstica.** Literal: *"se considerará cuenta de consumidor
aquella cuyo titular sea persona física, y la operativa que se lleve a cabo con la misma sea
**exclusivamente de carácter doméstico**"*, y *"determinadas condiciones de la cuenta dependen de... que a
través de la misma se lleve a cabo operativa de carácter personal o doméstico, o de carácter profesional o
empresarial"*. **Confirma que declarar "particular" fue correcto y que meter actividad profesional por esa
cuenta podría cambiar las condiciones.** Refuerza la decisión de §11.2 undecies: la cuenta es un almacén.

**3. Servicio VoP (verificación del beneficiario) — importante para la transferencia.** Literal: *"si el
sistema ha avisado previamente al Cliente de que los datos del beneficiario no coinciden con los asociados
a la cuenta de destino, y aun así el Cliente autoriza expresamente la transferencia, dicha operación se
considerará válidamente autorizada. En ese caso, BANKINTER no asumirá ninguna responsabilidad"*.
**Regla: si al transferir aparece un aviso de que el nombre del beneficiario no coincide, PARAR y
revisar.** Si se continúa, el banco no responde de nada.

**4. La tarjeta llega con los límites a cero.** La ficha fija **límite de compras 0,00 € diario y mensual**
y **límite de cajeros 0,00 € diario y mensual**. La tarjeta no funcionará hasta que se fijen límites desde
la app. Dado que el plan es no usarla, **conviene dejarlos en cero**: es una capa de seguridad gratuita.

**5. Duplicado de tarjeta: 25 €. Reposición urgente: 20 €.** No afecta si la tarjeta se queda guardada.

**6. Ambigüedad menor sobre la gratuidad de la tarjeta.** El importe figura como 0,00 €, pero el texto
añade: *"Esta comisión no se cobrará si el Titular cumple con las condiciones de bonificación establecidas
en el contrato de la Cuenta Asociada"*. La nota 1 del documento de comisiones (§11.2 quaterdecies) sí es
tajante: *"La Cuenta Digital incluye una tarjeta de débito sin comisiones de emisión ni de mantenimiento
para el primer titular"*. **Se interpreta que es gratuita sin condiciones**, pero si algún día apareciera
un cargo, esa nota 1 es el argumento para reclamarlo.

**7. Las comunicaciones van por "Correo Web", no por email.** Es el medio principal del contrato: hay que
darse de alta en Banca Online y entrar a consultarlas. **El correo electrónico es solo un aviso
complementario.** Implicación: si Bankinter notifica un cambio de tipo o de condiciones, estará ahí.
Revisarlo en la revisión del 01-04-2027.

### ⚠ Sigue sin aparecer el 3,00 % TAE

Ninguno de los documentos aportados hasta ahora lo contiene. Se han revisado: documento de comisiones,
información contractual del marco de pagos, precontractual de la tarjeta e impreso de depositantes.
**Falta la ficha de "Depósitos a la vista y de ahorro"** con la remuneración. Pendiente de verificar:

1. TAE 3,00 % / TIN ≈ 2,96 %.
2. Saldo máximo remunerado.
3. Fecha hasta la que el tipo está garantizado.
4. Ausencia de condiciones.

**Mitigación:** existe el **derecho de desistimiento de 14 días naturales**. Aunque se firme sin haber
visto el tipo, hay dos semanas para deshacer la operación sin coste ni explicaciones. Eso reduce el riesgo
de firmar, pero **no sustituye a comprobarlo**.

### Aviso sobre datos personales

Las capturas incluyen nombre, NIF y la referencia de la tarjeta de débito en cada página. No se han copiado
a este repositorio. **Conviene no reenviarlas a nadie más.**

## 11.2 septendecies ✅ VERIFICADO: la ficha de remuneración confirma el 3,00 % (07-11-2026)

El usuario aporta la **Ficha de Información Precontractual de Depósitos a la Vista y Ahorro**
(ref. SUC0716-00716). Es el documento que faltaba. **Todo lo que había que comprobar queda confirmado.**

### La remuneración, en los términos exactos del banco

| Concepto | Lo que dice la ficha |
|---|---|
| **T.A.E.** | **3,00 %** ✔ |
| **Tipo de interés nominal (TIN)** | **2,96 %** ✔ |
| **Saldo máximo** | **100.000,00 euros** ✔ |
| **Periodo de liquidación** | **Mensual** ✔ |
| **Condiciones de remuneración garantizadas hasta** | **11/05/2027 (inclusive)** |
| **Condición para que aplique** | *"siempre que la contratación de la Cuenta se lleve a cabo desde **29/10/2026 hasta el 11/11/2026** (ambas inclusive)"* |
| A partir del 12/05/2027 | *"el tipo de interés podrá cambiar... previa comunicación al cliente con una antelación mínima de 2 meses, sin que exista garantía de mantenimiento del tipo indicado más allá de dicha fecha"* |
| **Indicador de riesgo** | **1/6** (el más bajo) ✔ |
| **Comisión de mantenimiento** | **0,00 €** anual ✔ |
| **Comisión de gestión de apuntes** | **0,00 €** ✔ |
| **Cancelación** | *"en cualquier momento y sin necesidad de causa alguna ni preaviso"*; *"la resolución del contrato marco será **gratuita** para el cliente"* ✔ |
| **Traslado de cuentas** | Adherido a los Principios comunes: **Sí** ✔ |

**No figura ninguna condición de vinculación.** Ni nómina, ni recibos, ni compras con tarjeta, ni saldo
mínimo. La única condición es **haber contratado dentro de la ventana del 29-10 al 11-11-2026**.

### Verificación aritmética

La ficha da la fórmula: **Capital × Rédito × Tiempo / 36500**, con liquidación mensual.

    TIN 2,96 % capitalizado mensualmente → (1 + 0,0296/12)^12 − 1 = 3,0005 %  ✔ coincide con el TAE declarado

La nota al pie aclara que el TAE *"está calculado para un supuesto saldo diario mantenido durante un año de
6.000,00 euros"*. **Eso no limita nada**: al no haber comisiones fijas, el 3,00 % es idéntico para 6.000 €
que para 15.000 €. Es solo el ejemplo normalizado que exige el Banco de España.

### Lo que cobrará, con fechas reales

| | |
|---|---|
| Abono mensual sobre 15.000 € | **≈ 37,00 € brutos → ≈ 29,97 € netos** |
| **Tramo garantizado (07-11-2026 → 11-05-2027, 185 días)** | **≈ 225,04 € brutos → ≈ 182,28 € netos** |
| Equivalente anual si se mantuviera el tipo | 444 € brutos / 360 € netos |

**Corrección a la estimación anterior (§11.2 duodecies):** se dijo que el tipo estaría garantizado "hasta
≈ 30-04-2027" a partir de fuentes de prensa que discrepaban. **La fecha real del contrato es el
11/05/2027.** Once días más de los estimados.

### Datos de la cuenta

- **IBAN: ES51 0128 8700 1001 0135 5722** (cuenta 0128-8700-10-0101355722)
- Titular único: el usuario
- Divisa: euros
- Fecha del documento: 07-11-2026

### Comisiones nuevas que aparecen aquí

| Concepto | Importe | ¿Aplica? |
|---|---|---|
| **Descubierto tácito** | **8,12 % TAE** + comisión del **4,50 % sobre el mayor saldo deudor, mínimo 15,00 €** | Solo si el saldo se va a negativo |
| Gastos de reclamación de descubierto | 0 € / 15 € / 40 € / **45 €** según importe | Idem |
| **Atención manual de adeudos** | **3,00 € por cargo** cuando no se puede hacer automáticamente por falta de saldo | No habrá domiciliaciones |
| Comisión de recuento de monedas | 10 € por cada 500 monedas, solo actividad empresarial o profesional | No: cuenta de uso doméstico |

Confirma por tercera vez la misma regla: **nunca dejar el saldo en negativo.**

### Cláusula de modificación: lo que hay que vigilar

*"Dichas modificaciones podrán afectar tanto a las condiciones aplicadas a los servicios de pago **como a
la remuneración asociada a la cuenta corriente**"*, con preaviso mínimo de **2 meses** y comunicación por
**CORREO WEB**. Si el cliente no manifiesta su disconformidad antes de la entrada en vigor, **se entiende
que acepta**; si no está conforme, puede resolver el contrato sin gastos.

**Implicación operativa:** el aviso del cambio de tipo llegará al **Correo Web de la banca online**, no al
email. Hay que entrar a leerlo. Es exactamente para esto el recordatorio del calendario.

### Veredicto

**Todas las comprobaciones exigidas en §11.2 duodecies y §11.2 terdecies quedan superadas.** La
documentación es coherente consigo misma y con lo anunciado. **Puede firmar.**

Red de seguridad adicional: **derecho de desistimiento de 14 días naturales** desde la entrada en vigor,
sin motivos y sin coste, notificable por escrito (correo postal a Paseo de la Castellana 29, 28046 Madrid,
o cualquier otro medio admitido en derecho), con devolución en 30 días naturales.

## 11.2 duodevicies CUENTA ABIERTA (07-11-2026) y tareas pendientes

**Cuenta Digital de Bankinter contratada el 07-11-2026**, dentro de la ventana exigida (29-10 a
11-11-2026). Condiciones adquiridas: **3,00 % TAE / 2,96 % TIN, saldo máximo 100.000 €, liquidación
mensual, garantizado hasta el 11-05-2027, sin condiciones de vinculación** (§11.2 septendecies).

**IBAN: ES51 0128 8700 1001 0135 5722.** Titular único.

### Mapa del capital previsto una vez hecha la transferencia

| Dónde | Importe | Rendimiento |
|---|---|---|
| Letra A (Banco de España, vence ≈ nov-2027) | 11.000 € nominales | 3,079 % del periodo |
| Letra B (Banco de España, vence 04-06-2027) | 8.000 € nominales | — |
| **Bankinter Cuenta Digital** | **≈ 15.000 €** | **3,00 % TAE** |
| CaixaBank (operativa, impuestos, Bizum, domiciliaciones) | ≈ 4.000 € | 0 % |
| MyInvestor | 0 € | Abierta sin uso |

Con esto, **todo el capital del usuario pasa a estar remunerado salvo el colchón operativo**, por primera
vez desde que arrancó el proyecto.

### Pendientes, en orden

| # | Tarea | Cuándo |
|---|---|---|
| 1 | **Darse de alta en Banca Online** y localizar el **Correo Web** (es el canal oficial de avisos; el email es solo complementario) | Ya |
| 2 | Desde el **ordenador**, descargar el contrato y revisar la **Cláusula Primera** | Próximos días |
| 3 | Configurar **avisos por correo electrónico, no por SMS** (0,10 €/mensaje) | Al entrar |
| 4 | **Dejar los límites de la tarjeta en 0,00 €** (vienen así de fábrica): seguridad gratuita si no se va a usar | Al entrar |
| 5 | Comprobar que **ya está cargado el pago de los modelos trimestrales** en CaixaBank | Antes de transferir |
| 6 | **Transferencia de prueba de 10 €** y confirmar que llega | Antes del grueso |
| 7 | Transferir el resto hasta ≈ 15.000 €, comprobando el **límite diario** de CaixaBank | Tras la prueba |
| 8 | Avisar a la asesoría de que hay una cuenta nueva con rendimientos | Antes del cierre del ejercicio |

**Regla del punto 6-7:** mientras el dinero siga en CaixaBank, deshacer la operación es trivial. La
transferencia no tiene fecha límite; el alta sí la tenía. Por eso se separan.

### Fechas en el calendario

| Fecha | Evento |
|---|---|
| **18-11-2026** | Aviso: último margen para desistir (**límite 21-11-2026**, 14 días naturales, sin motivos ni coste) |
| **01-04-2027** | Revisar el tipo antes de que caduque la garantía del **11-05-2027** |
| 17-05-2027 | Pedir renovación de la Letra B |
| 04-06-2027 | Amortiza la Letra B |

### Lo que sigue sin hacerse, y vale más que todo esto

Recordatorio deliberado: la cuenta remunerada aporta ≈ 360 € al año. **Siguen pendientes los dos asuntos
de mayor impacto del proyecto**, ambos relacionados con dos hijos menores a cargo:

1. **El seguro de vida.** El usuario **no tiene cobertura propia** (la póliza MyBox Vida asegura a su
   pareja). Necesidad estimada: 75.000–100.000 €.
2. **El testamento.** Sin él, **la pareja no hereda nada** por no estar casados. Coste aproximado en
   notaría: 50–80 €.

## 11.2 undevicies ✅ CONTRATO DE APERTURA VERIFICADO (07-11-2026)

Revisado el **CONTRATO CUENTA DIGITAL** (ref. SUC0435-00435), 18 páginas, firmado en Madrid el 07-11-2026
por el usuario y por Bankinter S.A. **Cierra la verificación: no queda nada pendiente.**

### Condiciones Particulares: coinciden al 100 % con la ficha precontractual

| Concepto | Contrato |
|---|---|
| Producto | **CONTRATO CUENTA DIGITAL** ✔ |
| IBAN | ES51-0128-8700-1001-0135-5722 · SWIFT BKBKESMMXXX ✔ |
| Titular | Único (F.I. 1 = Titular, F.A. 1 = Personal) ✔ |
| **Tipo de interés nominal** | **2,96 %** ✔ |
| **T.A.E.** | **3,00 %** ✔ |
| **Saldo máximo** | **100.000,00 euros** ✔ |
| **Garantizado hasta** | **11/05/2027 inclusive**, contratando entre el 29/10 y el 11/11/2026 ✔ |
| Liquidación | Mensual ✔ |
| Mantenimiento / gestión de apuntes | 0,00 € / 0,00 € ✔ |

**No aparece ninguna condición de vinculación.** Confirmado contra el documento firmado.

### La Cláusula Primera (Condición General 1, "Objeto y duración")

Es la que la ficha señalaba como reguladora del tipo a partir del 12/05/2027. Dice:

- **Modificaciones con preaviso mínimo de 2 meses** para clientes consumidores (15 días para no
  consumidores). *"Dichas modificaciones podrán afectar tanto a las condiciones aplicadas a los servicios
  de pago **como a la remuneración asociada a la cuenta corriente**"*.
- **⚠ El silencio equivale a aceptación:** *"Se entiende que el Cliente acepta la modificación si éste no
  notifica al Banco, antes de la fecha de entrada en vigor de la modificación propuesta, su
  disconformidad con la misma"*.
- Si no está conforme, **puede resolver el contrato sin gastos** antes de esa fecha, con devolución
  proporcional de comisiones anticipadas.
- La comunicación se remite por **CORREO WEB** (Condición General 1, "Comunicaciones legales").
- Las modificaciones **claramente más beneficiosas** pueden aplicarse sin preaviso.
- **Desistimiento: 14 días naturales**, notificable por **(i) cualquier oficina, (ii) Banca Telefónica
  91 657 88 00, (iii) carta a Paseo de la Castellana 29, 28046 Madrid, o (iv) cualquier otro medio
  admitido en derecho.** *(Corrección: se puede ejercer por teléfono, no hace falta carta.)*

### Dos cláusulas con consecuencias prácticas

**1. La condición de consumidor depende del uso que se dé a la cuenta.** Literal:

> *"Si durante la vigencia del presente contrato Bankinter detectase que el uso que el titular hace de la
> cuenta ha variado y que se utiliza para llevar a cabo operativa relacionada con su actividad empresarial
> o profesional, pasará a tener la consideración de **no consumidor**. En ese caso no le será de
> aplicación la normativa referida en el párrafo anterior, **pudiendo asimismo variar las condiciones
> económicas de la cuenta**."*

Perder la condición de consumidor supondría: preaviso de modificaciones reducido de 2 meses a 15 días,
pérdida de la protección de la Ley 16/2011, la Orden EHA/2899/2011, la Ley 22/2007 y el RDL 19/2018, y la
posibilidad de que **cambien las condiciones económicas**. **Es la confirmación contractual más fuerte de
la estrategia de §11.2 undecies: por esta cuenta no puede pasar nada de la actividad de autónomo.**

**2. Clasificación MiFID: cliente minorista** (máxima protección). El contrato advierte que, si el cliente
solicitara reclasificarse como profesional, *"las obligaciones de información de BANKINTER serán muy
reducidas"*. **Nunca solicitar ese cambio.**

### Resuelto: el documento de la "hipoteca"

La fila listada como *"Dossier alta omnicanal/solicitud hipoteca"* resulta ser el **"Dossier Alta de
Cliente"** (ref. SUC0843-00843): la identificación del cliente, los términos de contratación por internet
y el anexo de protección de datos. **No hay ninguna solicitud de hipoteca ni de financiación.** Era solo
el nombre interno de la plantilla.

### Estado de la verificación

| Documento | Estado |
|---|---|
| Documento informativo de comisiones | ✔ revisado (§11.2 quaterdecies) |
| Información contractual / marco de pagos | ✔ revisado (§11.2 quindecies) |
| Precontractual de tarjeta débito + impreso de depositantes | ✔ revisado (§11.2 sexdecies) |
| Ficha precontractual de depósitos (FIPRE) | ✔ revisado (§11.2 septendecies) |
| **Contrato Cuenta Digital** | **✔ revisado (este apartado)** |
| Dossier Alta de Cliente | ✔ revisado, sin incidencias |

**Los cinco documentos son coherentes entre sí y con lo anunciado. No procede desistir.** El plazo del
21-11-2026 queda como red de seguridad sin uso.

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
