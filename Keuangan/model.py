class Transaksi:
    """Mewakili satu transaksi keuangan."""

    def __init__(self, tanggal, jenis, keterangan, jumlah):
        self.tanggal = tanggal
        self.jenis = jenis
        self.keterangan = keterangan
        self.jumlah = jumlah

    def tampilkan_info(self):
        """Mengembalikan informasi transaksi dalam bentuk teks."""
        return (
            f"{self.tanggal} | {self.jenis} | "
            f"{self.keterangan} | Rp{self.jumlah:,}"
        )


class Keuangan:
    """Mengelola kumpulan transaksi keuangan."""

    def __init__(self, transaksi=None):
        self.transaksi = transaksi if transaksi is not None else []

    def tambah(self, transaksi):
        """Menambahkan objek transaksi ke dalam daftar."""
        self.transaksi.append(transaksi)

    def total_pemasukan(self):
        """Menghitung seluruh pemasukan."""
        return sum(
            data.jumlah for data in self.transaksi
            if data.jenis == "pemasukan"
        )

    def total_pengeluaran(self):
        """Menghitung seluruh pengeluaran."""
        return sum(
            data.jumlah for data in self.transaksi
            if data.jenis == "pengeluaran"
        )

    def saldo(self):
        """Menghitung saldo akhir."""
        return self.total_pemasukan() - self.total_pengeluaran()
