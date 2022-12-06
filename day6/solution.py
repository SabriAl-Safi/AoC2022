def getMarkerIdx(buffer, numDistinct):
    return next(i
                for i in range(numDistinct, len(buffer))
                if len(set(buffer[i-numDistinct:i])) == numDistinct)

stream = open('input.txt', 'r').read()

## Part 1
print(getMarkerIdx(stream, 4))

## Part 2
print(getMarkerIdx(stream, 14))
