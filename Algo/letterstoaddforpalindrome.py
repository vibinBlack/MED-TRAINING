def ispalin(given):
    given = list(given)
    n = len(given)
    if given == given[n::-1]:
        return 1
    else:
        return 0
def leftcal(given):
    lcount = 0
    lflag = 0
    while len(given) > 0:
        result = ispalin(given)
        if result:
            lflag = 1
            break
        else:
            lcount += 1
            given = given[:-1]
    if lflag:
        return lcount
    
def rightcal(given):
    rcount = 0
    rflag = 0
    while len(given) > 0:
        result = ispalin(given)
        if result:
            rflag = 1
            break
        else:
            rcount += 1 
            given = given[1:]
    if rflag:
        return rcount 

given = input()
n = len(given)
lcount = leftcal(given)
rcount = rightcal(given)
print(min(lcount,rcount))
