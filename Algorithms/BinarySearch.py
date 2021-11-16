def binarySearchHelper(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return "Element found at index {index}".format(index = arr.index(key))
        
        elif arr[mid] > key:
            return binarySearchHelper(arr, low, mid - 1, key)
        else:
            return binarySearchHelper(arr, mid+1, high, key)
    return "Element not found"

def binarySearch(arr, n, key):
    res = binarySearchHelper(arr, 0, n-1, key)
    print(res)

n = int(input("Enter the size of an array: "))
print("Enter the elements: ")
lst = [int(input()) for _ in range(n)]
key = int(input("Enter the element to search: "))
binarySearch(lst, n, key)


