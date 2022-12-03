def priority(char):
    o = ord(char)
    return o - 38 if (65 <= o <= 90) else o - 96

def compartments(sack):
    cptSize = int(len(sack)/2)
    return sack[:cptSize], sack[cptSize:]

def overlap2(a, b):
    return (set(a) & set(b))

def overlap3(a, b, c):
    return overlap2(overlap2(a, b), c)

def chunk(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

## Part 1
sacks = [_.strip() for _ in open('input.txt', 'r').readlines()]
cpts = [compartments(s) for s in sacks]
overlaps = [overlap2(c[0], c[1]).pop() for c in cpts]
print(sum([priority(o) for o in overlaps]))

## Part 2
groups = chunk(sacks, 3)
badges = [overlap3(g[0], g[1], g[2]).pop() for g in groups]
print(sum([priority(b) for b in badges]))
