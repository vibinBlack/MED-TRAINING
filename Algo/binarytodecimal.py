binary = input()

po = len(binary) -1
decimal = 0

for i in binary:
    if i == '1':
        decimal += 2**(po)
        po -= 1
    else:
        po -= 1
print(decimal)
