import sys
from lolstatsLib.league import *
from lolstatsLib.account import *

a = Account(sys.argv[1])
l = League(a)
print(l.printLeagueInfoToHTML())
