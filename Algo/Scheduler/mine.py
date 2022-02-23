empid = ['emp1','emp2','emp3','emp4']
intime = [540,600,570,620]
outime = [1080,1110,1110,1110]
breakt = [[780,840],[810,870],[780,840],[840,900]]
dic = {}
start = 0
sch = list()
for i in range(len(empid)):
    r = list()
    in_1 = intime[i]
    brk1 = breakt[i][0]
    brk2 = breakt[i][1]
    ot_t = outime[i]
    r.append([in_1, brk1])
    r.append([brk2, ot_t])
    dic[empid[i]] = r
print(dic)
urcal = 1
while urcal==1:
    ce1 = int(input("Enter first employee's ID: \n"))
    ce2 = int(input("Enter second employee's ID: \n"))
    meet_hrs = float(input("Meet duration hrs : "))
    meet = int(meet_hrs*60)
    ce1 = ce1 - 1
    ce2 = ce2 - 1
    l1 = dic[empid[ce1]]
    l2 = dic[empid[ce2]]
    #print(l1)
    #print(l2)
    if l1[0][0] <= l2[0][0]:
        a1 = l2[0][0]
    else:
        a1 = l1[0][0]
    if l1[0][1] <= l2[0][1]:
        a2 = l1[0][1]
    else:
        a2 = l2[0][1]
    if l1[1][0] <= l2[1][0]:
        b1 = l2[1][0]
    else:
        b1 = l1[1][0]
    if l1[1][1] <= l2[1][1]:
        b2 = l1[1][1]
    else:
        b2 = l2[1][1]
    r1 = [a1, a2]
    print(r1)
    
    r2 = [b1, b2]
    print(r2)
    if abs(a1-a2) >= meet:
        start = a1
    elif abs(b1-b2) >= meet:
        start = b1
    else:
        print("Not possible")
    if start:
        end = start + meet
    sch.append(start)
    sch.append(end)
    if l1[0][0] < start:
        dic[empid[ce1]].append([l1[0][0], start])
    elif l1[0][0] == start and end < l1[0][1]:
        dic[empid[ce1]].append([end, l1[1][0]])
    if l2[0][0] < start:
        dic[empid[ce2]].append([l1[0][0], start])
    elif l2[0][0] == start and end < l2[0][1]:
        dic[empid[ce2]].append([end, l2[1][0]])
    print(sch)
    print(dic[empid[ce1]])
    print(dic[empid[ce2]])
    urcal += 1
    




