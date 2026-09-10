"""Métricas de rentabilidad y riesgo de una cartera."""

from __future__ import annotations

import math
import statistics
from datetime import date
from typing import Iterable, Sequence


def rentabilidad_simple(valor_inicial: float, valor_final: float, aportaciones: float = 0.0) -> float:
    """(valor final - aportaciones netas) / valor inicial - 1. Sólo orientativa."""
    if valor_inicial <= 0:
        raise ValueError("valor_inicial debe ser positivo")
    return (valor_final - aportaciones) / valor_inicial - 1.0


def twr(valores: Sequence[float], flujos: Sequence[float]) -> float:
    """Time-Weighted Return.

    `valores[i]` es el valor de la cartera al final del periodo i, y `flujos[i]`
    la aportación (positiva) o retirada (negativa) realizada justo al INICIO del
    periodo i. `valores[0]` es el valor inicial y `flujos[0]` debe ser 0.
    Neutraliza el efecto de cuándo se aporta: mide la calidad de la inversión.
    """
    if len(valores) != len(flujos) or len(valores) < 2:
        raise ValueError("valores y flujos deben tener la misma longitud >= 2")
    acumulado = 1.0
    for i in range(1, len(valores)):
        base = valores[i - 1] + flujos[i]
        if base <= 0:
            raise ValueError(f"base no positiva en el periodo {i}")
        acumulado *= valores[i] / base
    return acumulado - 1.0


def xnpv(tasa: float, flujos: Iterable[tuple[date, float]]) -> float:
    flujos = list(flujos)
    t0 = flujos[0][0]
    return sum(f / (1.0 + tasa) ** ((d - t0).days / 365.0) for d, f in flujos)


def xirr(flujos: Sequence[tuple[date, float]], tol: float = 1e-9, max_iter: int = 200) -> float:
    """TIR con fechas reales (equivalente a XIRR de hojas de cálculo).

    Convención: aportaciones negativas, valor final / retiradas positivas.
    Mide la rentabilidad que ha obtenido el dinero del inversor (money-weighted).
    Usa bisección sobre [-0.99, 10], suficiente para carteras personales.
    """
    flujos = sorted(flujos, key=lambda x: x[0])
    if not any(f < 0 for _, f in flujos) or not any(f > 0 for _, f in flujos):
        raise ValueError("se necesitan flujos negativos y positivos")
    lo, hi = -0.99, 10.0
    f_lo = xnpv(lo, flujos)
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        f_mid = xnpv(mid, flujos)
        if abs(f_mid) < tol:
            return mid
        if (f_lo < 0) == (f_mid < 0):
            lo, f_lo = mid, f_mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def rentabilidades_periodicas(valores: Sequence[float]) -> list[float]:
    return [valores[i] / valores[i - 1] - 1.0 for i in range(1, len(valores))]


def volatilidad_anualizada(rentabilidades: Sequence[float], periodos_por_anyo: int = 12) -> float:
    """Desviación típica muestral anualizada (regla raíz del tiempo)."""
    if len(rentabilidades) < 2:
        raise ValueError("se necesitan al menos dos rentabilidades")
    return statistics.stdev(rentabilidades) * math.sqrt(periodos_por_anyo)


def drawdown_maximo(valores: Sequence[float]) -> float:
    """Mayor caída desde un máximo previo, como fracción negativa (p. ej. -0.25)."""
    maximo = -math.inf
    peor = 0.0
    for v in valores:
        maximo = max(maximo, v)
        peor = min(peor, v / maximo - 1.0)
    return peor


def ratio_sharpe(rentabilidad_anual: float, volatilidad_anual: float, tasa_libre: float) -> float:
    if volatilidad_anual <= 0:
        raise ValueError("volatilidad debe ser positiva")
    return (rentabilidad_anual - tasa_libre) / volatilidad_anual
