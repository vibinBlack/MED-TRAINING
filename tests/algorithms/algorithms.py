"""Python assessment programs/Algorithms"""

import re
import csv
import itertools


def binary_to_decimal(bin_num):
    """Converts a binary number to its equivalent decimal number"""
    dec_num = 0
    for i in range(0, len(bin_num)):
        dec_num = dec_num + int(bin_num[len(bin_num) - i - 1]) * 2 ** i
    return dec_num


def decimal_to_binary(dec_num):
    """converts a decimal number to its equivalent binary number"""
    bin_num = ""
    while dec_num >= 0:
        bin_num += str(dec_num % 2)
        dec_num //= 2
        if dec_num == 0:
            break
    return bin_num[::-1]


def calculator_expression(expr):
    """Evaluates and returns the result of a given expression"""
    if bool(re.search(r'^[+-]?[0-9][0-9/*+-.]*[0-9]$', expr)):
        exprs = []
        temp = ""
        for i in expr:
            if i in ["+", "-", "*", "/"]:
                if temp != "":
                    exprs.append(float(temp))
                else:
                    exprs.append(0)
                exprs.append(i)
                temp = ""
            else:
                temp = temp + i
        exprs.append(float(temp))
        while len(exprs) != 1:
            if "/" in exprs:
                i = exprs.index("/")
                exprs[i] = exprs[i - 1] / exprs[i + 1]
            elif "*" in exprs:
                i = exprs.index("*")
                exprs[i] = exprs[i - 1] * exprs[i + 1]
            elif "-" in exprs:
                i = exprs.index("-")
                exprs[i] = exprs[i - 1] - exprs[i + 1]
            elif "+" in exprs:
                i = exprs.index("+")
                exprs[i] = exprs[i - 1] + exprs[i + 1]
            exprs.pop(i + 1)
            exprs.pop(i - 1)
        return exprs[0]
    return 0


def fibnoacci_series(num):
    """returns fibnoacci series of n numbers"""
    fib = [0, 1]
    for i in range(2, num):
        fib.append(fib[i - 1] + fib[i - 2])
    # print(*fib, sep=",")
    return fib


def check_prime_or_not(num):
    """Checks whether the given number is prime or not and returns true if it is"""
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def linear_search(numbers, search_number):
    """searches with every element in a list"""
    for ele in numbers:
        if ele == search_number:
            return True
    return False


