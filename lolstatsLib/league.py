from enum import Enum
import json
from .networking import Networking

class LeagueTypes(Enum):
    SOLO = "RANKED_SOLO_5x5"
    FLEX = "RANKED_FLEX_SR"
class League:
    def __init__(self, account, leaguetype):
        net = Networking()
        self.leagueJson = json.loads(net.doLeagueRequest(account))
        for i in range(0, len(self.leagueJson)):
            if self.leagueJson[i]['queueType'] == str(leaguetype.value):
                self.leagueJson = self.leagueJson[i]
    def getJson(self):
        return self.leagueJson
    def getLeagueId(self):
        return self.leagueJson["leagueid"]
    def getSummonerId(self):
        return self.leagueJson["summonerid"]
    def getSummonerName(self):
        return self.leagueJson["summonerName"]
    def getQueueType(self):
        return self.leagueJson["queueType"]
    def getTier(self):
        return self.leagueJson["tier"]
    def getRank(self):
        return self.leagueJson["rank"]
    def getLeaguePoints(self):
        return self.leagueJson["leaguePoints"]
    def getWins(self):
        return self.leagueJson["wins"]
    def getLosses(self):
        return self.leagueJson["losses"]
    def getHotStreak(self):
        return self.leagueJson["hotStreak"]
    def getVeteran(self):
        return self.leagueJson["veteran"]
    def getFreshBlood(self):
        return self.leagueJson["freshBlood"]
    def getInactive(self):
        return self.leagueJson["inactive"]

    def getWinLoseRatio(self):
        return int(self.leagueJson["wins"]) / int(self.leagueJson["losses"])
    def getWinsInPercent(self):
        return 100 * int(self.leagueJson["losses"]) / (int(self.leagueJson["wins"])+int(self.leagueJson["losses"]))
    def getLossesInPercent(self):
        return 100 * int(self.leagueJson["losses"]) / (int(self.leagueJson["wins"])+int(self.leagueJson["losses"]))
