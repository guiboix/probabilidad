import tempfile
import unittest
from datetime import date
from pathlib import Path

from cartera import carga


class TestCarga(unittest.TestCase):
    def test_leer_vl_ordena_y_agrupa(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "vl.csv"
            p.write_text("fecha,activo,valor_liquidativo\n2026-09-18,F,9.9\n2026-09-11,F,10\n2026-09-11,G,1\n", encoding="utf-8")
            s = carga.leer_vl(p)
            self.assertEqual(set(s), {"F", "G"})
            self.assertEqual(s["F"][0], (date(2026, 9, 11), 10.0))
            self.assertEqual(s["F"][1][1], 9.9)


if __name__ == "__main__":
    unittest.main()
