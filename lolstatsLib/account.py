import json
from .networking import Networking
from .league import *

class Account:
    def __init__(self, accountName):
        net = Networking()
        self.accountJson = json.loads(net.doAccountRequest(accountName))
    def getJson(self):
        return self.accountJson
    def getProfileIconId(self):
        return self.accountJson["profileIconId"]
    def getName(self):
        return self.accountJson["name"]
    def getLevel(self):
        return self.accountJson["summonerLevel"]
    def getPuuid(self):
        return self.accountJson["puuid"]
    def getAccountId(self):
        return self.accountJson["accountId"]
    def getId(self):
        return self.accountJson["id"]
    def getRevisionDate(self):
        return self.accountJson["revisionDate"]
    def getSkillLevel(self):
        l = League(self)
        soloTier = l.getTier(0)
        flexTier = l.getTier(1)
        soloBase = 0
        flexBase = 0
        skillLevel = 1

        if(soloTier == "IRON"):
            soloBase = 100
        elif(soloTier == "BRONZE"):
            soloBase = 200
        elif(soloTier == "SILVER"):
            soloBase = 300
        elif(soloTier == "GOLD"):
            soloBase = 400
        elif(soloTier == "PLATINUM"):
            soloBase = 750
        elif(soloTier == "DIAMOND"):
            soloBase = 1000
        else:
            soloBase = 80

        if(flexTier == "IRON"):
            flexBase = 100
        elif(flexTier == "BRONZE"):
            flexBase = 200
        elif(flexTier == "SILVER"):
            flexBase = 300
        elif(flexTier == "GOLD"):
            flexBase = 400
        elif(flexTier == "PLATINUM"):
            flexBase = 750
        elif(flexTier == "DIAMOND"):
            flexBase = 1000
        else:
            flexBase = 80

        skillLevel = soloBase + flexBase + self.getLevel()*2
        return skillLevel
