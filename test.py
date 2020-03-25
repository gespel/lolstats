import sys
from lolstatsLib import *

a = Account(sys.argv[1])
c = Champions(a)
l = League(a, LeagueTypes.SOLO)
print(l.getWinLoseRatio())