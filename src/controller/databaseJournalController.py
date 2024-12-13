from ..database.databaseEntity import DatabaseEntity
from ..models.journalEntity import JournalEntity
from pathlib import Path
from ..controller.databaseStatisticController import DatabaseStatisticController  

class DatabaseJournalController:
    def __init__(self, db_name: str):
        # Menentukan folder database yang sejajar dengan folder controller
        db_folder = Path(__file__).parent.parent / "database"
        db_folder.mkdir(exist_ok=True)  # Membuat folder jika belum ada
        db_path = db_folder / db_name  # Path lengkap untuk database.db
        self.db = DatabaseEntity(db_path)

        # Membuat instance dari DatabaseStatisticController
        self.statistic_controller = DatabaseStatisticController(db_name)

    def save_journal_entry(self, journal_entry: JournalEntity):
        """
        Menyimpan entri jurnal ke database dan otomatis update statistik.
        """
        # Mengubah objek jurnal menjadi dictionary
        journal_data = journal_entry.to_dict()
        
        # Menggunakan metode add_data dari DatabaseEntity untuk menyimpan data jurnal
        self.db.addData("JOURNAL_LOG", **journal_data)
        print(f"Data jurnal '{journal_entry.title}' berhasil disimpan.")
        
        # Mengambil data country dan city dari jurnal_entry
        country = journal_entry.country
        city = journal_entry.city
        
        # Cek apakah country dan city sudah ada di tabel STATISTIC
        existing_data = self.statistic_controller.get_country_city_data()
        
        # Mengatur flag untuk mencocokkan country dan city
        is_existing = False
        for data in existing_data:
            if data['Country'] == country and data['City'] == city:
                is_existing = True
                break
        
        if is_existing:
            # Jika sudah ada, ambil count dan increment
            query = f"""
                UPDATE STATISTIC
                SET count = count + 1
                WHERE Country = '{country}' AND City = '{city}'
            """
            self.db.executeQuery(query)
            print(f"Count untuk {country}, {city} berhasil di-update.")
        else:
            # Jika belum ada, tambahkan entri baru dengan count 1
            statistic_entry = {
                'id': journal_data['id'],  # Asumsikan ID jurnal digunakan untuk ID statistik
                'country': country,
                'city': city,
                'count': 1
            }
            # Menggunakan metode save_statistic_entry dari DatabaseStatisticController
            self.statistic_controller.save_statistic_entry(statistic_entry)
            print(f"Data statistik baru untuk {country}, {city} berhasil ditambahkan.")

    def get_country_city_data(self):
        """
        Mengambil daftar country dan city dari database jurnal.
        """
        # Menggunakan query langsung dari DatabaseEntity
        query = "SELECT DISTINCT Country, City FROM JOURNAL_LOG"  # Ganti dengan nama tabel Anda
        result = self.db.executeQuery(query)  # Pastikan DatabaseEntity memiliki metode executeQuery
        return result

    def get_all_journal_entries(self):
        """
        Mengambil semua entri jurnal dari database.
        """
        return self.db.getData(
            "JOURNAL_LOG", "id", "title", "country", "city", "date", "description", "image_path"
        )

    def close_connection(self):
        """
        Menutup koneksi database.
        """
        self.db.close()
