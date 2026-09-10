# 3. Letras del Tesoro frente a fondos indexados

## 3.1 Conclusión

- Las Letras **no son una mala inversión**; son el instrumento adecuado para el dinero que no puede
  bajar de valor. Su problema en 2026 es que, tras IRPF e inflación, su rentabilidad real es negativa
  (≈ −1 %; véase documento 01).
- Un fondo indexado de renta variable global tiene una rentabilidad esperada mayor a largo plazo, pero
  sin garantía y con caídas temporales que pueden superar el 30 %.
- Con horizonte largo, la ventaja del fondo se amplía por dos vías distintas: la prima de riesgo de la
  renta variable (incierta) y el **diferimiento fiscal** (cierto).

## 3.2 Comparación cualitativa

| Criterio | Letras del Tesoro | Fondo indexado RF euro corto plazo | Fondo indexado RV global |
|---|---|---|---|
| Riesgo de pérdida nominal a vencimiento | Nulo (Estado español) | Bajo pero existe (precio varía) | Alto a corto, decrece con horizonte |
| Volatilidad anual típica | ~0 % | 1–4 % | 12–20 % |
| Rentabilidad esperada 2026 | ≈ 2,2–2,7 % bruto | Similar a Letras más/menos décimas | Desconocida; referencia histórica larga 5–8 % nominal |
| Liquidez | Vender antes de vencimiento en secundario (posible, con coste) | Diaria, sin coste | Diaria, sin coste |
| Fiscalidad | Tributa cada vencimiento, sin retención | Traspasable sin tributar | Traspasable sin tributar |
| Coste | 0 (compra directa BdE) | TER ~0,10–0,20 % | TER ~0,10–0,25 % |
| Filtro ético aplicable | No (financia al Estado en su conjunto) | Sí (versiones ESG/SRI) | Sí (versiones ESG/SRI) |
| Esfuerzo | Renovar en cada subasta | Ninguno | Ninguno |

## 3.3 El efecto del diferimiento fiscal aislado

`python -m cartera comparar --tipo-letra 0.02663 --fondo 0.02663 --coste-fondo 0 --anyos 10`

Con **la misma rentabilidad bruta** (2,663 %) y sin costes, el fondo termina con 12.434,75 € frente a
12.378,91 € de las Letras renovadas: +0,04 puntos anualizados a 10 años. Es pequeño a estos tipos,
pero crece con la rentabilidad y con el plazo. No es motivo suficiente por sí solo para cambiar.

## 3.4 Escenario con prima de riesgo (supuesto, no predicción)

`python -m cartera comparar --tipo-letra 0.02663 --fondo 0.05 --anyos 10`

| Opción | Valor final neto (10.000 € a 10 años) | Neto anualizado |
|---|---|---|
| Letras renovadas | 12.378,91 € | 2,16 % |
| Fondo al 5 % bruto − 0,35 % costes | 14.660,78 € | 3,90 % |

El 5 % es un supuesto conservador respecto a la media histórica de la renta variable mundial,
pero cualquier década concreta puede quedar muy por debajo (o en negativo). Véase la simulación.

## 3.5 Simulación con incertidumbre

`python -m cartera simular --inicial 10000 --mensual 200 --anyos 10`

| Escenario | Aportado | P5 | Mediana | P95 | P(acabar por debajo de lo aportado) |
|---|---|---|---|---|---|
| Conservador (RF corto) | 34.000 € | 37.136 € | 39.949 € | 42.963 € | 0,0 % |
| Moderado 40/60 | 34.000 € | 34.755 € | 44.979 € | 58.576 € | 3,8 % |
| Equilibrado 60/40 | 34.000 € | 32.744 € | 47.322 € | 69.404 € | 6,8 % |
| Agresivo 90/10 | 34.000 € | 28.217 € | 48.672 € | 87.368 € | 13,5 % |

Lectura: a 10 años, una cartera 60/40 tiene una mediana ~18 % superior a la conservadora, pero
en el 5 % de los peores casos queda por debajo de lo aportado. Es el precio de la rentabilidad extra.
Los parámetros son los de `data/supuestos.json` (ilustrativos) y el modelo es lognormal i.i.d., que
**subestima** las colas (crisis) respecto a la realidad.

## 3.6 Cuándo tiene sentido mantener Letras

- Fondo de emergencia y gastos previstos a < 3 años.
- Parte del bloque "renta fija" si se prefiere cero riesgo de precio a cambio de renovar manualmente.
- Cuando el tipo de la Letra supere claramente la inflación esperada (no es el caso en 09-2026).

## 3.7 Cuándo NO conviene pasar de Letras a fondos

- Si el dinero se necesita en menos de 3–5 años.
- Si no hay fondo de emergencia aparte.
- Si una caída del 20 % llevaría a vender: en ese caso el fondo de renta variable destruirá valor por
  comportamiento, no por el producto.
