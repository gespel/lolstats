from .networking import Networking
from .champions import *
from .account import Account
from .league import League
import json

class Player:
    def __init__(self, entry):
        self.teamId = entry["teamId"]
        self.championId = entry["championId"]
        self.name = entry["summonerName"]
    def getLevel(self):
        a = Account(self.name)
        return a.getLevel()
    def getTeam(self):
        if(self.teamId == 100):
            return "Red"
        if(self.teamId == 200):
            return "Blue"
    def getName(self):
        return self.name
    def getChampionId(self):
        return self.championId
    def getChampion(self):
        champ = Champion(str(self.championId))
        return str(champ.championName)
    def getChampionPoints(self):
        champs = Champions(self.name)
        return str(champs.getChampionScore())

class BlueTeam:
    def __init__(self):
        self.players = []
        return None
    def addPlayer(self, p):
        self.players.append(p)
    def getList(self):
        return self.players
    def printList(self):
        for p in self.players:
            print(p.getName() + " " + str(p.getLevel()))
    def printTeamToHTML(self):
        out = "<tr>"
        for p in self.players:
            out += "<td><a href='index.php?name=" + p.getName() + "&summoner=Summoner'>" + p.getName() + "</a><br>Level: " + str(p.getLevel()) + "<br>" + str(p.getChampion()).capitalize() + " (" + p.getChampionPoints() + ")" + "</td>"
        out += "</tr>"
        return out

class RedTeam:
    def __init__(self):
        self.players = []
        return None
    def addPlayer(self, p):
        self.players.append(p)
    def getList(self):
        return self.players
    def printList(self):
        for p in self.players:
            print(p.getName() + " " + str(p.getLevel()))
    def printTeamToHTML(self):
        out = "<tr>"
        for p in self.players:
            out += "<td><a href='index.php?name=" + p.getName() + "&summoner=Summoner'>" + p.getName() + "</a><br>Level: " + str(p.getLevel()) + "<br>" + str(p.getChampion()).capitalize() + " (" + p.getChampionPoints() + ")" + "</td>"
        out += "</tr>"
        return out

class Game:
    def __init__(self, account):
        net = Networking()
        self.gameJson = json.loads(net.doGameRequest(account))
    def getJson(self):
        return self.gameJson
    def getGameType(self):
        return self.gameJson["gameType"]
    def printGameInfoToHTML(self):
        out = ""
        bT = BlueTeam()
        rT = RedTeam()

        for player in self.gameJson["participants"]:
            p = Player(player)
            if p.getTeam() == "Red":
                rT.addPlayer(p)
            if p.getTeam() == "Blue":
                bT.addPlayer(p)

        out += "<table border='1'>"
        out += "<th colspan='5'>Red</th>"
        out += str(rT.printTeamToHTML())
        out += "<th colspan='5'>Blue</th>"
        out += str(bT.printTeamToHTML())
        out += "</table>"
        return out



