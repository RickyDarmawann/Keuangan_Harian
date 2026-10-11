import unittest
from Keuangan.model import Transaksi, Keuangan


class TestKeuangan(unittest.TestCase):
    """Pengujian untuk class Transaksi dan Keuangan."""

    def setUp(self):
        self.data1 = Transaksi(
            "2026-10-10", "pemasukan", "Uang saku", 100000
        )
        self.data2 = Transaksi(
            "2026-10-10", "pengeluaran", "Makan", 25000
        )
        self.data3 = Transaksi(
            "2026-10-10", "pengeluaran", "Transportasi", 15000
        )

        self.keuangan = Keuangan([
            self.data1, self.data2, self.data3
        ])

    def test_total_pemasukan(self):
        self.assertEqual(self.keuangan.total_pemasukan(), 100000)

    def test_total_pengeluaran(self):
        self.assertEqual(self.keuangan.total_pengeluaran(), 40000)

    def test_saldo(self):
        self.assertEqual(self.keuangan.saldo(), 60000)

    def test_tambah_transaksi(self):
        data4 = Transaksi(
            "2026-10-10", "pemasukan", "Bonus", 50000
        )
        self.keuangan.tambah(data4)

        self.assertEqual(self.keuangan.total_pemasukan(), 150000)

    def test_tampilkan_info(self):
        hasil = self.data1.tampilkan_info()

        self.assertIn("Uang saku", hasil)
        self.assertIn("100,000", hasil)


if __name__ == "__main__":
    unittest.main()
