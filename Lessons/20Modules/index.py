# module = a file containing code you want to include in your program
#          use import to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

import platform
# import math
# import math as m
# from math import *
# Not recommended due to conflict of variable name
from math import pi

import calculator as cal

print(pi)
print(cal.add(20, 10))
print(cal.sub(20, 10))
print(cal.velocity)
print(cal.admin)

x = platform.system()
print(x)

print(dir(cal))
