def decimaltobinary(decimal):
    if decimal >= 1:
        decimaltobinary(decimal//2)
    print(decimal%2,end='')

decimal = int(input())
decimaltobinary(decimal)
