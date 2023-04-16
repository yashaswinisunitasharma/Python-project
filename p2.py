N=9

def isrightnum(sudoku,row,col,num):
    for i in range(9):
        if sudoku[row][i]==num:
            return False
    
    for i in range(9):
        if sudoku[i][col]==num:
            return False

    #now we will check for num exsits in 3x3 grid
    startrow=row-row%3
    startcol=col-col%3
    for i in range(3):
        for j in range(3):
            if sudoku[startrow+i][startcol+j]==num:
                return False

    return True

def SOLVESUDOKU(sudoku,row,col):
    if row==N-1 and col==N:
        return True
    
    if col==N:
        row=row+1
        col=0

    if sudoku[row][col]>0:
        return SOLVESUDOKU(sudoku,row,col+1)

    for num in range(1,N+1):
        if isrightnum(sudoku,row,col,num):
            sudoku[row][col]=num

            if SOLVESUDOKU(sudoku,row,col+1):
                return True
