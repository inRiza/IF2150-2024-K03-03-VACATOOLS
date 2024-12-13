class JournalEntity:
    def __init__(self, id, title, country, city, date, description=None, image_path=None):
        self.id = id
        self.title = title
        self.country = country
        self.city = city
        self.date = date
        self.description = description
        self.image_path = image_path

    def to_dict(self):
        """Convert the entity to a dictionary for database insertion."""
        return {
            "id": self.id,
            "title": self.title,
            "country": self.country,
            "city": self.city,
            "date": self.date,
            "description": self.description,
            # "image_path": self.image_path,
        }

    def __str__(self):
        return f"JournalEntity(id={self.id}, title={self.title}, country={self.country}, city={self.city}, date={self.date}, description={self.description})"

# image_path={self.image_path} -- kalau mau pake image