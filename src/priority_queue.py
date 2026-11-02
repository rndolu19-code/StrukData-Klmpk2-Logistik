from src.antrean import Queue


class PriorityQueue:
    """Antrean prioritas ganda: Express didahulukan dibanding Regular.

    Dua antrean FIFO dipakai secara terpisah. Hasilnya setara dengan
    menyisipkan paket Express tepat setelah Express terakhir dan sebelum
    Regular pertama, tetapi enqueue tetap O(1) tanpa penelusuran. Urutan
    antar sesama Express (dan sesama Regular) tetap first-come, first-served.
    """

    EXPRESS = "Express"
    REGULAR = "Regular"

    def __init__(self, kapasitas=None):
        if kapasitas is not None and kapasitas <= 0:
            raise ValueError("Kapasitas harus lebih dari 0!")

        self.express_queue = Queue()
        self.regular_queue = Queue()
        self.kapasitas = kapasitas  # kapasitas total depo

    def is_empty(self):
        return self.express_queue.is_empty() and self.regular_queue.is_empty()

    def is_full(self):
        return self.kapasitas is not None and self.get_total_paket() >= self.kapasitas

    def get_total_paket(self):
        return self.express_queue.get_size() + self.regular_queue.get_size()

    def enqueue(self, paket):
        if paket.jenis_layanan not in (self.EXPRESS, self.REGULAR):
            raise ValueError("Jenis layanan tidak valid!")

        if self.is_full():
            raise RuntimeError("Depo penuh (overflow)! Paket tidak dapat ditambahkan.")

        if paket.jenis_layanan == self.EXPRESS:
            self.express_queue.enqueue(paket)
        else:
            self.regular_queue.enqueue(paket)

    def dequeue(self):
        if not self.express_queue.is_empty():
            return self.express_queue.dequeue()

        if not self.regular_queue.is_empty():
            return self.regular_queue.dequeue()

        raise RuntimeError("Tidak ada paket dalam antrean (underflow)!")

    def peek(self):
        """Paket yang akan diambil kurir berikutnya (tanpa mengeluarkan)."""
        if not self.express_queue.is_empty():
            return self.express_queue.front()

        if not self.regular_queue.is_empty():
            return self.regular_queue.front()

        raise RuntimeError("Tidak ada paket dalam antrean (underflow)!")

    def cari(self, id_paket):
        paket = self.express_queue.cari(id_paket)
        if paket is None:
            paket = self.regular_queue.cari(id_paket)
        return paket

    def display(self):
        print("\n===== ANTREAN EXPRESS =====")
        self.express_queue.display()

        print("\n===== ANTREAN REGULAR =====")
        self.regular_queue.display()
