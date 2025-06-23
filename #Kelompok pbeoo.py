#Kelompok
#kkkk
#hhhh
#balapppp
#atosperson
#pankness ndlogok
#ariancok
#Kelompok 1 PBO PROJEK UAS
#Yardan Raditya laksana_K3524017
#Muhammad Irfan Maulana_K3524059
#Muhammad Ridwan Auliansyach_K3524061
#Khoirul Bagus Wicaksono_K3524077

class ProdukRoti:
    def _init_(self, nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual):
        self.nama_produk = nama_produk
        self.kode_produk = kode_produk
        self.bahan_baku = bahan_baku
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual

    def hitung_profit(self, jumlah):
        return (self.harga_jual * jumlah) - (self.biaya_produksi * jumlah)

    def info_produk(self):
        return f"""
        Nama Produk: {self.nama_produk}
        Kode Produk: {self.kode_produk}
        Bahan Baku: {', '.join(self.bahan_baku.keys())}
        Biaya Produksi: Rp{self.biaya_produksi:,.2f}/pcs
        Harga Jual: Rp{self.harga_jual:,.2f}/pcs
        """


class RotiManis(ProdukRoti):
    def _init_(self, nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual):
        super()._init_(nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual)


class Croissant(ProdukRoti):
    def _init_(self, nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual):
        super()._init_(nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual)


class KueKering(ProdukRoti):
    def _init_(self, nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual):
        super()._init_(nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual)


class ButterCookies(KueKering):
    def _init_(self, nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual):
        super()._init_(nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual)


class Muffin(KueKering):
    def _init_(self, nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual):
        super()._init_(nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual)
