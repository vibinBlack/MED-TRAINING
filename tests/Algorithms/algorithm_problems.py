"""
Solving Assessment Problems
"""
import operator
from itertools import permutations
import pandas as pd


def bin_to_dec():
    """
    Binary to Decimal Conversion
    """
    bin_num = input("Binary Input : ")
    for i in bin_num:
        if i not in ['0', '1']:
            print("Invalid Input the Binary Number contains only 0 or 1")
            return bin_to_dec()

    dec_num = 0
    for i in range(len(bin_num) - 1, -1, -1):
        dec_num += int(bin_num[i]) * (2 ** (len(bin_num) - i - 1))
    return dec_num


def dec_to_bin():
    """
    Decimal to Binary Conversion
    """
    try:
        dec_num = int(input("Decimal Input : "))
    except ValueError:
        print("Invalid Input the Decimal Number must be an integer")
        return dec_to_bin()

    if dec_num < 0:
        print("Please give positive Input only")
        return dec_to_bin()

    bin_num = ''
    while dec_num >= 0:
        rem = dec_num % 2
        dec_num = dec_num // 2
        bin_num += str(rem)
        if dec_num == 0:
            break
    return bin_num[::-1]


ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.xor,
}


def temp_func(k, temp):
    """ temporary function for calculator function """
    temp1 = ops[temp[k]](float(temp[k - 1]), float(temp[k + 1]))
    temp[k] = temp1
    temp.pop(k - 1)
    temp.pop(k)
    return temp


def calculator(temp):
    """
    Calculator to solve arithmetic expressions (For these options' dictionary\
        is defined above, and we also imported operator in the beginning)
    """
    try:
        if '/' in temp:
            k = temp.index('/')
            return calculator(temp_func(k, temp))
        if '*' in temp:
            k = temp.index('*')
            return calculator(temp_func(k, temp))
        if '%' in temp:
            k = temp.index('%')
            return calculator(temp_func(k, temp))
        if '-' in temp:
            k = temp.index('-')
            return calculator(temp_func(k, temp))
        if '+' in temp:
            k = temp.index('+')
            return calculator(temp_func(k, temp))
        print("Output Value :", end=" ")
    except ValueError:
        print("You have given wrong input format")
        temp[0] = ''
    return temp[0]


def fibonacci_series():
    """ Printing first N fibonacci series """
    try:
        size = int(input("How many fibonacci numbers to be printed? "))
    except ValueError:
        print("Invalid input the number must be an Integer")
        return fibonacci_series()
    var_x, var_y = 0, 1
    temp = [var_x]
    for _ in range(size - 1):
        temp.append(var_y)
        var_x, var_y = var_y, var_x + var_y
    return temp


