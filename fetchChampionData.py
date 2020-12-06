import sys
from lolstatsLib import *

a = Account(sys.argv[1])
c = Champions(a)
print(c.championListToHTML(c.getTopChampions(5)))