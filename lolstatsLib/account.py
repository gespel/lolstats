import json
from .networking import Networking

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