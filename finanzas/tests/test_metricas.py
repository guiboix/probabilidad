import unittest
from datetime import date

from cartera import metricas


class TestMetricas(unittest.TestCase):
    def test_rentabilidad_simple(self):
        self.assertAlmostEqual(metricas.rentabilidad_simple(1000, 1100), 0.10)
        self.assertAlmostEqual(metricas.rentabilidad_simple(1000, 1100, aportaciones=100), 0.0)

    def test_twr_independiente_de_aportaciones(self):
        # Mercado sube 10 % y luego baja 10 %; aportación grande en medio no cambia el TWR
        valores = [1000, 1100, 990 + 0]  # sin aportación
        flujos = [0, 0, 0]
        base = metricas.twr(valores, flujos)
        valores2 = [1000, 1100, (1100 + 10_000) * 0.9]
        flujos2 = [0, 0, 10_000]
        self.assertAlmostEqual(metricas.twr(valores2, flujos2), base)
        self.assertAlmostEqual(base, 0.99 - 1)

    def test_xirr_un_flujo(self):
        flujos = [(date(2025, 1, 1), -1000.0), (date(2026, 1, 1), 1050.0)]
        self.assertAlmostEqual(metricas.xirr(flujos), 0.05, places=4)

    def test_xirr_varios_flujos(self):
        flujos = [(date(2024, 1, 1), -1000.0), (date(2025, 1, 1), -1000.0), (date(2026, 1, 1), 2200.0)]
        tir = metricas.xirr(flujos)
        self.assertAlmostEqual(metricas.xnpv(tir, flujos), 0.0, places=5)
        self.assertGreater(tir, 0.06)
        self.assertLess(tir, 0.07)

    def test_xirr_requiere_signos(self):
        with self.assertRaises(ValueError):
            metricas.xirr([(date(2025, 1, 1), -1.0), (date(2026, 1, 1), -1.0)])

    def test_volatilidad(self):
        r = [0.01, -0.01, 0.01, -0.01]
        vol = metricas.volatilidad_anualizada(r, 12)
        self.assertGreater(vol, 0.03)
        self.assertLess(vol, 0.05)

    def test_drawdown(self):
        self.assertAlmostEqual(metricas.drawdown_maximo([100, 120, 90, 110, 130]), -0.25)
        self.assertEqual(metricas.drawdown_maximo([100, 110, 120]), 0.0)

    def test_sharpe(self):
        self.assertAlmostEqual(metricas.ratio_sharpe(0.07, 0.10, 0.02), 0.5)


if __name__ == "__main__":
    unittest.main()
