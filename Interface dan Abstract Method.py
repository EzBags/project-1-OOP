# Kelompok 1 PBO PROJEK UAS
# Interface dan Abstract Classes
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
    def _init_(self, nama_produk: str, kode_produk: str, bahan_baku: Dict[str, str], 
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


# Abstract class untuk berbagai strategi proses produksi
class StrategiProduksi(ABC):
    @abstractmethod
    def execute_produksi(self, produk) -> str:
        """Abstract method untuk menjalankan strategi produksi"""
        pass