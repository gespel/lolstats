<?php
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
		    <th>Skillpoints</th>
		</tr>
                <tr>
                    <td>$summonerStatsArr[0]</td>
		    <td>$summonerStatsArr[1]</td>
		    <td><b>$summonerStatsArr[2]</b></td>
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
    function printGameInfo() {
        $gameInfo = exec("python3 fetchGameData.py '" . $_GET['name'] . "'");
        echo("<h1>Game</h1>");
        echo($gameInfo);
    }
    function main() {
        if($_GET['name'] != NULL) {
            echo("<title>LolStats - ".$_GET['name']."</title>");

            if(isset($_GET['summoner'])) {
                printSummonerStats();
                printLeagueInfo();
                printSummonerChampions();
            }
            if(isset($_GET['game'])) {
                printGameInfo();
            }
        }
        else {
            echo("<title>LolStats</title>");
        }
    }
?>
<!DOCTYPE HTML>
<!--
	Caminar by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
-->
<html>
	<head>
		<title>LolStats</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="assets/css/main.css" />
	</head>
	<body>

		<!-- Header -->
			<header id="header">
				<div class="logo"><a href="#">LolStats <span>by Sten Heimbrodt</span></a></div>
			</header>

		<!-- Main -->
			<section id="main">
				<div class="inner">

				<!-- One -->
					<section id="two" class="wrapper style1">
						<div class="content">
								<center>
                                    <form action = "index.php" method = "get" />
                                        <p>Enter the summoner name:</p>
                                        <input type = "text" name = "name" />
                                        <br>
                                        <input type = "submit" name = "game" value = "Game"/>
                                        <input type = "submit" name = "summoner" value = "Summoner"/>
                                    </form>
								</center>
								<?php main(); ?>
						</div>
					</section>
		<!-- Footer -->
			<footer id="footer">
				<div class="container">
					<ul class="icons">
						<li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
						<li><a href="#" class="icon fa-facebook"><span class="label">Facebook</span></a></li>
						<li><a href="#" class="icon fa-instagram"><span class="label">Instagram</span></a></li>
						<li><a href="#" class="icon fa-envelope-o"><span class="label">Email</span></a></li>
					</ul>
				</div>
				<div class="copyright">
					&copy; LolStats. All rights reserved. Images <a href="https://unsplash.com">Unsplash</a> Design <a href="https://templated.co">TEMPLATED</a>
				</div>
			</footer>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.poptrox.min.js"></script>
			<script src="assets/js/skel.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>
