"""Schedule meetings"""
import csv
from datetime import datetime, date, time, timedelta
import random

FILE_NAME = "employees.csv"


def time_str_to_date(time_string):
    """converts time string of format HH:MM to datetime object"""
    time_string = time_string.split(":")
    dummy_date = date(1, 1, 1)
    string_time = time(int(time_string[0]), int(time_string[1]))
    return datetime.combine(dummy_date, string_time)


def schedule_meeting(id1, id2, meeting_time):
    """Create a new meeting between two employee based on their availability"""
    with open(FILE_NAME, encoding="UTF-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        id_i = -1
        in_time_i = -1
        out_time_i = -1
        break_time_i = -1
        meetings_i = -1
        for index, ele in enumerate(header):
            if ele == "Id":
                id_i = index
            elif ele == "In Time":
                in_time_i = index
            elif ele == "Out Time":
                out_time_i = index
            elif ele == "Break Time":
                break_time_i = index
            elif ele == "Meetings":
                meetings_i = index
        rows = []
        e1_meetings = []
        e2_meetings = []
        for i, row in enumerate(reader):
            if row[id_i] == str(id1):
                emp_1 = {"emp_id": id1,
                         "in_time": time_str_to_date(row[in_time_i]),
                         "out_time": time_str_to_date(row[out_time_i]),
                         "break_in": time_str_to_date(row[break_time_i].split("-")[0]),
                         "break_out": time_str_to_date(row[break_time_i].split("-")[1]),
                         }
                emp1_index = i
                e1_meetings = row[meetings_i].split()
                e1_meetings.append(row[break_time_i])
            if row[id_i] == str(id2):
                emp_2 = {"emp_id": id2,
                         "in_time": time_str_to_date(row[in_time_i]),
                         "out_time": time_str_to_date(row[out_time_i]),
                         "break_in": time_str_to_date(row[break_time_i].split("-")[0]),
                         "break_out": time_str_to_date(row[break_time_i].split("-")[1]),
                         }
                emp2_index = i
                e2_meetings = row[meetings_i].split()
                e2_meetings.append(row[break_time_i])
            rows.append(row)
        file.close()

    e1_meetings.sort()
    e2_meetings.sort()
    available = []
    while 1:
        sch_meeting = schedule(e1_meetings, e2_meetings, emp_1, emp_2, meeting_time)
        if sch_meeting is not None:
            e1_meetings.append(sch_meeting)
            e2_meetings.append(sch_meeting)
            e1_meetings.sort()
            e2_meetings.sort()
            available.append(sch_meeting)
        else:
            break
    print(available)

    if len(available) > 0:
        #scheduled_meeting = random.choice(available)
        scheduled_meeting = available[0]
        rows[emp1_index][meetings_i] = \
            (rows[emp1_index][meetings_i] + " " + scheduled_meeting).strip()
        rows[emp2_index][meetings_i] = \
            (rows[emp2_index][meetings_i] + " " + scheduled_meeting).strip()

        with open(FILE_NAME, 'w', encoding="utf-8", newline="\n") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(header)
            csvwriter.writerows(rows)
            file.close()


def schedule(e1_meetings, e2_meetings, emp_1, emp_2, meeting_time):
    """shcedule a meeting based on the availability and meeting times of two employees"""
    for i, e1_meeting in enumerate(e1_meetings):
        e1_stime = time_str_to_date(e1_meeting.split("-")[0])
        e1_etime = time_str_to_date(e1_meeting.split("-")[1])
        for j, e2_meeting in enumerate(e2_meetings):
            e2_stime = time_str_to_date(e2_meeting.split("-")[0])
            e2_etime = time_str_to_date(e2_meeting.split("-")[1])
            in_time = emp_2["in_time"] if (emp_2["in_time"] - emp_1["in_time"]).total_seconds() > 0 \
                else emp_1["in_time"]
            out_time = emp_1["out_time"] if (emp_2["out_time"] - emp_1["out_time"]).total_seconds() > 0 \
                else emp_2["out_time"]
            start_time = e1_stime if (e2_stime - e1_stime).total_seconds() > 0 \
                else e2_stime
            end_time = e2_etime if (e2_etime - e1_etime).total_seconds() > 0 \
                else e1_etime
            if i == 0 and j == 0:
                if (start_time - in_time).total_seconds() >= meeting_time * 60:
                    return (in_time + timedelta(minutes=0)).time().strftime("%H:%M") + "-" + \
                           (in_time + timedelta(minutes=meeting_time)).time().strftime("%H:%M")
                if len(e1_meetings) == 1 and len(e2_meetings) == 1 and \
                        (out_time - end_time).total_seconds() >= meeting_time * 60:
                    return (end_time + timedelta(minutes=0)).time().strftime("%H:%M") + "-" + \
                           (end_time + timedelta(minutes=meeting_time)).time().strftime("%H:%M")
            else:
                last_meeting_emp1_end_time = time_str_to_date(e1_meetings[i - 1].split("-")[1]) if i > 0 else in_time
                last_meeting_emp2_end_time = time_str_to_date(e2_meetings[j - 1].split("-")[1]) if j > 0 else in_time
                last_meeting_end_time = last_meeting_emp2_end_time if (last_meeting_emp2_end_time \
                    - last_meeting_emp1_end_time).total_seconds() > 0 else last_meeting_emp1_end_time
                if (start_time - last_meeting_end_time).total_seconds() >= meeting_time * 60:
                    return (last_meeting_end_time + timedelta(minutes=0)).time().strftime("%H:%M") \
                           + "-" + (last_meeting_end_time + timedelta(minutes=meeting_time)).time().strftime("%H:%M")
                if i == len(e1_meetings) - 1 and j == len(e2_meetings) - 1:
                    if (out_time - end_time).total_seconds() >= meeting_time * 60:
                        return (end_time + timedelta(minutes=0)).time().strftime("%H:%M") \
                               + "-" + (end_time + timedelta(minutes=meeting_time)).time().strftime("%H:%M")
    return None


def get_meetings_by_id(emp_id):
    """returns the meetings of a given employee in a list"""
    with open(FILE_NAME, "r", encoding="UTF-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        meetings_i = -1
        for index, ele in enumerate(header):
            if ele == "Id":
                id_i = index
            elif ele == "Meetings":
                meetings_i = index
        rows = []
        emp_meetings = []
        for row in reader:
            if row[id_i] == str(emp_id):
                emp_meetings = row[meetings_i].split()
            rows.append(row)
        emp_meetings.sort()
        file.close()
    return emp_meetings


def insert_new_employee(employee_name, in_time, out_time, break_time):
    """Inserts a new employee details name, in time, out time, break time"""
    emp_id = 1
    try:
        with open(FILE_NAME, 'r', encoding="utf-8", newline="\n") as file:
            csvreader = csv.reader(file)
            next(csvreader)
            for row in csvreader:
                emp_id = int(row[0]) + 1
            file.close()
    except FileNotFoundError:
        create_new_csv_file()
    with open(FILE_NAME, 'a', encoding="utf-8", newline="\n") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow([emp_id, employee_name, in_time, out_time, break_time, ""])
        file.close()
    return emp_id


def create_new_csv_file():
    """creates a new employee csv file even if a old file exists"""
    with open(FILE_NAME, 'w', encoding="utf-8", newline="\n") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(["Id", "Employee Name", "In Time", "Out Time", "Break Time", "Meetings"])
        file.close()
