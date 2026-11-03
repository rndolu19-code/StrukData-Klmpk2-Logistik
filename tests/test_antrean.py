import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.antrean import Queue
from src.manajer_logistik import ManajerLogistik
from src.paket import Paket
from src.priority_queue import PriorityQueue


def buat_paket(id_paket, layanan):
    return Paket(id_paket, "Andi", "Budi", "Kupang", layanan)


class TestQueue(unittest.TestCase):
    def test_fifo(self):
        q = Queue()
        q.enqueue(buat_paket("P001", "Regular"))
        q.enqueue(buat_paket("P002", "Regular"))
        self.assertEqual(q.dequeue().id_paket, "P001")
        self.assertEqual(q.dequeue().id_paket, "P002")
        self.assertTrue(q.is_empty())

    def test_underflow(self):
        with self.assertRaises(RuntimeError):
            Queue().dequeue()
        with self.assertRaises(RuntimeError):
            Queue().front()

    def test_overflow(self):
        q = Queue(kapasitas=2)
        q.enqueue(buat_paket("P001", "Regular"))
        q.enqueue(buat_paket("P002", "Regular"))
        self.assertTrue(q.is_full())
        with self.assertRaises(RuntimeError):
            q.enqueue(buat_paket("P003", "Regular"))

    def test_enqueue_setelah_kosong(self):
        q = Queue()
        q.enqueue(buat_paket("P001", "Regular"))
        q.dequeue()
        q.enqueue(buat_paket("P002", "Regular"))
        self.assertEqual(q.front().id_paket, "P002")
        self.assertEqual(q.get_size(), 1)

    def test_cari(self):
        q = Queue()
        q.enqueue(buat_paket("P001", "Regular"))
        self.assertIsNotNone(q.cari("P001"))
        self.assertIsNone(q.cari("XXX"))

    def test_kapasitas_tidak_valid(self):
        with self.assertRaises(ValueError):
            Queue(kapasitas=0)


class TestPriorityQueue(unittest.TestCase):
    def test_urutan_prioritas(self):
        pq = PriorityQueue()
        pq.enqueue(buat_paket("P001", "Regular"))
        pq.enqueue(buat_paket("P002", "Express"))
        pq.enqueue(buat_paket("P003", "Regular"))
        pq.enqueue(buat_paket("P004", "Express"))

        urutan = []
        while not pq.is_empty():
            urutan.append(pq.dequeue().id_paket)

        self.assertEqual(urutan, ["P002", "P004", "P001", "P003"])

    def test_underflow(self):
        with self.assertRaises(RuntimeError):
            PriorityQueue().dequeue()

    def test_overflow_total(self):
        pq = PriorityQueue(kapasitas=2)
        pq.enqueue(buat_paket("P001", "Regular"))
        pq.enqueue(buat_paket("P002", "Express"))
        with self.assertRaises(RuntimeError):
            pq.enqueue(buat_paket("P003", "Express"))

    def test_layanan_tidak_valid(self):
        with self.assertRaises(ValueError):
            PriorityQueue().enqueue(buat_paket("P001", "Kilat"))


class TestManajerLogistik(unittest.TestCase):
    def setUp(self):
        self.m = ManajerLogistik(kapasitas=2)

    def test_id_normalisasi_dan_duplikat(self):
        self.m.tambah_paket(" p001 ", "A", "B", "Kupang", "express")
        with self.assertRaises(ValueError):
            self.m.tambah_paket("P001", "A", "B", "Kupang", "Regular")

    def test_data_kosong(self):
        with self.assertRaises(ValueError):
            self.m.tambah_paket("P001", "  ", "B", "Kupang", "Regular")
        with self.assertRaises(ValueError):
            self.m.tambah_paket("", "A", "B", "Kupang", "Regular")

    def test_layanan_tidak_valid(self):
        with self.assertRaises(ValueError):
            self.m.tambah_paket("P001", "A", "B", "Kupang", "Kilat")

    def test_overflow_tidak_mencatat_id(self):
        self.m.tambah_paket("P001", "A", "B", "Kupang", "Regular")
        self.m.tambah_paket("P002", "A", "B", "Kupang", "Regular")
        with self.assertRaises(RuntimeError):
            self.m.tambah_paket("P003", "A", "B", "Kupang", "Regular")
        self.assertNotIn("P003", self.m.daftar_id)

    def test_proses_paket_masuk_riwayat(self):
        self.m.tambah_paket("P001", "A", "B", "Kupang", "Regular")
        self.m.tambah_paket("P002", "A", "B", "Kupang", "Express")
        self.m.proses_paket()
        self.assertEqual(self.m.riwayat[0].id_paket, "P002")
        self.assertEqual(self.m.riwayat[0].status, Paket.STATUS_DIAMBIL)

    def test_proses_paket_kosong(self):
        with self.assertRaises(RuntimeError):
            self.m.proses_paket()


if __name__ == "__main__":
    unittest.main()
