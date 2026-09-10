"""Interfaz de línea de comandos.

    python -m cartera letras --precio 973.78 --dias 364 [--nominal 10000] [--inflacion 0.033]
    python -m cartera comparar --tipo-letra 0.02663 --fondo 0.05 --anyos 10 --importe 10000
    python -m cartera informe [--data data]
    python -m cartera simular --inicial 10000 --mensual 200 --anyos 15 [--data data]
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from . import carga, letras, metricas, rebalanceo, simulacion
from .fiscalidad import cuota_ahorro


def _pct(x: float) -> str:
    return f"{x * 100:.2f} %"


def cmd_letras(a: argparse.Namespace) -> None:
    r = letras.analizar(a.precio, a.dias, a.nominal, a.otras_rentas, a.inflacion)
    print(f"# Letra: precio {a.precio:.2f} por 1.000 €, {a.dias} días, nominal {a.nominal:,.0f} €\n")
    print(f"| Concepto | Valor |\n|---|---|")
    print(f"| Tipo anual simple bruto (ACT/360, criterio Tesoro) | {_pct(r.tipo_anual_bruto)} |")
    print(f"| TAE bruta | {_pct(r.tae_bruta)} |")
    print(f"| Rendimiento bruto | {r.rendimiento_bruto:,.2f} € |")
    print(f"| IRPF (base del ahorro) | {r.impuesto:,.2f} € |")
    print(f"| Rendimiento neto | {r.rendimiento_neto:,.2f} € |")
    print(f"| TAE neta | {_pct(r.tae_neta)} |")
    if r.tae_real_neta is not None:
        print(f"| TAE real neta (inflación {_pct(a.inflacion)}) | {_pct(r.tae_real_neta)} |")


def cmd_comparar(a: argparse.Namespace) -> None:
    """Letra renovada cada año vs. fondo de acumulación con diferimiento fiscal.

    Simplificación: rentabilidad constante, sin volatilidad. Sirve para ver el
    efecto del diferimiento fiscal y del tipo, no para predecir.
    """
    v_letra = a.importe
    for _ in range(a.anyos):
        bruto = v_letra * a.tipo_letra
        v_letra += bruto - cuota_ahorro(bruto).cuota  # tributa cada año
    v_fondo_bruto = a.importe * (1 + a.fondo - a.coste_fondo) ** a.anyos
    plusvalia = v_fondo_bruto - a.importe
    v_fondo_neto = v_fondo_bruto - cuota_ahorro(plusvalia).cuota  # tributa al final
    print(f"# Comparativa a {a.anyos} años, {a.importe:,.0f} € iniciales (sin volatilidad)\n")
    print("| Opción | Supuesto | Valor final neto | Rentabilidad neta anualizada |\n|---|---|---|---|")
    print(f"| Letras renovadas cada año | {_pct(a.tipo_letra)} bruto, tributa cada año | {v_letra:,.2f} € | {_pct((v_letra / a.importe) ** (1 / a.anyos) - 1)} |")
    print(f"| Fondo de acumulación | {_pct(a.fondo)} bruto − {_pct(a.coste_fondo)} costes, tributa al reembolsar | {v_fondo_neto:,.2f} € | {_pct((v_fondo_neto / a.importe) ** (1 / a.anyos) - 1)} |")
    print("\nAviso: el fondo asume una rentabilidad que NO está garantizada; la letra sí, si se mantiene a vencimiento.")


def cmd_informe(a: argparse.Namespace) -> None:
    data = Path(a.data)
    sup = carga.leer_supuestos(data / "supuestos.json")
    print(f"# Informe de cartera — {date.today().isoformat()}\n")

    ruta_cartera = data / "cartera.csv"
    if ruta_cartera.exists():
        valores, objetivo, clases = carga.leer_cartera(ruta_cartera)
        total = sum(valores.values())
        print(f"## Posiciones (total {total:,.2f} €)\n")
        print("| Activo | Clase | Valor | Peso actual | Peso objetivo | Desviación | Fuera de banda |\n|---|---|---|---|---|---|---|")
        for d in rebalanceo.desviaciones(valores, objetivo):
            fb = "SÍ" if d.fuera_de_banda(sup["banda_abs"], sup["banda_rel"]) else "no"
            print(f"| {d.activo} | {clases.get(d.activo, '')} | {d.valor:,.2f} € | {_pct(d.peso_actual)} | {_pct(d.peso_objetivo)} | {d.diferencia * 100:+.2f} pp | {fb} |")
        if a.aportacion:
            print(f"\n### Reparto sugerido de una aportación de {a.aportacion:,.2f} € (sin vender)\n")
            for act, imp in rebalanceo.ordenes_con_aportacion(valores, objetivo, a.aportacion).items():
                print(f"- {act}: {imp:,.2f} €")
    else:
        print("_No hay data/cartera.csv; copia data/plantilla_cartera.csv y rellénalo._\n")

    ruta_letras = data / "letras.csv"
    if ruta_letras.exists():
        print("\n## Letras del Tesoro\n")
        print("| Compra | Vencimiento | Nominal | Precio | Tipo anual bruto | TAE neta |\n|---|---|---|---|---|---|")
        for l in carga.leer_letras(ruta_letras):
            r = letras.analizar(l.precio_compra, l.dias, l.nominal)
            print(f"| {l.fecha_compra} | {l.fecha_vencimiento} | {l.nominal:,.0f} € | {l.precio_compra:.2f} | {_pct(r.tipo_anual_bruto)} | {_pct(r.tae_neta)} |")

    ruta_mov = data / "movimientos.csv"
    if ruta_mov.exists():
        movs = carga.leer_movimientos(ruta_mov)
        flujos = [(f, -imp) for f, _, t, imp in movs if t == "aportacion"]
        flujos += [(f, imp) for f, _, t, imp in movs if t == "retirada"]
        valoraciones = [(f, imp) for f, _, t, imp in movs if t == "valoracion"]
        if flujos and valoraciones:
            ultima = max(valoraciones)
            try:
                tir = metricas.xirr(flujos + [ultima])
                print(f"\n## Rentabilidad del inversor (TIR / XIRR) hasta {ultima[0]}: {_pct(tir)}\n")
            except ValueError as e:
                print(f"\n_No se pudo calcular la TIR: {e}_\n")


def cmd_simular(a: argparse.Namespace) -> None:
    sup = carga.leer_supuestos(Path(a.data) / "supuestos.json")
    print(f"# Simulación Monte Carlo: {a.inicial:,.0f} € iniciales + {a.mensual:,.0f} €/mes durante {a.anyos} años\n")
    print("| Escenario | Rent. esp. | Vol. | Aportado | P5 | P25 | Mediana | P75 | P95 | P(perder) |\n|---|---|---|---|---|---|---|---|---|---|")
    for esc in sup["escenarios"]:
        r = simulacion.simular(a.inicial, a.mensual, a.anyos, esc, a.n)
        p = r.percentiles
        print(f"| {esc.nombre} | {_pct(esc.rentabilidad_anual)} | {_pct(esc.volatilidad_anual)} | {r.aportado_total:,.0f} € | {p[5]:,.0f} | {p[25]:,.0f} | {p[50]:,.0f} | {p[75]:,.0f} | {p[95]:,.0f} | {_pct(r.prob_perder_dinero)} |")
    print("\nLos parámetros son supuestos de data/supuestos.json, no predicciones. Modelo lognormal i.i.d. mensual.")


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(prog="cartera", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("letras", help="analiza una Letra del Tesoro")
    s.add_argument("--precio", type=float, required=True, help="precio por 1.000 € nominal (p. ej. 973.78)")
    s.add_argument("--dias", type=int, required=True)
    s.add_argument("--nominal", type=float, default=1000.0)
    s.add_argument("--otras-rentas", type=float, default=0.0, help="otras rentas del ahorro del año")
    s.add_argument("--inflacion", type=float, default=None, help="inflación anual esperada, p. ej. 0.033")
    s.set_defaults(func=cmd_letras)

    s = sub.add_parser("comparar", help="letras renovadas vs fondo de acumulación")
    s.add_argument("--tipo-letra", type=float, required=True)
    s.add_argument("--fondo", type=float, required=True, help="rentabilidad bruta anual supuesta del fondo")
    s.add_argument("--coste-fondo", type=float, default=0.0035, help="costes anuales totales del fondo")
    s.add_argument("--anyos", type=int, default=10)
    s.add_argument("--importe", type=float, default=10_000.0)
    s.set_defaults(func=cmd_comparar)

    s = sub.add_parser("informe", help="informe de la cartera a partir de data/")
    s.add_argument("--data", default="data")
    s.add_argument("--aportacion", type=float, default=0.0, help="importe de la próxima aportación a repartir")
    s.set_defaults(func=cmd_informe)

    s = sub.add_parser("simular", help="proyección Monte Carlo")
    s.add_argument("--inicial", type=float, required=True)
    s.add_argument("--mensual", type=float, default=0.0)
    s.add_argument("--anyos", type=int, required=True)
    s.add_argument("--n", type=int, default=5_000)
    s.add_argument("--data", default="data")
    s.set_defaults(func=cmd_simular)

    a = p.parse_args(argv)
    a.func(a)


if __name__ == "__main__":
    main()
