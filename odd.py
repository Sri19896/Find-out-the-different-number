
def stray(l):
    l = list(l)
    for i in l:
        if l.count(i) > 1:
            continue
        else:
            return(i)


print(stray([17, 17, 3, 17, 17, 17, 17]))
