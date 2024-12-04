from typing import List, Optional

from models.databaseEntity import DatabaseEntity
from models.bucketlistEntity import BucketlistEntity

class DatabaseBucketlistController:

    def __init__(self, database_entity:DatabaseEntity):
        self.database_entity = database_entity


    def createBucketlist(self, Bucketlist: BucketlistEntity):
        """Menambahkan bucketList baru ke database."""
        self.database_entity.addData(
            "bucketList",
            judul       = Bucketlist.judul,
            nama_negara = Bucketlist.nama_negara,
            nama_kota   = Bucketlist.nama_kota,
            deskripsi   = Bucketlist.deskripsi
        )


    def readallBucketlists(self) -> List[BucketlistEntity]:
        """Membaca seuluruh bucketList dalam bentuk List."""
        bucketlistsData = self.database_entity.getData("bucketList")
        return [BucketlistEntity(**data) for data in bucketlistsData]


    def readBucketlist(self, bucketlistID: int) -> BucketlistEntity:
        """Membaca satu jurnal berdasarkan ID-nya."""
        bucketlist = self.database_entity.getData("bucketList", id=bucketlistID)
        return BucketlistEntity(
            id                      = bucketlist[0].get("id"),
            judul                   = bucketlist[0].get("judul"),
            nama_negara             = bucketlist[0].get("nama_negara"),
            nama_kota               = bucketlist[0].get("nama_kota"),
            tanggal_perjalanan      = bucketlist[0].get("tanggal_perjalanan"),
            deskripsi_perjalanan    = bucketlist[0].get("deskripsi_perjalanan")
        )


    def updateBucketlist(self, updated_bucketlist: BucketlistEntity):
        """Mengubah entri jurnal pada ID tertentu."""
        self.database_entity.setData("bucketList", {"id":updated_bucketlist.id},
                                        judul       = updated_bucketlist.judul,
                                        nama_negara = updated_bucketlist.nama_negara,
                                        nama_kota   = updated_bucketlist.nama_kota,
                                        deskripsi   = updated_bucketlist.deskripsi)


    def deleteBucketlist(self, bucketlistID: int):
        """Menghapus jurnal dengan ID tertentu dari database."""
        self.database_entity.delData("bucketList", id=bucketlistID)