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
        """Menyimpan entri jurnal ke database."""
        # Mengubah objek jurnal menjadi dictionary
        journal_data = journal_entry.to_dict()
        # Menggunakan metode add_data dari DatabaseEntity untuk menyimpan data
        self.db.addData("JOURNAL_LOG", **journal_data)
        print(f"Data jurnal '{journal_entry.title}' berhasil disimpan.")

    def get_all_journal_entries(self):
        """Mengambil semua entri jurnal dari database."""
        return self.db.getData("JOURNAL_LOG", "id", "title", "country", "city", "date", "description", "image_path")

    def close_connection(self):
        """Menutup koneksi database."""
        self.db.close()
