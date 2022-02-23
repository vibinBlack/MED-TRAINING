import pandas as pd

'''
empid       in-time    out-time          break
emp1          09:00       18:00       13:00 - 14:00
emp2          10:00      18:30        13:30 - 14:30
emp3          09:30      18:30        13:00 - 14:00
emp4          10:20      18:30        14:00 - 15:00


'''


empid = ['emp1','emp2','emp3','emp4']
intime = [540,600,570,620]
outime = [1080,1110,1110,1110]
breakt = [[780,840],[810,870],[780,840],[840,900]]

maxsch = sch = list()


# 1,2 210min
#2,3 180min
# 3,4 210min
urcall = 1

while urcall:
    cmp_emp1 = int(input("Meeting to schedule between emp:"))
    cmp_emp2 = int(input("and emp:"))
    meet_hrs = float(input("Meet time:"))
    meet = int(meet_hrs*60)
    i = cmp_emp1-1
    j = cmp_emp2-1

    brk1 = brk2 = in_t = ot_t = 0

    in_1 = intime[i]
    in_2 = intime[j]

    if breakt[i][0] <= breakt[j][0]:
        brk1 = breakt[i][0]
    else:
        brk1 = breakt[j][0]
    
    
    if breakt[i][1] <= breakt[j][1]:
        brk2 = breakt[j][1]
    else:
        brk2 = breakt[i][1]

    ot_1 = outime[i]
    ot_2 = outime[j]

    if in_1 <= in_2:
        in_t = in_2
    else:
        in_t = in_1

    if ot_1 <= ot_2:
        ot_t = ot_1
    else:
        ot_t = ot_2
    
    
    maxt = list()
    max1 = max2 = 0
    max1 = abs(brk1 - in_t)
    max2 = abs(ot_t - brk2)

    maxt.append(max1)
    maxt.append(max2)
    maxsch.append([in_t, brk1])
    maxsch.append([brk2, ot_t])

    

    if meet > max1 and meet > max2:
        print("Meeting can't be scheduled")
        pass
    #Only possible to schedule meet in Afternoon
    elif meet > max1 and meet <= max2:
        sch.append(brk2)
        sch.append(brk2+meet)
    #Only posssible to schedule meet in Morning
    elif meet <= max1 and meet > max2:
        sch.append(in_t)
        sch.append(in_t+meet)
    #possible to schedule meet at any time.
    else:
        sch.append(in_t)
        sch.append(in_t+meet)
    print(sch)

    print("The meets can be scheduled in following intervals")
    print(maxsch)
    print("Possible Maximum Minutes of meet in morning and evening")
    print(maxt)



    df = pd.DataFrame({'duration': sch})
    #print(df)

    f_df = pd.to_datetime(df.duration, unit='m').dt.strftime('%H:%M')
    Final = f_df.values.tolist()
    print("The meeting is scheduled in the following hours")
    print(Final)
    confirm = int(input("Confirm the Meeting: \n Enter 1 for YES or 0 for NO :\n"))
    if confirm:
        print("Meeting is scheduled")
    urcall = int(input("Want to schedule another meeting \n Enter 0 or 1 : \n"))


