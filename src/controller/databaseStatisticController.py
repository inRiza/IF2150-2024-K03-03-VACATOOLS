from ..database.databaseEntity import DatabaseEntity
from ..models.statisticEntity import StatisticEntity
from pathlib import Path


class DatabaseStatisticController:
    def __init__(self, db_name: str):
        # Menentukan folder database yang sejajar dengan folder controller
        db_folder = Path(__file__).parent.parent / "database"
        db_folder.mkdir(exist_ok=True)  # Membuat folder jika belum ada
        db_path = db_folder / db_name  # Path lengkap untuk database.db
        self.db = DatabaseEntity(db_path)

    def save_statistic_entry(self, statistic_entry: StatisticEntity):
        """
        Menyimpan entri statistic ke database.
        """
        # Mengubah objek statistic menjadi dictionary
        statistic_data = statistic_entry.to_dict()
        # Menggunakan metode addData dari DatabaseEntity untuk menyimpan data
        self.db.addData("STATISTIC", **statistic_data)
        print(f"Data statistik '{statistic_entry.country}' berhasil disimpan.")

    def get_country_city_data(self):
        """
        Mengambil daftar country dan city dari database.
        """
        query = "SELECT DISTINCT country, city FROM STATISTIC"
        result = self.db.executeQuery(query)
        return [{"country": row[0], "city": row[1]} for row in result]

    def get_all_statistic_entries(self):
        """
        Mengambil semua entri statistic dari database.
        """
        return self.db.getData(
            "STATISTIC", "id", "country", "city", "count"
        )

    def get_country_visit_statistics(self):
        """
        Mengambil statistik jumlah kunjungan per negara dari database.
        """
        query = """
        SELECT country, SUM(count) as total_visits
        FROM STATISTIC
        GROUP BY country
        ORDER BY total_visits DESC
        """
        result = self.db.executeQuery(query)
        return [{"country": row[0], "total_visits": row[1]} for row in result]

    def calculate_country_counts(self):
        """
        Menghitung jumlah kunjungan berdasarkan country dari tabel journal_log.
        """
        query = """
        SELECT nama_negara AS country, COUNT(*) AS count
        FROM journal_log
        GROUP BY nama_negara
        ORDER BY count DESC
        """
        result = self.db.executeQuery(query)
        return [{"country": row[0], "count": row[1]} for row in result]

    def close_connection(self):
        """
        Menutup koneksi database.
        """
        self.db.close()
    def fetch_country_city_from_journal(self):
        """
        Mengambil country dan city dari tabel JOURNAL_LOG.
        """
        query = "SELECT country, city FROM JOURNAL_LOG"
        result = self.db.executeQuery(query)
        return [{"country": row[0], "city": row[1]} for row in result]

    def update_country_visit_statistics(self):
        """
        Menghitung jumlah kunjungan per country dari tabel JOURNAL_LOG
        dan memperbarui tabel STATISTIC.
        """
        # Ambil data dari JOURNAL_LOG
        journal_data = self.fetch_country_city_from_journal()
        print(f"Data dari JOURNAL_LOG: {journal_data}")  # Debugging

        country_count = {}

        # Hitung jumlah kunjungan per country
        for entry in journal_data:
            country = entry["country"]
            country_count[country] = 1
    

        print(f"Hitungan per negara: {country_count}")  # Debugging

        # Perbarui data di tabel STATISTIC
        for country, count in country_count.items():
            self.db.addData("STATISTIC", country=country, city="", count=count)
            print(f"Data ditambahkan ke STATISTIC: {country}, count: {count}")  # Debugging

        print("Statistik kunjungan berhasil diperbarui dari JOURNAL_LOG.")

    def delete_statistic_by_country(self, country):
        """
        Menghapus entri statistik dari tabel STATISTIC berdasarkan negara yang diberikan.
        """
        # Periksa apakah data dengan country tersebut ada
        select_query = "SELECT id FROM STATISTIC WHERE country = ? LIMIT 1"
        result = self.db.executeQuery2(select_query, (country,))
        
        if result:
            # Ambil ID entri pertama yang ditemukan
            id_to_delete = result[0][0]
            
            # Hapus entri berdasarkan ID
            delete_query = "DELETE FROM STATISTIC WHERE id = ?"
            self.db.executeQuery2(delete_query, (id_to_delete,))
            
            print(f"Entri statistik untuk negara '{country}' berhasil dihapus.")
        else:
            print(f"Tidak ada entri statistik untuk negara '{country}' yang ditemukan.")
