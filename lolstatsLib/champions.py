import json
from .networking import Networking

class Champion:
    def __init__(self, id):
        self.championName = self.getNameById(id)
        self.id = id
    def getNameById(self, Id):
        with open('champion.json', encoding='utf-8') as fh:
            championsData = json.load(fh)
        for champion in championsData:
            if champion["key"] == Id:
                return champion["id"]

class Champions:
    def __init__(self, account):
        net = Networking()
        self.championsJson = json.loads(net.doChampionsRequest(account))
        #self.championsJson
    def getJson(self):
        return self.championsJson
    def getNameById(self, Id):
        with open('champion.json', encoding='utf-8') as fh:
            championsData = json.load(fh)
        #fh = open("champion.json")
        #championsData = json.load(fh)
        for champion in championsData:
            if champion["key"] == Id:
                return champion["id"]
    def printChampionScoreAndLevelWithNames(self):
        #print(self.championsJson)
        for champion in self.championsJson:
            print(str(self.getNameById(str(champion["championId"]))) + " " + str(champion["championLevel"])  + " " + str(champion["championPoints"]))
    def printChampionScoreAndLevelWithNamesToHTML(self):
        #print(self.championsJson)
        for champion in self.championsJson:
            print(str(self.getNameById(str(champion["championId"]))) + " " + str(champion["championLevel"])  + " " + str(champion["championPoints"]) + "<br>")
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
    def championListToHTMLTable(self):
        icon = ""
        name = ""
        with open('champion.json', encoding='utf-8') as fh:
            championsData = json.load(fh)
        #print(championsData['data'])
        out = "<table border='1'><tr><th></th><th>Champion</th><th>Level</th><th>Points</th></tr>"
        for champion in self.championsJson:
            for champion2 in championsData["data"]:
                if championsData["data"][champion2]["key"] == str(champion["championId"]):
                    icon = championsData["data"][champion2]["image"]["full"]
                    name = championsData["data"][champion2]["id"]
            out += "<tr><td><img src='http://ddragon.leagueoflegends.com/cdn/11.15.1/img/champion/" + icon + "' style='width:48px;height:48px;'></td><td>" + name + "</td><td>" + str(champion["championLevel"]) + "</td><td>" + str(champion["championPoints"]) + "</td></tr>"
        out += "</table>"
        return out
    def getChampionScore(self, name):
        for champion in self.championsJson:
            if str(self.getNameById(str(champion["championId"]))) == name:
                return champion["championPoints"]
        return 0
