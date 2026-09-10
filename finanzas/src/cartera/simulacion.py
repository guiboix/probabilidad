"""Proyección Monte Carlo de una cartera con aportaciones periódicas.

Modelo: rentabilidad mensual lognormal i.i.d. (hipótesis simplificadora: sin
autocorrelación ni colas gruesas; véase Tema 7 del curso de probabilidad para
por qué la suma de muchos periodos tiende a la normal, y sus límites).

Los parámetros (rentabilidad esperada y volatilidad anual) son SUPUESTOS del
usuario, no predicciones. Se leen de data/supuestos.json.
"""

from __future__ import annotations

import math
import random
import statistics
from dataclasses import dataclass


@dataclass(frozen=True)
class Escenario:
    nombre: str
    rentabilidad_anual: float  # media aritmética esperada
    volatilidad_anual: float


@dataclass(frozen=True)
class ResultadoSimulacion:
    escenario: str
    anyos: int
    aportado_total: float
    percentiles: dict[int, float]  # p5, p25, p50, p75, p95 del valor final
    prob_perder_dinero: float  # P(valor final < aportado total)
    media: float


def _parametros_mensuales(r_anual: float, vol_anual: float) -> tuple[float, float]:
    """Convierte media/vol aritméticas anuales en parámetros log-normales mensuales."""
    sigma_m = vol_anual / math.sqrt(12.0)
    # media aritmética mensual -> media del logaritmo (corrección de Itô)
    mu_m = math.log(1.0 + r_anual) / 12.0 - sigma_m**2 / 2.0
    return mu_m, sigma_m


def simular(
    valor_inicial: float,
    aportacion_mensual: float,
    anyos: int,
    escenario: Escenario,
    n_simulaciones: int = 5_000,
    semilla: int | None = 42,
) -> ResultadoSimulacion:
    if anyos <= 0 or n_simulaciones <= 0:
        raise ValueError("anyos y n_simulaciones deben ser positivos")
    rng = random.Random(semilla)
    mu_m, sigma_m = _parametros_mensuales(escenario.rentabilidad_anual, escenario.volatilidad_anual)
    meses = anyos * 12
    finales: list[float] = []
    for _ in range(n_simulaciones):
        v = valor_inicial
        for _ in range(meses):
            v = v * math.exp(rng.gauss(mu_m, sigma_m)) + aportacion_mensual
        finales.append(v)
    finales.sort()
    aportado = valor_inicial + aportacion_mensual * meses

    def pct(p: int) -> float:
        idx = min(len(finales) - 1, max(0, round(p / 100.0 * (len(finales) - 1))))
        return finales[idx]

    return ResultadoSimulacion(
        escenario=escenario.nombre,
        anyos=anyos,
        aportado_total=aportado,
        percentiles={p: round(pct(p), 2) for p in (5, 25, 50, 75, 95)},
        prob_perder_dinero=sum(1 for f in finales if f < aportado) / len(finales),
        media=round(statistics.fmean(finales), 2),
    )


def valor_determinista(valor_inicial: float, aportacion_mensual: float, anyos: int, r_anual: float) -> float:
    """Valor final sin incertidumbre (interés compuesto mensual). Útil como referencia."""
    i = (1.0 + r_anual) ** (1.0 / 12.0) - 1.0
    meses = anyos * 12
    v = valor_inicial * (1.0 + i) ** meses
    if i == 0:
        return v + aportacion_mensual * meses
    return v + aportacion_mensual * ((1.0 + i) ** meses - 1.0) / i
