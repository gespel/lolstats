<center>
<form action = "index.php" method = "get" />
	<p>Gib den Beschwörernamen an:</p>
	<input type = "text" name = "name" />
	<input type = "submit" />
</form>
<?php
    if($_GET['name'] != NULL) {
        echo("<title>LolStats - ".$_GET['name']."</title>");
        function printSummonerStats() {
            $summonerStats = exec("python3 fetchSummonerData.py '" . $_GET['name'] . "'");
            $summonerStatsArr = explode(".", $summonerStats);
            echo("<h1>Summoner</h1>");
            echo
            ("
                <table border='1'>
                    <tr>
                        <th>Name</th>
                        <th>Level</th>
                    </tr>
                    <tr>
                        <td>$summonerStatsArr[0]</td>
                        <td>$summonerStatsArr[1]</td>
                    </tr>
                </table><br>
            ");
        }
        function printSummonerChampions() {
            $championStats = exec("python3 fetchChampionData.py '" . $_GET['name'] . "'");
            echo("<h1>Champions</h1>");
            echo($championStats);
        }
        function printLeagueInfo() {
            $leagueInfo = exec("python3 fetchLeagueData.py '" . $_GET['name'] . "'");
            echo("<h1>Ranked</h1>");
            echo($leagueInfo);
        }
        printSummonerStats();
        printLeagueInfo();
        printSummonerChampions();
    }
    else {
        echo("<title>LolStats</title>");
    }
?>
</center>

