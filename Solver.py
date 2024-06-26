import numpy as np
import Helper
import Review


BlankGameBoard = np.zeros((9,9))
DefaultPossibilityBoard = [[None]*9]*9
possibleNumbers = np.array([1,2,3,4,5,6,7,8,9])

def retUniqueValues(row,col,currentGame):
    r = Helper.checkRow(row,col,currentGame)
    c = Helper.checkColumn(row,col,currentGame)
    g = Helper.checkGrid(row,col,currentGame)
    a = set(list(r))
    v = list(set(possibleNumbers) - set(r) - set(c) - set(g))
    #print(v)
    return v

##

def possibilityCheck(currentGame):
    CurrPossibilityBoard = []
    
    for r in range(9):
        currentRow = []
        for c in range(9):
            if currentGame[r][c] == None:
                currentRow.append(retUniqueValues(r,c,currentGame))
            else:
                currentRow.append(None)
        CurrPossibilityBoard.append(currentRow)

    # for r in range(9):
    #     CurrPossibilityBoard[r] = Helper.checkRowPossible(CurrPossibilityBoard[r])
    CurrPossibilityBoard = Review.rowReview(CurrPossibilityBoard)
    CurrPossibilityBoard = Review.gridReview(CurrPossibilityBoard)
    CurrPossibilityBoard = Review.colReview(CurrPossibilityBoard)
    Helper.boardPrint(CurrPossibilityBoard)
    return CurrPossibilityBoard
    


def SolverStep(game):
    CurrGame = game
    possibilityMatrix = possibilityCheck(CurrGame)
    for r in range(len(possibilityMatrix)):
        for c in range(len(possibilityMatrix)):
            if possibilityMatrix[r][c] != None:
                if len(possibilityMatrix[r][c]) == 1:
                    CurrGame[r][c] = possibilityMatrix[r][c][0]        
    return CurrGame

def Solver(defaultGame):
    GameStateHistory = {}
    cg = defaultGame
    GameStateHistory[0] = cg.copy()
    counter = 1
    anyChange = False
    while ((None in cg) & (counter < 81) & (anyChange == False)):
        prev = cg.copy()
        nextStep = SolverStep(cg)
        anyChange = (prev == nextStep).all()
        cg = nextStep
        GameStateHistory[counter] = cg.copy()
        counter+=1
        #Gameboard.displayGameState(cg)
    return GameStateHistory

#v = Solver(PracticeGame)
#print(v)
