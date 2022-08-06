from alayina_gider import ortamaBirBak
import pymongo

class Mangocu:

    def __init__(self) -> None:
        self.cluster = pymongo.MongoClient(ortamaBirBak("TPBOT_MONGO"))
        self.db      = self.cluster["mongodb_tp"]
        self.user    = self.db["users"]

    def uyeyi_bul(self,id: str):
        """uyeyi bulur yoksa None doner"""
        return self.user.find_one({"id":str(id)})

    def uyeyi_guncelle(self,id: str, json):
        """uyeyi mongo db $ update formatinda gunceller, yoksa olusturur"""

        self.user.find_one_and_update({"id":str(id)}, json, upsert=True)