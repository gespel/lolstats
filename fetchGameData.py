import sys
from lolstatsLib.game import *
from lolstatsLib.account import *

a = Account(sys.argv[1])
g = Game(a)
print(g.printGameInfoToHTML())