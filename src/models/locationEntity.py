class LocationEntity:
    def __init__(self, country, city):
        self.country = country
        self.city = city

    def to_dict(self):
        """Convert the entity to a dictionary for database insertion."""
        return {
            "country": self.country,
            "city": self.city
        }

    def __str__(self):
        return f"LocationEntity(country={self.country}, city={self.city})"
