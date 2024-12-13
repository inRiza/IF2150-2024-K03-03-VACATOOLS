import logging
from ..models.statisticEntity import StatisticEntity
from ..database.databaseEntity import DatabaseEntity

class ViewStatisticController:
    def __init__(self, db_controller: DatabaseEntity):
        self.statistic = []  # Store created statistic
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

    def create_statistic(self, country, city, count):
        """
        Create a new statistic and add it to the list.
        """
        self.validate_input(['country', 'city', 'count'], country=country, city=city, count=count)

        new_statistic = StatisticEntity(
            id=self.next_id,
            country=country,
            city=city,
            count=count,
        )
        
        if not new_statistic:
            raise ValueError("Failed to create statistic.")
        
        self.statistic.append(new_statistic)
        self.next_id += 1
        logging.info(f"statistic created: {new_statistic}")
        
        # Kirim entitas ke controller database untuk disimpan
        self.db_controller.save_statistic_entry(new_statistic)

        return new_statistic


    def get_statistic(self):
        """
        Get all statistic.
        """
        return self.statistic

    def search_statistic(self, query, attribute="title"):
        """
        Search statistic by a specific attribute (default: title).
        Supported attributes: title, country, city, description.
        """
        valid_attributes = {"title", "country", "city", "count"}
        if attribute not in valid_attributes:
            raise ValueError(f"Atribut '{attribute}' tidak valid. Gunakan salah satu dari {valid_attributes}.")

        return [
            statistic for statistic in self.statistic 
            if query.lower() in (getattr(statistic, attribute, "") or "").lower()
        ]

    def delete_statistic(self, statistic_id):
        """
        Delete a statistic by its ID.
        """
        for statistic in self.statistic:
            if statistic.id == statistic_id:
                self.statistic.remove(statistic)
                logging.info(f"statistic with ID {statistic_id} deleted.")
                return
        raise KeyError(f"statistic dengan ID {statistic_id} tidak ditemukan.")

    def update_statistic(self, statistic_id, **updates):
        """
        Update a statistic's attributes by its ID.
        Supported attributes: title, country, city, description.
        """
        valid_attributes = {"country", "city", "description"}
        for statistic in self.statistic:
            if statistic.id == statistic_id:
                for key, value in updates.items():
                    if key in valid_attributes:
                        setattr(statistic, key, value)
                    else:
                        raise ValueError(f"Atribut '{key}' tidak valid. Gunakan salah satu dari {valid_attributes}.")
                logging.info(f"statistic with ID {statistic_id} updated: {statistic}")
                return
        raise KeyError(f"statistic dengan ID {statistic_id} tidak ditemukan.")
    


