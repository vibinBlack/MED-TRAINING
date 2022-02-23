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

    #print("The meets can be scheduled in following intervals")
    print(maxsch)
    #print("Possible Maximum Minutes of meet in morning and evening")
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
empid  cur     in-time      break              out-time          
emp1   cur1       09:00    13:00 - 14:00          18:00       
emp2   cur2       10:00    13:30 - 14:30         18:30       
emp3   cur3       09:30    13:00 - 14:00         18:30        
emp4   cur4       10:20    14:00 - 15:00         18:30       


'''


empid = ['emp1','emp2','emp3','emp4']
intime = [540,600,570,620]
outime = [1080,1110,1110,1110]
breakt = [[780,840],[810,870],[780,840],[840,900]]
cur1 = list()
cur2 = list()
cur3 = list()
cur4 = list()
curs = [cur1, cur2, cur3, cur4]

#TESTCASES
'''
1. (1,2)  1.5  10 - 11:30
2. (1,3)  1.5  11:30 - 13
3. (1,3)  4    14 - 18
4. (2,4)  2    11:30 - 13:30
5. (1,3)  0.5  9:30 - 10
6. (2,4)  3.5  15:00 - 18:30
7. (3,4)  1    10:20 - 11:30
'''


brk11 = 0
brk12 = 0
brk21 = 0
brk22 = 0
ein_1 = 0
ein_2 = 0
eot_1 = 0
eot_2 = 0
ein_t = 0
eot_t = 0
count = 0
Meetz = list()
addthem = list()


while urcal:
    cmp_emp1 = int(input("Meeting to schedule between empno:"))
    cmp_emp2 = int(input("and empno:"))
    meet_hrs = float(input("Meet in hrs : "))
    meet = int(meet_hrs*60)
    #print(addthem)
    
    if cmp_emp1 in addthem or cmp_emp2 in addthem:
        if cmp_emp1 not in addthem:
            addthem.append(cmp_emp1)
        if cmp_emp2 not in addthem:
            addthem.append(cmp_emp2)

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
            Final, in_t, flagi, flagb, brk2 = caal(meet,in_t,ebrk1,ebrk2,ot_t)

        #Final, in_t, flagi, flagb, brk2 = caal(meet,in_t,brk1,brk2,ot_t)
    else:
        if cmp_emp1 not in addthem:
            addthem.append(cmp_emp1)
        if cmp_emp2 not in addthem:
            addthem.append(cmp_emp2)
            
        i = cmp_emp1-1
        j = cmp_emp2-1
    
        ein_1 = intime[i]
        ein_2 = intime[j]

        if breakt[i][0] <= breakt[j][0]:
            ebrk1 = breakt[i][0]
        else:
            ebrk1 = breakt[j][0]
    
    
        if breakt[i][1] <= breakt[j][1]:
            ebrk2 = breakt[j][1]
        else:
            ebrk2 = breakt[i][1]

        eot_1 = outime[i]
        eot_2 = outime[j]

        if ein_1 <= ein_2:
            ein_t = ein_2
        else:
            ein_t = ein_1

        if eot_1 <= eot_2:
            eot_t = eot_1
        else:
            eot_t = eot_2
        
            
        Final, in_t, flagi, flagb, brk2 = caal(meet,ein_t,ebrk1,ebrk2,eot_t)     
        print(in_t)
        print(ein_t)
        print(brk2)
        print(ebrk2)
        print(flagi)
        print(flagb)   
        

        '''
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
            '''

    
    if Final == 0:
        urcal = int(input("Want to schedule another meeting \n Enter 0 or 1 : \n"))
        count += 1
    else:
        print("The meeting is scheduled in the following hours")
        Meetz.append({(cmp_emp1,cmp_emp2): Final})
        print(Final)
        print(Meetz)
        
        confirm = int(input("Confirm the Meeting: \n Enter 1 for YES or 0 for NO :\n"))
        if confirm:
            print("Meeting is scheduled")
            count += 1
        urcal = int(input("Want to schedule another meeting \n Enter 0 or 1 : \n"))