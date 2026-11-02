# Laporan Ringkas: Logistik Express (Kelompok 2)

## 1. Latar Belakang
Depo logistik last-mile menerima paket Express/Same-Day dan Regular. Paket harus
dimuat ke kurir sesuai urutan kedatangan, dengan Express didahulukan.

## 2. Rancangan
- `Queue` (FIFO, linked list) sebagai dasar.
- `PriorityQueue` memakai dua `Queue` agar prioritas ganda tetap O(1).
- `ManajerLogistik` mengelola validasi, riwayat, dan statistik.

## 3. Kompleksitas
| Operasi | Waktu |
|---------|-------|
| enqueue / dequeue / front | O(1) |
| cari paket | O(n) |
| tampilkan antrean | O(n) |

## 4. Penanganan Kasus Batas
- Dequeue pada antrean kosong: underflow (`RuntimeError`).
- Enqueue saat depo penuh: overflow (`RuntimeError`).
- Setelah antrean menjadi kosong, `rear_node` direset ke `None`.
- Input kosong, ID duplikat, dan layanan tidak valid ditolak.

## 5. Keterbatasan
Express yang terus masuk dapat membuat Regular tidak pernah terambil (starvation).
Solusi lanjutan: aturan aging, misalnya setiap N Express diselingi satu Regular.

## 6. Skenario Pengujian
Lihat `tests/test_antrean.py` (FIFO, prioritas, underflow, overflow, validasi).
