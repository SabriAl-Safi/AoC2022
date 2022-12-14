moves = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]

def vecAdd(a, b): return (a[0]+b[0], a[1]+b[1])
def vecSub(a, b): return (a[0]-b[0], a[1]+b[1])
def gradual(s, t, m): return m[s[0]][s[1]] >= m[t[0]][t[1]] - 1
def inBounds(t, m): return 0<=t[0]<len(m) and 0<=t[1]<len(m[1])
def validStep(s, t, m): return inBounds(t, m) and gradual(s, t, m)
def steps(s, hmap):
    return list(filter(
        lambda t: validStep(s, t, hmap),
        [vecAdd(s, m) for m in moves]))
def validReverseStep(s, t, m): return inBounds(t, m) and gradual(t, s, m)
def reverseSteps(s, hmap):
    return list(filter(
        lambda t: validReverseStep(s, t, hmap),
        [vecAdd(s, m) for m in moves]))
def matIdxOf(c, m):
    return next(iter([(i, j) for i in range(len(m)) for j in range(len(m[i])) if m[i][j] == c]))
    
hmap = [ list(map(ord,_.strip())) for _ in open('input.txt', 'r').readlines()]

## Part 1
s = matIdxOf(ord('S'), hmap)
e = matIdxOf(ord('E'), hmap)
hmap[s[0]][s[1]] = ord('a')
hmap[e[0]][e[1]] = ord('z')

dist = { s: 0 }
boundary = [s]

while(len(boundary)):
    v = boundary.pop(0)
    d = dist[v]
    for t in steps(v, hmap):
        if t in dist:
            continue
        dist[t] = d + 1
        boundary.append(t)
print(dist[e])

## Part 2
dist = { e: 0 }
boundary = [e]

while(len(boundary)):
    v = boundary.pop(0)
    d = dist[v]
    for t in reverseSteps(v, hmap):
        if t in dist:
            continue
        dist[t] = d + 1
        boundary.append(t)
        if hmap[t[0]][t[1]] == ord('a'):
            print(t, d+1)
            boundary = []
            break
