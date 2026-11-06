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
