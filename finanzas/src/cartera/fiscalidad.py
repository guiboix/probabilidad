"""Fiscalidad del ahorro en España (IRPF, base del ahorro).

Los tramos aquí codificados son los vigentes para rentas de 2025 en adelante
(declaración de 2026): 19 % / 21 % / 23 % / 27 % / 30 %.
Se aplican por igual a intereses de Letras, plusvalías de fondos y dividendos.

ATENCIÓN: verificar cada año en la web de la Agencia Tributaria. Los tramos son
un parámetro de `data/supuestos.json`; este módulo solo los aplica.
"""

from __future__ import annotations

from dataclasses import dataclass

# (límite superior del tramo en euros, tipo). El último tramo no tiene límite.
TRAMOS_AHORRO_2026: list[tuple[float | None, float]] = [
    (6_000.0, 0.19),
    (50_000.0, 0.21),
    (200_000.0, 0.23),
    (300_000.0, 0.27),
    (None, 0.30),
]

RETENCION_CUENTA = 0.19  # retención a cuenta en fondos / depósitos (las Letras no llevan)


@dataclass(frozen=True)
class ResultadoFiscal:
    base: float
    cuota: float

    @property
    def tipo_efectivo(self) -> float:
        return 0.0 if self.base <= 0 else self.cuota / self.base

    @property
    def neto(self) -> float:
        return self.base - self.cuota


def cuota_ahorro(base: float, tramos=TRAMOS_AHORRO_2026) -> ResultadoFiscal:
    """Cuota íntegra de la base del ahorro para una base positiva.

    Bases negativas (pérdidas) devuelven cuota 0; la compensación de pérdidas
    con ganancias de los cuatro años siguientes no se modela aquí.
    """
    if base <= 0:
        return ResultadoFiscal(base=base, cuota=0.0)
    cuota = 0.0
    inferior = 0.0
    for limite, tipo in tramos:
        if limite is None or base <= limite:
            cuota += (base - inferior) * tipo
            break
        cuota += (limite - inferior) * tipo
        inferior = limite
    return ResultadoFiscal(base=base, cuota=round(cuota, 2))


def tipo_marginal(base: float, tramos=TRAMOS_AHORRO_2026) -> float:
    """Tipo que soportaría el siguiente euro de rendimiento."""
    for limite, tipo in tramos:
        if limite is None or base < limite:
            return tipo
    return tramos[-1][1]
