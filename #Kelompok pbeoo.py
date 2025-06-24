# Kelompok 1 PBO PROJEK UAS
# Yardan Raditya laksana_K3524017
# Muhammad Irfan Maulana_K3524059
# Muhammad Ridwan Auliansyach_K3524061
# Khoirul Bagus Wicaksono_K3524077

from abc import ABC, abstractmethod
try:
    from typing import Protocol, Dict, List
except ImportError:
    # Fallback untuk Python versi lama
    from typing import Dict, List
    class Protocol:
        pass


# Interface untuk produk yang dapat diproduksi
class ProdukInterface(Protocol):
    def hitung_profit(self, jumlah: int) -> float:
        """Menghitung profit dari produk"""
        pass
    
    def info_produk(self) -> str:
        """Menampilkan informasi produk"""
        pass
    
    def get_waktu_produksi(self) -> int:
        """Mendapatkan waktu produksi dalam menit"""
        pass


# Interface untuk proses produksi
class ProsesInterface(Protocol):
    def pengadonan(self, produk) -> str:
        """Proses pengadonan"""
        pass
    
    def pemanggangan(self, produk) -> str:
        """Proses pemanggangan"""
        pass


# Abstract Base Class untuk semua produk roti
class ProdukRoti(ABC):
    def __init__(self, nama_produk: str, kode_produk: str, bahan_baku: Dict[str, str], 
                 biaya_produksi: float, harga_jual: float):
        self.nama_produk = nama_produk
        self.kode_produk = kode_produk
        self.bahan_baku = bahan_baku
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual

    def hitung_profit(self, jumlah: int) -> float:
        """Method konkret untuk menghitung profit"""
        return (self.harga_jual * jumlah) - (self.biaya_produksi * jumlah)

    def info_produk(self) -> str:
        """Method konkret untuk menampilkan info produk"""
        return f"""
        Nama Produk: {self.nama_produk}
        Kode Produk: {self.kode_produk}
        Kategori: {self.get_kategori()}
        Bahan Baku: {', '.join(self.bahan_baku.keys())}
        Biaya Produksi: Rp{self.biaya_produksi:,.2f}/pcs
        Harga Jual: Rp{self.harga_jual:,.2f}/pcs
        Waktu Produksi: {self.get_waktu_produksi()} menit
        Tingkat Kesulitan: {self.get_tingkat_kesulitan()}
        """

    @abstractmethod
    def get_kategori(self) -> str:
        """Abstract method untuk mendapatkan kategori produk"""
        pass

    @abstractmethod
    def get_waktu_produksi(self) -> int:
        """Abstract method untuk mendapatkan waktu produksi dalam menit"""
        pass

    @abstractmethod
    def get_tingkat_kesulitan(self) -> str:
        """Abstract method untuk mendapatkan tingkat kesulitan produksi"""
        pass

    @abstractmethod
    def get_suhu_pemanggangan(self) -> int:
        """Abstract method untuk mendapatkan suhu pemanggangan"""
        pass

    @abstractmethod
    def perlu_pengembangan(self) -> bool:
        """Abstract method untuk menentukan apakah perlu proses pengembangan"""
        pass


# Abstract class untuk produk yang memerlukan topping
class ProdukDenganTopping(ProdukRoti):
    @abstractmethod
    def get_jenis_topping(self) -> List[str]:
        """Abstract method untuk mendapatkan jenis topping yang tersedia"""
        pass

    @abstractmethod
    def aplikasi_topping(self) -> str:
        """Abstract method untuk proses aplikasi topping"""
        pass


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


# Abstract class untuk berbagai strategi proses produksi
class StrategiProduksi(ABC):
    @abstractmethod
    def execute_produksi(self, produk: ProdukRoti) -> str:
        """Abstract method untuk menjalankan strategi produksi"""
        pass


class ProduksiStandar(StrategiProduksi):
    def execute_produksi(self, produk: ProdukRoti) -> str:
        return f"Menjalankan produksi standar untuk {produk.nama_produk}"


class ProduksiEkspres(StrategiProduksi):
    def execute_produksi(self, produk: ProdukRoti) -> str:
        return f"Menjalankan produksi ekspres untuk {produk.nama_produk} (waktu dikurangi 30%)"


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