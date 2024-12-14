import os
import pytest
from pathlib import Path
from ..models.journalEntity import JournalEntity
from ..controller.databaseJournalController import DatabaseJournalController

class TestDatabaseJournalController:
    @pytest.fixture
    def journal_controller(self):
        # Buat instance controller dengan database sementara untuk pengujian
        db_name = "test_journallog.db"
        controller = DatabaseJournalController(db_name)

        # Setup: Buat tabel yang dibutuhkan di database
        controller.db.executeQuery("""
            CREATE TABLE IF NOT EXISTS JOURNAL_LOG (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                country TEXT NOT NULL,
                city TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT
            );
        """)

        controller.db.executeQuery("""
            CREATE TABLE IF NOT EXISTS LOCATION (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Country TEXT NOT NULL,
                City TEXT NOT NULL
            );
        """)

        yield controller

        # Teardown: Hapus database setelah pengujian selesai
        controller.close_connection()
        os.remove(Path(__file__).parent.parent / "database" / db_name)

    def test_save_journal_entry(self, journal_controller):
        journal = JournalEntity("Perjalanan ke Jogja", "Indonesia", "Yogyakarta", "2024-12-01", "Mengunjungi Candi Borobudur")
        journal_controller.save_journal_entry(journal)

        # Verifikasi data berhasil disimpan
        results = journal_controller.get_all_journal_entries()
        assert len(results) == 1
        assert results[0]["title"] == "Perjalanan ke Jogja"
        assert results[0]["country"] == "Indonesia"
        assert results[0]["city"] == "Yogyakarta"
        assert results[0]["date"] == "2024-12-01"
        assert results[0]["description"] == "Mengunjungi Candi Borobudur"

    def test_get_country_city_data(self, journal_controller):
        # Tambahkan lokasi ke tabel LOCATION
        journal_controller.db.executeQuery("INSERT INTO LOCATION (Country, City) VALUES ('Indonesia', 'Bali'), ('Japan', 'Tokyo')")

        results = journal_controller.get_country_city_data()
        assert len(results) == 2
        assert ("Indonesia", "Bali") in results
        assert ("Japan", "Tokyo") in results

    def test_get_journal_entry_by_id(self, journal_controller):
        journal = JournalEntity("Liburan ke Jepang", "Japan", "Kyoto", "2024-11-15", "Mengunjungi kuil terkenal")
        journal_controller.save_journal_entry(journal)

        # Ambil data berdasarkan ID
        result = journal_controller.get_journal_entry_by_id(1)
        assert result is not None
        assert result["title"] == "Liburan ke Jepang"
        assert result["country"] == "Japan"
        assert result["city"] == "Kyoto"
        assert result["date"] == "2024-11-15"
        assert result["description"] == "Mengunjungi kuil terkenal"

    def test_delete_journal_by_id(self, journal_controller):
        journal = JournalEntity("Liburan ke Bali", "Indonesia", "Denpasar", "2024-10-10", "Menghadiri festival budaya")
        journal_controller.save_journal_entry(journal)

        # Hapus data berdasarkan ID
        journal_controller.delete_journal_by_id(1)
        results = journal_controller.get_all_journal_entries()
        assert len(results) == 0

    def test_get_all_journal_entries(self, journal_controller):
        journal1 = JournalEntity("Piknik", "Jepang", "Osaka", "2024-11-20", "Mengunjungi kastil Osaka")
        journal2 = JournalEntity("Berlayar", "Italia", "Venice", "2024-12-05", "Naik gondola di kanal")
        journal_controller.save_journal_entry(journal1)
        journal_controller.save_journal_entry(journal2)

        results = journal_controller.get_all_journal_entries()
        assert len(results) == 2
        assert results[0]["title"] == "Piknik"
        assert results[1]["title"] == "Berlayar"
