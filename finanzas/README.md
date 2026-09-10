# Gestión de cartera personal — Letras del Tesoro y fondos indexados éticos

Proyecto para gestionar una cartera de inversión particular en España con tres criterios declarados por
el usuario: **rentabilidad, ética y seguridad**. Incluye documentación de decisión y un paquete Python
(sin dependencias externas) para calcular rentabilidades, comparar productos, rebalancear y simular.

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
4. **No se puede pasar a una recomendación concreta** sin los datos de `docs/01_perfil_y_objetivos.md`
   (importe, horizonte, tolerancia a caídas, fondo de emergencia, definición de "ético").

## Estructura

```
finanzas/
├── README.md
├── docs/
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
│   └── README.md
├── src/cartera/                     # paquete Python (stdlib únicamente)
│   ├── fiscalidad.py  letras.py  metricas.py  rebalanceo.py  simulacion.py  carga.py  cli.py
└── tests/                           # 32 tests unittest
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
