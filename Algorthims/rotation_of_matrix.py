def rotate_90_clockwise(mat):
    N = len(mat[0])
    for i in range(N//2):
        for j in range(i,N-i-1):
            temp = mat[i][j]
            mat[i][j] = mat[N-1-j][i]
            mat[N-1-j][i] = mat[N-1-i][N-1-j]
            mat[N-1-i][N-1-j] = mat[j][N-1-i]
            mat[j][N-1-i] = temp 

def printMatrix(mat):
    N = len(mat[0])
    for i in range(N):
        print(mat[i]) 

N = int(input("Enter the number of Rows :"))
M = int(input("Enter the number of columns :"))

mat_num = [[int(input()) for x in range(M)] for y in range(N)]


rotate_90_clockwise(mat_num)
printMatrix(mat_num)
