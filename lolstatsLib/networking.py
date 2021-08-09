import requests

class Networking:
    keyfile = open("api.key", "r")
    api_key = keyfile.readline().split('\n')

    header = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": str(api_key[0]),
        "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"
    }
    def doAccountRequest(self, accountName):
        return requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + accountName, headers=self.header).content.decode('utf-8')
    def doLeagueRequest(self, account):
        return requests.get("https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + account.getId(), headers=self.header).content.decode('utf-8')
    def doChampionsRequest(self, account):
        return requests.get("https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + account.getId(), headers=self.header).content.decode('utf-8')
    def doGameRequest(self, account):
        return requests.get("https://euw1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + account.getId(), headers=self.header).content.decode('utf-8')