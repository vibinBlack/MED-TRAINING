def bubble_sort(arr,n):
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def test_case1():
    assert bubble_sort([9,6,8,7,2,0], 6) == [0,2,6,7,8,9]

def test_case2():
    assert bubble_sort([1,3,6,2,5,9,6], 7) == [1,2,3,5,6,6,9]

def test_case3():
    assert bubble_sort([2,6,9,8,2,0,47,6], 8) == [0,2,2,6,6,8,9,47]

def test_case4():
    assert bubble_sort([8,5,6,2,10], 5) == [2,5,6,8,10]