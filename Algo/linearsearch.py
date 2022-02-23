li = list(map(int,input().split()))
flag = 0
key = int(input())
for i in range(len(li)):
    if li[i] == key:
        flag = 1
        break
if flag:
    print("The key found at index :",i)
else:
    print("Key not found")
