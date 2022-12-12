from functools import reduce

def cycle(state):
    if abs((state[1] % 40) - state[0]) <= 1:
        img[state[1]] = '#'
    state[1] += 1
    if (state[1] - 20) % 40 == 0:
        state[2] += state[0] * state[1]
    return state
    

def apply(state, op):
    if op[0] == 'noop':
        state = cycle(state)

    if op[0] == 'addx':
        state = cycle(state)
        state = cycle(state)
        state[0] += int(op[1])
    return state

ops = [ _.strip().split(' ') for _ in  open('input.txt', 'r').readlines() ]
img = ['.'] * 240
state = reduce(apply, ops, [1, 0, 0, img])

## Part 1
print(state[2])

## Part 2
chimg = [ img[i:i+40] for i in range(0, len(img), 40)]
for i in chimg:
    print(''.join(i))
