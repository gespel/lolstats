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
            $summonerStats = exec("python fetchSummonerData.py '" . $_GET['name'] . "'");
            $summonerStatsArr = explode(".", $summonerStats);
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
                </table>
            ");
        }
        function printSummonerChampions() {
            $championStats = exec("python fetchChampionData.py '" . $_GET['name'] . "'");
            echo($championStats);
        }
        echo("<h3>Summoner</h3>");
        printSummonerStats();
        echo("<h3>Top 5 Champs</h3>");
        printSummonerChampions();
    }
    else {
        echo("<title>LolStats</title>");
    }
?>
</center>

