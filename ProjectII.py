from datetime import datetime
import random

def getTime():
    t = datetime.now()
    return t.microsecond

def benchmarkTime(method,input):
    t = getTime()
    c = method(input)
    return getTime()- t ,c

def benchmark(method,input,n):
    t = 0
    for i in range(n):
        b = benchmarkTime(method,input)
        t += b[0]
    return t/n , b[1:]

def min(L):
    if len(L) == 1:
        c = L.pop(0)
        return c
    else:
        a = L.pop(0)
        c = min(L)
        if a <= c: c = a
    return c

def min2(L):
    if len(L) == 1:
        return L[0]
    else:
        c = min2(L[1:])
        return c if c < L[0] else L[0]

def min3(L):
    for i in range(len(L)):
        if i == 0: c = L[0]
        elif L[i] < c: c = L[i]
    return c

def farthestPair(L):
    for i in range(len(L)):
        if i == 0:
            c = L[0] ; d = L[0]
        else:
            if L[i] < c: c = L[i] ; i1 = i
            if L[i] > d: d = L[i] ; i2 = i
    return c ,i1, d,i2

def binarySearch():


    return

def binarySort():

    return

b = range(0,10**3,3)
random.shuffle(b)
print benchmark(min2,b,10)
print benchmark(min3,b,10)
d = farthestPair(b)
print d
print b[d[1]]
