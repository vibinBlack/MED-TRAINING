def linearSearch(arr, key):
    for num in arr:
        if num == key:
            return "Element found at {index} index".format(index = arr.index(key))

    return "Element not found"


n = int(input("Enter the size of the array: "))
lst = [int(input()) for _ in range(n)]
key = int(input("Enter the element you want to search: "))
output = linearSearch(lst, key)
print(output)
