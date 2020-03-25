import requests
from enum import Enum
import json

keyfile = open("api.key","r")
api_key = keyfile.readline().split('\n')

header = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": str(api_key[0]),
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"
}

class Account:
	def __init__(self, accountName):
		r = requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+accountName, headers=header)
		self.accountJson = json.loads(r.content.decode('utf-8'))
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

class LeagueTypes(Enum):
	SOLO = "RANKED_SOLO_5x5"
	FLEX = "RANKED_FLEX_SR"

class League:
	def __init__(self, account, leaguetype):
		l = requests.get("https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + account.getId(), headers=header)
		self.leagueJson = json.loads(l.content.decode('utf-8'))
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

class Champions:
	def __init__(self, account):
		r = requests.get("https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"+account.getId(), headers=header)
		self.championsJson = json.loads(r.content)
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
