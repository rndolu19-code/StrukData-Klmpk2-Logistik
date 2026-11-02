# Strukdat-2-LogistikExpress

Sistem Sorting & Pemenuhan Pesanan Kurir Last-Mile (Depo Logistik).
Tugas Proyek Struktur Data & Algoritma, Kelompok 2: Logistik & E-Commerce Fulfillment
(fokus **Queue & Priority Queue**).

## Cara Menjalankan
Membutuhkan Python 3.8 atau lebih baru. Tidak ada pustaka eksternal.

```bash
git clone <url-repository>
cd Strukdat-2-LogistikExpress
python main.py
```

Menjalankan pengujian:

```bash
python -m unittest discover -s tests -v
```

## Fitur
| Menu | Fungsi                                                  |
|------|---------------------------------------------------------|
| 1    | Tambah paket (Express / Regular)                        |
| 2    | Lihat antrean Express dan Regular                       |
| 3    | Pengambilan paket oleh kurir (dequeue sesuai prioritas) |
| 4    | Cari paket (di antrean dan riwayat)                     |
| 5    | Riwayat paket yang sudah diambil                        |
| 6    | Statistik paket dan kapasitas depo                      |

## Struktur Folder
```
Strukdat-2-LogistikExpress/
├── main.py                  # CLI
├── src/
│   ├── node.py              # Node linked list
│   ├── paket.py             # Entitas Paket
│   ├── antrean.py           # Queue FIFO kustom
│   ├── priority_queue.py    # Priority Queue (Express > Regular)
│   └── manajer_logistik.py  # Kelas manajer utama
├── tests/test_antrean.py    # Unit test
└── docs/laporan.md          # Laporan ringkas
```

## Struktur Data yang Digunakan
- **Node**: simpul linked list (`data`, `next`).
- **Queue (FIFO)**: linked list dengan penunjuk `front_node` dan `rear_node`.
  `enqueue` dan `dequeue` berjalan O(1). Tidak memakai `queue.Queue` maupun `list.pop(0)`.
- **PriorityQueue**: dua `Queue`, yaitu Express dan Regular. `dequeue` selalu mengambil
  dari Express lebih dulu, baru Regular. Sesama Express (dan sesama Regular) tetap
  first-come, first-served. Hasilnya setara dengan menyisipkan Express di depan antrean
  tanpa merusak urutan sesamanya, namun tanpa penelusuran (O(1)).
- **ManajerLogistik**: validasi input, pencatatan ID unik, riwayat, dan statistik.

## Penanganan Kesalahan
- **Underflow**: mengambil paket saat antrean kosong.
- **Overflow**: menambah paket saat depo penuh (kapasitas default 50).
- Validasi: ID kosong/duplikat, data kosong, jenis layanan tidak valid.

## Pembagian Tugas
| Anggota                            | Tugas                                 |
|------------------------------------|---------------------------------------|
|  Immanuel Reiskian Pa Ndolu        | `priority_queue.py`, `paket.py`       |
|  Carly Dessaputra Nenabu           | `manajer_logistik.py`                 |
|  Reinatalie Stefani Filia Palus    | `antrean.py`, `node.py`               |
|  Anggra Christian Dethan           |  README                               |
|  Petrin Clarita Lado               |  unit test                            |
|  Martha Angelika Jelu Gega         | `main.py`, `antrean.py`               |

## Alur Git
Setiap anggota bekerja di branch fitur (misal `feat/queue`), membuka Pull Request ke
`main`, dan memakai pesan commit konvensional (`feat:`, `fix:`, `docs:`, `test:`).
