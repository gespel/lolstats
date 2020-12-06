import sys
from lolstatsLib.account import *
from lolstatsLib.league import *
from lolstatsLib.champions import *

a = Account(sys.argv[1])
l = League(a, LeagueTypes.SOLO)
c = Champions(a)

#print(a.getLevel())
#print(l.getTier())
c.printChampionScoreAndLevelWithNames()
