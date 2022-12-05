def cleanCrateRow(s):
    return s.strip()[1::4].ljust(9)

def transpose(m):
    return [ [m[i][j] for i in range(8)] for j in range(9) ]

def cleanOpRow(s):
    return list(map(int, s.strip().split(' ')[1::2]))

file = open('input.txt', 'r').readlines()

## Part 1
stacks = [list(''.join(_).strip()) for _ in transpose(list(map(cleanCrateRow, file[7::-1])))]
ops = list(map(cleanOpRow, file[10:]))
for op in ops:
    move = stacks[op[1]-1][-op[0]:]
    stacks[op[1]-1] = stacks[op[1]-1][:-op[0]]
    stacks[op[2]-1] = stacks[op[2]-1] + move[::-1]
print(''.join([st[-1] for st in stacks]))

## Part 2
stacks = [list(''.join(_).strip()) for _ in transpose(list(map(cleanCrateRow, file[7::-1])))]
for op in ops:
    move = stacks[op[1]-1][-op[0]:]
    stacks[op[1]-1] = stacks[op[1]-1][:-op[0]]
    stacks[op[2]-1] = stacks[op[2]-1] + move
print(''.join([st[-1] for st in stacks]))
