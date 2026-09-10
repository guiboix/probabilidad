import unittest

from cartera.fiscalidad import cuota_ahorro, tipo_marginal


class TestFiscalidad(unittest.TestCase):
    def test_primer_tramo(self):
        self.assertAlmostEqual(cuota_ahorro(1000).cuota, 190.0)

    def test_frontera_tramo(self):
        self.assertAlmostEqual(cuota_ahorro(6000).cuota, 1140.0)

    def test_segundo_tramo(self):
        # 6000*0.19 + 4000*0.21 = 1140 + 840
        self.assertAlmostEqual(cuota_ahorro(10_000).cuota, 1980.0)

    def test_tramo_superior(self):
        # 1140 + 44000*0.21 + 150000*0.23 + 100000*0.27 + 100000*0.30
        esperado = 1140 + 9240 + 34500 + 27000 + 30000
        self.assertAlmostEqual(cuota_ahorro(400_000).cuota, esperado)

    def test_perdidas_sin_cuota(self):
        r = cuota_ahorro(-500)
        self.assertEqual(r.cuota, 0.0)
        self.assertEqual(r.tipo_efectivo, 0.0)

    def test_marginal(self):
        self.assertEqual(tipo_marginal(0), 0.19)
        self.assertEqual(tipo_marginal(6000), 0.21)
        self.assertEqual(tipo_marginal(1_000_000), 0.30)


if __name__ == "__main__":
    unittest.main()
