## Create , update and Read Employee Timings Data 

import csv 
from datetime import datetime

File_path = "C:/Users/venka/OneDrive/Desktop/CCBP Code Snippets and Python Book/MED-TRAINING/CSV Assesment/employees_data.csv"

column_names = ["Employee Id","Employee Name",'In-Time','Out-Time',"Break-Time","Meeting-Time"]

def employee_check(emp_id):
    name = emp_id.replace(' ','')
    with open(File_path,'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] == emp_id:
                return False 

    return True 


def create_data(test=None,data=None):
    if not test:
        emp_id = input("Enter the Employee Id : ")
        if not employee_check(emp_id):
            print("Employee is Already Existed !!")
            return False
        emp_name = input("Enter the Employee Name : ")
        in_time = input("Enter the Employee In-Time : ")
        out_time = input("Enter the Employee Out Time : ")
        break_start_time = input("Enter the Employee break start time : ")
        break_end_time = input("Enter the Employee Break end Time : ")
        meet_start_time= input("Enter the meet start time of employee :")
        meet_end_time = input("Enter the meet end time of Employee : ")
        in_time = datetime.strptime(in_time,"%H:%M").time()
        out_time = datetime.strptime(out_time,"%H:%M").time()
        break_start_time = datetime.strptime(break_start_time,"%H:%M").time()
        break_end_time = datetime.strptime(break_end_time,"%H:%M").time()
        break_time = str(break_start_time) +'-'+ str(break_end_time)
        meet_start_time = datetime.strptime(meet_start_time,"%H:%M").time()
        meet_end_time = datetime.strptime(meet_end_time,"%H:%M").time()
        meet_time = str(meet_start_time)+'-'+str(meet_end_time)
        data = [emp_id,emp_name,in_time,out_time,break_time,meet_time]

        if not in_time<break_start_time<break_end_time<out_time:
            print("Enter the Valid time Inputs") 
            return False 

        with open (File_path,'a') as file:
            writer = csv.writer(file)
            #writer.writerow(column_names)
            writer.writerow(data)
            print("Employee Data entered Successfully")
            file.close()
def update_data(data=None):
    if not data:
        emp_id = input("Enter the Employee Id : ")
    with open(File_path,'r+') as file:
        data_reader = csv.reader(file)
        flag =0
        new_data=[]
        for row in data_reader:
            if not data and row[0] == emp_id:
                flag = 1
                if not data:
                    print("1.In-time\n2.Out-Time\n3.Break-Time\n4.Meet-Time")
                    choice = int(input('Enter Any Choice of Above : '))
                    if choice == 1:
                        new_in_time = input("Enter the New In-time of Employee : ")
                        new_in_time = datetime.strptime(new_in_time,"%H:%M").time()
                        row[2] = new_in_time 
                    if choice == 2:
                        new_out_time = input("Enter the new out time of Employee : ")
                        new_out_time = datetime.strptime(new_out_time,"%H:%M").time()
                        row[3] = new_out_time 

                    if choice == 3:
                        new_break_start_time = input("Enter the new break start time : ")
                        new_break_start_time = datetime(new_break_start_time,"%H:%M").time()
                        new_break_end_time = input("Enter the new break end time : ")
                        new_break_end_time = datetime.strptime(new_break_end_time,"%H:%M").time()
                        new_break_time = str(new_break_start_time) + "-" + str(new_break_end_time)
                        row[4] = new_break_time 
                    if choice == 4:
                        new_meet_start_time = input("Enter the new meet start time of employee :")
                        new_meet_start_time = datetime.strptime(new_meet_start_time,"%H:%M").time()
                        new_meet_end_time = input("Enter the new meet end time of employee : ")
                        new_meet_end_time = datetime.strptime(new_meet_end_time,"%H:%M").time()
                        new_meet_time = str(new_meet_start_time)+'-'+str(new_meet_end_time)
                        row[5] = new_meet_time
            if data and row[0] == data[0]:
                flag = 1
                row = data
            new_data.append(row)
        file.close()
        if flag == 1:
            with open(File_path,'w') as file:
                writer = csv.writer(file)
                writer.writerow(column_names)
                writer.writerows(new_data)
                print("Employee Data updated Successfully!!!")
    return "Failed"

def read_data():
    '''Function for reading Data'''
    with open(File_path, 'r') as file:
        reader = csv.reader(file)
        #next(reader)
        count = 0
        for row in reader:
            if row:
                count += 1
                print("\nEmployee Id : "+row[0],"Employee Name : "+row[1], " In-Time : "+row[2], end=" ")
                print(" Out-Time : "+row[3], " Break-Time : "+row[4])
                print("Employee Meetings: ",row[5])
        file.close()
    return count
print("1.ReadData\n2.CreateData\n3.UpdateData")
option = int(input("Please Select one option from Above: "))
if option == 1:
    read_data()
elif option == 2:
    create_data()
elif option == 3:
    update_data()
else:
    print("You Have Entered Wrong input")

