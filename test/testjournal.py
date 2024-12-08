
from src.controller.databaseJournalController import DatabaseJournalController

def test_create_journal():
    db_controller = DatabaseJournalController()
    db_controller.create_journal(
        "Judul Test", "Indonesia", "Bandung", "2024-12-07", "Deskripsi Test", "path/to/image.jpg"
    )
    print("Test berhasil.")

if __name__ == "__main__":
    test_create_journal()
