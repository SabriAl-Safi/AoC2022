from functools import reduce
from math import lcm

def endInt(l): return int(l.split(' ')[-1])

def readNote(note):
    lines = note.split('\n')
    return [
        readList(lines[1][18:]),
        lines[2][19:],
        endInt(lines[3]),
        endInt(lines[4]),
        endInt(lines[5]),
        0]

def readList(l): return list(map(int, l.split(',')))

def processItem(monks, m, item):
    old = item
    worry = (eval(m[1]) % monks[-1]) #// 3
    target = m[3] if (worry % m[2] == 0) else m[4]
    monks[target][0].append(worry)

def takeTurn(monks, m):
    for i in m[0]:
        processItem(monks, m, i)
    m[5] += len(m[0])
    m[0] = []
    return monks

def takeRound(monks): return reduce(takeTurn, monks[:-1], monks)

def takeNRounds(monks, n):
    for _ in range(n):
        monks = takeRound(monks)
    return monks

notes = open('input.txt', 'r').read().split('\n\n')
monks = list(map(readNote, notes))
l = reduce(lcm, [m[2] for m in monks], 1)
monks.append(l)

## Part 1
takeNRounds(monks, 20)
nums = [m[5] for m in monks[:-1]]
nums.sort(reverse=True)
print(nums[0] * nums[1])

## Part 2
takeNRounds(monks, 10000)
nums = [m[5] for m in monks[:-1]]
nums.sort(reverse=True)
print(nums[0] * nums[1])
