class BucketEntity:
    def __init__(self, id, title, country, city, description=None):
        self.id = id
        self.title = title
        self.country = country
        self.city = city
        self.description = description

    def to_dict(self):
        """Convert the entity to a dictionary for database insertion."""
        return {
            "id": self.id,
            "title": self.title,
            "country": self.country,
            "city": self.city,
            "description": self.description,
        }

    def __str__(self):
        return f"JournalEntity(id={self.id}, title={self.title}, country={self.country}, city={self.city}, description={self.description})"
