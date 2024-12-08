from typing import List, Optional

from src.models.databaseEntity import DatabaseEntity
from src.models.journalEntity import JournalEntity

class DatabaseJournalController:

    def __init__(self, database_entity:DatabaseEntity):
        self.database_entity = database_entity


    def createJournal(self, journal: JournalEntity):
        """Menambahkan jurnal baru ke database."""
        self.database_entity.addData(
            "journalLog",
            judul                   = journal.judul,
            nama_negara             = journal.nama_negara,
            nama_kota               = journal.nama_kota,
            tanggal_perjalanan      = journal.tanggal_perjalanan,
            deskripsi_perjalanan    = journal.deskripsi_perjalanan
        )


    def readallJournals(self) -> List[JournalEntity]:
        """Membaca seuluruh jurnal dalam bentuk List."""
        journalsData = self.database_entity.getData("journalLog")
        return [JournalEntity(**data) for data in journalsData]


    def readJournal(self, journalID: int) -> JournalEntity:
        """Membaca satu jurnal berdasarkan ID-nya."""
        journal = self.database_entity.getData("journalLog", id=journalID)
        return JournalEntity(
            id                      = journal[0].get("id"),
            judul                   = journal[0].get("judul"),
            nama_negara             = journal[0].get("nama_negara"),
            nama_kota               = journal[0].get("nama_kota"),
            tanggal_perjalanan      = journal[0].get("tanggal_perjalanan"),
            deskripsi_perjalanan    = journal[0].get("deskripsi_perjalanan")
        )


    def updateJournal(self, updated_journal: JournalEntity):
        """Mengubah entri jurnal pada ID tertentu."""
        self.database_entity.setData("journalLog", {"id":updated_journal.id},
                                        judul                   = updated_journal.judul,
                                        nama_negara             = updated_journal.nama_negara,
                                        nama_kota               = updated_journal.nama_kota,
                                        tanggal_perjalanan      = updated_journal.tanggal_perjalanan,
                                        deskripsi_perjalanan    = updated_journal.deskripsi_perjalanan)


    def deleteJournal(self, journalID: int):
        """Menghapus jurnal dengan ID tertentu dari database."""
        self.database_entity.delData("journalLog", id=journalID)