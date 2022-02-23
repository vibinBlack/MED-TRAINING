def binarysearch(li,low,high,key):
    if high >= low:
        mid = (high+low)//2
        if key == li[mid]:
            flag = 1
            return mid
        elif key < li[mid]:
            high = mid -1
            return binarysearch(li,low,high,key)
        elif key > li[mid]:
            low = mid + 1
            return binarysearch(li,low,high,key)
    else:
        return -1


li = list(map(int,input().split()))
n = len(li)
key = int(input())
high = len(li)
low = 0
flag = 0


result = binarysearch(li,low,high,key)
if result!= -1:
    print(f"Key found at index: {result}")
else:
    print("Key not found")
