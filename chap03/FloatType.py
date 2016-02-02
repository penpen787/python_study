__author__ = 'PenPen'
#Float Type
a = 1.2
print(type(a))

b = 3e3
print(b)

c = -0.2e-04
print(c)

import sys
print(sys.float_info)

# Infinite
print(float('inf'))
print(float('-inf'))
inf = float('inf')

print(inf/1000*float('-inf'))

# Check Float -> Int without Error
a = 1.2
b = 2.0
print(a.is_integer())
print(b.is_integer())

# Round , Ceil , Floor
print(round(1.2))
print(round(-1.2))

import math
print(math.ceil(1.2))
print(math.ceil(-1.2))
print(math.floor(1.2))
print(math.floor(-1.2))

# Float calculate Error
print(1.1+2.2)
print(1.1*6)