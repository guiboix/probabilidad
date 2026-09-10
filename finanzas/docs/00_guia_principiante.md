# 0. Guía para quien empieza desde cero

Este documento explica, sin dar nada por sabido, las palabras y las ideas que aparecen en el resto del
proyecto. Léelo antes que los demás. Cada término lleva un ejemplo con tus propios números siempre que
es posible.

## 0.1 Las cuatro ideas que lo sostienen todo

**1. Rentabilidad es lo que ganas; riesgo es cuánto puede variar lo que ganas.**
No existe un producto que dé mucha rentabilidad con poco riesgo. Cuando alguien lo ofrece, o hay un
riesgo que no se ve, o es una estafa. Lo único que puedes elegir es cuánto riesgo aceptas y a cambio de qué.

**2. La inflación es un riesgo aunque no se vea.**
Si los precios suben un 3,3 % al año y tu dinero gana un 2,2 % neto, has perdido un 1,1 % de capacidad
de compra. El saldo de la cuenta sube, pero compra menos. Por eso "no perder dinero" y "no perder poder
adquisitivo" son cosas distintas.

**3. El tiempo cambia qué es arriesgado.**
Un producto que puede caer un 15 % en un año malo es arriesgado si necesitas el dinero el año que viene,
y mucho menos si no lo necesitas en diez. Por eso lo primero es decidir *cuándo* vas a necesitar cada euro.

**4. Los costes se pagan siempre; la rentabilidad, a veces.**
Una comisión del 1 % anual se cobra tanto si el fondo sube como si baja. A veinte años se lleva alrededor
del 18 % de lo que habrías tenido. Por eso este proyecto prefiere productos con comisiones por debajo del 0,3 %.

## 0.2 Los productos que aparecen en este proyecto

| Término | Qué es, en llano | Tu caso |
|---|---|---|
| **Letra del Tesoro** | Le prestas dinero al Estado español durante 3, 6, 9 o 12 meses. Pagas menos de 1.000 € hoy y te devuelven 1.000 € al vencer. La diferencia es tu ganancia. | Tienes dos: 8.000 € que amortizan el 06-11-2026 y 8.000 € el 04-06-2027. |
| **Nominal** | Lo que te devuelven al vencimiento (siempre múltiplos de 1.000 €). | 8.000 € por Letra. |
| **Precio de compra** | Lo que pagaste por cada 1.000 € de nominal. Cuanto más bajo, más ganas. | Aprox. 980,28 y 974,93. |
| **Amortizar / vencer** | El día en que el Estado te devuelve el nominal. | 06-11-2026 y 04-06-2027. |
| **Subasta** | El Tesoro vende las Letras cada mes en una puja. Pides un importe y, si aceptas el precio medio, te las adjudican. | Para renovar, hay que pedir en la subasta de días antes del vencimiento. |
| **Custodio** | Quien guarda tus valores y te cobra por ello. Una Letra en el Banco de España cuesta 0,15 % al vencer; en un banco, ≈ 0,6 % al comprar más custodia anual. | Documento 11. |
| **Cuenta directa del Banco de España** | Cuenta gratuita en el Banco de España para comprar deuda pública sin intermediarios. Se abre con certificado digital o Cl@ve. | Es donde conviene renovar las Letras. |
| **Escalera** | Tener varias Letras que vencen en fechas distintas. Cada vencimiento es una ocasión para decidir. | Dos peldaños separados unos 7 meses. |
| **Bono del Estado** | Como la Letra, pero a 3 o 5 años y pagando un interés (cupón) cada año. Si lo vendes antes de vencer, su precio puede haber bajado. En la web del Tesoro, lo que vence en 12 meses o menos se llama Letra; lo de 2 a 5 años, Bono; lo de 10 años o más, Obligación. | Lo que tú tienes son Letras. Documento 10 §10.3. |
| **Cupón** | El interés anual que paga un bono, en euros por cada 1.000 € de nominal. | Un cupón del 2,8 % son 28 € al año por cada 1.000 €. |
| **TIR (rentabilidad a vencimiento)** | Lo que ganas al año si mantienes un bono hasta el final, contando cupones y precio de compra. | La calcula `python -m cartera bono`. |
| **Fondo de inversión** | Una cesta de muchos bonos o acciones gestionada por una entidad. Compras una parte de la cesta. | Vas a empezar con 300 €. |
| **Participación** | Cada trozo del fondo que posees. | Con 300 € y un valor de 10 € por participación, tendrías 30. |
| **Valor liquidativo (VL)** | El precio de una participación. Se calcula una vez al día. | Es el dato que anotarás cada semana. |
| **Fondo indexado** | Un fondo que copia un índice (una lista de bonos o acciones) en vez de que alguien elija. Es más barato y, de media, lo hace mejor que la mayoría de gestores. | Todos los candidatos del proyecto lo son, salvo alguno de renta fija a muy corto plazo. |
| **Fondo de gestión activa** | Un gestor elige qué comprar. Cuesta más y no suele batir al índice a largo plazo. | Solo se usa si no hay indexado en esa categoría. |
| **Renta fija** | Bonos: préstamos a Estados o empresas que pagan intereses. Riesgo bajo o medio. | Las Letras son renta fija a corto plazo; el primer fondo también será renta fija. |
| **Renta variable** | Acciones: trozos de empresas. Riesgo alto a corto plazo, mejor rentabilidad esperada a largo. | 0 % de momento, por decisión tuya. |
| **Fondo monetario** | Renta fija a plazos de días o semanas. Se mueve muy poco; rinde parecido a las Letras. | Alternativa a las Letras si no quieres renovar en subasta. |
| **ETF** | Fondo que cotiza en bolsa como una acción. En España no permite el traspaso sin impuestos. | Por eso el proyecto prefiere fondos tradicionales. |

