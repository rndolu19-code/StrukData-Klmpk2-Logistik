from src.paket import Paket
from src.priority_queue import PriorityQueue


class ManajerLogistik:
    """Kelas manajer utama yang mengatur alur kerja depo logistik."""

    KAPASITAS_DEPO = 50

    def __init__(self, kapasitas=KAPASITAS_DEPO):
        self.antrean = PriorityQueue(kapasitas)
        self.riwayat = []
        self.daftar_id = set()

    def tambah_paket(self, id_paket, nama_pengirim, nama_penerima, alamat, layanan):
        id_paket = id_paket.strip().upper()
        nama_pengirim = nama_pengirim.strip()
        nama_penerima = nama_penerima.strip()
        alamat = alamat.strip()
        layanan = layanan.strip().title()

        if not id_paket:
            raise ValueError("ID paket tidak boleh kosong!")

        if not (nama_pengirim and nama_penerima and alamat):
            raise ValueError("Data paket tidak boleh kosong!")

        if id_paket in self.daftar_id:
            raise ValueError("ID paket sudah digunakan!")

        if layanan not in (PriorityQueue.EXPRESS, PriorityQueue.REGULAR):
            raise ValueError("Jenis layanan tidak valid! Pilih Express atau Regular.")

        paket = Paket(id_paket, nama_pengirim, nama_penerima, alamat, layanan)

        # Jika overflow, enqueue melempar error sebelum ID dicatat.
        self.antrean.enqueue(paket)
        self.daftar_id.add(id_paket)

        print("Paket berhasil ditambahkan!")

    def lihat_antrean(self):
        self.antrean.display()

    def proses_paket(self):
        """Kurir mengambil satu paket sesuai urutan prioritas."""
        paket = self.antrean.dequeue()
        paket.tandai_diambil()
        self.riwayat.append(paket)

        print("\nPaket berhasil dimuat ke kurir!")
        paket.tampilkan_info()

    def cari_paket(self, id_paket):
        id_paket = id_paket.strip().upper()

        paket = self.antrean.cari(id_paket)
        if paket is not None:
            print("Paket ditemukan di antrean!")
            paket.tampilkan_info()
            return

        for paket in self.riwayat:
            if paket.id_paket == id_paket:
                print("Paket ditemukan dalam riwayat!")
                paket.tampilkan_info()
                return

        print("Paket tidak ditemukan.")

    def lihat_riwayat(self):
        if not self.riwayat:
            print("Belum ada paket yang diambil.")
            return

        for paket in self.riwayat:
            paket.tampilkan_info()

    def statistik(self):
        print("\n===== STATISTIK PAKET =====")
        print("Express menunggu :", self.antrean.express_queue.get_size())
        print("Regular menunggu :", self.antrean.regular_queue.get_size())
        print("Total menunggu   :", self.antrean.get_total_paket())
        print("Kapasitas depo   :", self.antrean.kapasitas)
        print("Sudah diambil    :", len(self.riwayat))
