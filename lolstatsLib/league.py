from enum import Enum
import json
from .networking import Networking

class LeagueTypes(Enum):
    SOLO = "RANKED_SOLO_5x5"
    FLEX = "RANKED_FLEX_SR"
class League:
    def __init__(self, account):
        net = Networking()
        self.leagueJson = json.loads(net.doLeagueRequest(account))
    def getJson(self):
        return self.leagueJson
    def getLeagueId(self, leaguetype):
        return self.leagueJson[leaguetype]["leagueid"]
    def getSummonerId(self, leaguetype):
        return self.leagueJson[leaguetype]["summonerid"]
    def getSummonerName(self, leaguetype):
        return self.leagueJson[leaguetype]["summonerName"]
    def getQueueType(self, leaguetype):
        return self.leagueJson[leaguetype]["queueType"]
    def getTier(self, leaguetype):
        return self.leagueJson[leaguetype]["tier"]
    def getRank(self, leaguetype):
        return self.leagueJson[leaguetype]["rank"]
    def getLeaguePoints(self, leaguetype):
        return self.leagueJson[leaguetype]["leaguePoints"]
    def getWins(self, leaguetype):
        return self.leagueJson[leaguetype]["wins"]
    def getLosses(self, leaguetype):
        return self.leagueJson[leaguetype]["losses"]
    def getHotStreak(self, leaguetype):
        return self.leagueJson[leaguetype]["hotStreak"]
    def getVeteran(self, leaguetype):
        return self.leagueJson[leaguetype]["veteran"]
    def getFreshBlood(self, leaguetype):
        return self.leagueJson[leaguetype]["freshBlood"]
    def getInactive(self, leaguetype):
        return self.leagueJson[leaguetype]["inactive"]

    def getWinLoseRatio(self, leaguetype):
        return float(self.leagueJson[leaguetype]["wins"]) / float(self.leagueJson[leaguetype]["losses"])
    def getWinsInPercent(self, leaguetype):
        return 100 * float(self.leagueJson[leaguetype]["wins"]) / (float(self.leagueJson[leaguetype]["wins"])+float(self.leagueJson[leaguetype]["losses"]))
    def getLossesInPercent(self, leaguetype):
        return (100 * float(self.leagueJson[leaguetype]["losses"]) / (float(self.leagueJson[leaguetype]["wins"])+float(self.leagueJson[leaguetype]["losses"])))

    def printLeagueInfoToHTML(self):
        out = "<table border='1'><tr><th>Type</th><th>League</th><th>Points</th></tr>"
        for liga in self.leagueJson:
            if liga["queueType"] == "RANKED_FLEX_SR":
                a = "Flex"
            if liga["queueType"] == "RANKED_SOLO_5x5":
                a = "Solo"
            out += "<tr><td>" + a + "</td><td>" + liga["tier"].lower().capitalize() + " " + str(liga["rank"]) + "</td><td>" + str(liga["leaguePoints"]) + "</td></tr>"
        out += "</table>"
        return out