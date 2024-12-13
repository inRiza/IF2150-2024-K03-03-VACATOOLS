class StatisticEntity:
    def __init__(self, id, country, city, count):
        self.id = id
        self.country = country
        self.city = city
        self.count = count

    def to_dict(self):
        """Convert the entity to a dictionary for database insertion."""
        return {
            "id": self.id,
            "country": self.country,
            "city": self.city,
            "count": self.count,
        }

    def __str__(self):
        return f"JournalEntity(id={self.id}, country={self.country}, city={self.city}, count={self.count})"
