terminal = [_.strip().split('\n') for _ in open('input.txt', 'r').read().split('$')[1:]]

## Part 1
curDir = ''
parent = {}
children = {}
filesize = {}
dirsize = {}

for cmd in terminal[1:]:    
    if curDir not in children:
        children[curDir] = []

    if curDir not in dirsize:
        dirsize[curDir] = 0
        
    if len(cmd) == 1:
        cdcmd = cmd[0]
        if cdcmd == 'cd ..':
            curDir = parent[curDir]
        else:
            curDir = curDir + '/' + cdcmd[3:]
        
    else:
        for output in cmd[1:]:
            if output[:3] == 'dir':
                childDir = curDir + '/' + output[4:]
                parent[childDir] = curDir
                children[curDir].append(childDir)
                
            else:
                s = int(output.split(' ')[0])
                f = output.split(' ')[1]
                filesize[f] = s
                dirsize[curDir] += s

def getSize(d, kids, dSize):
    for c in kids[d]:
        dSize[d] += getSize(c, kids, dSize)
    return dSize[d]

used = getSize('', children, dirsize)

print(sum([dirsize[_] for _ in dirsize if dirsize[_] < 100000]))

## Part 2
mindel = 30000000 - (70000000-used)
print(min([dirsize[_] for _ in dirsize if dirsize[_] > mindel]))
