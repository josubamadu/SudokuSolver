import numpy as np
from collections import Counter

def boardPrint(board):
    print("---")
    for item in board:
        print(item)
    print("---")
    print("\n")

def checkRow(row,column,currentGame):
    valueList = getRowValues(row,currentGame)
    #print(valueList)
    return valueList

def checkColumn(row,column,currentGame):
    valueList = getColumnValues(column,currentGame)
    #print(valueList)
    return valueList
    pass

def checkGrid(row,column,currentGame):
    currGridRow = row//3
    currGridColumn = column//3
    gridValueList = getGridValues(currGridRow,currGridColumn,currentGame)
    #print(gridValueList)
    return gridValueList
    pass

def getRowValues(row,currentGame):
    l = []
    for x in range(currentGame.shape[0]):
        if currentGame[row,x] != None:
            l.append(currentGame[row,x])
    return l
    

def getColumnValues(column,currentGame):
    l = []
    for x in range(currentGame.shape[0]):
        if currentGame[x,column] != None:
            l.append(currentGame[x,column])
    return l

def getGridValues(GridRow,GridCol,currentGame):
    gridValueList = []
    for r in range(9):
        for c in range(9):
            if (r // 3 == GridRow) & (c // 3 == GridCol):
                if currentGame[r][c] != None:
                    gridValueList.append(currentGame[r][c])
    return gridValueList 

### Possibililty board

def checkRowPossible(row):
    u = []
    for x in range(len(row)):
        if row[x] != None:
            u = u + row[x]
    return reduction(u,row)

def checkColumnPossible(col):
    u = []
    for x in range(len(col)):
        if col[x] != None:
            u = u + col[x]
    return reduction(u,col)

def reduction(u,currentSpan):
    k = list(Counter(u).keys())
    counts = Counter(u).values()
    for idx, items in enumerate(counts):
        if items == 1:
            uniqueVal = k[idx]
            for x in range(len(currentSpan)):
                if currentSpan[x] != None:
                    if (uniqueVal in currentSpan[x]):
                        l = [uniqueVal]
                        currentSpan[x] = l
    return currentSpan

def checkGridPossible():
    pass