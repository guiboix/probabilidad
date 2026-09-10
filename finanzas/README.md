# Gestión de cartera personal — Letras del Tesoro y fondos indexados éticos

Proyecto para gestionar una cartera de inversión particular en España con tres criterios declarados por
el usuario: **rentabilidad, ética y seguridad**. Incluye documentación de decisión y un paquete Python
(sin dependencias externas) para calcular rentabilidades, comparar productos, rebalancear y simular.

> **Si empiezas desde cero, lee primero [`docs/00_guia_principiante.md`](docs/00_guia_principiante.md).** Explica cada palabra y cada comando con tus propios números.

## Conclusión principal (10-09-2026)

1. La percepción de que las Letras rinden poco es correcta y cuantificable: la Letra a 12 meses de la
   subasta del 4 de agosto de 2026 (2,663 % bruto) rinde **2,19 % neto de IRPF** y **−1,08 % real** con la
   inflación de agosto (3,3 %). Pierde poder adquisitivo.
2. No existe un producto "seguro y más rentable". La alternativa es repartir el dinero por horizonte:
   Letras para lo que se necesita a < 3 años; fondos indexados (con filtro ético) para lo que se puede
   dejar > 7–10 años; renta fija corta en medio.
3. En MyInvestor la vía más barata y con control ético total son los **fondos indexados sueltos**
   (coste ≈ TER 0,10–0,30 %, sin custodia); la cartera automatizada cuesta ≈ 0,40 % y no filtra ética;
   la Cartera Sostenible filtra (art. 9) pero cuesta 0,81 % o más según la fuente.
4. Situación declarada: fondo de emergencia aparte; dos Letras de 8.000 € que amortizan el 06-11-2026 y el
   04-06-2027 y se mantienen renovándose; rinden ≈ 290 € netos y pierden ≈ 238 € de poder adquisitivo al año.
5. Perfil acordado: **muy conservador**. Renta variable 0 % de momento; al menos el 85 % del capital en
   Letras y renta fija a corto plazo; hasta un 15 % en fondos de renta fija ética de riesgo 2 para aprender.
6. Otros productos analizados (documento 10): Bonos del Estado a 3 años (2,87 % el 03-09-2026) y cuenta
   remunerada de MyInvestor (2,5 % TAE promocional) merecen estudio; plan de pensiones depende de los
   ingresos (dato pendiente); crowdlending, cripto, estructurados y subordinadas quedan descartados.
7. Primer paso acordado: 300 € en un fondo de renta fija de bajo riesgo con filtro ético, con ahorro nuevo,
   para aprender (documento 09). La ampliación se decide por comprensión y tolerancia, no por la
   rentabilidad de los primeros meses (§9.7). Avisos de vencimiento: `.ics` importable y comando `escalera`; los
   recordatorios automáticos en la sesión no se pudieron crear por permisos (documento 08 §8.5). Para la cartera completa siguen faltando horizonte, tolerancia a caídas y
   nivel ético (documento 01).

## Estructura

```
finanzas/
├── README.md
├── docs/
│   ├── 00_guia_principiante.md      # vocabulario y conceptos explicados desde cero
│   ├── 01_perfil_y_objetivos.md     # datos que faltan + hechos verificados sept. 2026
│   ├── 02_politica_inversion.md     # principios, asignación objetivo, reglas de rebalanceo
│   ├── 03_letras_vs_fondos.md       # comparación cuantitativa y cualitativa
│   ├── 04_myinvestor_opciones.md    # vías A/B, fondos ESG candidatos, checklist de contratación
│   ├── 05_criterios_eticos.md       # vocabulario ESG/SRI/SFDR y decisión a tomar
│   ├── 06_fiscalidad.md             # base del ahorro 2026, traspasos, reglas prácticas
│   └── 07_plan_accion.md            # fases y checklist
├── data/
│   ├── supuestos.json               # parámetros (inflación, tipo letra, bandas, escenarios) con fuente
│   ├── plantilla_*.csv              # plantillas; los CSV reales están en .gitignore
│   ├── calendario_vencimientos.ics  # eventos de decisión/amortización de las Letras, importable en cualquier calendario
│   └── README.md
├── src/cartera/                     # paquete Python (stdlib únicamente)
│   ├── fiscalidad.py  letras.py  bonos.py  escalera.py  metricas.py  rebalanceo.py  simulacion.py  carga.py  cli.py
└── tests/                           # 43 tests unittest
```

