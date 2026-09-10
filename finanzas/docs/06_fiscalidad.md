# 6. Fiscalidad para un residente fiscal en España

> Vigente para rentas de 2025 y 2026 según fuentes consultadas (Raisin, Holded, Wolters Kluwer,
> idealista/news). Verificar en agenciatributaria.es antes de cada declaración. No sustituye a un asesor fiscal.

## 6.1 Base del ahorro (aplica a Letras, fondos, depósitos, dividendos, ETF)

| Tramo | Tipo |
|---|---|
| Hasta 6.000 € | 19 % |
| 6.000 – 50.000 € | 21 % |
| 50.000 – 200.000 € | 23 % |
| 200.000 – 300.000 € | 27 % |
| Más de 300.000 € | 30 % |

La escala es estatal (igual en todas las comunidades del régimen común). Se aplica al conjunto de
rendimientos y ganancias del año, no producto a producto. Está implementada en `cartera.fiscalidad`.

## 6.2 Por producto

| Producto | Cuándo tributa | Retención | Particularidades |
|---|---|---|---|
| Letras del Tesoro | Al vencimiento o venta, como rendimiento del capital mobiliario | **Sin retención** (se paga en la declaración) | Rendimiento = nominal − precio de compra |
| Fondos de inversión (UCITS) | Solo al **reembolsar**, como ganancia patrimonial | 19 % a cuenta | **Traspaso entre fondos sin tributar** (diferimiento). Requisito: fondo con > 500 partícipes |
| ETF | Al vender, como ganancia patrimonial | 19 % | Los ETF **no** admiten traspaso sin tributar en España (salvo excepciones muy limitadas). Por eso este proyecto prioriza fondos sobre ETF |
| Cuenta remunerada / depósito | Al cobrar intereses | 19 % | |
| Dividendos de fondos de distribución | Al cobrarlos | 19 % | Preferir clases de acumulación |

## 6.3 Reglas útiles

- **Compensación:** pérdidas patrimoniales compensan ganancias del mismo año; el remanente, hasta 4 años.
  Además, hasta un 25 % entre rendimientos del capital mobiliario y ganancias patrimoniales.
- **Regla de los dos meses (antifraude):** si se vende un fondo con pérdidas y se recompra el mismo
  en los 2 meses anteriores o posteriores, la pérdida no se puede computar hasta que se venda de nuevo.
  No afecta a los traspasos.
- **FIFO:** al reembolsar parcialmente, se consideran vendidas primero las participaciones más antiguas.
- **Modelo 720 / D-6:** no aplican a fondos comercializados en España a través de MyInvestor
  (custodia en entidad española). Confirmar si se abren cuentas en brókers extranjeros.
- **Impuesto sobre el Patrimonio:** solo por encima del mínimo exento autonómico (700.000 € en la mayoría);
  irrelevante a la escala de este proyecto salvo indicación contraria.

## 6.4 Implicación práctica para la transición Letras → fondos

- Dejar vencer las Letras (sin venderlas antes) y no renovar la parte que se quiera mover: no hay
  penalización fiscal adicional, el rendimiento tributa igual que si se renovaran.
- Una vez en fondos, rebalancear mediante traspasos y aportaciones: cero impacto fiscal hasta el reembolso final.
- Anotar en `movimientos.csv` cada aportación y reembolso con fecha: es lo que permite calcular la
  ganancia patrimonial y la TIR real.
