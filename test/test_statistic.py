import unittest
from src.controller.databaseStatisticController import DatabaseStatisticController

class TestStatisticController(unittest.TestCase):
    def setUp(self):
        """
        Setup sebelum pengujian. Menginisialisasi database dan membersihkan tabel.
        """
        self.controller = DatabaseStatisticController("test_database.db")
        self.controller.db.executeQuery("DELETE FROM JOURNAL_LOG")
        self.controller.db.executeQuery("DELETE FROM STATISTIC")

    def test_update_country_visit_statistics(self):
        """
        Menguji fungsi update_country_visit_statistics.
        """
        # Tambahkan data dummy ke JOURNAL_LOG
        self.controller.db.addData("JOURNAL_LOG", title="Trip 1", country="Japan", city="Tokyo", date="2023-12-01", description="Vacation in Tokyo")
        self.controller.db.addData("JOURNAL_LOG", title="Trip 2", country="Japan", city="Osaka", date="2023-12-02", description="Vacation in Osaka")
        self.controller.db.addData("JOURNAL_LOG", title="Trip 3", country="USA", city="New York", date="2023-12-03", description="Vacation in NYC")

        # Jalankan fungsi untuk memperbarui statistik
        self.controller.update_country_visit_statistics()

        # Ambil data dari tabel STATISTIC
        stats = self.controller.get_country_visit_statistics()

        # Uji hasil
        expected_stats = [
            {"country": "Japan", "total_visits": 2},
            {"country": "USA", "total_visits": 1},
        ]
        self.assertEqual(stats, expected_stats)

    def tearDown(self):
        """
        Membersihkan setelah pengujian.
        """
        self.controller.close_connection()

if __name__ == "__main__":
    unittest.main()
