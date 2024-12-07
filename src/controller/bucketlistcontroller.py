from typing import List, Optional
from models.bucketlistEntity import BucketlistEntity
from src.contoller.databaseBucketlistController import DatabaseBucketlistController

class BucketlistController:
    def __init__(self, db_controller: DatabaseBucketlistController):
        self.db_controller = db_controller


    def create_buckerlist(self, bucket_id: int, judul: str, nama_negara: str, nama_kota: str,
                 deskripsi: str) -> bool:
        try:
            bucketlist = BucketlistEntity(
                bucket_id = None, 
                judul = judul, 
                nama_negara = nama_negara, 
                nama_kota = nama_kota, 
                deskripsi = deskripsi)
            self.db_controller.add_bucketlist(bucketlist)
            return True
        
        except Exception as e:
            printf("Error: ", e)
            return False
    
    def update_bucketlist(bucket_id: int, judul: str, nama_negara: str, nama_kota: str,
                 deskripsi: str) -> List[bucketlistEntity]:
        """ Melakukan update bucketlist dengan ID tertentu."""
        try:
            bucketlist = BucketlistEntity(
                bucket_id = None, 
                judul = judul, 
                nama_negara = nama_negara, 
                nama_kota = nama_kota, 
                deskripsi = deskripsi)
            self.db_controller.add_bucketlist(bucketlist)
            return True
        except Exception as e:
            printf("Error updating bucketlist: ", e)
            return False


    def delete_bucketlist(self, bucket_id: int) -> bool:
        """Menghapus bucketlist dengan ID tertentu dari database."""
        try:
            self.db_controller.delete_bucketlist(bucket_id)
            return True
        except Exception as e:
            printf("Error deleting bucketlist: ", e)
            return False

    def get_bucketlist(self, bucket_id: int) -> Optional[bucketlistEntity]:
        """Mengambil bucketlist dengan ID tertentu dari database."""
        try:
            return self.db_controller.readBucketlist(bucket_id)
        except Exception as e:
            printf("Error getting bucketlist: ", e)
            return None
    
    def get_allbucketlist(self) -> List[bucketlistEntity]
        """Mengambil semua bucketlist dari database."""
        try:
            return self.db_controller.readallBucketlists()
        except Exception as e:
            printf("Error getting all bucketlist: ", e)
            return None


