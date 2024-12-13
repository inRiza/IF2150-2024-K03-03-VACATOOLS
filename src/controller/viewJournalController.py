import logging
from ..models.journalEntity import JournalEntity
from ..database.databaseEntity import DatabaseEntity

class ViewJournalController:
    def __init__(self, db_controller: DatabaseEntity):
        self.journals = []  # Store created journals
        self.next_id = 1000    # Initialize auto-incrementing ID
        self.db_controller = db_controller
        logging.basicConfig(level=logging.INFO)

    def validate_input(self, required_fields, **kwargs):
        """
        Validate required input fields.
        """
        for field in required_fields:
            if not kwargs.get(field):
                raise ValueError(f"Field '{field}' harus diisi.")

    def create_journal(self, title, country, city, date, description=None, image_path=None):
        """
        Create a new journal and add it to the list.
        """
        self.validate_input(['title', 'country', 'city', 'date'], title=title, country=country, city=city, date=date)

        new_journal = JournalEntity(
            id=self.next_id,
            title=title,
            country=country,
            city=city,
            date=date,
            description=description,
            image_path=image_path
        )
        
        if not new_journal:
            raise ValueError("Failed to create journal.")
        
        self.journals.append(new_journal)
        self.next_id += 1
        logging.info(f"Journal created: {new_journal}")
        
        # Kirim entitas ke controller database untuk disimpan
        self.db_controller.save_journal_entry(new_journal)

        return new_journal

    def get_journals(self):
        """
        Get all journals.
        """
        return self.journals

    def search_journals(self, query, attribute="title"):
        """
        Search journals by a specific attribute (default: title).
        Supported attributes: title, country, city, date, description.
        """
        valid_attributes = {"title", "country", "city", "date", "description"}
        if attribute not in valid_attributes:
            raise ValueError(f"Atribut '{attribute}' tidak valid. Gunakan salah satu dari {valid_attributes}.")

        return [
            journal for journal in self.journals 
            if query.lower() in (getattr(journal, attribute, "") or "").lower()
        ]

    def delete_journal(self, journal_id):
        """
        Delete a journal by its ID.
        """
        for journal in self.journals:
            if journal.id == journal_id:
                self.journals.remove(journal)
                logging.info(f"Journal with ID {journal_id} deleted.")
                return
        raise KeyError(f"Journal dengan ID {journal_id} tidak ditemukan.")

    def update_journal(self, journal_id, **updates):
        """
        Update a journal's attributes by its ID.
        Supported attributes: title, country, city, date, description, image_path.
        """
        valid_attributes = {"title", "country", "city", "date", "description", "image_path"}
        for journal in self.journals:
            if journal.id == journal_id:
                for key, value in updates.items():
                    if key in valid_attributes:
                        setattr(journal, key, value)
                    else:
                        raise ValueError(f"Atribut '{key}' tidak valid. Gunakan salah satu dari {valid_attributes}.")
                logging.info(f"Journal with ID {journal_id} updated: {journal}")
                return
        raise KeyError(f"Journal dengan ID {journal_id} tidak ditemukan.")
