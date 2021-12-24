def spiral_matrix(mat_num):
    N = len(mat_num)      #Ending Index of Row
    M = len(mat_num[0])   #Ending Index of Column
    i=0                   #starting index of Row
    j=0                   # starting index of column
    
    while (i < N and j < M):
        for x in range(j,M):
            print(mat_num[i][x],end=" ")

        i+=1 

        for x in range(i,N):
            print(mat_num[x][M-1],end=" ")

        M-=1

        if(i<N):
            for x in range(M-1,j-1,-1):
                print(mat_num[N-1][x],end=" ")
            N-=1 

        if(j<M):
            for x in range(N-1,i-1,-1):
                print(mat_num[x][j],end=" ")

            j+=1

    print()
    




N = int(input("Enter the number of Rows:"))
M = int(input("Enter the number of columns:"))
mat_num = [[int(input()) for x in range(M)] for y in range(N)]


spiral_matrix(mat_num)