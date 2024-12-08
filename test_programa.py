import unittest
from programa import fatorial

class TestFatorial(unittest.TestCase):

    def test_fatorial_de_zero(self):
        self.assertEqual(fatorial(0), 1)

    def test_fatorial_de_um(self):
        self.assertEqual(fatorial(1), 1)

    def test_fatorial_de_numero_positivo(self):
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(6), 720)
        self.assertEqual(fatorial(10), 3628800)

    def test_fatorial_negativo(self):
        with self.assertRaises(ValueError):
            fatorial(-1)

if __name__ == '__main__':
    unittest.main()
