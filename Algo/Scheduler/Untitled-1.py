import pandas as pd

def caal(meet, c1, c2, in_t, brk1, brk2, ot_t):
    maxt = list()
    maxsch = list()
    sch = list()
    st = 0
    if c1 == [] and c2 == []:
        c1.append(in_t)
        c2.append(in_t)
    elif len(c1) == 1 and len(c2)==1:
        v11 = c1[0]
        v22 = c2[0]
        if v11 >= v22:
            st = v11
        else:
            st = v22
    elif len(c1) == 2:
        
            
            

    elif len(c1) == 2 and len(c2)==0:
        v1 = c1[0]
        v2 = c1[1]
    
    max1 = abs(                                                               )


    
    
    #print("The meets can be scheduled in following intervals")
    print(maxsch)
    #print("Possible Maximum Minutes of meet in morning and evening")
    print(maxt)
    print(meet)



    df = pd.DataFrame({'duration': sch})
    #print(df)

    f_df = pd.to_datetime(df.duration, unit='m').dt.strftime('%H:%M')
    Final = f_df.values.tolist()
    
    
    return Final, in_t, brk2






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

urcal = 1
ebrk1 = 0
ebrk2 = 0
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
    
    Final, curs[cmp_emp1], curs[cmp_emp2] in_t, brk2 = caal(meet, curs[cmp_emp1], curs[cmp_emp2], ein_t, ebrk1, ebrk2, eot_t )
    

    
