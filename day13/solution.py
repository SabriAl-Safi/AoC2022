packets = [ _.split('\n') for _ in open('input.txt', 'r').read().split('\n\n')]
packets = [ [eval(p[0]), eval(p[1])] for p in packets ]

def listDiff(a, b):
    aint, bint = isinstance(a, int), isinstance(b, int)
    if aint and bint: return (b-a)
    if (aint and not bint): return listDiff([a], b)
    if (not aint and bint): return listDiff(a, [b])
    if a == [] and b == []: return 0
    if a == []: return 1
    if b == []: return -1
    c = listDiff(a[0], b[0])
    if c == 0: return listDiff(a[1:], b[1:])
    return c

## Part 1
print(sum([i+1 for i, p in enumerate(packets) if listDiff(p[0], p[1]) >= 0]))

## Part 2
packets = [p[0] for p in packets] + [p[1] for p in packets]
filt1 = list(filter(lambda p : listDiff(p, [[2]]) > 0, packets))
filt2 = list(filter(lambda p : listDiff(p, [[6]]) > 0, packets))
print((len(filt1)+1) * (len(filt2)+2))
