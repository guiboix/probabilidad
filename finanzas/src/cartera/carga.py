"""Lectura de los ficheros CSV y JSON de la carpeta data/.

Formatos (cabeceras obligatorias):
- cartera.csv:     activo,clase,isin,valor,peso_objetivo
- movimientos.csv: fecha,activo,tipo,importe      (tipo: aportacion|retirada|valoracion)
- letras.csv:      fecha_compra,fecha_vencimiento,nominal,precio_compra
- supuestos.json:  ver data/supuestos.json
"""

from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

from .letras import Letra
from .simulacion import Escenario


def _fecha(s: str) -> date:
    return date.fromisoformat(s.strip())


def leer_cartera(ruta: Path) -> tuple[dict[str, float], dict[str, float], dict[str, str]]:
    """Devuelve (valores por activo, pesos objetivo por activo, clase por activo)."""
    valores, objetivo, clases = {}, {}, {}
    with open(ruta, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            activo = fila["activo"].strip()
            valores[activo] = float(fila["valor"] or 0)
            objetivo[activo] = float(fila["peso_objetivo"] or 0)
            clases[activo] = fila.get("clase", "").strip()
    return valores, objetivo, clases


def leer_movimientos(ruta: Path) -> list[tuple[date, str, str, float]]:
    with open(ruta, newline="", encoding="utf-8") as f:
        return [
            (_fecha(r["fecha"]), r["activo"].strip(), r["tipo"].strip(), float(r["importe"]))
            for r in csv.DictReader(f)
        ]


def leer_letras(ruta: Path) -> list[Letra]:
    with open(ruta, newline="", encoding="utf-8") as f:
        return [
            Letra(
                fecha_compra=_fecha(r["fecha_compra"]),
                fecha_vencimiento=_fecha(r["fecha_vencimiento"]),
                nominal=float(r["nominal"]),
                precio_compra=float(r["precio_compra"]),
            )
            for r in csv.DictReader(f)
        ]


def leer_supuestos(ruta: Path) -> dict:
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)
    datos["escenarios"] = [
        Escenario(e["nombre"], e["rentabilidad_anual"], e["volatilidad_anual"])
        for e in datos.get("escenarios", [])
    ]
    return datos
