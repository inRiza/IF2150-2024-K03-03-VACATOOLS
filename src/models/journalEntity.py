class JournalEntity:
    def __init__(self, id: int, judul: str, nama_negara: str, nama_kota: str,
                 tanggal_perjalanan: str, deskripsi_perjalanan: str, image_path: str):
        self.id = id
        self.judul = judul
        self.nama_negara = nama_negara
        self.nama_kota = nama_kota
        self.tanggal_perjalanan = tanggal_perjalanan
        self.deskripsi_perjalanan = deskripsi_perjalanan
        self.image_path = image_path

    def __repr__(self):
        return (f"JournalEntity(id={self.id}, judul={self.judul}, nama_negara={self.nama_negara}, "
                f"nama_kota={self.nama_kota}, tanggal_perjalanan={self.tanggal_perjalanan}, "
                f"deskripsi_perjalanan={self.deskripsi_perjalanan}, image_path={self.image_path})")
