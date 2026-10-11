from datetime import datetime


def validasi_transaksi(jenis, keterangan, jumlah):
    """Memeriksa apakah data transaksi sudah sesuai."""

    jenis = jenis.lower().strip()
    keterangan = keterangan.strip()

    if jenis not in ["pemasukan", "pengeluaran"]:
        raise ValueError("Jenis harus pemasukan atau pengeluaran.")

    if not keterangan:
        raise ValueError("Keterangan tidak boleh kosong.")

    if jumlah <= 0:
        raise ValueError("Jumlah transaksi harus lebih dari nol.")

    return jenis, keterangan, jumlah

def validasi_tanggal(tanggal):
    """Memeriksa apakah tanggal menggunakan format YYYY-MM-DD."""
    try:
        datetime.strptime(tanggal, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Format tanggal harus YYYY-MM-DD.")

    return tanggal