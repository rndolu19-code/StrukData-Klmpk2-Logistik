from src.manajer_logistik import ManajerLogistik


def tampilkan_menu():
    print("\n================================")
    print("       LOGISTIK EXPRESS")
    print("================================")
    print("1. Tambah Paket")
    print("2. Lihat Antrean Paket")
    print("3. Pengambilan Paket Kurir")
    print("4. Cari Paket")
    print("5. Riwayat Paket")
    print("6. Statistik Paket")
    print("0. Keluar")
    print("================================")


def tambah_paket(manajer):
    print("\n===== TAMBAH PAKET =====")
    id_paket = input("ID Paket: ")
    pengirim = input("Nama Pengirim: ")
    penerima = input("Nama Penerima: ")
    alamat = input("Alamat Tujuan: ")
    layanan = input("Jenis Layanan (Express/Regular): ")

    manajer.tambah_paket(id_paket, pengirim, penerima, alamat, layanan)


def main():
    manajer = ManajerLogistik()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                tambah_paket(manajer)
            elif pilihan == "2":
                manajer.lihat_antrean()
            elif pilihan == "3":
                manajer.proses_paket()
            elif pilihan == "4":
                manajer.cari_paket(input("Masukkan ID Paket: "))
            elif pilihan == "5":
                manajer.lihat_riwayat()
            elif pilihan == "6":
                manajer.statistik()
            elif pilihan == "0":
                print("Terima kasih telah menggunakan aplikasi.")
                break
            else:
                print("Pilihan tidak tersedia!")
        except (ValueError, RuntimeError) as error:
            print("Terjadi kesalahan:", error)


if __name__ == "__main__":
    main()
