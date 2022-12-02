def nonZeroMod(a, b):
    m = a % b
    return m if m > 0 else b

def scoreByNum(opNum, myNum):
    score = myNum
    diff = nonZeroMod(myNum - opNum, 3)
    return score + 6 if diff == 1 else score + 3 if diff == 3 else score

def scoreByChar1(opHand, myHand):
    return scoreByNum(ord(opHand) - 64, ord(myHand) - 87)

def scoreByChar2(opHand, end):
    opNum = ord(opHand) - 64
    myNum = nonZeroMod(opNum + (ord(end) - 89), 3)
    return scoreByNum(opNum, myNum)

games = [_.strip().split(' ') for _ in open('input.txt', 'r').readlines()]
print(sum([scoreByChar1(_[0], _[1]) for _ in games]))
print(sum([scoreByChar2(_[0], _[1]) for _ in games]))
