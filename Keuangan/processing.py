# Menghitung total pemasukan dari daftar transaksi
def hitung_pemasukan(transaksi):
    total = 0

    for data in transaksi:
        if data["jenis"] == "pemasukan":
            total += data["jumlah"]

    return total


# Menghitung total pengeluaran dari daftar transaksi
def hitung_pengeluaran(transaksi):
    total = 0

    for data in transaksi:
        if data["jenis"] == "pengeluaran":
            total += data["jumlah"]

    return total


# Menghitung saldo dari total pemasukan dikurangi pengeluaran
def hitung_saldo(transaksi):
    pemasukan = hitung_pemasukan(transaksi)
    pengeluaran = hitung_pengeluaran(transaksi)

    return pemasukan - pengeluaran


# Mengurutkan transaksi berdasarkan jumlah dari terkecil ke terbesar
def urutkan_transaksi(transaksi):
    return sorted(transaksi, key=lambda data: data["jumlah"])


# Menghitung total dari beberapa nominal yang diberikan
def hitung_total(*args):
    """Menjumlahkan beberapa nilai transaksi."""
    return sum(args)


# Membuat ringkasan dengan informasi tambahan
def buat_ringkasan(**kwargs):
    """Mengembalikan informasi ringkasan dalam bentuk dictionary."""
    return kwargs
