from Keuangan.model import Transaksi, Keuangan


def tes_total_pemasukan():
    data = Transaksi("2026-10-10", "pemasukan", "Uang saku", 100000)
    keuangan = Keuangan([data])

    assert keuangan.total_pemasukan() == 100000
    print("Tes total pemasukan berhasil.")


def tes_total_pengeluaran():
    data = Transaksi("2026-10-10", "pengeluaran", "Makan", 25000)
    keuangan = Keuangan([data])

    assert keuangan.total_pengeluaran() == 25000
    print("Tes total pengeluaran berhasil.")


def tes_saldo():
    data1 = Transaksi("2026-10-10", "pemasukan", "Uang saku", 100000)
    data2 = Transaksi("2026-10-10", "pengeluaran", "Makan", 25000)
    keuangan = Keuangan([data1, data2])

    assert keuangan.saldo() == 75000
    print("Tes saldo berhasil.")


if __name__ == "__main__":
    tes_total_pemasukan()
    tes_total_pengeluaran()
    tes_saldo()
    print("Semua tes lokal selesai.")
