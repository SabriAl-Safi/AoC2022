import operator
from functools import reduce
vec = { 'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0) }

def vecAdd(a, b):
    return tuple(map(operator.add, a, b))

def vecSub(a, b):
    return tuple(map(operator.sub, a, b))

def initRope(n):
    return [ (0, 0) for _ in range(n) ]

def drag(head, tail):
    (dx, dy) = vecSub(head, tail)
    ax, ay = abs(dx), abs(dy)
    if ax == 2 and ay == 2:
        return vecAdd(tail, (dx//2, dy//2)) 
    if ax == 2:
        return vecAdd(tail, (dx//2, dy)) 
    if ay == 2:
        return vecAdd(tail, (dx, dy//2))
    return tail

def dragSection(rope, i):
    rope[i] = drag(rope[i-1], rope[i])
    return rope

def moveRope(state, vec):
    rope = state[0]
    tailSet = state[1]
    rope[0] = vecAdd(rope[0], vec)
    rope = reduce(dragSection, range(1, len(rope)), rope)
    return [rope, tailSet | set([rope[-1]])]

def moveRopeN(state, vec, n):
    newState = moveRope(state, vec)
    return newState if n == 1 else moveRopeN(newState, vec, n-1)

def applyMove(state, move):
    return moveRopeN(state, move[0], move[1])

def tailSet(ropeLength, moves):
    return reduce(applyMove, moves, [initRope(ropeLength), set()])[1]

headMoves = [ [vec[_[0]], int(_[1:])] for _ in open('input.txt', 'r').readlines() ]

## Part 1
print(len(tailSet(2, headMoves)))

## Part 2
print(len(tailSet(10, headMoves)))
