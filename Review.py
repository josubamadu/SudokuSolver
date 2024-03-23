import Helper

def rowReview(CurrPossibilityBoard):
    for r in range(9):
        CurrPossibilityBoard[r] = Helper.checkRowPossible(CurrPossibilityBoard[r])
    return CurrPossibilityBoard

def colReview(CurrPossibilityBoard):
    for c in range(9):
        col = []
        for x in range(len(CurrPossibilityBoard)):
            if CurrPossibilityBoard[x][c] != None:
                col.append(CurrPossibilityBoard[x][c])
            else:
                col.append(None)
        outputColumn = Helper.checkRowPossible(col)
        for r in range(9):
            CurrPossibilityBoard[r][c] = outputColumn[r]
    return CurrPossibilityBoard

def gridReview(CurrPossibilityBoard):
    for r in range(len(CurrPossibilityBoard)//3):
        for c in range(len(CurrPossibilityBoard)//3):
            Grid = Helper.getGridValues(r,c,CurrPossibilityBoard)
            t = Helper.checkGridPossible(Grid)
            for row in range(9):
                for col in range(9):
                    if (r == row//3) & (c == col//3):
                        if CurrPossibilityBoard[row][col] != None:
                            CurrPossibilityBoard[row][col] = t.pop(0)
    return CurrPossibilityBoard