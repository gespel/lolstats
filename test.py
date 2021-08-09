import sys
from lolstatsLib.account import *
from lolstatsLib.league import *
from lolstatsLib.champions import *
from lolstatsLib.game import *

a = Account(sys.argv[1])
print(a.getSkillLevel())
#l = League(a)
#c = Champions(a)

#print(g.getJson())
#g.printGameInfoToHTML()
#print(l.getLossesInPercent())
#print(c.championListToHTMLTable())