## Uso

```bash
cd finanzas
export PYTHONPATH=src            # o: pip install -e .

# Rentabilidad bruta, neta y real de una Letra (precio por 1.000 € nominal, días a vencimiento)
python -m cartera letras --precio 973.78 --dias 364 --nominal 10000 --inflacion 0.033

# Letras renovadas vs fondo de acumulación (efecto del diferimiento fiscal y de la prima de riesgo)
python -m cartera comparar --tipo-letra 0.02663 --fondo 0.05 --anyos 10 --importe 10000

# Proyección Monte Carlo con los escenarios de data/supuestos.json
python -m cartera simular --inicial 10000 --mensual 200 --anyos 10

# Calendario de vencimientos de las Letras y plan de transición (requiere data/letras.csv)
python -m cartera escalera --data data --peso-letras 0.5 --reserva 5000 --inflacion 0.033

# TIR, duración y rendimiento neto de un Bono del Estado (o cualquier bono con cupón)
python -m cartera bono --precio 995 --cupon 0.028 --anyos 3 --nominal 8000

# Seguimiento de un fondo a partir de sus valores liquidativos (data/vl.csv)
python -m cartera seguimiento --data data --periodos-anyo 52

# Informe de la cartera real (requiere data/cartera.csv etc.; ver data/README.md)
python -m cartera informe --data data --aportacion 500

make test
```

## Relación con el resto del repositorio

El repositorio contiene un curso de probabilidad. La simulación (`simulacion.py`) aplica directamente
sus contenidos: rentabilidades como variables aleatorias, distribución lognormal, percentiles y
Teorema Central del Límite (Tema 7) para justificar, y limitar, el modelo.

## Fuentes consultadas (10-09-2026)

- Tesoro Público, resultado subasta Letras 12 meses 04-08-2026: <https://www.tesoro.es/deuda-publica/subastas/resultado-ultimas-subastas/letras-del-tesoro>
- CaixaBank, funcionamiento y calendario de Letras 2026: <https://www.caixabank.com/es/esfera/content/como-funcionan-letras-tesoro>
- Finect, reunión BCE 10-09-2026 e inflación: <https://www.finect.com/usuario/davidcarmona/articulos/reunion-bce-septiembre-2026-el-mercado-da-por-hecha-una-subida-de-tipos-al-250>
- Rankia, carteras indexadas MyInvestor 2026: <https://www.rankia.com/blog/fondos-inversion/6976506-carteras-indexadas-myinvestor-opiniones>
- MyInvestor, fondos indexados sin custodia: <https://myinvestor.es/inversion/fondos-indexados/>
- MyInvestor, Cartera Sostenible (nota de prensa): <https://myinvestor.es/notas-de-prensa/myinvestor-amplia-su-gama-de-inversiones-automatizadas-con-la-nueva-cartera-ahorro-y-la-cartera-mas-sostenible-del-mercado/>
- fernandezlauritsen.com, fondos indexados MyInvestor 2026 (comisiones carteras): <https://fernandezlauritsen.com/blog/es/fondos-indexados-myinvestor/>
- Raisin / Holded / idealista, tramos IRPF base del ahorro 2026: <https://www.raisin.com/es-es/tributacion/declaracion-de-la-renta/tramos-irpf/>

Las páginas de tesoro.es, rankia.com y finect.com no eran accesibles directamente desde el entorno de
trabajo; las cifras proceden de los extractos de búsqueda y deben verificarse en origen.

## Aviso

Material informativo y de organización personal. No es asesoramiento financiero ni fiscal regulado.
