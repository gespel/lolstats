#!/usr/bin/env python3
import sys
from lolstatsLib.account import *
from lolstatsLib.league import *
from lolstatsLib.champions import *

a = Account(sys.argv[1])
c = Champions(a)
print(c.championListToHTMLTable())