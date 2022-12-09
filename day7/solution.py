terminal = [_.strip().split('\n') for _ in open('input.txt', 'r').read().split('$')[1:]]

## Part 1
curDir = ''
parent = {}
children = {}
filesize = {}
dirsize = {}

for cmd in terminal[1:]:
    #print(cmd)
    
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
        #print('Change dir to ' + curDir)
        
    else:
        for output in cmd[1:]:
            if output[:3] == 'dir':
                childDir = curDir + '/' + output[4:]
                parent[childDir] = curDir
                children[curDir].append(childDir)
                #print(output[4:] + ' child dir of ' + curDir)
                
            else:
                s = int(output.split(' ')[0])
                f = output.split(' ')[1]
                filesize[f] = s
                dirsize[curDir] += s
                #print(f + ' has size ' + str(s))

#print(filesize)
#print(dirsize)

for lDir in children:
    if len(children[lDir]) > 0:
        continue
    lSize = dirsize[lDir]
    while lDir != '':
        lDir = parent[lDir]
        dirsize[lDir] += lSize
        lSize = dirsize[lDir]
    
print(sum([dirsize[_] for _ in dirsize if dirsize[_] < 100000]))

## Part 2
used = dirsize['']
print(dirsize)
##unused = 70000000-used
##print(unused)
##mindel = 30000000 - unused
##print(mindel)
##print(min([dirsize[_] for _ in dirsize if dirsize[_] > mindel]))
