from tkinter import*


winsu=Tk()
winsu.title("Sudoku Solver")
winsu.geometry("542x555")



label1=Label(winsu,text="Enter the Number and Click Solve",fg="purple",font=6)
label1.grid(row=0,columnspan=10,column=1)

errorlabel=Label(winsu,text="",fg="green") #this will show error while sudoku is not solvabel
errorlabel.grid(row=19,column=1,columnspan=10,pady=10)

Solvedright=Label(winsu,text="",fg="blue") #this will be shown when sudoku is correct
Solvedright.grid(row=19,column=1,columnspan=20,pady=10)

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



    sudoku[row][col]=0
    return False  

def solver(sudoku):
    if SOLVESUDOKU(sudoku,0,0):
        return sudoku
    else:
        return "no"


inputcell={}#this will take input 

def validateinput(d):
    out=(d.isdigit() or d=="") and len(d)<2
    return out

reg=winsu.register(validateinput)   

def grid3x3(row,column,cellcolor):
    for i in range(3):
        for j in range(3):
            inputwid=Entry(winsu,width=9,bg=cellcolor,justify="center",validate="key",validatecommand=(reg,"%P"))
            inputwid.grid(row=row+i+1,column=column+j+1,sticky="nsew",padx=1,pady=1,ipady=13)
            inputcell[(row+i+1,column+j+1)]=inputwid

def grid9x9():
    color="#BDA1FF"
    for rowno in range(1,10,3):
        for colno in range(0,9,3):
            grid3x3(rowno,colno,color)
            if color=="#BDA1FF":
                color="#7BFFAA"
            else:
                color="#BDA1FF"

def clearValues():
    errorlabel.configure(text="")
    Solvedright.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell=inputcell[(row,col)]
            cell.delete(0,END)

def getvalues():
    store=[]
    errorlabel.configure(text="")
    Solvedright.configure(text="")
    for row in range(2,11):
        rows=[]
        for col in range(1,10):
            val=inputcell[(row,col)].get()
            if val=="":
                rows.append(0)
            else:
                rows.append(int(val))

        store.append(rows)
    newvalues(store)

valuegetbutton=Button(winsu,command=getvalues,text="Solve",width=10)
valuegetbutton.grid(row=18,column=1,columnspan=5,pady=20)

valueclearbutton=Button(winsu,command=clearValues,text="Clear",width=10)
valueclearbutton.grid(row=18,column=5,columnspan=5,pady=20)

def newvalues(S):
    sol=solver(S)
    if sol!="no":
        for rows in range(2,11):
            for col in range(1,10):
                inputcell[(rows,col)].delete(0,"end")
                inputcell[(rows,col)].insert(0,sol[rows-2][col-1])
        Solvedright.configure(text="Sudoku Solved Correctly!")
    else:
        errorlabel.configure(text="This Sudoku is not Solvable")


grid9x9()
winsu.mainloop()