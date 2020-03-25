import sys
from lolstatsLib import *

a = Account(sys.argv[1])
print(a.getName() + "." + str(a.getLevel()))
