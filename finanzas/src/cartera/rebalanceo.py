"""Rebalanceo hacia una asignación objetivo.

Regla preferente para un inversor particular en España: rebalancear con las
NUEVAS APORTACIONES (comprar lo que está infraponderado) y, entre fondos, con
TRASPASOS (no tributan). Vender para rebalancear genera plusvalías gravadas y
se deja como último recurso, solo cuando se supera la banda de tolerancia.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Desviacion:
    activo: str
    valor: float
    peso_actual: float
    peso_objetivo: float

    @property
    def diferencia(self) -> float:
        return self.peso_actual - self.peso_objetivo

    def fuera_de_banda(self, banda_abs: float, banda_rel: float) -> bool:
        """Banda absoluta (p. ej. 5 puntos) o relativa (p. ej. 25 % del peso)."""
        return abs(self.diferencia) > min(banda_abs, banda_rel * self.peso_objetivo) if self.peso_objetivo > 0 else self.valor > 0


def pesos_actuales(posiciones: dict[str, float]) -> dict[str, float]:
    total = sum(posiciones.values())
    if total <= 0:
        raise ValueError("el valor total debe ser positivo")
    return {k: v / total for k, v in posiciones.items()}


def desviaciones(posiciones: dict[str, float], objetivo: dict[str, float]) -> list[Desviacion]:
    suma = sum(objetivo.values())
    if abs(suma - 1.0) > 1e-6:
        raise ValueError(f"los pesos objetivo suman {suma:.4f}, deben sumar 1")
    actuales = pesos_actuales(posiciones)
    activos = sorted(set(posiciones) | set(objetivo))
    return [
        Desviacion(a, posiciones.get(a, 0.0), actuales.get(a, 0.0), objetivo.get(a, 0.0))
        for a in activos
    ]


def ordenes_con_aportacion(
    posiciones: dict[str, float], objetivo: dict[str, float], aportacion: float
) -> dict[str, float]:
    """Reparte una aportación nueva para acercar la cartera al objetivo SIN vender.

    Algoritmo: calcula el déficit de cada activo respecto al objetivo sobre el
    total futuro (actual + aportación) y reparte la aportación proporcionalmente
    a los déficits positivos. Si ningún activo está en déficit, reparte según
    el objetivo.
    """
    if aportacion <= 0:
        raise ValueError("la aportación debe ser positiva")
    total_futuro = sum(posiciones.values()) + aportacion
    deficits = {
        a: max(0.0, objetivo.get(a, 0.0) * total_futuro - posiciones.get(a, 0.0))
        for a in set(posiciones) | set(objetivo)
    }
    suma_deficit = sum(deficits.values())
    if suma_deficit <= 0:
        return {a: round(aportacion * w, 2) for a, w in objetivo.items()}
    return {a: round(aportacion * d / suma_deficit, 2) for a, d in deficits.items() if d > 0}


def ordenes_completas(posiciones: dict[str, float], objetivo: dict[str, float]) -> dict[str, float]:
    """Importes a comprar (+) o vender/traspasar (-) para clavar el objetivo."""
    total = sum(posiciones.values())
    return {
        a: round(objetivo.get(a, 0.0) * total - posiciones.get(a, 0.0), 2)
        for a in sorted(set(posiciones) | set(objetivo))
    }
