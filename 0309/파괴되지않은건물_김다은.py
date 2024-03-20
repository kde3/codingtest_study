def 누적합(matrix, rowLen, colLen) :
    for i in range(rowLen) :
        for j in range(colLen) :
            matrix[i][j+1] += matrix[i][j]

    for i in range(colLen) :
        for j in range(rowLen) :
            matrix[j+1][i] += matrix[j][i]

def 점찍기(matrix, r1, c1, r2, c2, degree) :
    matrix[r1][c1] += degree
    matrix[r2+1][c2+1] += degree

    matrix[r1][c2+1] -= degree
    matrix[r2+1][c1] -= degree  
                
def solution(board, skill):

    rowLen = len(board)
    colLen = len(board[0])

    matrix = [[0]*(colLen + 1) for _ in range(rowLen + 1)]

    for type_, r1, c1, r2, c2, degree in skill :
        # attack
        if type_ == 1 :
            점찍기(matrix, r1, c1, r2, c2, -degree)
        #heal
        else:
            점찍기(matrix, r1, c1, r2, c2, degree)


    누적합(matrix, rowLen, colLen)


    for i in range(rowLen) :
        for j in range(colLen) :
            board[i][j] += matrix[i][j]
            
    cnt = 0
    for row in board :
        for e in row :
            if e > 0 :
                cnt += 1

    return cnt