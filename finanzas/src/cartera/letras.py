"""Letras del Tesoro: emitidas al descuento sobre nominal de 1.000 €.

Convenciones del Tesoro Público:
- Plazos de 3, 6, 9 y 12 meses.
- El "tipo de interés medio" publicado usa base ACT/360 para plazos <= 376 días.
- No hay retención a cuenta, pero el rendimiento tributa en la base del ahorro.
- Compra en subasta vía Banco de España / tesoro.es sin comisión de compra;
  mantener hasta vencimiento elimina el riesgo de precio.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from .fiscalidad import TRAMOS_AHORRO_2026, cuota_ahorro

NOMINAL = 1_000.0


@dataclass(frozen=True)
class Letra:
    fecha_compra: date
    fecha_vencimiento: date
    nominal: float
    precio_compra: float  # importe pagado por cada 1.000 € de nominal

    @property
    def dias(self) -> int:
        return (self.fecha_vencimiento - self.fecha_compra).days

    @property
    def importe_pagado(self) -> float:
        return self.nominal * self.precio_compra / NOMINAL

    @property
    def rendimiento_bruto(self) -> float:
        return self.nominal - self.importe_pagado

    def tipo_anual(self, base: int = 360) -> float:
        return tipo_desde_precio(self.precio_compra, self.dias, base)


def tipo_desde_precio(precio: float, dias: int, base: int = 360) -> float:
    """Tipo de interés simple anualizado a partir del precio por 1.000 € nominal.

    Es la fórmula del Tesoro para plazos hasta 376 días:
        tipo = (nominal / precio - 1) * base / dias
    """
    if dias <= 0:
        raise ValueError("dias debe ser positivo")
    return (NOMINAL / precio - 1.0) * base / dias


def precio_desde_tipo(tipo: float, dias: int, base: int = 360) -> float:
    """Precio por 1.000 € de nominal dado el tipo anual simple."""
    if dias <= 0:
        raise ValueError("dias debe ser positivo")
    return NOMINAL / (1.0 + tipo * dias / base)


def rentabilidad_efectiva(precio: float, dias: int) -> float:
    """Rentabilidad efectiva anual (TAE) compuesta, base 365."""
    if dias <= 0:
        raise ValueError("dias debe ser positivo")
    return (NOMINAL / precio) ** (365.0 / dias) - 1.0


@dataclass(frozen=True)
class AnalisisLetra:
    tipo_anual_bruto: float
    tae_bruta: float
    rendimiento_bruto: float
    impuesto: float
    rendimiento_neto: float
    tae_neta: float
    tae_real_neta: float | None  # None si no se aporta inflación
    comisiones: float = 0.0  # comisiones del intermediario descontadas del neto


def analizar(
    precio: float,
    dias: int,
    nominal_total: float = NOMINAL,
    otras_rentas_ahorro: float = 0.0,
    inflacion: float | None = None,
    tramos=TRAMOS_AHORRO_2026,
    comision_compra: float = 0.0,
    comision_compra_minimo: float = 0.0,
    comision_custodia_anual: float = 0.0,
    comision_amortizacion: float = 0.0,
    comision_amortizacion_minimo: float = 0.0,
    comision_amortizacion_maximo: float | None = None,
) -> AnalisisLetra:
    """Rentabilidad bruta, neta de IRPF y real de una posición en Letras.

    `otras_rentas_ahorro` permite calcular el impuesto marginal correcto si el
    inversor ya tiene otros rendimientos en la base del ahorro ese año.

    Comisiones (en tanto por uno sobre el nominal, salvo mínimos/máximos en euros):
    - compra: la cobra un banco intermediario (CaixaBank ≈ 0,6 %, mín. 30,05 €;
      Banco de España 0 %).
    - custodia anual: banco intermediario ≈ 0,05 %; Banco de España 0 %.
    - amortización: Banco de España 0,15 % sobre el importe transferido
      (mín. 0,90 €, máx. 200 €); bancos, normalmente 0.
    Las comisiones NO reducen la base del IRPF salvo la de amortización del BdE
    (criterio DGT); aquí, por prudencia, ninguna se deduce fiscalmente.
    """
    importe = nominal_total * precio / NOMINAL
    bruto = nominal_total - importe
    impuesto = (
        cuota_ahorro(otras_rentas_ahorro + bruto, tramos).cuota
        - cuota_ahorro(otras_rentas_ahorro, tramos).cuota
    )
    c_compra = max(nominal_total * comision_compra, comision_compra_minimo) if comision_compra or comision_compra_minimo else 0.0
    c_custodia = nominal_total * comision_custodia_anual * dias / 365.0
    c_amort = nominal_total * comision_amortizacion
    if comision_amortizacion:
        c_amort = max(c_amort, comision_amortizacion_minimo)
        if comision_amortizacion_maximo is not None:
            c_amort = min(c_amort, comision_amortizacion_maximo)
    comisiones = c_compra + c_custodia + c_amort
    neto = bruto - impuesto - comisiones
    tae_bruta = rentabilidad_efectiva(precio, dias)
    tae_neta = (1.0 + neto / importe) ** (365.0 / dias) - 1.0
    real = None if inflacion is None else (1.0 + tae_neta) / (1.0 + inflacion) - 1.0
    return AnalisisLetra(
        tipo_anual_bruto=tipo_desde_precio(precio, dias),
        tae_bruta=tae_bruta,
        rendimiento_bruto=round(bruto, 2),
        impuesto=round(impuesto, 2),
        rendimiento_neto=round(neto, 2),
        tae_neta=tae_neta,
        tae_real_neta=real,
        comisiones=round(comisiones, 2),
    )
