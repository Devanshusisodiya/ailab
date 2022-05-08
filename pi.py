# APPROXIMATING VALUE OF PI
# THIS GIVES A PRETTY FAIR ESTIMATE OF PI
# BUT DECRESING THE dx FURTHER GIVES MORE ACCURATE ESTIMATION 
# FOR 10000 ITERATIONS GIVES ESTIMATE CORRECT TO 5 DECIMAL PLACES
from math import *

x, y = 0, 1
length = 0

i = dx = 0.1
# SMALLER THE dx, MORE ACCURATE THE ESTIMATION

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

while i < 1:
    base = i
    theta = acos(base)
    perp = sin(theta)
    length += distance(x, y, base, perp)
    x, y = base, perp
    i = i + dx

pi = length * 2
print(pi)
