from typing import List, Optional
from src.controller.databaseJournalController import DatabaseJournalController
from src.models.journalEntity import JournalEntity


class TravelJournalController:
    def __init__(self, db_controller: DatabaseJournalController):
        """
        Inisialisasi TravelJournalController.
        """
        self.db_controller = db_controller

    def create_journal(
        self, judul: str, nama_negara: str, nama_kota: str, tanggal_perjalanan: str, deskripsi: str
    ) -> bool:
        """
        Tambahkan jurnal baru ke database.
        """
        try:
            journal = JournalEntity(
                id=None,  # ID akan diatur oleh database
                judul=judul,
                nama_negara=nama_negara,
                nama_kota=nama_kota,
                tanggal_perjalanan=tanggal_perjalanan,
                deskripsi_perjalanan=deskripsi,
            )
            self.db_controller.createJournal(journal)
            return True
        except Exception as e:
            print(f"Error creating journal: {e}")
            return False

    def get_all_journals(self) -> List[JournalEntity]:
        """
        Ambil semua jurnal dari database.
        """
        try:
            return self.db_controller.readallJournals()
        except Exception as e:
            print(f"Error fetching journals: {e}")
            return []

    def get_journal_by_id(self, journal_id: int) -> Optional[JournalEntity]:
        """
        Ambil jurnal berdasarkan ID.
        """
        try:
            return self.db_controller.readJournal(journal_id)
        except Exception as e:
            print(f"Error fetching journal with ID {journal_id}: {e}")
            return None

    def update_journal(
        self, journal_id: int, judul: str, nama_negara: str, nama_kota: str, tanggal_perjalanan: str, deskripsi: str
    ) -> bool:
        """
        Perbarui jurnal berdasarkan ID.
        """
        try:
            updated_journal = JournalEntity(
                id=journal_id,
                judul=judul,
                nama_negara=nama_negara,
                nama_kota=nama_kota,
                tanggal_perjalanan=tanggal_perjalanan,
                deskripsi_perjalanan=deskripsi,
            )
            self.db_controller.updateJournal(updated_journal)
            return True
        except Exception as e:
            print(f"Error updating journal: {e}")
            return False

    def delete_journal(self, journal_id: int) -> bool:
        """
        Hapus jurnal berdasarkan ID.
        """
        try:
            self.db_controller.deleteJournal(journal_id)
            return True
        except Exception as e:
            print(f"Error deleting journal with ID {journal_id}: {e}")
            return False
