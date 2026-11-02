import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from paket import Paket
from antrean import Antrean

class TestAntreanLogistik(unittest.TestCase):
    def setUp(self):
        self.antrean_regular = Antrean()
        self.paket_2 = Paket("P002", "Ani", "Regular")

    def test_tambah_paket(self):
        self.antrean_regular.enqueue(self.paket_2)
        self.assertEqual(self.antrean_regular.ukuran(), 1)

    def test_antrean_kosong(self):
        self.assertTrue(self.antrean_regular.is_empty())

if __name__ == '__main__':
    unittest.main()
