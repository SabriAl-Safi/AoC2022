def GetTotalCals(calList):
    return sum([int(c) for c in str(calList).split('\n')])

elfCals = open('input.txt', 'r').read().split('\n\n')
elfTotCals = [GetTotalCals(_) for _ in elfCals]
print(max(elfTotCals))
print(sum(sorted(elfTotCals, reverse=True)[:3]))
