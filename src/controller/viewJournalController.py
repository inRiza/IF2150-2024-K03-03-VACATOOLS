import logging
import os
import json
from ..models.journalEntity import JournalEntity
from ..controller.databaseJournalController import DatabaseJournalController

class ViewJournalController:
    def __init__(self, db_controller: DatabaseJournalController):
        self.journals = []  # Store created journals
        self.db_controller = db_controller
        self.next_id = self.load_next_id()  # Initialize next ID from saved file
        logging.basicConfig(level=logging.INFO)

    def load_next_id(self):
        """Load the next available ID from a file."""
        try:
            if os.path.exists("next_id.json"):
                with open("next_id.json", "r") as f:
                    data = json.load(f)
                    return data.get("next_id", 1000)  # Default to 1000 if file doesn't contain valid data
        except Exception as e:
            logging.error(f"Failed to load next_id: {e}")
        return 1000  # Default if no saved file exists

    def save_next_id(self):
        """Save the next available ID to a file."""
        try:
            with open("next_id.json", "w") as f:
                json.dump({"next_id": self.next_id}, f)
        except Exception as e:
            logging.error(f"Failed to save next_id: {e}")

    def validate_input(self, required_fields, **kwargs):
        """
        Validate required input fields.
        """
        for field in required_fields:
            if not kwargs.get(field):
                raise ValueError(f"Field '{field}' harus diisi.")

    def create_journal(self, title, country, city, date, description=None):  # image_path=None
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
            # image_path=image_path
        )

        if not new_journal:
            raise ValueError("Failed to create journal.")

        self.journals.append(new_journal)
        logging.info(f"Journal created: {new_journal}")

        # Kirim entitas ke controller database untuk disimpan
        self.db_controller.save_journal_entry(new_journal)

        # Increment the ID and save the new value
        self.next_id += 1
        self.save_next_id()  # Save the updated ID

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
        valid_attributes = {"title", "country", "city", "date", "description"} 
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
