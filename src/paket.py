class Paket:
    """Representasi satu paket di depo logistik."""

    STATUS_MENUNGGU = "Menunggu"
    STATUS_DIAMBIL = "Sudah Diambil Kurir"

    def __init__(
        self,
        id_paket,
        nama_pengirim,
        nama_penerima,
        alamat_tujuan,
        jenis_layanan,
    ):
        self.id_paket = id_paket
        self.nama_pengirim = nama_pengirim
        self.nama_penerima = nama_penerima
        self.alamat_tujuan = alamat_tujuan
        self.jenis_layanan = jenis_layanan
        self.status = self.STATUS_MENUNGGU

    def tandai_diambil(self):
        self.status = self.STATUS_DIAMBIL

    def tampilkan_info(self):
        print("--------------------------------")
        print("ID Paket       :", self.id_paket)
        print("Nama Pengirim  :", self.nama_pengirim)
        print("Nama Penerima  :", self.nama_penerima)
        print("Alamat Tujuan  :", self.alamat_tujuan)
        print("Jenis Layanan  :", self.jenis_layanan)
        print("Status         :", self.status)
        print("--------------------------------")
