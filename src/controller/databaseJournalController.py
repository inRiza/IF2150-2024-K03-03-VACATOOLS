from ..database.databaseEntity import DatabaseEntity
from ..models.journalEntity import JournalEntity
from pathlib import Path


class DatabaseJournalController:
    def __init__(self, db_name: str):
        # Menentukan folder database yang sejajar dengan folder controller
        db_folder = Path(__file__).parent.parent / "database"
        db_folder.mkdir(exist_ok=True)  # Membuat folder jika belum ada
        db_path = db_folder / db_name  # Path lengkap untuk database.db
        self.db = DatabaseEntity(db_path)

    def save_journal_entry(self, journal_entry: JournalEntity):
        """
        Menyimpan entri jurnal ke database.
        """
        # Mengubah objek jurnal menjadi dictionary
        journal_data = journal_entry.to_dict()
        # Menggunakan metode add_data dari DatabaseEntity untuk menyimpan data
        self.db.addData("JOURNAL_LOG", **journal_data)
        print(f"Data jurnal '{journal_entry.title}' berhasil disimpan.")

    def get_country_city_data(self):
        """
        Mengambil daftar country dan city dari database.
        """
        # Menggunakan query langsung dari DatabaseEntity
        query = "SELECT DISTINCT Country, City FROM LOCATION"  # Ganti dengan nama tabel Anda
        result = self.db.executeQuery(query)  # Pastikan DatabaseEntity memiliki metode executeQuery
        return result

    def get_all_journal_entries(self):
        """
        Mengambil semua entri jurnal dari database.
        """
        return self.db.getData(
            "JOURNAL_LOG", "id", "title", "country", "city", "date", "description"
        )
        # "image_path"
    
    def get_journal_entry_by_id(self, journal_id: int):
        """
        Mengambil entri jurnal berdasarkan ID.
        """
        query = f"SELECT * FROM JOURNAL_LOG WHERE id = {journal_id}"
        result = self.db.executeQuery(query)
        
        if result:
            columns = [desc[0] for desc in self.db.cursor.description]  # Ambil nama kolom dari hasil query
            return dict(zip(columns, result[0]))  # Mengubah hasil menjadi dictionary dengan nama kolom sebagai key
        return None  # Jika tidak ada hasil

    def delete_journal_by_id(self, journal_id: int):
        """
        Menghapus entri jurnal dari database berdasarkan ID.
        """
        query = f"DELETE FROM JOURNAL_LOG WHERE id = {journal_id}"
        self.db.executeQuery(query)
        print(f"Data jurnal dengan ID {journal_id} berhasil dihapus.")

    
    def close_connection(self):
        """
        Menutup koneksi database.
        """
        self.db.close()
