import unittest

from cartera import simulacion


class TestSimulacion(unittest.TestCase):
    def test_determinista(self):
        self.assertAlmostEqual(simulacion.valor_determinista(1000, 0, 1, 0.05), 1050.0, places=6)
        self.assertAlmostEqual(simulacion.valor_determinista(0, 100, 1, 0.0), 1200.0)

    def test_sin_volatilidad_coincide_con_determinista(self):
        esc = simulacion.Escenario("cero vol", 0.05, 0.0)
        r = simulacion.simular(1000, 100, 3, esc, n_simulaciones=10)
        self.assertAlmostEqual(r.percentiles[50], simulacion.valor_determinista(1000, 100, 3, 0.05), places=0)
        self.assertEqual(r.prob_perder_dinero, 0.0)

    def test_percentiles_ordenados_y_reproducibles(self):
        esc = simulacion.Escenario("test", 0.05, 0.15)
        r1 = simulacion.simular(10_000, 200, 5, esc, n_simulaciones=500, semilla=1)
        r2 = simulacion.simular(10_000, 200, 5, esc, n_simulaciones=500, semilla=1)
        self.assertEqual(r1, r2)
        p = r1.percentiles
        self.assertLessEqual(p[5], p[25])
        self.assertLessEqual(p[25], p[50])
        self.assertLessEqual(p[50], p[95])
        self.assertAlmostEqual(r1.aportado_total, 10_000 + 200 * 60)

    def test_mediana_cerca_de_media_geometrica(self):
        # Con corrección de Itô, la mediana del valor sin aportaciones ≈ V0*(1+r)^T * exp(-sigma^2 T/2)
        esc = simulacion.Escenario("test", 0.06, 0.15)
        r = simulacion.simular(10_000, 0, 10, esc, n_simulaciones=20_000, semilla=3)
        esperado = 10_000 * (1.06 ** 10) * (2.718281828 ** (-(0.15 ** 2) * 10 / 2))
        self.assertLess(abs(r.percentiles[50] / esperado - 1), 0.03)


if __name__ == "__main__":
    unittest.main()
