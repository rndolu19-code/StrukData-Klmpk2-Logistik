import unittest
import sys
import os

# Menambahkan direktori src ke system path agar modul dapat diimpor dengan benar
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from paket import Paket
from antrean import Antrean

class TestAntreanLogistikLengkap(unittest.TestCase):
    def setUp(self):
        """Inisialisasi objek sebelum setiap test dijalankan."""
        self.antrean = Antrean()
        self.paket_1 = Paket("P001", "Budi", "Express")
        self.paket_2 = Paket("P002", "Ani", "Regular")
        self.paket_3 = Paket("P003", "Siti", "SameDay")

    def test_antrean_awal_kosong(self):
        """Memastikan antrean baru dalam kondisi kosong."""
        self.assertTrue(self.antrean.is_empty())
        self.assertEqual(self.antrean.ukuran(), 0)

    def test_enqueue_satu_paket(self):
        """Menguji penambahan satu paket ke dalam antrean."""
        self.antrean.enqueue(self.paket_1)
        self.assertFalse(self.antrean.is_empty())
        self.assertEqual(self.antrean.ukuran(), 1)

    def test_enqueue_banyak_paket(self):
        """Menguji penambahan beberapa paket secara berurutan."""
        self.antrean.enqueue(self.paket_1)
        self.antrean.enqueue(self.paket_2)
        self.antrean.enqueue(self.paket_3)
        self.assertEqual(self.antrean.ukuran(), 3)

    def test_dequeue_paket(self):
        """Menguji pengambilan/penghapusan paket dari antrean (FIFO)."""
        self.antrean.enqueue(self.paket_1)
        self.antrean.enqueue(self.paket_2)
        
        paket_keluar = self.antrean.dequeue()
        self.assertEqual(paket_keluar.id_paket, "P001")
        self.assertEqual(self.antrean.ukuran(), 1)

    def test_peek_antrean(self):
        """Menguji fungsi peek untuk melihat elemen terdepan tanpa menghapusnya."""
        self.antrean.enqueue(self.paket_1)
        self.antrean.enqueue(self.paket_2)
        
        front_paket = self.antrean.peek()
        self.assertEqual(front_paket.id_paket, "P001")
        self.assertEqual(self.antrean.ukuran(), 2)

    def test_antrean_kosong_dequeue(self):
        """Menguji penanganan ketika dequeue dilakukan pada antrean kosong."""
        with self.assertRaises(Exception):
            self.antrean.dequeue()

if __name__ == '__main__':
    unittest.main()
