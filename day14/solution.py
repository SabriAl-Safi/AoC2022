from itertools import pairwise
from functools import reduce

def parseCorner(s): return tuple(map(int, s.split(',')))
def parsePath(s): return list(map(parseCorner, s.split('->')))
def vecAdd(a, b): return ( a[0]+b[0], a[1]+b[1] )
def nRange(n): return range(n+1) if n > 0 else range(n, 1)
def vecRange(c): return set([vecAdd(c[0], (i, j))
                         for i in nRange(c[1][0]-c[0][0])
                         for j in nRange(c[1][1]-c[0][1])])
def pathCells(s): return reduce(set.union, map(vecRange, pairwise(parsePath(s))))

paths = list(map(pathCells, open('input.txt', 'r').readlines()))
rock = reduce(set.union, paths)
bottom = max([r[1] for r in rock])
s = (500, 0)
num = 0
d = (0, 1)
dl = (-1, 1)
dr = (1, 1)

## Part 1
while s[1] <= bottom:

    n = vecAdd(s, d)
    if n not in rock:
        s = n
        continue

    n = vecAdd(s, dl)
    if n not in rock:
        s = n
        continue

    n = vecAdd(s, dr)
    if n not in rock:
        s = n
        continue

    rock.add(s)
    num += 1
    s = (500, 0)

print(num)

## Part 2
rock = reduce(set.union, paths)
depth = 2 + max([r[1] for r in rock])
s = (500, 0)
num = 0
d = (0, 1)
dl = (-1, 1)
dr = (1, 1)

## Part 1
while (500, 0) not in rock:
    if s[1] + 1 == depth:
        rock.add(s)
        num+=1
        s = (500, 0)
        continue

    n = vecAdd(s, d)
    if n not in rock:
        s = n
        continue

    n = vecAdd(s, dl)
    if n not in rock:
        s = n
        continue

    n = vecAdd(s, dr)
    if n not in rock:
        s = n
        continue

    rock.add(s)
    num += 1
    s = (500, 0)

print(num)
