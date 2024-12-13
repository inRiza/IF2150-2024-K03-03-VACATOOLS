import logging
from ..models.bucketEntity import BucketEntity
from ..database.databaseEntity import DatabaseEntity

class ViewBucketListController:
    def __init__(self, db_controller: DatabaseEntity):
        self.bucket = []  # Store created bucket
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

    def create_bucket(self, title, country, city, description=None):
        """
        Create a new bucket and add it to the list.
        """
        self.validate_input(['title', 'country', 'city'], title=title, country=country, city=city)

        new_bucket = BucketEntity(
            id=self.next_id,
            title=title,
            country=country,
            city=city,
            description=description,
        )
        
        if not new_bucket:
            raise ValueError("Failed to create bucket.")
        
        self.bucket.append(new_bucket)
        self.next_id += 1
        logging.info(f"bucket created: {new_bucket}")
        
        # Kirim entitas ke controller database untuk disimpan
        self.db_controller.save_bucket_entry(new_bucket)

        return new_bucket


    def get_bucket(self):
        """
        Get all bucket.
        """
        return self.bucket

    def search_bucket(self, query, attribute="title"):
        """
        Search bucket by a specific attribute (default: title).
        Supported attributes: title, country, city, description.
        """
        valid_attributes = {"title", "country", "city", "description"}
        if attribute not in valid_attributes:
            raise ValueError(f"Atribut '{attribute}' tidak valid. Gunakan salah satu dari {valid_attributes}.")

        return [
            bucket for bucket in self.bucket 
            if query.lower() in (getattr(bucket, attribute, "") or "").lower()
        ]

    def delete_bucket(self, bucket_id):
        """
        Delete a bucket by its ID.
        """
        for bucket in self.bucket:
            if bucket.id == bucket_id:
                self.bucket.remove(bucket)
                logging.info(f"bucket with ID {bucket_id} deleted.")
                return
        raise KeyError(f"bucket dengan ID {bucket_id} tidak ditemukan.")

    def update_bucket(self, bucket_id, **updates):
        """
        Update a bucket's attributes by its ID.
        Supported attributes: title, country, city, description.
        """
        valid_attributes = {"title", "country", "city", "description"}
        for bucket in self.bucket:
            if bucket.id == bucket_id:
                for key, value in updates.items():
                    if key in valid_attributes:
                        setattr(bucket, key, value)
                    else:
                        raise ValueError(f"Atribut '{key}' tidak valid. Gunakan salah satu dari {valid_attributes}.")
                logging.info(f"bucket with ID {bucket_id} updated: {bucket}")
                return
        raise KeyError(f"bucket dengan ID {bucket_id} tidak ditemukan.")
