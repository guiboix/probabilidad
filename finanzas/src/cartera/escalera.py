"""Escalera de Letras del Tesoro (varias letras con vencimientos escalonados).

Cada vencimiento es una ventana natural de decisión: renovar, mover a fondos
o mezclar. Este módulo calcula el calendario y reparte cada vencimiento según
la asignación objetivo sin vender nada antes de tiempo.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from .letras import Letra, analizar


@dataclass(frozen=True)
class Vencimiento:
    fecha: date
    dias_restantes: int
    nominal: float
    importe_pagado: float
    tipo_anual_bruto: float
    tae_neta: float
    rendimiento_neto: float


def calendario(letras: list[Letra], hoy: date, otras_rentas_ahorro: float = 0.0) -> list[Vencimiento]:
    """Vencimientos futuros ordenados por fecha. Las letras ya vencidas se omiten."""
    out = []
    for l in sorted(letras, key=lambda x: x.fecha_vencimiento):
        if l.fecha_vencimiento < hoy:
            continue
        r = analizar(l.precio_compra, l.dias, l.nominal, otras_rentas_ahorro)
        out.append(
            Vencimiento(
                fecha=l.fecha_vencimiento,
                dias_restantes=(l.fecha_vencimiento - hoy).days,
                nominal=l.nominal,
                importe_pagado=l.importe_pagado,
                tipo_anual_bruto=r.tipo_anual_bruto,
                tae_neta=r.tae_neta,
                rendimiento_neto=r.rendimiento_neto,
            )
        )
    return out


def plan_transicion(
    letras: list[Letra], hoy: date, peso_objetivo_letras: float, reserva_minima: float = 0.0
) -> list[tuple[date, float, float, float]]:
    """Para cada vencimiento: (fecha, nominal que vence, importe a renovar, importe a mover).

    Se renueva lo necesario para que las Letras vivas tras el vencimiento sean
    max(reserva_minima, peso_objetivo_letras * total de la escalera). El resto
    se libera para otros activos. Simplificación: el total de la escalera se
    toma como el nominal actual (no incluye lo que ya se haya movido a fondos).
    """
    if not 0.0 <= peso_objetivo_letras <= 1.0:
        raise ValueError("peso_objetivo_letras debe estar entre 0 y 1")
    vivas = [l for l in letras if l.fecha_vencimiento >= hoy]
    total = sum(l.nominal for l in vivas)
    objetivo = max(reserva_minima, peso_objetivo_letras * total)
    resultado = []
    en_letras = total
    for l in sorted(vivas, key=lambda x: x.fecha_vencimiento):
        restantes = en_letras - l.nominal
        renovar = min(l.nominal, max(0.0, objetivo - restantes))
        mover = l.nominal - renovar
        resultado.append((l.fecha_vencimiento, l.nominal, round(renovar, 2), round(mover, 2)))
        en_letras = restantes + renovar
    return resultado
