import sys
from lolstatsLib.account import *

a = Account(sys.argv[1])
print(a.getName() + "." + str(a.getLevel()) + "." + str(a.getSkillLevel()))
