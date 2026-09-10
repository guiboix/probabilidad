# 1. Perfil del inversor y objetivos

> Estado: **PENDIENTE DE RELLENAR POR EL USUARIO**. Nada de lo que sigue puede decidirse sin estos datos.
> Todo el resto del proyecto (asignación, productos, simulaciones) depende de las respuestas.

## 1.1 Datos que faltan y por qué importan

| Dato | Por qué importa | Respuesta |
|---|---|---|
| Importe total invertible hoy (€) | Escala de todo; determina si merece la pena diversificar en varios fondos | **≈ 30.000 €**: 16.000 € en Letras + ≈ 14.000 € en la cuenta de CaixaBank que hacen de fondo de emergencia. Los "bonos" que menciona el usuario son las propias Letras (comprados en la web del Tesoro; las cifras cuadran: 16.000 + 14.000 = 30.000) |
| Importe actual en Letras del Tesoro y vencimientos | Es el dinero que se plantea mover; sus vencimientos marcan el calendario natural sin vender antes | **Aportado 10-09-2026:** dos Letras a 12 meses de 8.000 € cada una (16.000 €), amortizaciones el **06-11-2026** y el **04-06-2027**. Se mantienen renovándose de momento. Precios inferidos de las subastas del 04-11-2025 (1,99 %) y 02-06-2026 (2,54 %). Falta confirmar que 8.000 € es nominal |
| Capacidad de ahorro mensual (€) | Permite rebalancear con aportaciones (sin tributar) y usar aportaciones periódicas | Sin dato. Autónomo: ingresos variables |
| Fondo de emergencia ya cubierto (meses de gastos) | Es requisito previo a asumir volatilidad. Referencia habitual: 3–6 meses de gastos en liquidez o Letras | **Son los ≈ 14.000 € en la cuenta de CaixaBank** (aclarado 10-09-2026): cumplen la función de colchón y a la vez el usuario los considera invertibles "si ve que los productos son seguros". Salida mensual mínima ≈ 770–1.020 € (autónomo; 600 € personales + 500 €/trimestre de asesoría e impuestos; falta saber si la cuota de autónomos va aparte). Cubren 14–18 meses. Referencia prudente para un autónomo: 9–12 meses → sobran ≈ 2.500–6.000 € (documento 11 §11.2 ter) |
| Horizonte de la inversión (años) | Con menos de 5 años la renta variable tiene una probabilidad relevante de estar en pérdidas (véase `simular`) | |
| Necesidades de liquidez previstas (vivienda, coche, estudios…) y fecha | Ese dinero no debe ir a renta variable | |
| Tolerancia a caídas: ¿qué caída temporal del total (10 %, 20 %, 35 %) haría vender por miedo? | Define el porcentaje máximo de renta variable | Declarado: perfil muy conservador. Cifra concreta: sin dato; de momento RV 0 % |
| Otras rentas del ahorro del año (intereses, dividendos) | Cambian el tipo marginal que se aplica a nuevos rendimientos | |
| Situación fiscal: residencia fiscal, comunidad autónoma | La base del ahorro es estatal, pero conviene confirmar residencia en España | |
| Comisiones bancarias | Restan rentabilidad sin riesgo | CaixaBank: sin comisión de mantenimiento (declarado). Letras en Banco de España: 0,15 % al vencer |
| Definición personal de "ético" | Véase `05_criterios_eticos.md`; sin definirlo no se puede filtrar productos | |

## 1.2 Objetivo declarado

Del enunciado del usuario (10-09-2026):

- Gestionar la cartera para obtener rentabilidad **de forma ética y segura**.
- Dispone de cuenta en MyInvestor y está abierto a fondos de inversión.
- Tiene dinero en Letras del Tesoro y percibe que su rentabilidad es baja frente a otros productos.
- Es autónomo. El fondo de emergencia son los ≈ 14.000 € de la cuenta corriente; los considera invertibles en productos seguros cuando tenga confianza. Mantiene las Letras renovándose de momento.
- Quiere empezar con un fondo de bajo riesgo y buena ética para familiarizarse (documento 09), con 300 €.
- Lo que llama "bonos" son las Letras del Tesoro compradas en la web del Tesoro (aclarado 10-09-2026). No hay otros bonos.
- Su capital está en **CaixaBank**, pero las Letras las compra en la web del Tesoro (cuenta directa del Banco de España): canal sin comisiones de compra ni custodia (documento 11). Pendiente: dónde están los bonos.
- No tiene experiencia previa. Pide explicaciones de principiante (documento 00) y una cartera **muy
  conservadora** para la mayor parte del capital (documento 02 §2.2).

Detalle de la escalera de Letras y su plan de transición: `08_escalera_letras.md`.

## 1.3 Contradicción que hay que resolver explícitamente

"Segura" y "más rentable que las Letras" tiran en direcciones opuestas. Las Letras son, para un residente
en España, el activo con menos riesgo de crédito y de precio (si se mantienen a vencimiento). Cualquier
producto con mayor rentabilidad esperada la obtiene a cambio de **volatilidad** (fondos de renta
variable), **riesgo de crédito o de tipos** (renta fija corporativa o a largo plazo) o **iliquidez**.

La forma habitual de reconciliar ambas cosas no es buscar un producto "seguro y rentable" (no existe),
sino **repartir por horizonte temporal**:

1. Dinero que se puede necesitar en menos de ~3 años: Letras, cuenta remunerada, fondo monetario.
2. Dinero a más de ~7–10 años: mayoritariamente renta variable global diversificada, aceptando caídas temporales.
3. Tramo intermedio: mezcla, normalmente vía renta fija de duración corta/media.

Qué porcentaje va a cada tramo se decide con la tabla 1.1, no antes.

## 1.4 Hechos comprobados (septiembre 2026) que sustentan la percepción del usuario

| Dato | Valor | Fuente |
|---|---|---|
| Tipo medio Letras 12 meses, subasta 04-08-2026 | 2,663 % (precio 973,78) | tesoro.es (resultado citado vía búsqueda; verificar) |
| Tipo medio Letras 3 meses, subasta 12-05-2026 | 2,154 % | CaixaBank (artículo divulgativo) |
| Facilidad de depósito BCE (julio 2026) | 2,25 %; el mercado esperaba subida a 2,50 % el 10-09-2026 | Finect / Rankia (prensa financiera) |
| Inflación interanual eurozona, agosto 2026 | 3,3 % | Finect (prensa financiera) |

Cálculo con `python -m cartera letras --precio 973.78 --dias 364 --nominal 10000 --inflacion 0.033`:

| Concepto | Valor |
|---|---|
| TAE bruta | 2,70 % |
| TAE neta de IRPF (19 %) | 2,19 % |
| TAE **real** neta con inflación 3,3 % | **−1,08 %** |

Conclusión (hecho, no interpretación): con los datos de agosto–septiembre de 2026, una Letra a 12 meses
**pierde poder adquisitivo** después de impuestos e inflación. La percepción del usuario es correcta.
Lo que no se deduce de esto es que otro producto vaya a ganar: la alternativa a una pérdida real segura
del 1 % es una ganancia real *esperada* pero incierta.

## 1.5 Limitaciones

- No se ha podido acceder directamente a tesoro.es ni a MyInvestor desde este entorno; las cifras
  provienen de resúmenes de prensa y deben comprobarse en la fuente primaria antes de operar.
- La decisión del BCE del 10-09-2026 no estaba confirmada al redactar esto.
- Este proyecto no constituye asesoramiento financiero regulado.
