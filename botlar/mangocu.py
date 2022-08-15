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

    def bir_uye_filtrele_guncelle(self, filtre, guncelle):
        """bir uyeyi filtreler ve gunceller"""

        return self.user.find_one_and_update(filtre, guncelle)


    class Cuzdan:
        def __init__(self, rcc: int, rsc: int, ibo: int, rccp: int, rscp: int, ibop: int, kgt: int) -> None:
            self.ricardo = rcc
            self.risitas = rsc
            self.ibo = ibo
            self.pending_ricardo = rccp
            self.pending_risitas = rscp
            self.pending_ibo = ibop
            self.kgt = kgt

    class Deste:
        def __init__(self, kullanici, deste={}) -> None:
            self.mangocu = Mangocu.sikleton()
            self.deste=deste
            self.kullanici=kullanici

        def varmi(self, no: int):
            return no in self.deste.keys() and self.deste[no] > 0

        def varsa_azalt(self, no: int):
            """kart varsa bir azaltir ve true doner"""
            return None != self.mangocu.bir_uye_filtrele_guncelle(
                #{"id": self.kullanici["id"], "deste": {no: {"$gt": 0}}},
                #{"$inc", {"deste": {no: -1}}}
                {"id": self.kullanici["id"], f"kart_{no}": {"$gt": 0}},
                {"$inc": {f"kart_{no}": -1}}
            )

    class Uye:
        def __init__(self, id: int, mangocu) -> None:
            self.id = str(id)
            self.mangocu: Mangocu = mangocu

        def bul(self):
            return self.mangocu.uyeyi_bul(self.id)
        def varmi(self, nitelik: str, nicelik: int=1):
            return None != self.mangocu.user.find_one({"id": self.id, nitelik: {"$gte": nicelik}})

        def guncelle(self, sorgu):
            return self.mangocu.uyeyi_yarat_guncelle(self.id, sorgu)
        def ver(self, nitelik: str, nicelik: int = 1):
            return self.mangocu.uyeyi_yarat_guncelle(self.id, {"$inc": {nitelik: nicelik}})
        def hepsini_ver(self, nitel_nicel):
            return self.mangocu.uyeyi_yarat_guncelle(self.id, {"$inc": nitel_nicel})
            
        def ez(self, nitelik: str, nicelik: int):
            return self.mangocu.uyeyi_yarat_guncelle(self.id, {"$set": {nitelik: nicelik}})

        def varsa_azalt(self, nitelik: str, nicelik: int = 1):
            return None != self.mangocu.bir_uye_filtrele_guncelle(
                {"id": self.id, nitelik: {"$gte": nicelik}},
                {"$inc": {nitelik: -1*nicelik}}
            )
        def hepsi_varsa_azalt(self, nitel_nicel):
            return None != self.mangocu.bir_uye_filtrele_guncelle(
                {"id": self.id}|{nitelik: {"$gte": nicelik} for nitelik, nicelik in nitel_nicel.items()},
                {"$inc": {nitelik: -1*nicelik for nitelik, nicelik in nitel_nicel.items()}}
            )

        def kgt(self):
            kullanici = self.bul()
            kgt = kullanici.get("kgt") or 0
            simdi = int(datetime.datetime.utcnow().timestamp())
            sure = 23 * 60 * 60
            if simdi < sure + kgt:
                return False
            self.ez("kgt", simdi)
            self.ver("karanlik_guc_")
            self.ver("risitas_coin_pending", 500)
            return True

        def cuzdan(self):
            kullanici = self.bul()
            rcc = 0 
            rsc = 0 
            ibo = 0
            rccp = 0 
            rscp = 0
            ibop = 0
            kgt = 0
            if kullanici is not None:
                rcc = kullanici.get("ricardo_coin") or 0
                rsc = kullanici.get("risitas_coin") or 0
                ibo = kullanici.get("ibo_coin") or 0
                rccp = kullanici.get("ricardo_coin_pending") or 0
                rscp = kullanici.get("risitas_coin_pending") or 0
                ibop = kullanici.get("ibo_coin_pending") or 0
                kgt = kullanici.get("karanlik_guc") or 0
            return Mangocu.Cuzdan(rcc, rsc, ibo, rccp, rscp, ibop, kgt)

        def deste(self):
            kullanici = self.bul()
            deste = {}
            if kullanici is not None:
                deste = kullanici.get("deste") or {}
            return Mangocu.Deste(kullanici, deste=deste)


    def uye(self, id: int):
        return self.Uye(id, self)
