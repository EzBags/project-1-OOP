# Kelompok 1 PBO PROJEK UAS
# Produk Classes
# Muhammad Irfan Maulana_K3524059


from interfaces import ProdukRoti, ProdukDenganTopping, StrategiProduksi
from typing import List


class RotiManis(ProdukRoti):
    def get_kategori(self) -> str:
        return "Roti Manis"

    def get_waktu_produksi(self) -> int:
        return 180  # 3 jam

    def get_tingkat_kesulitan(self) -> str:
        return "Sedang"

    def get_suhu_pemanggangan(self) -> int:
        return 180  # Celsius

    def perlu_pengembangan(self) -> bool:
        return True


class Croissant(ProdukRoti):
    def get_kategori(self) -> str:
        return "Pastry"

    def get_waktu_produksi(self) -> int:
        return 240  # 4 jam (termasuk laminating)

    def get_tingkat_kesulitan(self) -> str:
        return "Sulit"

    def get_suhu_pemanggangan(self) -> int:
        return 200  # Celsius

    def perlu_pengembangan(self) -> bool:
        return True


class KueKering(ProdukDenganTopping):
    def get_kategori(self) -> str:
        return "Kue Kering"

    def get_waktu_produksi(self) -> int:
        return 90  # 1.5 jam

    def get_tingkat_kesulitan(self) -> str:
        return "Mudah"

    def get_suhu_pemanggangan(self) -> int:
        return 160  # Celsius

    def perlu_pengembangan(self) -> bool:
        return False

    def get_jenis_topping(self) -> List[str]:
        return ["Gula Halus", "Coklat Chip", "Kacang"]

    def aplikasi_topping(self) -> str:
        return f"Aplikasi topping {', '.join(self.get_jenis_topping())} pada {self.nama_produk}"


class ButterCookies(KueKering):
    def get_jenis_topping(self) -> List[str]:
        return ["Gula Halus", "Almond Slice"]

    def aplikasi_topping(self) -> str:
        return f"Aplikasi topping khusus butter cookies: {', '.join(self.get_jenis_topping())}"


class Muffin(ProdukDenganTopping):
    def get_kategori(self) -> str:
        return "Muffin"

    def get_waktu_produksi(self) -> int:
        return 60  # 1 jam

    def get_tingkat_kesulitan(self) -> str:
        return "Mudah"

    def get_suhu_pemanggangan(self) -> int:
        return 175  # Celsius

    def perlu_pengembangan(self) -> bool:
        return True

    def get_jenis_topping(self) -> List[str]:
        return ["Blueberry", "Chocolate Chip", "Streusel"]

    def aplikasi_topping(self) -> str:
        return f"Aplikasi topping muffin: {', '.join(self.get_jenis_topping())}"


# Implementasi Strategy Pattern untuk Produksi
class ProduksiStandar(StrategiProduksi):
    def execute_produksi(self, produk) -> str:
        return f"Menjalankan produksi standar untuk {produk.nama_produk}"


class ProduksiEkspres(StrategiProduksi):
    def execute_produksi(self, produk) -> str:
        return f"Menjalankan produksi ekspres untuk {produk.nama_produk} (waktu dikurangi 30%)"