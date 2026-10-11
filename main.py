from Keuangan.fileio import (
    buat_file_transaksi,
    baca_transaksi,
    tambah_transaksi,
    simpan_laporan
)
from Keuangan.processing import (
    hitung_pemasukan,
    hitung_pengeluaran,
    hitung_saldo,
    urutkan_transaksi
)
from Keuangan.validasi import validasi_transaksi, validasi_tanggal
# from Keuangan.model import Transaksi, Keuangan
from Keuangan.processing import hitung_total, buat_ringkasan


def tampilkan_menu():
    """Menampilkan menu utama program."""
    print("\n=== SISTEM KEUANGAN HARIAN ===")
    print("1. Lihat transaksi")
    print("2. Tambah transaksi")
    print("3. Lihat ringkasan keuangan")
    print("4. Simpan laporan")
    print("5. Urutkan transaksi")
    print("0. Keluar")


def tampilkan_transaksi(transaksi):
    """Menampilkan seluruh transaksi yang tersimpan."""
    if not transaksi:
        print("Belum ada transaksi.")
        return

    for data in transaksi:
        print(
            f"{data['tanggal']} | {data['jenis']} | "
            f"{data['keterangan']} | Rp{data['jumlah']:,}"
        )


def main():
    """Menjalankan menu dan menghubungkan fungsi program."""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            transaksi = baca_transaksi()
            tampilkan_transaksi(transaksi)

        elif pilihan == "2":
            try:
                tanggal = input("Tanggal (YYYY-MM-DD): ")
                tanggal = validasi_tanggal(tanggal)
                jenis = input("Jenis (pemasukan/pengeluaran): ")
                keterangan = input("Keterangan: ")
                jumlah = int(input("Jumlah uang: "))

                jenis, keterangan, jumlah = validasi_transaksi(
                    jenis=jenis,
                    keterangan=keterangan,
                    jumlah=jumlah
                )

                tambah_transaksi(tanggal, jenis, keterangan, jumlah)
                print("Transaksi berhasil ditambahkan.")

            except ValueError as error:
                print(f"Input tidak valid: {error}")

        elif pilihan == "3":
            transaksi = baca_transaksi()
            pemasukan = hitung_pemasukan(transaksi)
            pengeluaran = hitung_pengeluaran(transaksi)
            saldo = hitung_saldo(transaksi)

            total = hitung_total(pemasukan, pengeluaran)
            ringkasan = buat_ringkasan(
                pemasukan=pemasukan,
                pengeluaran=pengeluaran,
                saldo=saldo,
                total_transaksi=len(transaksi)
            )

            print(f"Total pemasukan: Rp{ringkasan['pemasukan']:,}")
            print(f"Total pengeluaran: Rp{ringkasan['pengeluaran']:,}")
            print(f"Saldo akhir: Rp{ringkasan['saldo']:,}")
            print(f"Jumlah transaksi: {ringkasan['total_transaksi']}")
            print(f"Total perputaran uang: Rp{total:,}")

        elif pilihan == "4":
            transaksi = baca_transaksi()
            pemasukan = hitung_pemasukan(transaksi)
            pengeluaran = hitung_pengeluaran(transaksi)
            saldo = hitung_saldo(transaksi)

            simpan_laporan(
                transaksi,
                pemasukan,
                pengeluaran,
                saldo,
                nama_file="laporan_keuangan.txt"
            )
            print("Laporan berhasil disimpan.")

        elif pilihan == "5":
            transaksi = baca_transaksi()
            hasil = urutkan_transaksi(transaksi)
            tampilkan_transaksi(hasil)

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak tersedia.")


if __name__ == "__main__":
    # tes_class()
    buat_file_transaksi()
    main()
