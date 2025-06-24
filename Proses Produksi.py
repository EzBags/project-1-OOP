# Kelompok 1 PBO PROJEK UAS
# proses_produksi
# Muhammad Ridwan Auliansyach_K3524061


from interfaces import ProdukRoti, ProdukDenganTopping, StrategiProduksi
from produk_classes import ProduksiStandar


class ProsesProduksi:
    def __init__(self, strategi: StrategiProduksi = None):
        self.strategi = strategi or ProduksiStandar()

    def set_strategi(self, strategi: StrategiProduksi):
        self.strategi = strategi

    @staticmethod
    def pengadonan(produk: ProdukRoti) -> str:
        return f"Proses pengadonan untuk {produk.nama_produk} selesai."

    @staticmethod
    def pengembangan(produk: ProdukRoti) -> str:
        if produk.perlu_pengembangan():
            return f"Proses pengembangan untuk {produk.nama_produk} selesai (waktu: 45 menit)."
        return f"{produk.nama_produk} tidak memerlukan proses pengembangan."

    @staticmethod
    def pemanggangan(produk: ProdukRoti) -> str:
        suhu = produk.get_suhu_pemanggangan()
        return f"Proses pemanggangan untuk {produk.nama_produk} selesai pada suhu {suhu}°C."

    @staticmethod
    def topping(produk: ProdukRoti) -> str:
        if isinstance(produk, ProdukDenganTopping):
            return produk.aplikasi_topping()
        return f"{produk.nama_produk} tidak memerlukan proses topping."

    def simulasi_produksi(self, produk: ProdukRoti):
        print("\n=== Simulasi Produksi ===")
        print(f"Produk: {produk.nama_produk}")
        print(f"Kategori: {produk.get_kategori()}")
        print(f"Tingkat Kesulitan: {produk.get_tingkat_kesulitan()}")
        print(f"Estimasi Waktu: {produk.get_waktu_produksi()} menit")
        print("-" * 30)
        print(self.strategi.execute_produksi(produk))
        print(self.pengadonan(produk))
        print(self.pengembangan(produk))
        print(self.pemanggangan(produk))
        print(self.topping(produk))
        print("=== Produksi Selesai ===\n")