## 0.3 Cómo se mide el riesgo (y cómo leerlo en la ficha de un fondo)

| Término | Qué significa | Cómo lo usarás |
|---|---|---|
| **Volatilidad** | Cuánto suele oscilar el precio en un año. Una volatilidad del 4 % quiere decir que en la mayoría de años el fondo se moverá entre −4 % y +4 % alrededor de su media; en años malos, más. | Una Letra tiene volatilidad ≈ 0. Un fondo de renta fija a corto plazo, 1–2 %. Uno de bolsa mundial, 15 %. |
| **Caída máxima (drawdown)** | La peor bajada desde un máximo hasta el siguiente mínimo. | Es el número que responde a "¿cuánto puedo llegar a ver en rojo?". |
| **Indicador de riesgo del KID (1 a 7)** | Escala oficial europea. 1 = casi no se mueve; 7 = puede perder mucho. | Para ti, de momento: 1 o 2. |
| **Duración** | Cuánto le afecta a un fondo de bonos que suban los tipos de interés. Duración 2 = cae ≈ 2 % si los tipos suben 1 punto. | "Corto plazo" = duración menor de 3. Es lo conservador. |
| **Calificación crediticia** | Nota que ponen las agencias a quien pide prestado. De AAA (máxima) a BBB− es "grado de inversión"; por debajo, "alto rendimiento" (más riesgo). | Para ti: grado de inversión. |
| **Riesgo de divisa** | Si el fondo tiene bonos en dólares, el cambio euro/dólar añade oscilación. | Buscar clase "EUR Hedged" (cubierta) o bonos en euros. |
| **Diversificación** | No poner todo en un mismo emisor, país o sector. Un fondo con 2.000 bonos apenas nota si uno quiebra. | Los indexados lo hacen por construcción. |

## 0.4 Costes y documentos

| Término | Qué es |
|---|---|
| **TER / gastos corrientes** | Lo que el fondo cobra cada año, en porcentaje. Se descuenta del valor liquidativo sin que lo veas. 0,15 % es barato; 1,5 % es caro. |
| **Comisión de custodia** | Lo que cobra el banco por guardar tus participaciones. En MyInvestor, 0 € en fondos indexados. |
| **KID (documento de datos fundamentales)** | Ficha oficial de 3 páginas de cada fondo: riesgo (1–7), costes, escenarios. Es lo primero que se lee. |
| **ISIN** | El "DNI" del fondo. Doce caracteres. Evita confundir clases parecidas. |
| **Clase de acumulación (Acc)** | El fondo reinvierte los intereses en vez de pagártelos. Evita pagar impuestos cada año. Es la que interesa. |
| **Artículo 8 / 9 (SFDR)** | Etiqueta europea de sostenibilidad. 8 = "promueve" criterios ambientales o sociales (muy amplio). 9 = tiene un objetivo sostenible (más estricto). No es un sello de calidad, es una obligación de informar. |
| **ESG / SRI / ISR / Screened** | Formas de filtrar empresas por ética. Explicadas en el documento 05. |

## 0.5 Impuestos, en dos frases

Los intereses de las Letras y las ganancias de los fondos tributan en la "base del ahorro": 19 % hasta
6.000 € de ganancia al año, 21 % hasta 50.000 €. Diferencia clave: la Letra tributa cada vez que vence; el
fondo solo cuando lo vendes, y puedes cambiar de un fondo a otro (**traspaso**) sin pagar nada. Detalle en el documento 06.

Con tus números: las dos Letras generan ≈ 350 € brutos al año, de los que Hacienda se queda ≈ 67 €.

## 0.6 Qué hace cada comando del proyecto (no hace falta programar)

Se ejecutan escribiendo una línea en la terminal, dentro de la carpeta `finanzas`. Todos imprimen una tabla.

| Comando | Para qué |
|---|---|
| `python -m cartera letras --precio 973.78 --dias 364 --nominal 8000 --inflacion 0.033` | Cuánto gana una Letra: bruto, neto de impuestos y real (descontando inflación). |
| `python -m cartera escalera --data data --inflacion 0.033 --peso-letras 1` | Calendario de tus dos Letras y aviso cuando toca decidir. |
| `python -m cartera seguimiento --data data` | Cómo va el fondo: rentabilidad, volatilidad y caída máxima con los VL que anotes. |
| `python -m cartera informe --data data` | Foto de toda la cartera y si algo se ha desviado del objetivo. |
| `python -m cartera simular --inicial 16300 --mensual 0 --anyos 5` | Qué rango de resultados puede dar cada tipo de cartera. |
| `python -m cartera comparar --tipo-letra 0.02663 --fondo 0.03 --anyos 5` | Letras renovadas frente a un fondo, sin incertidumbre. |

## 0.7 Orden de lectura recomendado

1. Este documento.
2. `08_escalera_letras.md`: tu situación actual con números.
3. `09_primer_fondo.md`: el fondo de 300 € y qué mirar.
4. `02_politica_inversion.md`: la cartera conservadora acordada y sus reglas.
5. `05_criterios_eticos.md`: para decidir qué significa "ético" para ti.
6. El resto, cuando haga falta.

## 0.8 Errores típicos de quien empieza (para reconocerlos)

- Mirar el fondo cada día. Con un producto de riesgo 2, el ruido diario no informa de nada.
- Vender tras una bajada y comprar tras una subida. Es la forma más habitual de perder dinero con buenos productos.
- Juzgar un producto por tres meses de resultado (documento 09 §9.7).
- Confundir "el banco me lo recomienda" con "me conviene": el banco cobra por lo que vende.
- Comprar algo que no se sabe explicar en dos frases.
