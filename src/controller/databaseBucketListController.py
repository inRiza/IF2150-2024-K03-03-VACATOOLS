from ..database.databaseEntity import DatabaseEntity
from ..models.bucketEntity import BucketEntity
from pathlib import Path

class DatabaseBucketListController:
    def __init__(self, db_name: str):
        # Menentukan folder database yang sejajar dengan folder controller
        db_folder = Path(__file__).parent.parent / "database"
        db_folder.mkdir(exist_ok=True)  # Membuat folder jika belum ada
        db_path = db_folder / db_name  # Path lengkap untuk database.db
        self.db = DatabaseEntity(db_path)

    def save_bucket_entry(self, bucket_entry: BucketEntity):
        """
        Menyimpan entri bucket ke database.
        """
        # Mengubah objek bucket menjadi dictionary
        bucket_data = bucket_entry.to_dict()
        # Menggunakan metode add_data dari DatabaseEntity untuk menyimpan data
        self.db.addData("BUCKET_LIST", **bucket_data)
        print(f"Data bucket '{bucket_entry.title}' berhasil disimpan.")

    def get_country_city_data(self):
        """
        Mengambil daftar country dan city dari database.
        """
        # Menggunakan query langsung dari DatabaseEntity
        query = "SELECT DISTINCT Country, City FROM LOCATION"  # Ganti dengan nama tabel Anda
        result = self.db.executeQuery(query)  # Pastikan DatabaseEntity memiliki metode executeQuery
        return result

    def get_all_bucket_entries(self):
        """
        Mengambil semua entri bucket dari database.
        """
        return self.db.getData(
            "BUCKET_LIST", "id", "title", "country", "city", "description"
        )
        
    def get_bucket_entry_by_id(self, bucket_id: int):
        """
        Mengambil entri bucket berdasarkan ID.
        """
        query = f"SELECT * FROM BUCKET_LIST WHERE id = {bucket_id}"
        result = self.db.executeQuery(query)
        
        if result:
            columns = [desc[0] for desc in self.db.cursor.description]  # Ambil nama kolom dari hasil query
            return dict(zip(columns, result[0]))  # Mengubah hasil menjadi dictionary dengan nama kolom sebagai key
        return None  # Jika tidak ada hasil
    
    def delete_bucket_by_id(self, bucket_id: int):
        """
        Menghapus entri jurnal dari database berdasarkan ID.
        """
        query = f"DELETE FROM BUCKET_LIST WHERE id = {bucket_id}"
        self.db.executeQuery(query)
        print(f"Data jurnal dengan ID {bucket_id} berhasil dihapus.")

    def close_connection(self):
        """
        Menutup koneksi database.
        """
        self.db.close()
