import unittest
from datetime import date

from cartera import letras


class TestLetras(unittest.TestCase):
    def test_subasta_agosto_2026(self):
        # Subasta 12 meses 4/8/2026: precio medio 973,78 -> tipo medio publicado 2,663 %.
        # Liquidación 7/8/2026, vencimiento 6/8/2027 = 364 días.
        tipo = letras.tipo_desde_precio(973.78, 364)
        self.assertAlmostEqual(tipo, 0.02663, places=4)

    def test_ida_y_vuelta_precio_tipo(self):
        p = letras.precio_desde_tipo(0.03, 182)
        self.assertAlmostEqual(letras.tipo_desde_precio(p, 182), 0.03, places=10)

    def test_tae_mayor_que_tipo_simple_360(self):
        # A 364 días la TAE (base 365, compuesta) es ligeramente distinta del simple ACT/360
        self.assertNotAlmostEqual(letras.rentabilidad_efectiva(973.78, 364), letras.tipo_desde_precio(973.78, 364), places=4)

    def test_analisis_neto(self):
        r = letras.analizar(973.78, 364, nominal_total=10_000)
        self.assertAlmostEqual(r.rendimiento_bruto, 262.2, places=1)
        self.assertAlmostEqual(r.impuesto, round(262.2 * 0.19, 2), places=1)
        self.assertLess(r.tae_neta, r.tae_bruta)
        self.assertIsNone(r.tae_real_neta)

    def test_real_negativa_con_inflacion_alta(self):
        r = letras.analizar(973.78, 364, inflacion=0.033)
        self.assertLess(r.tae_real_neta, 0)

    def test_impuesto_marginal_con_otras_rentas(self):
        sin = letras.analizar(973.78, 364, nominal_total=10_000)
        con = letras.analizar(973.78, 364, nominal_total=10_000, otras_rentas_ahorro=6_000)
        self.assertGreater(con.impuesto, sin.impuesto)

    def test_dataclass_letra(self):
        l = letras.Letra(date(2026, 8, 7), date(2027, 8, 6), 10_000, 973.78)
        self.assertEqual(l.dias, 364)
        self.assertAlmostEqual(l.importe_pagado, 9737.8)
        self.assertAlmostEqual(l.rendimiento_bruto, 262.2)

    def test_dias_invalidos(self):
        with self.assertRaises(ValueError):
            letras.tipo_desde_precio(990, 0)


if __name__ == "__main__":
    unittest.main()
