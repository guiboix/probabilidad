"""Bonos y Obligaciones del Estado (y bonos con cupón en general).

Diferencia con la Letra: el bono paga un cupón (interés) cada año y devuelve
el nominal al vencimiento. Su precio en el mercado sube cuando bajan los tipos
y baja cuando suben; si se mantiene hasta vencimiento, el resultado es el que
se fijó al comprar (la TIR), salvo impago del emisor.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from .fiscalidad import TRAMOS_AHORRO_2026, cuota_ahorro

NOMINAL = 1_000.0


@dataclass(frozen=True)
class Bono:
    emisor: str
    fecha_compra: date
    fecha_vencimiento: date
    nominal: float
    cupon_anual: float  # en tanto por uno sobre el nominal, p. ej. 0.028
    precio_compra: float  # por cada 1.000 € de nominal, sin cupón corrido

    @property
    def anyos(self) -> float:
        return (self.fecha_vencimiento - self.fecha_compra).days / 365.0

    @property
    def importe_pagado(self) -> float:
        return self.nominal * self.precio_compra / NOMINAL


def flujos(cupon_anual: float, anyos: float) -> list[tuple[float, float]]:
    """(tiempo en años, importe por 1.000 € nominal). Cupón anual; el último incluye el nominal."""
    n = int(round(anyos))
    if n <= 0:
        raise ValueError("el bono debe tener al menos un año de vida")
    c = NOMINAL * cupon_anual
    return [(t, c) for t in range(1, n)] + [(n, c + NOMINAL)]


def precio_desde_tir(tir: float, cupon_anual: float, anyos: float) -> float:
    return sum(f / (1.0 + tir) ** t for t, f in flujos(cupon_anual, anyos))


def tir_desde_precio(precio: float, cupon_anual: float, anyos: float, tol: float = 1e-10) -> float:
    """Rentabilidad anual a vencimiento (TIR) por bisección."""
    lo, hi = -0.5, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if precio_desde_tir(mid, cupon_anual, anyos) > precio:
            lo = mid  # precio calculado alto -> la TIR real es mayor
        else:
            hi = mid
        if hi - lo < tol:
            break
    return (lo + hi) / 2.0


def duracion_modificada(tir: float, cupon_anual: float, anyos: float) -> float:
    """Sensibilidad del precio a los tipos: caída aproximada (%) por cada +1 punto de tipos."""
    p = precio_desde_tir(tir, cupon_anual, anyos)
    macaulay = sum(t * f / (1.0 + tir) ** t for t, f in flujos(cupon_anual, anyos)) / p
    return macaulay / (1.0 + tir)


@dataclass(frozen=True)
class AnalisisBono:
    tir_bruta: float
    duracion_modificada: float
    cupon_anual_euros: float
    cupon_neto_anual_euros: float
    ganancia_total_bruta: float
    impuestos_totales: float
    ganancia_total_neta: float


def analizar(
    precio: float, cupon_anual: float, anyos: float, nominal_total: float = NOMINAL, tramos=TRAMOS_AHORRO_2026
) -> AnalisisBono:
    tir = tir_desde_precio(precio, cupon_anual, anyos)
    n = int(round(anyos))
    cupon = nominal_total * cupon_anual
    imp_cupon = cuota_ahorro(cupon, tramos).cuota  # tributa cada año (simplificación: sin otras rentas)
    ganancia_vto = nominal_total - nominal_total * precio / NOMINAL
    imp_vto = cuota_ahorro(ganancia_vto, tramos).cuota if ganancia_vto > 0 else 0.0
    bruta = cupon * n + ganancia_vto
    impuestos = imp_cupon * n + imp_vto
    return AnalisisBono(
        tir_bruta=tir,
        duracion_modificada=duracion_modificada(tir, cupon_anual, anyos),
        cupon_anual_euros=round(cupon, 2),
        cupon_neto_anual_euros=round(cupon - imp_cupon, 2),
        ganancia_total_bruta=round(bruta, 2),
        impuestos_totales=round(impuestos, 2),
        ganancia_total_neta=round(bruta - impuestos, 2),
    )
