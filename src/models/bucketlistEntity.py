class BucketlistEntity:
    def __init__(self, id: int, judul: str, nama_negara: str, nama_kota: str,
                 deskripsi: str):
        self.id = id
        self.judul = judul
        self.nama_negara = nama_negara
        self.nama_kota = nama_kota
        self.deskripsi = deskripsi

    def __repr__(self):
        return (f"BucketlistEntity(id={self.id}, judul={self.judul}, nama_negara={self.nama_negara}, nama_kota={self.nama_kota}, "
                f"deskripsi={self.deskripsi})")
