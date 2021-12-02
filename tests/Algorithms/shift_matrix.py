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
