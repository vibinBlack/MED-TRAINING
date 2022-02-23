li = list(map(int,input().split()))
key = int(input())
n = len(li)
low = 0
flag = 0
high = n-1
while high >= low:
    mid = high+low//2
    if key == li[mid]:
        flag = 1
        break
    elif key < li[mid]:
        high = mid - 1
    elif key > li[mid]:
        low = mid + 1
    else: 
        flag = 0
        break
if flag:
    print("The key found at index : ",mid)
else:
    print("Key not found")
