from src.models.journalEntity import JournalEntity  # Misalkan model Journal ada di folder model

class ViewJournalController:
    def __init__(self):
        self.journals = []  # Store created journals
        self.next_id = 1    # Initialize auto-incrementing ID

    def create_journal(self, judul, negara, kota, tanggal, deskripsi, image_path):
        # Auto-generate an ID for the new journal
        new_journal = JournalEntity(
            id=self.next_id,  # Automatically assign ID
            judul=judul,
            nama_negara=negara,
            nama_kota=kota,
            tanggal_perjalanan=tanggal,
            deskripsi_perjalanan=deskripsi,
            image_path=image_path
        )
        self.journals.append(new_journal)
        self.next_id += 1  # Increment ID for next journal
        print("Journal created:", new_journal)


    def get_journals(self):
        """Get all journals"""
        return self.journals  # Bisa dikembalikan sebagai daftar atau database query.

    def search_journals(self, query):
        """Search journals by title or other attributes"""
        return [journal for journal in self.journals if query.lower() in journal.judul.lower()]
