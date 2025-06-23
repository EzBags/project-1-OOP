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
        
from produk import *

class ProsesProduksi:
    @staticmethod
    def pengadonan(produk):
        return f"Proses pengadonan untuk {produk.nama_produk} selesai."

    @staticmethod
    def pengembangan(produk):
        if isinstance(produk, (RotiManis, Croissant, Muffin)):
            return f"Proses pengembangan untuk {produk.nama_produk} selesai."
        return f"{produk.nama_produk} tidak memerlukan proses pengembangan."

    @staticmethod
    def pemanggangan(produk):
        return f"Proses pemanggangan untuk {produk.nama_produk} selesai."

    @staticmethod
    def topping(produk):
        if isinstance(produk, KueKering):
            return f"Proses topping untuk {produk.nama_produk} selesai."
        return f"{produk.nama_produk} tidak memerlukan proses topping."

    @staticmethod
    def simulasi_produksi(produk):
        print("\n=== Simulasi Produksi ===")
        print(ProsesProduksi.pengadonan(produk))
        print(ProsesProduksi.pengembangan(produk))
        print(ProsesProduksi.pemanggangan(produk))
        print(ProsesProduksi.topping(produk))
        print("=== Produksi Selesai ===\n")
        
from produk import *
from produksi import ProsesProduksi

class MenuHanariBakery:
    def _init_(self):
        self.produk_list = []

    def tambah_produk(self):
        print("\nTambah Produk Baru")
        jenis = input("Jenis produk (roti/croissant/cookies/muffin): ").lower()
        nama = input("Nama produk: ")
        kode = input("Kode produk: ")
        biaya = float(input("Biaya produksi per pcs: "))
        harga = float(input("Harga jual per pcs: "))
        
        # Contoh bahan baku
        bahan = {
            "tepung": "500 gram",
            "gula": "100 gram",
            "telur": "2 butir"
        }

        if jenis == "roti":
            produk = RotiManis(nama, kode, bahan, biaya, harga)
        elif jenis == "croissant":
            produk = Croissant(nama, kode, bahan, biaya, harga)
        elif jenis == "cookies":
            produk = ButterCookies(nama, kode, bahan, biaya, harga)
        elif jenis == "muffin":
            produk = Muffin(nama, kode, bahan, biaya, harga)
        else:
            print("Jenis produk tidak valid!")
            return

        self.produk_list.append(produk)
        print(f"Produk {nama} berhasil ditambahkan!\n")

    def tampilkan_produk(self):
        print("\nDaftar Produk Hanari Bakery")
        for idx, produk in enumerate(self.produk_list, 1):
            print(f"{idx}. {produk.nama_produk} ({produk.kode_produk})")

    def hitung_profit(self):
        self.tampilkan_produk()
        pilihan = int(input("Pilih produk: ")) - 1
        jumlah = int(input("Jumlah yang akan diproduksi: "))
        produk = self.produk_list[pilihan]
        profit = produk.hitung_profit(jumlah)
        print(f"\nEstimasi profit untuk {produk.nama_produk}: Rp{profit:,.2f}\n")

    def jalankan_menu(self):
        while True:
            print("\n=== Hanari Bakery Management System ===")
            print("1. Tambah Produk Baru")
            print("2. Tampilkan Semua Produk")
            print("3. Kalkulator Estimasi Profit")
            print("4. Simulasi Proses Produksi")
            print("5. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == '1':
                self.tambah_produk()
            elif pilihan == '2':
                self.tampilkan_produk()
            elif pilihan == '3':
                self.hitung_profit()
            elif pilihan == '4':
                self.tampilkan_produk()
                pilihan = int(input("Pilih produk untuk simulasi: ")) - 1
                ProsesProduksi.simulasi_produksi(self.produk_list[pilihan])
            elif pilihan == '5':
                print("Terima kasih telah menggunakan sistem Hanari Bakery!")
                break
            else:
                print("Pilihan tidak valid!")