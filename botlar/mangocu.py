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


    class Cuzdan:
        def __init__(self, rcc: int, rsc: int, rccp: int, rscp: int) -> None:
            self.ricardo = rcc
            self.risitas = rsc
            self.pending_ricardo = rccp
            self.pending_risitas = rscp
    class Uye:
        def __init__(self, id: int, mangocu) -> None:
            self.id = str(id)
            self.mangocu: Mangocu = mangocu

        def bul(self):
            return self.mangocu.uyeyi_bul(self.id)
        def guncelle(self, sorgu):
            return self.mangocu.uyeyi_guncelle(self.id, sorgu)
        def ver(self, nitelik: str, nicelik: int):
            return self.mangocu.uyeyi_guncelle(self.id, {"$inc": {nitelik: nicelik}})
        def cuzdan(self):
            kullanici = self.bul()
            rcc = 0; rsc = 0; rccp = 0; rscp = 0
            if kullanici is not None:
                rcc = kullanici.get("ricardo_coin") or 0
                rsc = kullanici.get("risitas_coin") or 0
                rccp = kullanici.get("ricardo_coin_pending") or 0
                rscp = kullanici.get("risitas_coin_pending") or 0
            return Mangocu.Cuzdan(rcc, rsc, rccp, rscp)

    def uye(self, id: int):
        return self.Uye(id, self)
