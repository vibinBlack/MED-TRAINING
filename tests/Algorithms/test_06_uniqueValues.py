def finduniqueValues(li):
    res=[]
    for dic in li:
        for values in dic.values():
            if values not in res:
                res.append(values)
    return set(res)

def test_case_01():
    assert finduniqueValues([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]) == {"S009","S002","S005","S001","S007"}

def test_case_02():
    assert finduniqueValues([{"V":"S001"}, {"V": 9}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":9 },{"VIII":"S007"}]) == {9, 'S005', 'S007', 'S001'}

def test_case_03():
    assert finduniqueValues([{},{}]) == set()

def test_case_04():
    assert finduniqueValues([{"apples":5},{1:6},{"orange":6},{"banana":10},{3:3},{1:"$"}]) == {3, '$', 5, 6, 10}