def triangle_pattern():
    """
    Printing triangle pattern for given length is terms of *'s
    """
    try:
        length = int(input(" Enter the length of the side : "))
    except ValueError:
        print("Invalid input the length must be an Integer")
        return triangle_pattern()
    length = 2 * length - 1
    # (x_axis, y_axis) = (0, 0)
    temp = []
    for i in range(length):
        for j in range(0, length, 2):
            for k in range(0, length, 2):
                if k == i:
                    (x_axis, y_axis) = (i, length // 2 - k // 2)
                    temp.append((x_axis, y_axis))
                    (x_axis, y_axis) = (i, length // 2 + k // 2)
                    temp.append((x_axis, y_axis))
            if i == length - 1:
                (x_axis, y_axis) = (i, j)
                temp.append((x_axis, y_axis))
    for i in range(length):
        print()
        for j in range(length):
            if (i, j) in temp:
                print(" * ", end="")
            else:
                print("   ", end="")
    return None


def binary_search():
    """ Searching the element using Binary Search """
    try:
        arr1 = [int(i) for i in input("Enter the elements of the \
array with a white space each : ").split()]
        search1 = int(input("The element you want to search ? "))
    except ValueError:
        print("Invalid input the elements must be Integer")
        return binary_search()
    arr1.sort()

    def inner_binary(arr, search):
        if len(arr) == 1:
            if arr[0] != search:
                return f"The Element {search} is not found in the given array"
            return f"The Element {search} is found in the given array"
        if len(arr) > 1:
            if arr[(len(arr) - 1) // 2] > search:
                arr = arr[0:(len(arr) - 1) // 2]
            elif arr[(len(arr) - 1) // 2] < search:
                arr = arr[(len(arr) - 1) // 2 + 1: len(arr)]
            else:
                return f"The Element {search} is found in the given array"
        return inner_binary(arr, search)

    return inner_binary(arr1, search1)


def linear_search():
    """ Searching the element using Linear Search """
    try:
        arr = [int(i) for i in input("Enter the elements of the \
array with a white space each : ").split()]
        search = int(input("The element you want to search ? "))
    except ValueError:
        print("Invalid input the elements must be Integer")
        return linear_search()
    for i in arr:
        if i == search:
            return f"The Element {search} is found in the given array at index {arr.index(i)}"

    return f"The Element {search} is not found in the given array"


def palindrome():
    """ function to check for palindrome """
    input1 = input("Enter your input to check for palindrome ? ")
    if input1 == input1[::-1]:
        print(" Your given input is a palindrome !")
    else:
        print(" Your given input is not a palindrome !")
    return 0


def prime_numbers():
    """ function to print prime numbers between the given range """
    try:
        arr = [int(i) for i in input("Enter the 2 numbers with a white\
             space to print prime numbers between them : ").split()]
    except ValueError:
        print("Invalid input the numbers must be Integers")
        return prime_numbers()
    if len(arr) != 2:
        print("Enter 2 numbers only")
        return prime_numbers()
    arr.sort()
    temp = set()
    for i in range(arr[0], arr[1] + 1):
        if i == 2:
            temp.add(i)
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            if i not in (0, 1):
                temp.add(i)
    return temp


def right_angled_triangle():
    """ Printing pattern for right-angled triangle for given height """
    try:
        height = int(input(" Enter the height of the triangle : "))
    except ValueError:
        print("Invalid input the height must be an Integer")
        return right_angled_triangle()
    temp = []
    # (i, j) = (0, 0)
    for i in range(height):
        for j in range(height):
            if i == j:
                temp.append((i, j))
            if j == 0:
                temp.append((i, j))
            if i == height - 1:
                temp.append((i, j))
    for i in range(-2, height):
        for j in range(height):
            if (i, j) in temp:
                print(" # ", end=" ")
            else:
                print("   ", end=" ")
        print(" | ", end="")
        for j in range(height):
            if (i, height - j - 1) in temp:
                print(" # ", end=" ")
            else:
                print("   ", end=" ")
        print(" | ", end="")
        for j in range(height):
            if (j, i) in temp:
                print(" # ", end=" ")
            else:
                print("   ", end=" ")
        print(" | ", end="")
        for j in range(height):
            if (height - j - 1, i) in temp:
                print(" # ", end=" ")
            else:
                print("   ", end=" ")
        print(" | ", end="")
        print()
        for _ in range(4):
            if i == -2:
                print("____" * height, end="___")
            elif i < height - 1:
                print("    " * height, end=" | ")
            else:
                print("____" * height, end="_|_")
        print()
    return 0


def spiral_matrix():
    """ function to print Spiral Matrix for the given size """
    try:
        length = int(input("Enter the length of the Matrix : "))
    except ValueError:
        print("Invalid Input the length must be an integer")
        return spiral_matrix()
    print()
    dic = {}
    i, j, min_i, min_j, max_i, max_j = 0, 0, 1, 0, length - 1, length - 1
    status = "INC_J"
    for k in range(1, length * length + 1):
        dic[(i, j)] = k
        if status == "INC_J":
            j = j + 1
            if j == max_j:
                max_j = max_j - 1
                status = "INC_I"
        elif status == "INC_I":
            i = i + 1
            if i == max_i:
                max_i = max_i - 1
                status = "DEC_J"
        elif status == "DEC_J":
            j = j - 1
            if j == min_j:
                min_j = min_j + 1
                status = "DEC_I"
        elif status == "DEC_I":
            i = i - 1
            if i == min_i:
                min_i = min_i + 1
                status = "INC_J"
    for i in range(length):
        for j in range(length):
            print(dic[(i, j)], end=" " * (4 - len(str(dic[(i, j)]))))
        print("\n")
    return 0


def rotation_of_matrix():
    """ Matrix rotation """
    row = int(input("Enter the Number of Rows of the matrix : "))
    col = int(input("Enter the Number of Columns of the matrix : "))
    lis = []
    rot_lis = []
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(input(f"Enter the element at ({i},{j}) :"))
        lis.append(temp)
    r_c = [row, col]
    for i in range(max(r_c)):
        if i >= row:
            lis.insert(i, [])
    for i in lis:
        for j in range(max(r_c)):
            if j >= len(i):
                i.insert(j, ' ')
    for i in lis:
        for j in i:
            print(f" {j} ", end=" " * (3 - len(j)))
        print("\n")
    for i in range(max(r_c)):
        temp = []
        for j in range(max(r_c) - 1, -1, -1):
            temp.append(lis[j][i])
        rot_lis.append(temp)
    print("\n")
    for i in rot_lis:
        for j in i:
            print(f" {j} ", end=" " * (3 - len(j)))
        print("\n")
    return 0


def extract_csv():
    """ Extracting CSV file using pandas """
    data = pd.read_csv("student.csv")
    data = data.set_index('Student')
    data = data.to_dict('dict')
    print(data)
    print("/n", data.keys())
    print()
    print(data['English'])
    print()
    for i in data.keys():
        print(i, data[i]['Student 2'], sep=" : ")
    return 0


def scrambled_words():
    """ Printing the Scrambled words of a Sentence """
    words = list(word for word in input("Enter the sentence with only\
 these punctuations. (, . ? ; !) : ").split())
    for i in words:
        if i[len(i) - 1] in (',', '?', '.', ';', '!'):
            k = i[len(i) - 1]
            i = i[0:len(i) - 1]
            if len(i) <= 3:
                print(i + k, end=" ")
            else:
                perm = permutations(i[1:len(i) - 1])
                perm = set(perm)
                for j in list(perm):
                    if ''.join(j) != i[1:len(i) - 1]:
                        print(i[0] + ''.join(j) + i[len(i) - 1] + k, end=" ")
                        break
        else:
            if len(i) <= 3:
                print(i, end=" ")
            else:
                perm = permutations(i[1:len(i) - 1])
                perm = set(perm)
                for j in list(perm):
                    if ''.join(j) != i[1:len(i) - 1]:
                        print(i[0] + ''.join(j) + i[len(i) - 1], end=" ")
                        break
    return 0


def shift_matrix():
    # mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    for i in mat:
        for j in i:
            print(j, end=" " * (4 - len(str(j))))
        print("\n")
    length = len(mat)
    m = 0
    n = length
    out = []
    for _ in range((length + 1) // 2):
        k = []
        for i in range(m, n):
            for j in range(m, n):
                if i == m:
                    k.append(mat[i][j])
        for i in range(m + 1, n):
            for j in range(m, n):
                if j == n - 1:
                    k.append(mat[i][j])
        for i in range(m, n):
            for j in range(n - 2, m - 1, -1):
                if i == n - 1:
                    k.append(mat[i][j])
        for i in range(n - 2, m, -1):
            for j in range(m, n):
                if j == m:
                    k.append(mat[i][j])
        out.append(k)
        m = m + 1
        n = n - 1
    print()
    final = []
    shift = int(input("How many digits it should be shifted "))
    for i in out:
        if len(i) == 1:
            shift = 0
        if shift > len(i):
            shift = shift % len(i)
        for j in range(len(i)):
            final.append(i[j - shift])
    print()
    dic = {}
    i, j, min_i, min_j, max_i, max_j = 0, 0, 1, 0, length - 1, length - 1
    status = "INC_J"
    for k in range(0, length * length):
        dic[(i, j)] = final[k]
        if status == "INC_J":
            j = j + 1
            if j == max_j:
                max_j = max_j - 1
                status = "INC_I"
        elif status == "INC_I":
            i = i + 1
            if i == max_i:
                max_i = max_i - 1
                status = "DEC_J"
        elif status == "DEC_J":
            j = j - 1
            if j == min_j:
                min_j = min_j + 1
                status = "DEC_I"
        elif status == "DEC_I":
            i = i - 1
            if i == min_i:
                min_i = min_i + 1
                status = "INC_J"
    for i in range(length):
        for j in range(length):
            print(dic[(i, j)], end=" " * (4 - len(str(dic[(i, j)]))))
        print("\n")
    return 0


def select_problem():
    """
    Select the Problem
    """
    print("\n\n1.  Binary to Decimal Conversion\n2.  Decimal to Binary Conversion\
        \n3.  Calculator\n4.  Fibonacci Numbers\n5.  Triangle Pattern\n6.  Binary Search\
        \n7.  Linear Search\n8.  Palindrome\n9.  Prime Numbers\n10. Right Angled Triangle\
        \n11. Scrambled Words\n12. Extract data from CSV file\n13. Spiral Matrix\
        \n14. Rotation of Matrix (90 degrees)\n15. Shift the Matrix digits\nC.  Close the Program\n")
    try:
        select = input("Select the above number for corresponding problem : ")
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt occurred, Please restart the program")
        return 0

    if select == '1':
        print("\n-------** Binary to Decimal Conversion **--------\n")
        print("Decimal Output : ", bin_to_dec())

    if select == '2':
        print("\n-------** Decimal to Binary Conversion **--------\n")
        print("Binary Output : ", dec_to_bin())

    if select == '3':
        print("\n-------** Calculator **--------\n")
        string = input("Input Expression (NOTE : Use only these operators\
 '+', '-', '*', '/', '%'): ")
        lis = list(string)
        if lis[0] in ('-', '+'):
            lis.insert(0, '0')
        for i in range(len(string)):
            if lis[i] in ['+', '-', '/', '*', '%']:
                lis[i] = ' ' + lis[i] + ' '
        string = ''.join(lis)
        print(calculator(string.split()))

    if select == '4':
        print("\n-------** Fibonacci Numbers **--------\n")
        for i in fibonacci_series():
            print(i, end=" ")

    if select == '5':
        print("\n-------** Triangle Pattern **--------\n")
        try:
            triangle_pattern()
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt occurred, Please restart the program")
            return 0

    if select == '6':
        print("\n-------** Binary Search **--------\n")
        print(binary_search())

    if select == '7':
        print("\n-------** Linear Search **--------\n")
        print(linear_search())

    if select == '8':
        print("\n-------** Palindrome **--------\n")
        palindrome()

    if select == '9':
        print("\n-------** Prime Numbers **--------\n")
        for i in prime_numbers():
            print(i, end=" ")

    if select == '10':
        print("\n-------** Right Angled Triangle **--------\n")
        right_angled_triangle()

    if select == '11':
        print("\n-------** Scrambled Words **--------\n")
        scrambled_words()

    if select == '12':
        print("\n-------** Extract data from CSV file **--------\n")
        extract_csv()

    if select == '13':
        print("\n-------** Spiral Matrix **--------\n")
        spiral_matrix()

    if select == '14':
        print("\n-------** Rotation of Matrix **--------\n")
        rotation_of_matrix()

    if select == '15':
        print("\n-------** Shift Matrix Digits **--------\n")
        shift_matrix()

    if select in ['c', 'C']:
        print("Bye..!!")
        return 0

    return select_problem()


select_problem()
