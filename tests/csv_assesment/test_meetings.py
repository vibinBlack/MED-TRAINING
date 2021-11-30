'''test meetings'''
import meetings

def test_meetings():
    '''test employee creation and meetings scheduling'''
    meetings.create_new_csv_file()
    emp1_id = meetings.insert_new_employee(employee_name="Employee 1", \
        in_time="09:30", out_time="19:00", break_time="12:50-13:50")
    emp2_id = meetings.insert_new_employee(employee_name="Employee 2", \
        in_time="11:00", out_time="20:00", break_time="13:10-14:10")
    assert meetings.get_meetings_by_id(emp1_id) == []
    assert meetings.get_meetings_by_id(emp2_id) == []
    meetings.schedule_meeting(id1=emp1_id, id2=emp2_id, meeting_time=40)
    assert meetings.get_meetings_by_id(emp1_id) == ["11:00-11:40"]
    assert meetings.get_meetings_by_id(emp2_id) == ["11:00-11:40"]
    emp3_id = meetings.insert_new_employee(employee_name="Employee 3", \
        in_time="11:00", out_time="18:00", break_time="11:30-13:00")
    meetings.schedule_meeting(id1=emp1_id, id2=emp3_id, meeting_time=30)
    assert meetings.get_meetings_by_id(emp1_id) == ["11:00-11:40","13:50-14:20"]
    assert meetings.get_meetings_by_id(emp2_id) == ["11:00-11:40"]
    assert meetings.get_meetings_by_id(emp3_id) == ["13:50-14:20"]
    meetings.schedule_meeting(id1=emp2_id, id2=emp3_id, meeting_time=100)
    assert meetings.get_meetings_by_id(emp1_id) == ["11:00-11:40","13:50-14:20"]
    assert meetings.get_meetings_by_id(emp2_id) == ["11:00-11:40","14:20-16:00"]
    assert meetings.get_meetings_by_id(emp3_id) == ["13:50-14:20","14:20-16:00"]
