#!/usr/bin/python

import sys

a = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

def usage():
    print "./doublehornereval <n> <v>"    

def comp_poly(n, v, a):
    actualpos = 0
    actualneg = 0
    for i in range(n, -1, -1):
        actualpos = actualpos + a[i]*pow(v, i)
        actualneg = actualneg + a[i]*pow(-v, i)
    return {actualpos, actualneg}

if (len(sys.argv) != 3):
    usage()
    sys.exit()

n = int(sys.argv[1])
v = int(sys.argv[2])

sumodd = 0
sumeven = 0
actualpos = 0
actualneg = 0

if (n % 2 == 0):
    sumeven = a[n]
else:
    sumodd = a[n]

squared = v*v   #one multiply

for i in range(n, 0, -1): 
    if (i % 2 == 0):
        sumeven = sumeven*squared
        sumodd = sumodd + a[i-1]
    else:
        sumeven = sumeven + a[i-1]
        if (i == 1):
            sumodd = sumodd*v
        else:
            sumodd = sumodd*squared


finaleven = sumeven + sumodd 
finalodd = sumeven - sumodd 

actual = comp_poly(n, v, a)
print "ActualNeg: " + str(actual.pop())
print "ActualPos: " + str(actual.pop())
print "AlgoNeg:   " + str(finalodd)
print "AlgoPos:   " + str(finaleven)
print "sumodd:    " + str(sumodd)
print "sumeven:   " + str(sumeven)
