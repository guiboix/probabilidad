import unittest

from cartera import bonos


class TestBonos(unittest.TestCase):
    def test_bono_a_la_par(self):
        # cupón igual a la TIR -> precio 1000
        self.assertAlmostEqual(bonos.precio_desde_tir(0.03, 0.03, 3), 1000.0, places=6)
        self.assertAlmostEqual(bonos.tir_desde_precio(1000.0, 0.03, 3), 0.03, places=6)

    def test_ida_y_vuelta(self):
        p = bonos.precio_desde_tir(0.02871, 0.025, 3)
        self.assertLess(p, 1000.0)  # cupón < TIR -> bajo la par
        self.assertAlmostEqual(bonos.tir_desde_precio(p, 0.025, 3), 0.02871, places=6)

    def test_duracion(self):
        # bono cupón cero a 3 años: duración de Macaulay 3, modificada 3/(1+tir)
        d = bonos.duracion_modificada(0.03, 0.0, 3)
        self.assertAlmostEqual(d, 3 / 1.03, places=6)
        self.assertLess(bonos.duracion_modificada(0.03, 0.05, 5), 5.0)

    def test_analisis(self):
        r = bonos.analizar(1000.0, 0.03, 3, nominal_total=8000)
        self.assertAlmostEqual(r.cupon_anual_euros, 240.0)
        self.assertAlmostEqual(r.cupon_neto_anual_euros, 240.0 * 0.81, places=2)
        self.assertAlmostEqual(r.ganancia_total_bruta, 720.0)
        self.assertAlmostEqual(r.ganancia_total_neta, 720.0 * 0.81, places=2)

    def test_anyos_invalidos(self):
        with self.assertRaises(ValueError):
            bonos.flujos(0.03, 0.2)


if __name__ == "__main__":
    unittest.main()
