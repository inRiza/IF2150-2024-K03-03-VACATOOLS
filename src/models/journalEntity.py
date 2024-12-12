class JournalEntity:
    def __init__(self, title, country, city, date, description, image_path):
        self.title = title
        self.country = country
        self.city = city
        self.date = date
        self.description = description
        self.image_path = image_path

    def to_dict(self):
        """Convert the JournalEntry to a dictionary that can be used by the DatabaseController."""
        return {
            "title": self.title,
            "country": self.country,
            "city": self.city,
            "date": self.date,
            "description": self.description,
            "image_path": self.image_path
        }
