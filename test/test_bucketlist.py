import os
import pytest
from pathlib import Path
from ..src.models.bucketEntity import BucketEntity
from ..src.controller.databaseBucketListController import DatabaseBucketListController

class TestDatabaseBucketListController:
    @pytest.fixture
    def bucket_controller(self):
        # Buat instance controller dengan database sementara untuk pengujian
        db_name = "test_bucketlist.db"
        controller = DatabaseBucketListController(db_name)
        
        # Setup: Buat tabel yang dibutuhkan di database
        controller.db.executeQuery("""
            CREATE TABLE IF NOT EXISTS BUCKET_LIST (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                country TEXT NOT NULL,
                city TEXT NOT NULL,
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

    def test_save_bucket_entry(self, bucket_controller):
        bucket = BucketEntity("Liburan ke Bali", "Indonesia", "Bali", "Mengunjungi pantai")
        bucket_controller.save_bucket_entry(bucket)
        
        # Verifikasi data berhasil disimpan
        results = bucket_controller.get_all_bucket_entries()
        assert len(results) == 1
        assert results[0]["title"] == "Liburan ke Bali"
        assert results[0]["country"] == "Indonesia"
        assert results[0]["city"] == "Bali"
        assert results[0]["description"] == "Mengunjungi pantai"

    def test_get_country_city_data(self, bucket_controller):
        # Tambahkan lokasi ke tabel LOCATION
        bucket_controller.db.executeQuery("INSERT INTO LOCATION (Country, City) VALUES ('Indonesia', 'Jakarta'), ('USA', 'New York')")
        
        results = bucket_controller.get_country_city_data()
        assert len(results) == 2
        assert ("Indonesia", "Jakarta") in results
        assert ("USA", "New York") in results

    def test_get_bucket_entry_by_id(self, bucket_controller):
        bucket = BucketEntity("Mendaki Gunung", "Indonesia", "Lombok", "Rinjani")
        bucket_controller.save_bucket_entry(bucket)
        
        # Ambil data berdasarkan ID
        result = bucket_controller.get_bucket_entry_by_id(1)
        assert result is not None
        assert result["title"] == "Mendaki Gunung"
        assert result["country"] == "Indonesia"
        assert result["city"] == "Lombok"
        assert result["description"] == "Rinjani"

    def test_delete_bucket_by_id(self, bucket_controller):
        bucket = BucketEntity("Menjelajah Kuliner", "Thailand", "Bangkok", "Makanan jalanan")
        bucket_controller.save_bucket_entry(bucket)
        
        # Hapus data berdasarkan ID
        bucket_controller.delete_bucket_by_id(1)
        results = bucket_controller.get_all_bucket_entries()
        assert len(results) == 0

    def test_get_all_bucket_entries(self, bucket_controller):
        bucket1 = BucketEntity("Piknik", "Jepang", "Tokyo", "Hanami di taman Ueno")
        bucket2 = BucketEntity("Safari", "Afrika Selatan", "Cape Town", "Mengamati satwa liar")
        bucket_controller.save_bucket_entry(bucket1)
        bucket_controller.save_bucket_entry(bucket2)

        results = bucket_controller.get_all_bucket_entries()
        assert len(results) == 2
        assert results[0]["title"] == "Piknik"
        assert results[1]["title"] == "Safari"
