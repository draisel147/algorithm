# week6 rev3 page 17
import random as rd
a1 = []
n = int(input())
for i in range(n):
    a1.append(rd.randint(1,5))
print(a1)

def presortmode(a):
    a.sort()
    n = len(a)
    i = 0 
    modefrequency = 0 
    while i <= n-1:
        runlength = 1
        runvalue = a[i]
        while i + runlength <= n -1 and a[i + runlength] == runvalue:
            runlength = runlength + 1
        if runlength > modefrequency:
            modefrequency = runlength
            modevalue = runvalue
        i = i + runlength
    return modevalue
print(presortmode(a1))