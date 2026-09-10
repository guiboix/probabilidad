import unittest

from cartera import rebalanceo


class TestRebalanceo(unittest.TestCase):
    pos = {"RV": 7000.0, "RF": 3000.0}
    obj = {"RV": 0.6, "RF": 0.4}

    def test_pesos(self):
        p = rebalanceo.pesos_actuales(self.pos)
        self.assertAlmostEqual(p["RV"], 0.7)

    def test_desviaciones(self):
        d = {x.activo: x for x in rebalanceo.desviaciones(self.pos, self.obj)}
        self.assertAlmostEqual(d["RV"].diferencia, 0.10)
        self.assertTrue(d["RV"].fuera_de_banda(0.05, 0.25))
        self.assertFalse(rebalanceo.desviaciones({"RV": 6200.0, "RF": 3800.0}, self.obj)[1].fuera_de_banda(0.05, 0.25))

    def test_objetivo_debe_sumar_uno(self):
        with self.assertRaises(ValueError):
            rebalanceo.desviaciones(self.pos, {"RV": 0.6, "RF": 0.3})

    def test_aportacion_va_al_infraponderado(self):
        ordenes = rebalanceo.ordenes_con_aportacion(self.pos, self.obj, 1000.0)
        self.assertEqual(set(ordenes), {"RF"})
        self.assertAlmostEqual(ordenes["RF"], 1000.0)

    def test_aportacion_grande_reparte(self):
        ordenes = rebalanceo.ordenes_con_aportacion(self.pos, self.obj, 10_000.0)
        # total futuro 20000: RV objetivo 12000 (déficit 5000), RF objetivo 8000 (déficit 5000)
        self.assertAlmostEqual(ordenes["RV"], 5000.0)
        self.assertAlmostEqual(ordenes["RF"], 5000.0)
        self.assertAlmostEqual(sum(ordenes.values()), 10_000.0)

    def test_ordenes_completas(self):
        o = rebalanceo.ordenes_completas(self.pos, self.obj)
        self.assertAlmostEqual(o["RV"], -1000.0)
        self.assertAlmostEqual(o["RF"], 1000.0)


if __name__ == "__main__":
    unittest.main()
