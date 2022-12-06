def isStrDistinct(s):
    return len(s) == len(set(s))

def getMarkerIdx(buffer, n):
    return next(i for i in range(n, len(buffer)) if isStrDistinct(buffer[i-n:i]))

stream = open('input.txt', 'r').read()

## Part 1
print(getMarkerIdx(stream, 4))

## Part 2
print(getMarkerIdx(stream, 14))
