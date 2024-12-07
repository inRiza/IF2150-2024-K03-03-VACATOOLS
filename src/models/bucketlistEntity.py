class BucketlistEntity:
    def __init__(self, bucket_id: int, judul: str, nama_negara: str, nama_kota: str,
                 deskripsi: str):
        self.bucket_id = bucket_id
        self.judul = judul
        self.nama_negara = nama_negara
        self.nama_kota = nama_kota
        self.deskripsi = deskripsi

    def __repr__(self):
        return (f"BucketlistEntity(id={self.bucket_id}, judul={self.judul}, nama_negara={self.nama_negara}, nama_kota={self.nama_kota}, "
                f"deskripsi={self.deskripsi})")

    # def get_bucketlistByID(self, bucket_id):
    #     try :
    #         self.cursor.execute("SELECT * FROM bucketlist WHERE id = ?", (bucket_id,))
    #     except

    # def 
