import pytest
from pathlib import Path
from ..src.models.statisticEntity import StatisticEntity
from ..src.controller.databaseStatisticController import DatabaseStatisticController

class TestDatabaseStatisticController:
    @pytest.fixture
    def db_statistic_controller(self):
        # Assume test database is "test_statistic.db"
        controller = DatabaseStatisticController("test_statistic.db")
        yield controller
        controller.db.cursor.execute("DROP TABLE IF EXISTS STATISTIC")
        controller.db.commit()
        controller.close_connection()

    @pytest.fixture
    def sample_statistic(self):
        return StatisticEntity(country="Indonesia", city="Jakarta", count=10)

    def test_save_statistic_entry(self, db_statistic_controller, sample_statistic):
        db_statistic_controller.save_statistic_entry(sample_statistic)
        entries = db_statistic_controller.get_all_statistic_entries()
        
        assert len(entries) == 1
        assert entries[0][1] == "Indonesia"
        assert entries[0][2] == "Jakarta"
        assert entries[0][3] == 10

    def test_get_country_city_data(self, db_statistic_controller, sample_statistic):
        db_statistic_controller.save_statistic_entry(sample_statistic)
        country_city_data = db_statistic_controller.get_country_city_data()
        
        assert len(country_city_data) == 1
        assert country_city_data[0]["country"] == "Indonesia"
        assert country_city_data[0]["city"] == "Jakarta"

    def test_get_all_statistic_entries(self, db_statistic_controller, sample_statistic):
        db_statistic_controller.save_statistic_entry(sample_statistic)
        entries = db_statistic_controller.get_all_statistic_entries()
        
        assert len(entries) == 1
        assert entries[0][1] == "Indonesia"
        assert entries[0][2] == "Jakarta"
        assert entries[0][3] == 10

    def test_get_country_visit_statistics(self, db_statistic_controller):
        db_statistic_controller.save_statistic_entry(StatisticEntity(country="Indonesia", city="Jakarta", count=5))
        db_statistic_controller.save_statistic_entry(StatisticEntity(country="Indonesia", city="Bandung", count=7))
        db_statistic_controller.save_statistic_entry(StatisticEntity(country="Malaysia", city="Kuala Lumpur", count=3))

        visit_statistics = db_statistic_controller.get_country_visit_statistics()
        
        assert len(visit_statistics) == 2
        assert visit_statistics[0]["country"] == "Indonesia"
        assert visit_statistics[0]["total_visits"] == 12
        assert visit_statistics[1]["country"] == "Malaysia"
        assert visit_statistics[1]["total_visits"] == 3

    def test_delete_statistic_by_country(self, db_statistic_controller):
        db_statistic_controller.save_statistic_entry(StatisticEntity(country="Indonesia", city="Jakarta", count=5))
        db_statistic_controller.save_statistic_entry(StatisticEntity(country="Malaysia", city="Kuala Lumpur", count=3))

        db_statistic_controller.delete_statistic_by_country("Indonesia")
        entries = db_statistic_controller.get_all_statistic_entries()

        assert len(entries) == 1
        assert entries[0][1] == "Malaysia"
