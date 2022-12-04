def getRangePair(s):
    return [list(map(int,_.split('-'))) for _ in s.strip().split(',')]

def rangeContains(a, b):
    return (a[0] >= b[0] and a[1] <= b[1]) or (a[0] <= b[0] and a[1] >= b[1])

def rangeOverlaps(a, b):
    return (a[0] <= b[1] and a[1] >= b[0])

rangePairs = list(map(getRangePair, open('input.txt', 'r').readlines()))

## Part 1
containments = [rangeContains(r[0], r[1]) for r in rangePairs]
print(sum(containments))

## Part 2
overlaps = [rangeOverlaps(r[0], r[1]) for r in rangePairs]
print(sum(overlaps))
