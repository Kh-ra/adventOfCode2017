from math import *

global data
global ring

data = int(input())

data -= 1

# The ring that the data is in.
ring = floor((sqrt(data) + 1)/2)    

def quarter(x):
    return ring*(4*ring + x)

possibleDistance = [abs(quarter(-3) - data), abs(quarter(-1) - data), abs(quarter(1) - data), abs(quarter(3) - data)]

print("Dist:", ring + min(possibleDistance))
