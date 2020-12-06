import json
from .networking import Networking

class Champions:
    def __init__(self, account):
        net = Networking()
        self.championsJson = json.loads(net.doChampionsRequest(account))
    def getJson(self):
        return self.championsJson
    def getNameById(self, Id):
        with open('champion.json', encoding='utf-8') as fh:
            championsData = json.load(fh)
        #fh = open("champion.json")
        #championsData = json.load(fh)
        for champion in championsData["data"]:
            if championsData["data"][champion]["key"] == Id:
                return champion
    def printChampionScoreAndLevelWithNames(self):
        for champion in self.championsJson:
            print(str(self.getNameById(str(champion["championId"]))) + " " + str(champion["championLevel"])  + " " + str(champion["championPoints"]))
    def getChampionList(self):
        L = []
        for champion in self.championsJson:
            L.append(self.getNameById(str(champion["championId"])))
        return L
    def getTopChampions(self, n):
        L = []
        for champion in self.championsJson:
            L.append(self.getNameById(str(champion["championId"])))
        return L[:n]
    def championListToHTML(self, L):
        out = "<table border='1'><tr><th>Champion</th><th>Points</th></tr>"
        for item in L:
            out += "<tr><td>" + item + "</td><td>" + str(self.getChampionScore(item)) + "</td></tr>"
        out += "</table>"
        return out
    def getChampionScore(self, name):
        for champion in self.championsJson:
            if str(self.getNameById(str(champion["championId"]))) == name:
                return champion["championPoints"]
        return 0
