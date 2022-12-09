
def getVis(a):
    n = len(a)
    v = [0 for _ in a]
    ml = mr = -1
    for i in range(n):
        if a[i] > ml:
            v[i] = 1
            ml = a[i]
        if a[n-1-i] > mr:
            v[n-1-i] = 1
            mr = a[n-1-i]
    return v

def getScore(a):
    s = [0 for _ in a]
    for i in range(1, len(a)):
        j = 1
        while s[i-j] > 0 and a[i-j] < a[i]:
            j += s[i-j]
        s[i] = j
    return s

def getRevScore(a):
    return getScore(a[::-1])[::-1]

trees = [ list(map(int, _.strip())) for _ in open('input.txt', 'r').readlines()]
d = len(trees)
vis = [ [ 0 for i in range(d) ] for j in range(d) ]

## Part 1
for i in range(d):
    row = trees[i]
    col = [trees[_][i] for _ in range(d)]
    rowVis = getVis(row)
    colVis = getVis(col)

    for j in range(d):
        if rowVis[j] == 1:
            vis[i][j] = 1
        if colVis[j] == 1:
            vis[j][i] = 1

print(sum([sum(r) for r in vis]))

## Part 2
totScore = [ [ 1 for i in range(d) ] for j in range(d) ]
for i in range(d):
    row = trees[i]
    col = [trees[_][i] for _ in range(d)]
    rowS = getScore(row)
    rowRS = getRevScore(row)
    colS = getScore(col)
    colRS = getRevScore(col)

    for j in range(d):
        totScore[i][j] *= rowS[j]
        totScore[i][j] *= rowRS[j]
        totScore[j][i] *= colS[j]
        totScore[j][i] *= colRS[j]

print(max([max(r) for r in totScore]))
    
