from alayina_gider import ortamaBirBak
import pymongo
import datetime

class Mangocu:

    def __init__(self) -> None:
        if Mangocu.sik is not None:
            raise Exception("hassikleton")
        Mangocu.sik = self
        self.cluster = pymongo.MongoClient(ortamaBirBak("TPBOT_MONGO"))
        self.db      = self.cluster["mongodb_tp"]
        self.user    = self.db["users"]
        

    sik = None
    @staticmethod
    def sikleton():
        if Mangocu.sik is None:
            Mangocu()
        return Mangocu.sik

    def uyeyi_bul(self,id: str):
        """uyeyi bulur yoksa None doner"""
        return self.user.find_one({"id":str(id)})

    def uyeyi_yarat_guncelle(self,id: str, json):
        """uyeyi mongo db $ update formatinda gunceller, yoksa olusturur"""

        self.user.find_one_and_update({"id":str(id)}, json, upsert=True)


    class Cuzdan:
        def __init__(self, rcc: int, rsc: int, ibo: int, rccp: int, rscp: int, ibop: int, kgt: int) -> None:
            self.ricardo = rcc
            self.risitas = rsc
            self.ibo = ibo
            self.pending_ricardo = rccp
            self.pending_risitas = rscp
            self.pending_ibo = ibop
            self.kgt = kgt
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
        def ez(self, nitelik: str, nicelik: int):
            return self.mangocu.uyeyi_guncelle(self.id, {"$set": {nitelik: nicelik}})

        def kgt(self):
            kullanici = self.bul()
            kgt = kullanici.get("kgt") or 0
            simdi = int(datetime.datetime.utcnow().timestamp())
            sure = 23 * 60 * 60
            if simdi < sure + kgt:
                return False
            self.ez("kgt", simdi)
            self.ver("karanlik_guc_", 1)
            return True

        def cuzdan(self):
            kullanici = self.bul()
            rcc = 0; rsc = 0; rccp = 0; rscp = 0
            if kullanici is not None:
                rcc = kullanici.get("ricardo_coin") or 0
                rsc = kullanici.get("risitas_coin") or 0
                ibo = kullanici.get("ibo_coin") or 0
                rccp = kullanici.get("ricardo_coin_pending") or 0
                rscp = kullanici.get("risitas_coin_pending") or 0
                ibop = kullanici.get("ibo_coin_pending") or 0
                kgt = kullanici.get("karanlik_guc") or 0
            return Mangocu.Cuzdan(rcc, rsc, ibo, rccp, rscp, ibop)

    def uye(self, id: int):
        return self.Uye(id, self)
