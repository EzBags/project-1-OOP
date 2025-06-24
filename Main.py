# Kelompok 1 PBO PROJEK UAS
# Main
# Yardan Raditya laksana_K3524017


from interfaces import ProdukRoti
from produk_classes import RotiManis, Croissant, ButterCookies, Muffin, ProduksiStandar, ProduksiEkspres
from proses_produksi import ProsesProduksi
from typing import List


class MenuHanariBakery:
    def __init__(self):
        self.produk_list: List[ProdukRoti] = []
        self.proses_produksi = ProsesProduksi()

    def tambah_produk(self):
        print("\nTambah Produk Baru")
        print("Pilihan jenis produk:")
        print("1. roti - Roti Manis")
        print("2. croissant - Croissant/Pastry")
        print("3. cookies - Butter Cookies")
        print("4. muffin - Muffin")
        
        jenis = input("Jenis produk (roti/croissant/cookies/muffin): ").lower().strip()
        
        # Validasi jenis produk
        if jenis not in ["roti", "croissant", "cookies", "muffin"]:
            print(f"Jenis produk '{jenis}' tidak valid!")
            print("Pilihan yang tersedia: roti, croissant, cookies, muffin")
            return
        
        nama = input("Nama produk: ").strip()
        if not nama:
            print("Nama produk tidak boleh kosong!")
            return
            
        kode = input("Kode produk: ").strip()
        if not kode:
            print("Kode produk tidak boleh kosong!")
            return
        
        # Cek apakah kode produk sudah ada
        for produk in self.produk_list:
            if produk.kode_produk == kode:
                print(f"Kode produk '{kode}' sudah digunakan!")
                return
        
        try:
            biaya_input = input("Biaya produksi per pcs: ").strip()
            if not biaya_input:
                print("Biaya produksi tidak boleh kosong!")
                return
            biaya = float(biaya_input)
            if biaya <= 0:
                print("Biaya produksi harus lebih dari 0!")
                return
                
            harga_input = input("Harga jual per pcs: ").strip()
            if not harga_input:
                print("Harga jual tidak boleh kosong!")
                return
            harga = float(harga_input)
            if harga <= 0:
                print("Harga jual harus lebih dari 0!")
                return
            if harga <= biaya:
                print("Harga jual harus lebih besar dari biaya produksi!")
                return
        except ValueError:
            print("Input biaya dan harga harus berupa angka!")
            return
        
        # Bahan baku berdasarkan jenis produk
        bahan_baku = {
            "roti": {
                "tepung terigu": "500 gram",
                "gula": "100 gram",
                "telur": "2 butir",
                "ragi": "1 sdt",
                "mentega": "50 gram"
            },
            "croissant": {
                "tepung terigu": "500 gram",
                "mentega": "200 gram",
                "gula": "50 gram",
                "telur": "1 butir",
                "garam": "1 sdt"
            },
            "cookies": {
                "tepung terigu": "300 gram",
                "mentega": "150 gram",
                "gula halus": "100 gram",
                "telur": "1 butir"
            },
            "muffin": {
                "tepung terigu": "400 gram",
                "gula": "150 gram",
                "telur": "2 butir",
                "minyak": "100 ml",
                "baking powder": "1 sdt"
            }
        }
        
        bahan = bahan_baku[jenis]

        try:
            if jenis == "roti":
                produk = RotiManis(nama, kode, bahan, biaya, harga)
            elif jenis == "croissant":
                produk = Croissant(nama, kode, bahan, biaya, harga)
            elif jenis == "cookies":
                produk = ButterCookies(nama, kode, bahan, biaya, harga)
            elif jenis == "muffin":
                produk = Muffin(nama, kode, bahan, biaya, harga)
            
            self.produk_list.append(produk)
            print(f"\n✅ Produk '{nama}' berhasil ditambahkan!")
            print(f"Kategori: {produk.get_kategori()}")
            print(f"Kode: {kode}")
            print(f"Biaya: Rp{biaya:,.2f}")
            print(f"Harga: Rp{harga:,.2f}")
            print()
            
        except Exception as e:
            print(f"Error saat membuat produk: {e}")
            return

    def tampilkan_produk(self):
        if not self.produk_list:
            print("\nBelum ada produk yang terdaftar.")
            return
            
        print("\nDaftar Produk Hanari Bakery")
        for idx, produk in enumerate(self.produk_list, 1):
            print(f"{idx}. {produk.nama_produk} ({produk.kode_produk}) - {produk.get_kategori()}")

    def detail_produk(self):
        if not self.produk_list:
            print("\nBelum ada produk yang terdaftar.")
            return
            
        self.tampilkan_produk()
        try:
            pilihan = int(input("Pilih produk untuk melihat detail: ")) - 1
            if pilihan < 0 or pilihan >= len(self.produk_list):
                print("Pilihan tidak valid!")
                return
                
            produk = self.produk_list[pilihan]
            print(produk.info_produk())
        except (ValueError, IndexError):
            print("Input tidak valid!")

    def hitung_profit(self):
        if not self.produk_list:
            print("\nBelum ada produk yang terdaftar. Tambah produk terlebih dahulu.")
            return
            
        self.tampilkan_produk()
        try:
            pilihan = int(input("Pilih produk: ")) - 1
            if pilihan < 0 or pilihan >= len(self.produk_list):
                print("Pilihan tidak valid!")
                return
                
            jumlah = int(input("Jumlah yang akan diproduksi: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                return
                
            produk = self.produk_list[pilihan]
            profit = produk.hitung_profit(jumlah)
            waktu_total = produk.get_waktu_produksi() * jumlah
            print(f"\nEstimasi untuk {produk.nama_produk}:")
            print(f"Profit: Rp{profit:,.2f}")
            print(f"Waktu produksi total: {waktu_total} menit ({waktu_total/60:.1f} jam)")
            print()
        except (ValueError, IndexError):
            print("Input tidak valid!")

    def simulasi_produksi_menu(self):
        if not self.produk_list:
            print("\nBelum ada produk yang terdaftar. Tambah produk terlebih dahulu.")
            return
            
        print("\nPilih mode produksi:")
        print("1. Produksi Standar")
        print("2. Produksi Ekspres")
        
        try:
            mode = input("Pilih mode (1/2): ")
            if mode == "2":
                self.proses_produksi.set_strategi(ProduksiEkspres())
            else:
                self.proses_produksi.set_strategi(ProduksiStandar())
        except:
            print("Mode tidak valid, menggunakan produksi standar.")
            
        self.tampilkan_produk()
        try:
            pilihan = int(input("Pilih produk untuk simulasi: ")) - 1
            if pilihan < 0 or pilihan >= len(self.produk_list):
                print("Pilihan tidak valid!")
                return
                
            self.proses_produksi.simulasi_produksi(self.produk_list[pilihan])
        except (ValueError, IndexError):
            print("Input tidak valid!")

    def jalankan_menu(self):
        while True:
            print("\n=== Hanari Bakery Management System ===")
            print("1. Tambah Produk Baru")
            print("2. Tampilkan Semua Produk")
            print("3. Detail Produk")
            print("4. Kalkulator Estimasi Profit")
            print("5. Simulasi Proses Produksi")
            print("6. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == '1':
                self.tambah_produk()
            elif pilihan == '2':
                self.tampilkan_produk()
            elif pilihan == '3':
                self.detail_produk()
            elif pilihan == '4':
                self.hitung_profit()
            elif pilihan == '5':
                self.simulasi_produksi_menu()
            elif pilihan == '6':
                print("Terima kasih telah menggunakan sistem Hanari Bakery!")
                break
            else:
                print("Pilihan tidak valid!")


if __name__ == "__main__":
    # Contoh data produk untuk testing
    bakery = MenuHanariBakery()
    
    # Jalankan menu utama
    bakery.jalankan_menu()