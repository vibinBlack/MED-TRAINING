import pytest

def first(a,toMove):
    n=len(a)
    i=0
    j=0
    for i in range(n):
        if a[i]!=toMove:        # Checks if current element is not the toMove number and
            a[i],a[j]=a[j],a[i] # If Yes swap it with first found toMove element and
            j+=1                # Increment the index 
                                # If we found toMove number j will point to it and i will point to a non toMove number
    print(a)
    return a
first([7,7,7,7,7,7,7],2)

def test_first():
    assert first([1,2,3,4,2,9,6,2,7,3,2,4,11,6],2)==[1, 3, 4, 9, 6, 7, 3, 4, 11, 6, 2, 2, 2, 2]

def test_empty():
    assert first([],2)==[]

def test_same():
    assert first([7,7,7,7,7,7,7],7)==[7,7,7,7,7,7,7]