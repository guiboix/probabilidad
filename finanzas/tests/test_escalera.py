import unittest
from datetime import date

from cartera import escalera
from cartera.letras import Letra

HOY = date(2026, 9, 10)
L1 = Letra(date(2026, 2, 13), date(2027, 2, 12), 8000, 974.50)   # fechas/precio ilustrativos
L2 = Letra(date(2026, 8, 7), date(2027, 8, 6), 8000, 973.78)
VENCIDA = Letra(date(2025, 8, 8), date(2026, 8, 7), 8000, 978.00)


class TestEscalera(unittest.TestCase):
    def test_calendario_ordenado_y_sin_vencidas(self):
        cal = escalera.calendario([L2, VENCIDA, L1], HOY)
        self.assertEqual([v.fecha for v in cal], [L1.fecha_vencimiento, L2.fecha_vencimiento])
        self.assertEqual(cal[0].dias_restantes, (L1.fecha_vencimiento - HOY).days)
        self.assertAlmostEqual(cal[1].tipo_anual_bruto, 0.02663, places=4)

    def test_plan_todo_a_fondos(self):
        plan = escalera.plan_transicion([L1, L2], HOY, peso_objetivo_letras=0.0)
        self.assertEqual([(r, m) for _, _, r, m in plan], [(0.0, 8000.0), (0.0, 8000.0)])

    def test_plan_mitad(self):
        plan = escalera.plan_transicion([L1, L2], HOY, peso_objetivo_letras=0.5)
        # objetivo 8000 en letras: al vencer L1 quedan 8000 vivas (L2) -> no renovar L1
        self.assertEqual(plan[0][2:], (0.0, 8000.0))
        # al vencer L2 no queda nada -> renovar 8000
        self.assertEqual(plan[1][2:], (8000.0, 0.0))

    def test_reserva_minima_manda(self):
        plan = escalera.plan_transicion([L1, L2], HOY, peso_objetivo_letras=0.0, reserva_minima=5000)
        self.assertEqual(plan[0][2:], (0.0, 8000.0))
        self.assertEqual(plan[1][2:], (5000.0, 3000.0))

    def test_peso_invalido(self):
        with self.assertRaises(ValueError):
            escalera.plan_transicion([L1], HOY, 1.5)


if __name__ == "__main__":
    unittest.main()