def binary_search(numbers, search_number):
    """binary search"""
    numbers.sort()
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if search_number == numbers[mid]:
            return True
        if search_number > numbers[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False


def check_palindrome_or_not(string):
    """checks whether the given string is palindrome or not"""
    for i, _ in enumerate(string):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


def triangle_pattern(num):
    """Prints a triangle pattern of stars of specified length"""
    for i in range(num):
        if i in (0, num - 1):
            print(" " * (num - i) + "* " * (i + 1) + " " * (num - i))
        else:
            print(" " * (num - i) + "*" + " " * (i * 2 - 1) + "*" + " " * (num - i))


def right_angle_triangle_pattern(num):
    """Prints a triangle pattern of stars of specified length"""
    for i in range(num):
        if i in (0, num - 1):
            print("* " * (i + 1) + " " * (num - i))
        else:
            print("*" + " " * (i * 2 - 1) + "*" + " " * (num - i))


def scramble_words():
    """prints scrambled letters in words of a sentence """
    words = input("Enter your sentence ").split()
    for word in words:
        if len(word) <= 3:
            print(word, end=" ")
        else:
            last_char = ""
            if word[-1] in [",", ";", ".", "!", "?"]:
                last_char = word[-1]
                word = word[0:-1]
            scrambled = list(itertools.permutations(word[1:len(word) - 1]))
            for scr in scrambled:
                scrambled_word = "".join(scr)
                if scrambled_word != word[1:len(word) - 1]:
                    break
            print(word[0], scrambled_word, word[-1], last_char, sep="", end=" ")
    print()


def extract_csv():
    """Extracts the contents of a csv file"""
    with open("stats/students.csv", "rt", encoding="UTF-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        print(header)
        rows = []
        for row in reader:
            rows.append(row)
        print(rows)
        file.close()


def rotate_matrix(matrix):
    """rotates a given matrix in clockwise direction of any rows and columns"""
    rows = len(matrix)
    columns = len(matrix[0])
    rotated_matrix = []
    for i in range(columns):
        row = []
        for j in range(rows):
            row.append(matrix[rows - j - 1][i])
        rotated_matrix.append(row)
    return rotated_matrix


def spiral_matrix():
    """Prints a spiral matrix"""
    num = 10
    matrix = {}
    i, j = 0, 0
    min_i, min_j = 1, 0
    max_i = max_j = num - 1
    flag = "INC_J"

    for ele in range(1, num * num + 1):
        matrix[(i, j)] = ele

        if flag == "INC_J":
            j += 1
            if j == max_j:
                max_j -= 1
                flag = "INC_I"
        elif flag == "INC_I":
            i += 1
            if i == max_i:
                max_i -= 1
                flag = "DEC_J"
        elif flag == "DEC_J":
            j -= 1
            if j == min_j:
                min_j += 1
                flag = "DEC_I"
        elif flag == "DEC_I":
            i -= 1
            if i == min_i:
                min_i += 1
                flag = "INC_J"

    for i in range(num):
        for j in range(num):
            print(matrix[(i, j)], end=" " * (5 - len(str(matrix[(i, j)]))))
        print("\n")


def rotate_matrix_by_shifting(matrix, shift_by):
    """Shifts a given matrix by specified cells"""
    mat_len = len(matrix)
    i = j = 0
    min_i, min_j = 1, 0
    max_i = max_j = mat_len - 1
    flag = "INC_J"
    box_matrices = []
    box_matrix = []
    box_matrix_end = False
    for _ in range(0, mat_len * mat_len):
        box_matrix.append(matrix[i][j])
        if box_matrix_end:
            box_matrices.append(box_matrix)
            box_matrix = []
            box_matrix_end = False

        if flag == "INC_J":
            j += 1
            if j == max_j:
                max_j -= 1
                flag = "INC_I"
        elif flag == "INC_I":
            i += 1
            if i == max_i:
                max_i -= 1
                flag = "DEC_J"
        elif flag == "DEC_J":
            j -= 1
            if j == min_j:
                min_j += 1
                flag = "DEC_I"
        elif flag == "DEC_I":
            i -= 1
            if i == min_i:
                box_matrix_end = True
                min_i += 1
                flag = "INC_J"
    box_matrices.append(box_matrix)
    output = {}
    for box_mat, _ in enumerate(box_matrices):
        eff_shift = shift_by % len(box_matrices[box_mat])
        box_matrices[box_mat] = \
            box_matrices[box_mat][-eff_shift:] + box_matrices[box_mat][:-eff_shift]
        for i in range(mat_len):
            for j in range(mat_len):
                if i == box_mat and box_mat <= j < mat_len - box_mat:
                    output[(i, j)] = box_matrices[box_mat][j - box_mat]
                elif i == mat_len - box_mat - 1 and box_mat <= j < mat_len - box_mat:
                    output[(i, j)] = \
                        box_matrices[box_mat][(mat_len - box_mat * 2 - 1) * 2 + mat_len - box_mat - 1 - j]
                elif j == box_mat and box_mat <= i < mat_len - box_mat:
                    output[(i, j)] = \
                        box_matrices[box_mat][(mat_len - box_mat * 2 - 1) * 3 + mat_len - box_mat - 1 - i]
                elif j == mat_len - box_mat - 1 and box_mat <= i < mat_len - box_mat:
                    output[(i, j)] = \
                        box_matrices[box_mat][(mat_len - box_mat * 2 - 1) * 1 + i - box_mat]
    shifted_matrix = []
    for i in range(mat_len):
        shifted_row = []
        for j in range(mat_len):
            shifted_row.append(output[(i, j)])
        shifted_matrix.append(shifted_row)
    return shifted_matrix
