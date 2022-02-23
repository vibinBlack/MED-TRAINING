import pandas as pd
def caal(meet,in_t,brk1,brk2,ot_t):
    flagi = 0
    flagb = 0
    maxt = list()
    maxsch = list()
    sch = list()
    max1 = abs(brk1 - in_t)
    max2 = abs(ot_t - brk2)
        
    maxt.append(max1)
    maxt.append(max2)
    maxsch.append([in_t, brk1])
    maxsch.append([brk2, ot_t])

    print("The meets can be scheduled in following intervals")
    print(maxsch)
    print("Possible Maximum Minutes of meet in morning and evening")
    print(maxt)
    print(meet)

    if meet > max1 and meet > max2:
        print("Meeting can't be scheduled between the specified employees")
        return 0, in_t, flagi, flagb, brk2
    elif meet > max1 and meet <= max2:
        sch.append(brk2)
        sch.append(brk2+meet)  
        brk2 = brk2 + meet 
        flagb = 1      #Only possible to schedule meet in Afternoon
    elif meet <= max1 and meet > max2:
        sch.append(in_t)
        sch.append(in_t+meet)  
        in_t = in_t + meet
        flagi = 1      #Only posssible to schedule meet in Morning
    else:
        sch.append(in_t)
        sch.append(in_t+meet) 
        in_t = in_t+meet   
        flagi = 1   #possible to schedule meet at any time.
    print(sch)

    df = pd.DataFrame({'duration': sch})
    #print(df)

    f_df = pd.to_datetime(df.duration, unit='m').dt.strftime('%H:%M')
    Final = f_df.values.tolist()
    
    
    return Final, in_t, flagi, flagb, brk2
    
    

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

#FIRST_MEETING


# 1,2 210min
#2,3 180min
# 3,4 210min
urcal = 1
brk1 = 0
brk2 = 0
in_t = 0
ot_t = 0
count = 0


while urcal:
    cmp_emp1 = int(input("Meeting to schedule between empno:"))
    cmp_emp2 = int(input("and empno:"))
    meet_hrs = float(input("Meet in hrs : "))
    meet = int(meet_hrs*60)
    
    
    if count == 0:
        i = cmp_emp1-1
        j = cmp_emp2-1
    
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
            
        Final, in_t, flagi, flagb, brk2 = caal(meet,in_t,brk1,brk2,ot_t)
        
        
    else:
        i = cmp_emp1-1
        j = cmp_emp2-1

        ein_1 = intime[i]
        ein_2 = intime[j]

        if ein_1 <= ein_2:
            ein_t = ein_2
        else:
            ein_t = ein_1
        if breakt[i][0] <= breakt[j][0]:
            ebrk1 = breakt[i][0]
        else:
            ebrk1 = breakt[j][0]
        if breakt[i][1] <= breakt[j][1]:
            ebrk2 = breakt[j][1]
        else:
            ebrk2 = breakt[i][1]
        print(in_t)
        print(ein_t)
        print(brk2)
        print(ebrk2)
        print(flagi)
        print(flagb)
        if flagi == 1 and flagb == 0: 
            Final, in_t, flagi, flagb, brk2 = caal(meet,in_t,brk1,ebrk2,ot_t)
        elif flagi == 0 and flagb == 1:
            Final, in_t, flagi, flagb, brk2 = caal(meet,in_t,brk1,brk2,ot_t)
        elif flagi == 0 and flagb == 0:
            Final, in_t, flagi, flagb, brk2 = caal(meet,in_t,brk1,ebrk2,ot_t)

    
    if Final == 0:
        urcal = int(input("Want to schedule another meeting \n Enter 0 or 1 : \n"))
        count += 1
    else:
        print("The meeting is scheduled in the following hours")
        print(Final)
        
        confirm = int(input("Confirm the Meeting: \n Enter 1 for YES or 0 for NO :\n"))
        if confirm:
            print("Meeting is scheduled")
            count += 1
        urcal = int(input("Want to schedule another meeting \n Enter 0 or 1 : \n"))