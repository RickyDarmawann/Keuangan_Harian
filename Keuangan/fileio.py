# Membuat file transaksi jika file belum tersedia
def buat_file_transaksi(nama_file="transaksi.txt"):
    try:
        with open(nama_file, "x", encoding="utf-8") as file:
            file.write("tanggal,jenis,keterangan,jumlah\n")
    except FileExistsError:
        pass


# Membaca transaksi dari file dan melewati baris yang tidak valid
def baca_transaksi(nama_file="transaksi.txt"):
    transaksi = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if not baris or baris.startswith("tanggal,"):
                    continue

                try:
                    tanggal, jenis, keterangan, jumlah = baris.split(",", 3)

                    data = {
                        "tanggal": tanggal,
                        "jenis": jenis.strip().lower(),
                        "keterangan": keterangan.strip(),
                        "jumlah": int(jumlah)
                    }

                    if data["jenis"] not in ["pemasukan", "pengeluaran"]:
                        continue

                    if not data["keterangan"] or data["jumlah"] <= 0:
                        continue

                    transaksi.append(data)

                except ValueError:
                    continue

    except FileNotFoundError:
        print("File transaksi tidak ditemukan.")

    return transaksi


# Menambahkan transaksi baru ke dalam file
def tambah_transaksi(tanggal, jenis, keterangan, jumlah,
                     nama_file="transaksi.txt"):
    """Menambahkan transaksi baru ke file."""
    with open(nama_file, "a", encoding="utf-8") as file:
        file.write(f"{tanggal},{jenis},{keterangan},{jumlah}\n")

# Menyimpan laporan keuangan dengan mengganti isi laporan sebelumnya
def simpan_laporan(transaksi, total_pemasukan, total_pengeluaran,
                   saldo, nama_file="laporan_keuangan.txt"):
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("LAPORAN KEUANGAN HARIAN\n")
        file.write("=======================\n")
        file.write(f"Total pemasukan: Rp{total_pemasukan:,}\n")
        file.write(f"Total pengeluaran: Rp{total_pengeluaran:,}\n")
        file.write(f"Saldo akhir: Rp{saldo:,}\n\n")
        file.write("DAFTAR TRANSAKSI\n")

        for data in transaksi:
            file.write(
                f"{data['tanggal']} | {data['jenis']} | "
                f"{data['keterangan']} | Rp{data['jumlah']:,}\n"
            )
