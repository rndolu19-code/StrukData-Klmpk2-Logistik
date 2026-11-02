from src.node import Node


class Queue:
    """Antrean FIFO kustom berbasis linked list.

    Semua operasi utama (enqueue, dequeue, front) berjalan O(1)
    karena menyimpan penunjuk ke simpul depan dan belakang.
    """

    def __init__(self, kapasitas=None):
        if kapasitas is not None and kapasitas <= 0:
            raise ValueError("Kapasitas harus lebih dari 0!")

        self.front_node = None
        self.rear_node = None
        self.size = 0
        self.kapasitas = kapasitas

    def is_empty(self):
        return self.front_node is None

    def is_full(self):
        return self.kapasitas is not None and self.size >= self.kapasitas

    def get_size(self):
        return self.size

    def enqueue(self, data):
        """Menambah data di belakang antrean. Overflow jika sudah penuh."""
        if self.is_full():
            raise RuntimeError("Antrean penuh (overflow)!")

        new_node = Node(data)

        if self.is_empty():
            self.front_node = new_node
        else:
            self.rear_node.next = new_node

        self.rear_node = new_node
        self.size += 1

    def dequeue(self):
        """Mengeluarkan data dari depan antrean. Underflow jika kosong."""
        if self.is_empty():
            raise RuntimeError("Antrean kosong (underflow)!")

        removed_node = self.front_node
        self.front_node = removed_node.next

        if self.front_node is None:
            self.rear_node = None

        self.size -= 1
        return removed_node.data

    def front(self):
        """Melihat data paling depan tanpa mengeluarkannya."""
        if self.is_empty():
            raise RuntimeError("Antrean kosong (underflow)!")

        return self.front_node.data

    def __iter__(self):
        """Menelusuri data dari depan ke belakang tanpa mengubah antrean."""
        current = self.front_node
        while current is not None:
            yield current.data
            current = current.next

    def cari(self, id_paket):
        """Mencari paket berdasarkan ID. Mengembalikan None jika tidak ada."""
        for paket in self:
            if paket.id_paket == id_paket:
                return paket
        return None

    def display(self):
        if self.is_empty():
            print("Antrean masih kosong.")
            return

        for nomor, paket in enumerate(self, start=1):
            print(f"{nomor} - {paket.id_paket} | {paket.jenis_layanan}")
