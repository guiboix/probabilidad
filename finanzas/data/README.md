# Datos de la cartera

Los ficheros `cartera.csv`, `movimientos.csv` y `letras.csv` **no están en el repositorio**
(están en `.gitignore`) porque contienen datos personales. Copia cada plantilla y rellénala:

```bash
cp plantilla_cartera.csv cartera.csv
cp plantilla_movimientos.csv movimientos.csv
cp plantilla_letras.csv letras.csv
```

| Fichero | Columnas | Notas |
|---|---|---|
| `cartera.csv` | `activo,clase,isin,valor,peso_objetivo` | `valor` en euros a fecha de hoy; `peso_objetivo` en tanto por uno y deben sumar 1. |
| `movimientos.csv` | `fecha,activo,tipo,importe` | `tipo` ∈ `aportacion`, `retirada`, `valoracion`. La última `valoracion` con activo `TOTAL` se usa para la TIR. |
| `letras.csv` | `fecha_compra,fecha_vencimiento,nominal,precio_compra` | `precio_compra` por cada 1.000 € de nominal, como lo publica el Tesoro. |
| `supuestos.json` | ver fichero | Parámetros de simulación, bandas de rebalanceo y referencias de mercado con su fuente. |

`plantilla_letras.csv` refleja la estructura declarada por el usuario (dos Letras a 12 meses de 8.000 € nominal con
vencimientos separados 6 meses). Las fechas y el precio de la primera (974,50) son **supuestos** hasta que el usuario
los confirme con el resguardo del Banco de España; el de la segunda es el precio medio de la subasta del 04-08-2026.

Los demás datos de ejemplo de las plantillas son ilustrativos, salvo el precio 973,78 (subasta de
Letras a 12 meses del 4 de agosto de 2026), que se cita como referencia y debe verificarse en tesoro.es.
