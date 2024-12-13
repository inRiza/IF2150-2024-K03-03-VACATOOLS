from ..database.databaseEntity import DatabaseEntity
from ..models.bucketEntity import BucketEntity
from pathlib import Path

class DatabasebucketController:
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
        query = "SELECT DISTINCT Country, City FROM BUCKET_LIST"  # Ganti dengan nama tabel Anda
        result = self.db.executeQuery(query)  # Pastikan DatabaseEntity memiliki metode executeQuery
        return result

    def get_all_bucket_entries(self):
        """
        Mengambil semua entri bucket dari database.
        """
        return self.db.getData(
            "BUCKET_LIST", "id", "title", "country", "city", "description"
        )

    def close_connection(self):
        """
        Menutup koneksi database.
        """
        self.db.close()
