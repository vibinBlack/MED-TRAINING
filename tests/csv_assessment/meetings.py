'''
Schedule the Meetings and write the data into csv file
'''
import shutil
from tempfile import NamedTemporaryFile
from datetime import datetime, timedelta
import csv
import pandas as pd
from csv_methods import create_and_write_csv, read_csv, append_csv

def schedule_meeting():
    ''' Function to schedule meetings '''
    filename = 'employees.csv'
    csv_data = pd.read_csv(filename)
    print()
    print(csv_data.to_string())
    print()
    csv_data.set_index(['id'], inplace=True)
    csv_data = csv_data.transpose()
    csv_dict = csv_data.to_dict()
    print()
    for i in csv_dict.keys():
        j = [int(x) for x in csv_dict[i]['in time'].split(":")]
        k = [int(x) for x in csv_dict[i]['out time'].split(":")]
        csv_dict[i]['in time'] = datetime(2000,1,1, hour=j[0],minute= j[1])
        csv_dict[i]['out time'] = datetime(2000,1,1, hour=k[0],minute= k[1])
        break_in, break_out = csv_dict[i]['break time'].split('-')
        break_in = [int(x) for x in break_in.split(":")]
        break_out = [int(x) for x in break_out.split(":")]
        csv_dict[i]['break_in'] = datetime(2000,1,1, hour= break_in[0],minute= break_in[1])
        csv_dict[i]['break_out'] = datetime(2000,1,1, hour= break_out[0],minute= break_out[1])
        if str(csv_dict[i]['scheduled meetings']).strip() == 'nan':
            csv_dict[i]['scheduled meetings'] = '00:00-00:00'
        csv_dict[i]['scheduled meetings'] = list(x for x in csv_dict[i]['scheduled meetings'].split())
        csv_dict[i]['scheduled_in'] = []
        csv_dict[i]['scheduled_out'] = []
        for j in csv_dict[i]['scheduled meetings']:
            scheduled_in, scheduled_out = j.split('-')
            scheduled_in = [int(x) for x in scheduled_in.split(":")]
            scheduled_out = [int(x) for x in scheduled_out.split(":")]
            csv_dict[i]['scheduled_in'].append(datetime(2000,1,1, \
                hour= scheduled_in[0],minute= scheduled_in[1]))
            csv_dict[i]['scheduled_out'].append(datetime(2000,1,1, \
                hour= scheduled_out[0],minute= scheduled_out[1]))

    meeting_name = input("Meeting name : ")
    duration = int(input("Meeting time in minutes : "))
    meeting_bw = [int(x) for x in input("Give the id of both the employees separated with\
 a space whom to attend meeting : ").split()]
    if csv_dict[meeting_bw[0]]['in time'] > csv_dict[meeting_bw[1]]['in time'] :
        meeting_start = csv_dict[meeting_bw[0]]['in time']
    elif csv_dict[meeting_bw[0]]['in time'] < csv_dict[meeting_bw[1]]['in time'] :
        meeting_start = csv_dict[meeting_bw[1]]['in time']
    else:
        meeting_start = csv_dict[meeting_bw[0]]['in time']
    csv_dict[meeting_bw[0]]['scheduled_in'].extend(csv_dict[meeting_bw[1]]['scheduled_in'])
    csv_dict[meeting_bw[0]]['scheduled_out'].extend(csv_dict[meeting_bw[1]]['scheduled_out'])
    csv_dict[meeting_bw[0]]['scheduled_in'].append(csv_dict[meeting_bw[0]]['break_in'])
    csv_dict[meeting_bw[0]]['scheduled_out'].append(csv_dict[meeting_bw[0]]['break_out'])
    csv_dict[meeting_bw[0]]['scheduled_in'].append(csv_dict[meeting_bw[1]]['break_in'])
    csv_dict[meeting_bw[0]]['scheduled_out'].append(csv_dict[meeting_bw[1]]['break_out'])

    for i in range(len(csv_dict[meeting_bw[0]]['scheduled_out'])):
        for j in range(len(csv_dict[meeting_bw[0]]['scheduled_out'])):
            meeting_end = meeting_start + timedelta(minutes=duration)
            if meeting_start >  csv_dict[meeting_bw[0]]['scheduled_in'][j]\
                 and meeting_start <=  csv_dict[meeting_bw[0]]['scheduled_out'][j]:
                meeting_start = csv_dict[meeting_bw[0]]['scheduled_out'][j]
                meeting_end = meeting_start + timedelta(minutes=duration)
                if meeting_end >  csv_dict[meeting_bw[0]]['scheduled_in'][j]\
                     and meeting_end <=  csv_dict[meeting_bw[0]]['scheduled_out'][j]:
                    meeting_start = csv_dict[meeting_bw[0]]['scheduled_out'][j]
            meeting_end = meeting_start + timedelta(minutes=duration)
            if meeting_end >  csv_dict[meeting_bw[0]]['scheduled_in'][j]\
                 and meeting_end <=  csv_dict[meeting_bw[0]]['scheduled_out'][j]:
                meeting_start = csv_dict[meeting_bw[0]]['scheduled_out'][j]
            
                
            meeting_end = meeting_start + timedelta(minutes=duration)
            if meeting_end - meeting_start > csv_dict[meeting_bw[0]]['scheduled_out'][j]\
                 - csv_dict[meeting_bw[0]]['scheduled_in'][j]:
                if csv_dict[meeting_bw[0]]['scheduled_in'][j] > meeting_start\
                    and csv_dict[meeting_bw[0]]['scheduled_in'][j] <= meeting_end:
                    meeting_start = csv_dict[meeting_bw[0]]['scheduled_out'][j]
                    meeting_end = meeting_start + timedelta(minutes=duration)
                    if csv_dict[meeting_bw[0]]['scheduled_out'][j] > meeting_start\
                        and csv_dict[meeting_bw[0]]['scheduled_out'][j] <= meeting_end:
                        meeting_start = csv_dict[meeting_bw[0]]['scheduled_out'][j]
                        
                meeting_end = meeting_start + timedelta(minutes=duration)
                if csv_dict[meeting_bw[0]]['scheduled_out'][j] > meeting_start\
                    and csv_dict[meeting_bw[0]]['scheduled_out'][j] <= meeting_end:
                    meeting_start = csv_dict[meeting_bw[0]]['scheduled_out'][j]

    meeting_end = meeting_start + timedelta(minutes=duration)
    if meeting_start > csv_dict[meeting_bw[0]]['out time']\
         or meeting_end > csv_dict[meeting_bw[0]]['out time']:
        print("Slots are not available for today.")
    elif meeting_start > csv_dict[meeting_bw[1]]['out time']\
         or meeting_end > csv_dict[meeting_bw[1]]['out time']:
        print("Slots are not available for today.")
    else:
        meeting_start = meeting_start.strftime("%H:%M")
        meeting_end = meeting_end.strftime("%H:%M")
        meeting_time = meeting_start + '-' + meeting_end
        with open(filename, 'r', encoding='UTF-8') as file_read:
            reader = csv.DictReader(file_read)
            field_names = reader.fieldnames
            file_write = NamedTemporaryFile(mode='w', delete=False)
            with open(filename, 'r', encoding = 'UTF-8') as file_read_again, file_write:
                reader = csv.DictReader(file_read_again)
                writer = csv.DictWriter(file_write, fieldnames = field_names)
                writer.writeheader()
                for i in reader:
                    if int(i['id']) in meeting_bw:
                        i['scheduled meetings'] += ' ' + meeting_time
                        i['meetings'] += ' ' + meeting_name + ':' + meeting_time
                    writer.writerow(i)
                file_write.close()
            shutil.move(file_write.name, filename)
        print(f"Your meeting is scheduled at {meeting_time}")
    print()
    csv_data = pd.read_csv(filename)
    print(csv_data.to_string())

def select_task():
    ''' Select the task '''
    print("\n1. Create or Write a new CSV file\n2. Read existing CSV file\
\n3. Append data to existing file\n4. Schedule Meeting for Employees file\
\nC. Select any other option to exit")
    select = input("\nSelect the task : ")
    if select == '1':
        create_and_write_csv()
        return select_task()
    if select == '2':
        print(read_csv())
        return select_task()
    if select == '3':
        append_csv()
        return select_task()
    if select == '4':
        schedule_meeting()
        return select_task()
    return 0
select_task()
