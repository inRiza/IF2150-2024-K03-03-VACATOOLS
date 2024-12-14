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

    def close_connection(self):
        """
        Menutup koneksi database.
        """
        self.db.close()
